\ifndef{simpleTransformerImplementation}
\define{simpleTransformerImplementation}

\editme

\subsection{Simple Transformer Implementation}

\setupcode{import numpy as np}

\helpercode{def create_synthetic_sequence_data(n_samples=100, seq_length=10, vocab_size=50):
    """Create synthetic sequence data for demonstration."""
    np.random.seed(24)
    
    # Create random sequences
    X = np.random.randint(0, vocab_size, (n_samples, seq_length))
    
    # Create target: next token prediction
    y = np.roll(X, -1, axis=1)
    y[:, -1] = 0  # Padding token for last position
    
    return X, y}

\code{
# Create data
X_seq, y_seq = create_synthetic_sequence_data(200, 8, 30)

print(f"Sequence data: {X_seq.shape} -> {y_seq.shape}")
print(f"Sample sequence: {X_seq[0]}")
print(f"Target sequence: {y_seq[0]}")}

\subsection{Create and Test Basic Attention}

\loadcode{Attention}{mlai}

\code{d_model = 64
n_heads = 4
seq_length = 8
vocab_size = 30

# Create basic attention mechanism
attention = Attention(d_model)

# Test forward pass
X_test = np.random.randn(2, seq_length, d_model)
attn_output, attn_weights = attention.forward(X_test, X_test, X_test)

print("Basic Attention Test:")
print(f"Input shape: {X_test.shape}")
print(f"Output shape: {attn_output.shape}")
print(f"Attention weights shape: {attn_weights.shape}")
print(f"Attention weights sum (should be 1): {attn_weights.sum(axis=-1)[0, 0]}")
print(f"Model parameters: {attention.W_q.size + attention.W_k.size + attention.W_v.size + attention.W_o.size}")}

\subsection{Test Multi-Head Attention}

\loadcode{MultiHeadAttention}{mlai}

\code{# Test multi-head attention (built from basic attention)
multi_head_attention = MultiHeadAttention(d_model, n_heads)

# Forward pass
X_test = np.random.randn(2, seq_length, d_model)
attn_output, attn_weights = multi_head_attention.forward(X_test, X_test, X_test)

print("Multi-Head Attention Test:")
print(f"Input shape: {X_test.shape}")
print(f"Output shape: {attn_output.shape}")
print(f"Attention weights shape: {attn_weights.shape}")
print(f"Attention weights sum (should be 1): {attn_weights.sum(axis=-1)[0, 0]}")
print(f"Number of heads: {n_heads}")}

\subsection{Test Chain Rule in Attention}

\code{# Test gradient flow through attention (demonstrating chain rule)
from mlai import MeanSquaredError

X_test = np.random.randn(2, seq_length, d_model)

# Forward pass through attention
output, attn_weights = attention.forward(X_test, X_test, X_test)

# Create dummy loss using proper loss function (consistent with neural network)
target = np.random.randn(2, seq_length, d_model)
loss_fn = MeanSquaredError()
loss_value = loss_fn.forward(output, target)

# Backward pass (demonstrates three-path chain rule)
loss_gradient = loss_fn.gradient(output, target)
gradients = attention.backward(loss_gradient, X_test, X_test, X_test, attn_weights)

print("Chain Rule Demonstration:")
print(f"Loss value: {loss_value:.4f}")
print(f"Input gradient shape: {gradients['grad_input'].shape}")
print(f"Input gradient norm: {np.linalg.norm(gradients['grad_input']):.4f}")
print("This shows how gradients flow through Q, K, V transformations")
print(f"Three-path chain rule: grad_query + grad_key + grad_value = grad_input")
print(f"Gradient verification: {np.allclose(gradients['grad_input'], gradients['grad_query'] + gradients['grad_key'] + gradients['grad_value'])}")}

\subsection{Train Simple Attention Model}

\helpercode{def train_attention_model(X, y, n_epochs=50, learning_rate=0.001):
    """Train a simple attention model for sequence modeling."""
    from mlai import MeanSquaredError
    
    # Create model
    d_model = 64
    n_heads = 4
    vocab_size = 30
    
    # Use multi-head attention for learning
    model = MultiHeadAttention(d_model, n_heads)
    
    # Convert to embeddings (simplified)
    X_embedded = np.random.randn(len(X), X.shape[1], d_model)
    y_embedded = np.random.randn(len(y), y.shape[1], d_model)
    
    # Loss function (consistent with neural network)
    loss_fn = MeanSquaredError()
    
    # Training loop
    losses = []
    for epoch in range(n_epochs):
        # Forward pass through attention
        output, attn_weights = model.forward(X_embedded, X_embedded, X_embedded)
        
        # Compute loss using proper loss function
        loss = loss_fn.forward(output, y_embedded)
        
        # Backward pass (demonstrates chain rule)
        loss_gradient = loss_fn.gradient(output, y_embedded)
        
        # Use the existing backward method from the Attention class
        # This demonstrates proper gradient computation through the attention mechanism
        for i, head in enumerate(model.attention_heads):
            # Get the corresponding head data
            head_query = X_embedded[:, :, i*model.d_k:(i+1)*model.d_k]
            head_key = X_embedded[:, :, i*model.d_k:(i+1)*model.d_k] 
            head_value = X_embedded[:, :, i*model.d_k:(i+1)*model.d_k]
            head_weights = attn_weights[:, i]  # Get weights for this head
            
            # Compute gradients using the existing backward method
            gradients = head.backward(loss_gradient[:, :, i*model.d_k:(i+1)*model.d_k], 
                                    head_query, head_key, head_value, head_weights)
            
            # Update weights using computed gradients
            head.W_q -= learning_rate * gradients['grad_W_q']
            head.W_k -= learning_rate * gradients['grad_W_k']
            head.W_v -= learning_rate * gradients['grad_W_v']
            head.W_o -= learning_rate * gradients['grad_W_o']
        
        losses.append(loss)
        
        if epoch % 10 == 0:
            print(f"Epoch {epoch:3d}: Loss = {loss:.4f}")
    
    return model, losses}

\code{X_seq, y_seq = create_synthetic_sequence_data(200, 8, 30)
model, losses = train_attention_model(X_seq, y_seq)}

\setupplotcode{import matplotlib.pyplot as plt
import mlai.plot}

\plotcode{fig, ax = plt.subplots(figsize=plot.wide_figsize)
ax.plot(losses, linewidth=2)
ax.set_xlabel('Epoch')
ax.set_ylabel('Loss')
plt.grid(True, alpha=0.3)

print(f"Final training loss: {losses[-1]:.4f}")

mlai.write_figure("transformer-training-progress.svg", directory="\writeDiagramsDir/deepnn")}

\figure{\includediagram{\diagramsDir/deepnn/transformer-training-progress}{50%}}{Transformer Training Progress for sequence modeling}{transformer-training-progress}

\subsection{Visualise Attention Weights}

\helpercode{def visualise_attention_weights(model, X, filename="attention-weights.svg", directory="../diagrams"):
    """Visualise attention weights from the multi-head attention model."""
    # Get attention weights
    X_embedded = np.random.randn(1, X.shape[1], model.d_model)
    _, attn_weights = model.forward(X_embedded, X_embedded, X_embedded)
    
    # Get first head, first sample
    attn_weights = attn_weights[0, 0]  # First head, first sample
    
    # Plot
    fig, ax = plt.subplots(figsize=plot.big_figsize)
    im = ax.imshow(attn_weights, cmap='Blues', aspect='auto')
    
    ax.set_xlabel('Key Position')
    ax.set_ylabel('Query Position')
    
    plt.colorbar(im, ax=ax)
    plt.tight_layout()
    
    mlai.write_figure(filename, directory=directory)}

\plotcode{visualise_attention_weights(model, X_seq, "attention-weights.svg", directory="\writeDiagramsDir/deepnn/")}

\figure{\includediagram{\diagramsDir/deepnn/attention-weights}{60%}}{Attention weights visualisation from the first head showing which positions the model attends to}{attention-weights}

\subsection{Test Different Numbers of Heads}

\code{# Test different numbers of heads (showing composition)
d_model = 64
seq_length = 8

for n_heads in [1, 2, 4, 8]:
    multi_head_attention = MultiHeadAttention(d_model, n_heads)
    X_test = np.random.randn(2, seq_length, d_model)
    
    output, attn_weights = multi_head_attention.forward(X_test, X_test, X_test)
    
    print(f"n_heads={n_heads}: output shape={output.shape}, attn shape={attn_weights.shape}")
    print(f"  Each head processes {d_model//n_heads} dimensions")}

\subsection{Test Different Activation Functions}

\loadcode{SoftmaxActivation}{mlai}

\loadcode{SigmoidAttentionActivation}{mlai}

\loadcode{IdentityMinusSoftmaxActivation}{mlai}

\code{# Compare different activation functions for attention
from mlai import SoftmaxActivation, SigmoidAttentionActivation, IdentityMinusSoftmaxActivation

d_model = 32
seq_length = 4
X_test = np.random.randn(1, seq_length, d_model)

print("Comparing Attention Activation Functions:")
print("=" * 50)

# Standard softmax attention
softmax_attention = Attention(d_model, activation=SoftmaxActivation())
output_softmax, weights_softmax = softmax_attention.forward(X_test, X_test, X_test)

print("1. SoftmaxActivation (Standard):")
print(f"   Weights sum: {weights_softmax.sum(axis=-1)[0, 0]:.6f}")
print(f"   Weights range: [{weights_softmax.min():.6f}, {weights_softmax.max():.6f}]")
print(f"   Attention matrix:\n{weights_softmax[0, 0, :, :]}")

# Sigmoid with normalization
sigmoid_attention = Attention(d_model, activation=SigmoidAttentionActivation())
output_sigmoid, weights_sigmoid = sigmoid_attention.forward(X_test, X_test, X_test)

print("\n2. SigmoidAttentionActivation:")
print(f"   Weights sum: {weights_sigmoid.sum(axis=-1)[0, 0]:.6f}")
print(f"   Weights range: [{weights_sigmoid.min():.6f}, {weights_sigmoid.max():.6f}]")
print(f"   Attention matrix:\n{weights_sigmoid[0, 0, :, :]}")

# Identity minus softmax (interesting alternative)
identity_attention = Attention(d_model, activation=IdentityMinusSoftmaxActivation())
output_identity, weights_identity = identity_attention.forward(X_test, X_test, X_test)

print("\n3. IdentityMinusSoftmaxActivation:")
print(f"   Weights sum: {weights_identity.sum(axis=-1)[0, 0]:.6f}")
print(f"   Weights range: [{weights_identity.min():.6f}, {weights_identity.max():.6f}]")
print(f"   Diagonal entries (1-softmax): {np.diag(weights_identity[0, 0, :, :])}")
print(f"   Off-diagonal entries (-softmax): {weights_identity[0, 0, 0, 1]:.6f}, {weights_identity[0, 0, 1, 0]:.6f}")
print(f"   Attention matrix:\n{weights_identity[0, 0, :, :]}")

print("\nKey Differences:")
print("- Softmax: Standard attention, weights sum to 1, all positive")
print("- Sigmoid: Alternative activation, weights sum to 1, all positive") 
print("- Identity-Minus-Softmax: Diagonal positive (1-softmax), off-diagonal negative (-softmax), sum to 0")
print("  This creates a 'contrast' attention pattern that emphasizes self-connections while")
print("  de-emphasizing connections to other positions.")}

\subsection{Visualise Different Attention Patterns}

\helpercode{def visualise_attention_patterns():
    """Visualise different attention activation patterns."""
    import matplotlib.pyplot as plt
    
    d_model = 16
    seq_length = 6
    X_test = np.random.randn(1, seq_length, d_model)
    
    # Create attention mechanisms with different activations
    activations = [
        ('Softmax', SoftmaxActivation()),
        ('Sigmoid+Norm', SigmoidAttentionActivation()),
        ('Identity-Softmax', IdentityMinusSoftmaxActivation())
    ]
    
    fig, axes = plt.subplots(1, 3, figsize=(15, 4))
    
    for i, (name, activation) in enumerate(activations):
        attention = Attention(d_model, activation=activation)
        _, weights = attention.forward(X_test, X_test, X_test)
        
        # Get attention matrix for first sample
        attn_matrix = weights[0, 0, :, :]
        
        # Plot
        im = axes[i].imshow(attn_matrix, cmap='RdBu_r', vmin=-1, vmax=1, aspect='auto')
        axes[i].set_title(f'{name}\nSum: {attn_matrix.sum():.3f}')
        axes[i].set_xlabel('Key Position')
        axes[i].set_ylabel('Query Position')
        
        # Add colorbar
        plt.colorbar(im, ax=axes[i])
        
        # Add text annotations for small matrices
        if seq_length <= 6:
            for row in range(seq_length):
                for col in range(seq_length):
                    text = axes[i].text(col, row, f'{attn_matrix[row, col]:.2f}',
                                      ha="center", va="center", color="black", fontsize=8)
    
    plt.tight_layout()
    return fig}

\plotcode{fig = visualise_attention_patterns()
mlai.write_figure("attention-activation-comparison.svg", directory="\writeDiagramsDir/deepnn/")}

\figure{\includediagram{\diagramsDir/deepnn/attention-activation-comparison}{80%}}{Comparison of different attention activation functions showing how they create different attention patterns}{attention-activation-comparison}

\code{# Explanation of the different patterns
print("Analysis of Attention Patterns:")
print("=" * 50)
print()
print("1. SOFTMAX ATTENTION (Standard):")
print("   - All weights are positive (0 to 1)")
print("   - Each row sums to 1 (probability distribution)")
print("   - Represents 'how much to attend to each position'")
print("   - Higher values = more attention")
print()
print("2. SIGMOID + NORMALIZATION:")
print("   - Similar to softmax but uses sigmoid activation")
print("   - All weights positive, rows sum to 1")
print("   - Alternative way to create attention weights")
print()
print("3. IDENTITY MINUS SOFTMAX:")
print("   - Diagonal entries: positive (1 - softmax)")
print("   - Off-diagonal entries: negative (-softmax)")
print("   - Each row sums to 0 (not 1!)")
print("   - Creates 'contrast' attention:")
print("     * Positive diagonal = 'attend to self'")
print("     * Negative off-diagonal = 'de-emphasize others'")
print("   - Could be useful for tasks requiring:")
print("     * Self-focus (diagonal emphasis)")
print("     * Contrast learning (positive vs negative weights)")
print("     * Sparse attention patterns")
print()
print("This demonstrates how different activation functions can create")
print("fundamentally different attention behaviors, even with the same")
print("underlying Q, K, V computation!")}

\subsection{Positional Encoding Test}

\loadcode{PositionalEncoding}{mlai}

\code{# Test positional encoding
pe = PositionalEncoding(d_model, max_length=100)
X_test = np.random.randn(2, seq_length, d_model)

X_with_pe = pe.forward(X_test)

print("Positional Encoding Test:")
print(f"Input shape: {X_test.shape}")
print(f"Output shape: {X_with_pe.shape}")
print(f"PE added: {np.allclose(X_test + pe.pe[:seq_length], X_with_pe)}")}

\subsection{Simple Transformer Model}

\loadcode{Transformer}{mlai}

\code{# Create transformer model using the proper Model class
vocab_size = 30
d_model = 64
n_heads = 4

# Use the Transformer model class (inherits from Model)
transformer = Transformer(d_model=d_model, n_heads=n_heads, vocab_size=vocab_size)

print("Transformer Model Test:")
print(f"Model dimension: {transformer.d_model}")
print(f"Number of heads: {transformer.n_heads}")
print(f"Vocabulary size: {transformer.vocab_size}")
print(f"Is a Model: {isinstance(transformer, Model)}")
print(f"Has predict method: {hasattr(transformer, 'predict')}")
print(f"Has objective method: {hasattr(transformer, 'objective')}")
print(f"Has fit method: {hasattr(transformer, 'fit')}")}

\code{# Test forward pass with proper Model interface
X_test = np.random.randint(0, vocab_size, (2, 8))
output = transformer.predict(X_test)

print("Transformer Model Test:")
print(f"Input shape: {X_test.shape}")
print(f"Output shape: {output.shape}")
print(f"Model parameters: {transformer.embedding.size + transformer.output_projection.size + sum(head.W_q.size + head.W_k.size + head.W_v.size + head.W_o.size for head in transformer.attention.attention_heads)}")
print("This model follows the same pattern as NeuralNetwork - it's a proper Model class")}

\subsection{Training Simple Model}

\helpercode{def train_transformer_model(X, y, vocab_size, d_model=64, n_heads=4, n_epochs=100, learning_rate=0.001):
    """Train the transformer model using the proper Model class."""
    from mlai import MeanSquaredError
    
    # Create transformer model (inherits from Model)
    model = Transformer(d_model=d_model, n_heads=n_heads, vocab_size=vocab_size)
    
    # Loss function (consistent with neural network)
    loss_fn = MeanSquaredError()
    
    losses = []
    for epoch in range(n_epochs):
        # Forward pass using predict method (Model interface)
        output = model.predict(X)
        
        # Create dummy target for demonstration
        target = np.random.randn(*output.shape)
        
        # Compute loss using proper loss function
        loss = loss_fn.forward(output, target)
        
        # Compute loss gradient using proper loss function
        loss_gradient = loss_fn.gradient(output, target)
        
        # Simple gradient descent update (for demonstration)
        # In practice, you'd implement proper backpropagation
        model.embedding -= learning_rate * np.mean(loss_gradient, axis=(0, 1), keepdims=True)
        model.output_projection -= learning_rate * np.mean(loss_gradient, axis=(0, 1), keepdims=True)
        
        losses.append(loss)
        
        if epoch % 20 == 0:
            print(f"Epoch {epoch:3d}: Loss = {loss:.4f}")
    
    return model, losses}

\code{X_seq, y_seq = create_synthetic_sequence_data(200, 8, 30)
transformer_model, transformer_losses = train_transformer_model(X_seq, y_seq, vocab_size=30)}

\plotcode{fig, ax = plt.subplots(figsize=plot.wide_figsize)
ax.plot(transformer_losses, linewidth=2)
ax.set_xlabel('Epoch')
ax.set_ylabel('Loss')
ax.set_title('Transformer Model Training Progress')
plt.grid(True, alpha=0.3)

print(f"Final training loss: {transformer_losses[-1]:.4f}")}

mlai.write_figure("simple-transformer-training.svg", directory="\writeDiagramsDir/deepnn/")}

\figure{\includediagram{\diagramsDir/deepnn/simple-transformer-training}{50%}}{Simple Transformer Training Progress}{simple-transformer-training}

\endif

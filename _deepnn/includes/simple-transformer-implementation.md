\ifndef{simpleTransformerImplementation}
\define{simpleTransformerImplementation}

\editme

\subsection{Simple Transformer Implementation}

\setupcode{import numpy as np}

\helpercode{def create_interesting_sequence_data(pattern_type='arithmetic'):
    """Create interesting sequence data for transformer demonstration."""
    from mlai.data import generate_sequence_data
    
    # Generate different types of interesting sequences
    if pattern_type == 'arithmetic':
        X, y = generate_sequence_data(n_samples=200, seq_length=8, vocab_size=20, pattern_type='arithmetic')
        print("Arithmetic sequences: Learn mathematical patterns (2, 4, 6, 8, ...)")
    elif pattern_type == 'pattern':
        X, y = generate_sequence_data(n_samples=200, seq_length=10, vocab_size=15, pattern_type='pattern')
        print("Pattern sequences: Learn repeating patterns (A, B, C, A, B, C, ...)")
    elif pattern_type == 'text':
        X, y = generate_sequence_data(n_samples=200, seq_length=12, vocab_size=26, pattern_type='text')
        print("Text sequences: Learn word-like structures with spaces and punctuation")
    else:
        X, y = generate_sequence_data(n_samples=200, seq_length=8, vocab_size=20, pattern_type='next_token')
        print("Next token sequences: Standard language modeling task")
    
    return X, y}

\code{
# Create interesting arithmetic sequence data
X_seq, y_seq = create_interesting_sequence_data('arithmetic')

print(f"Sequence data: {X_seq.shape} -> {y_seq.shape}")
print(f"Sample sequence: {X_seq[0]}")
print(f"Target sequence: {y_seq[0]}")
print("The target is the input shifted by one place: at each position the task is")
print("to predict the next token, the same task a language model is trained on.")}

\subsection{Explore Different Sequence Types}

\code{# Let's explore different types of interesting sequences
print("Different Sequence Types for Transformer Learning:")
print("=" * 60)

# 1. Arithmetic sequences (mathematical patterns)
X_arith, y_arith = create_interesting_sequence_data('arithmetic')
print(f"\nArithmetic sequences:")
print(f"  Example: {X_arith[0]} -> {y_arith[0]}")
print(f"  Pattern: Each number increases by a fixed step")

# 2. Pattern sequences (repeating patterns)
X_pattern, y_pattern = create_interesting_sequence_data('pattern')
print(f"\nPattern sequences:")
print(f"  Example: {X_pattern[0]} -> {y_pattern[0]}")
print(f"  Pattern: Repeating cycles (A, B, C, A, B, C, ...)")

# 3. Text-like sequences (natural language structure)
X_text, y_text = create_interesting_sequence_data('text')
print(f"\nText sequences:")
print(f"  Example: {X_text[0]} -> {y_text[0]}")
print(f"  Pattern: Word-like structures with spaces and punctuation")

print(f"\nThese different sequence types test different transformer capabilities:")
print(f"- Arithmetic: Mathematical reasoning and number relationships")
print(f"- Pattern: Memory and pattern recognition across sequences")
print(f"- Text: Natural language structure and word boundaries")}

\subsection{Create and Test Basic Attention Layer}

\loadcode{AttentionLayer}{mlai}

\code{d_model = 64
n_heads = 4
seq_length = 8
vocab_size = 30

# Create basic attention layer (new modular approach)
attention_layer = AttentionLayer(d_model)

# Test forward pass (self-attention)
X_test = np.random.randn(2, seq_length, d_model)
attn_output = attention_layer.forward(X_test)

print("Basic Attention Layer Test:")
print(f"Input shape: {X_test.shape}")
print(f"Output shape: {attn_output.shape}")
print(f"Model parameters: {len(attention_layer.parameters)}")
print(f"Layer type: {type(attention_layer).__name__}")
print("This is now a proper Layer that can be composed with other layers!")}

\subsection{Test Multi-Head Attention Layer}

\loadcode{MultiHeadAttentionLayer}{mlai}

\code{# Test multi-head attention layer (new modular approach)
multi_head_attention = MultiHeadAttentionLayer(d_model, n_heads)

# Forward pass (self-attention)
X_test = np.random.randn(2, seq_length, d_model)
attn_output = multi_head_attention.forward(X_test)

print("Multi-Head Attention Layer Test:")
print(f"Input shape: {X_test.shape}")
print(f"Output shape: {attn_output.shape}")
print(f"Number of heads: {n_heads}")
print(f"Model parameters: {len(multi_head_attention.parameters)}")
print(f"Each head projects all {d_model} input features to its own {d_model // n_heads}-dimensional")
print("queries, keys and values; the head outputs are concatenated and projected by W_o.")}

\subsection{Check the Attention Gradients}

\notes{Before training with these layers we check the hand-derived gradients against finite differences. We use a small layer so the numerical gradient is quick to compute. We take a random linear function of the output as the "loss", so every output element contributes to the gradient.}

\code{from mlai.utils import finite_difference_gradient, verify_gradient_implementation

small_attention = AttentionLayer(d_model=4, causal=True)
X_small = np.random.randn(2, 3, 4)
G = np.random.randn(2, 3, 4)  # random weights defining the loss L = sum(G * output)

def loss_of_input(x_flat):
    return np.sum(small_attention.forward(x_flat.reshape(X_small.shape)) * G)

def loss_of_parameters(p):
    small_attention.parameters = p
    return np.sum(small_attention.forward(X_small) * G)

p0 = small_attention.parameters.copy()
numerical_input = finite_difference_gradient(loss_of_input, X_small.flatten())
numerical_params = finite_difference_gradient(loss_of_parameters, p0)
small_attention.parameters = p0

# Analytical gradients from the backward pass
small_attention.forward(X_small)
analytical_input = small_attention.backward(G)[0].flatten()
analytical_params = small_attention.gradients

print("Input gradient (three-path chain rule) matches:",
      verify_gradient_implementation(analytical_input, numerical_input, rtol=1e-4))
print("W_q, W_k, W_v, W_o gradients match:",
      verify_gradient_implementation(analytical_params, numerical_params, rtol=1e-4))}

\subsection{Train Simple Attention Model with Layered Architecture}

\notes{Tokens are integers, so we first represent each one as a one-hot vector. Multiplying a one-hot vector by a weight matrix picks out one row, so a `LinearLayer` applied to one-hot tokens is exactly an embedding layer. The model then adds positional encodings, applies causal multi-head self-attention, and maps each position to a score (logit) for every token in the vocabulary. We train with the softmax cross-entropy loss and plain minibatch gradient descent, using the gradients computed by the backward pass.}

\helpercode{def train_sequence_model(model, X, y, n_epochs=100, learning_rate=0.05, batch_size=20, n_train=150):
    """Train a next-token model with minibatch gradient descent.

    The first n_train sequences are used for training and the rest for testing.
    Returns the training losses, training accuracies and final test accuracy."""
    from mlai import SoftmaxCrossEntropyLoss

    vocab_size = int(max(X.max(), y.max())) + 1
    X_onehot = np.eye(vocab_size)[X]
    Y_onehot = np.eye(vocab_size)[y]
    train_idx = np.arange(n_train)
    test_idx = np.arange(n_train, len(X))

    loss_fn = SoftmaxCrossEntropyLoss()
    losses = []
    accuracies = []

    def evaluate():
        """Loss and accuracy on the training sequences."""
        logits = model.forward(X_onehot[train_idx])
        losses.append(loss_fn.forward(logits, Y_onehot[train_idx]))
        accuracies.append(np.mean(np.argmax(logits, axis=-1) == y[train_idx]))

    evaluate()  # performance with random weights, before training
    for epoch in range(n_epochs):
        order = np.random.permutation(train_idx)
        for start in range(0, len(order), batch_size):
            batch = order[start:start + batch_size]
            logits = model.forward(X_onehot[batch])
            # Backward pass: the gradient of the loss with respect to the logits
            # is propagated through every layer by the chain rule
            model.set_output_gradient(loss_fn.gradient(logits, Y_onehot[batch]))
            # Gradient descent step on all parameters
            model.parameters = model.parameters - learning_rate * model.gradients

        evaluate()
        if epoch % 20 == 0:
            print(f"Epoch {epoch:3d}: Loss = {losses[-1]:.4f}, Train accuracy = {accuracies[-1]:.3f}")

    test_accuracy = np.mean(np.argmax(model.forward(X_onehot[test_idx]), axis=-1) == y[test_idx])
    print(f"Test accuracy: {test_accuracy:.3f}")
    return losses, accuracies, test_accuracy}

\helpercode{def train_attention_model(X, y, d_model=32, n_heads=4, n_epochs=100, learning_rate=0.05):
    """Train an attention-only next-token model: embedding, positions, causal attention, output."""
    from mlai import LayeredNeuralNetwork, LinearLayer, PositionalEncodingLayer, MultiHeadAttentionLayer

    vocab_size = int(max(X.max(), y.max())) + 1
    model = LayeredNeuralNetwork([
        LinearLayer(vocab_size, d_model),                          # token embedding
        PositionalEncodingLayer(d_model),                          # add position information
        MultiHeadAttentionLayer(d_model, n_heads, causal=True),    # attend to earlier positions
        LinearLayer(d_model, vocab_size),                          # logits over the vocabulary
    ])
    losses, accuracies, test_accuracy = train_sequence_model(
        model, X, y, n_epochs=n_epochs, learning_rate=learning_rate)
    return model, losses, accuracies, test_accuracy}

\code{X_seq, y_seq = create_interesting_sequence_data('arithmetic')
model, losses, accuracies, test_accuracy = train_attention_model(X_seq, y_seq)}

\notes{The first prediction in each sequence cannot be made reliably: from a single number the model cannot know the step size, which is chosen at random from 1 to 4. One position in eight is therefore largely guesswork, so a test accuracy of around 90% is close to the best achievable on this data.}

\setupplotcode{import matplotlib.pyplot as plt
import mlai.plot}

\plotcode{fig, (ax1, ax2) = plt.subplots(1, 2, figsize=plot.big_wide_figsize)
ax1.plot(losses, linewidth=2)
ax1.set_xlabel('Epoch')
ax1.set_ylabel('Cross-entropy loss')
ax1.grid(True, alpha=0.3)
ax2.plot(accuracies, linewidth=2, color='orange')
ax2.set_xlabel('Epoch')
ax2.set_ylabel('Training accuracy')
ax2.grid(True, alpha=0.3)
plt.tight_layout()

print(f"Final training loss: {losses[-1]:.4f}")

mlai.write_figure("transformer-training-progress.svg", directory="\writeDiagramsDir/deepnn")}

\figure{\includediagram{\diagramsDir/deepnn/transformer-training-progress}{50%}}{Transformer Training Progress for sequence modeling}{transformer-training-progress}

\subsection{Visualise Attention Weights}

\helpercode{def visualise_attention_weights(model, X, filename="attention-weights.svg", directory="../diagrams"):
    """Visualise attention weights from the multi-head attention model."""
    from mlai import MultiHeadAttentionLayer
    attention_layer = [layer for layer in model.layers if isinstance(layer, MultiHeadAttentionLayer)][0]
    vocab_size = model.layers[0].input_size
    model.forward(np.eye(vocab_size)[X[:1]])
    # First head, first sample
    attn_weights = attention_layer.last_attention_weights[0, 0]
    
    # Plot
    fig, ax = plt.subplots(figsize=plot.big_figsize)
    im = ax.imshow(attn_weights, cmap='Blues', aspect='auto')
    
    ax.set_xlabel('Key Position')
    ax.set_ylabel('Query Position')
    ax.set_title(f'Input: {X[0]}')
    
    plt.colorbar(im, ax=ax)
    plt.tight_layout()
    
    mlai.write_figure(filename, directory=directory)}

\plotcode{visualise_attention_weights(model, X_seq, "attention-weights.svg", directory="\writeDiagramsDir/deepnn/")}

\figure{\includediagram{\diagramsDir/deepnn/attention-weights}{60%}}{Attention weights from the first head of the trained model for one arithmetic sequence. The causal mask makes the matrix lower triangular: each position can only attend to itself and earlier positions.}{attention-weights}

\subsection{Test Different Numbers of Heads}

\code{# Test different numbers of heads (showing composition)
d_model = 64
seq_length = 8

for n_heads in [1, 2, 4, 8]:
    multi_head_attention = MultiHeadAttentionLayer(d_model, n_heads)
    X_test = np.random.randn(2, seq_length, d_model)
    output = multi_head_attention.forward(X_test)
    attn_weights = multi_head_attention.last_attention_weights
    
    print(f"n_heads={n_heads}: output shape={output.shape}, attention weights shape={attn_weights.shape}")
    print(f"  Each head projects all {d_model} features to d_k = {d_model//n_heads} dimensions")}

\subsection{Test Different Activation Functions}

\loadcode{SoftmaxActivation}{mlai.neural_networks}

\helpercode{class SigmoidAttentionActivation:
    """Sigmoid attention weights, normalised so each query sums to one."""

    def forward(self, x, axis=-1):
        s = 1.0 / (1.0 + np.exp(-np.clip(x, -40.0, 40.0)))
        return s / np.sum(s, axis=axis, keepdims=True)}

\helpercode{class IdentityMinusSoftmaxActivation:
    """Contrast attention: I - softmax, so each query sums to zero."""

    def forward(self, x, axis=-1):
        softmax = SoftmaxActivation().forward(x, axis=axis)
        return np.eye(x.shape[axis]) - softmax}

\code{# Compare different activation functions for attention
d_model = 32
seq_length = 4
X_test = np.random.randn(1, seq_length, d_model)

print("Comparing Attention Activation Functions:")
print("=" * 50)

# Standard softmax attention
softmax_attention = AttentionLayer(d_model, activation=SoftmaxActivation())
output_softmax = softmax_attention.forward(X_test)
weights_softmax = softmax_attention.last_attention_weights

print("1. SoftmaxActivation (Standard):")
print(f"   Weights sum: {weights_softmax.sum(axis=-1)[0, 0]:.6f}")
print(f"   Weights range: [{weights_softmax.min():.6f}, {weights_softmax.max():.6f}]")
print(f"   Attention matrix:\n{weights_softmax[0, :, :]}")

# Sigmoid with normalization
sigmoid_attention = AttentionLayer(d_model, activation=SigmoidAttentionActivation())
output_sigmoid = sigmoid_attention.forward(X_test)
weights_sigmoid = sigmoid_attention.last_attention_weights

print("\n2. SigmoidAttentionActivation:")
print(f"   Weights sum: {weights_sigmoid.sum(axis=-1)[0, 0]:.6f}")
print(f"   Weights range: [{weights_sigmoid.min():.6f}, {weights_sigmoid.max():.6f}]")
print(f"   Attention matrix:\n{weights_sigmoid[0, :, :]}")

# Identity minus softmax (interesting alternative)
identity_attention = AttentionLayer(d_model, activation=IdentityMinusSoftmaxActivation())
output_identity = identity_attention.forward(X_test)
weights_identity = identity_attention.last_attention_weights

print("\n3. IdentityMinusSoftmaxActivation:")
print(f"   Weights sum: {weights_identity.sum(axis=-1)[0, 0]:.6f}")
print(f"   Weights range: [{weights_identity.min():.6f}, {weights_identity.max():.6f}]")
print(f"   Diagonal entries (1-softmax): {np.diag(weights_identity[0, :, :])}")
print(f"   Off-diagonal entries (-softmax): {weights_identity[0, 0, 1]:.6f}, {weights_identity[0, 1, 0]:.6f}")
print(f"   Attention matrix:\n{weights_identity[0, :, :]}")

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
        attention = AttentionLayer(d_model, activation=activation)
        attention.forward(X_test)
        weights = attention.last_attention_weights
        
        # Get attention matrix for first sample
        attn_matrix = weights[0, :, :]
        
        # Ensure it's 2D for plotting
        if attn_matrix.ndim == 1:
            # If 1D, reshape to square matrix
            seq_len = int(np.sqrt(len(attn_matrix)))
            attn_matrix = attn_matrix.reshape(seq_len, seq_len)
        elif attn_matrix.ndim == 3:
            # If 3D, take first sample
            attn_matrix = attn_matrix[0, :, :]
        
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

\code{# Show the different attention patterns
print("Attention Pattern Analysis:")
print("Softmax: Standard attention, weights sum to 1")
print("Sigmoid: Alternative activation, weights sum to 1") 
print("Identity-Softmax: Contrast attention, weights sum to 0")
print("This demonstrates different attention behaviors!")}

\notes{The different attention activation functions create fundamentally different behaviors:

**Softmax Attention (Standard):**
- All weights are positive (0 to 1)
- Each row sums to 1 (probability distribution)
- Represents 'how much to attend to each position'
- Higher values = more attention

**Sigmoid + Normalization:**
- Similar to softmax but uses sigmoid activation
- All weights positive, rows sum to 1
- Alternative way to create attention weights

**Identity Minus Softmax:**
- Diagonal entries: positive (1 - softmax)
- Off-diagonal entries: negative (-softmax)
- Each row sums to 0 (not 1!)
- Creates 'contrast' attention:
  * Positive diagonal = 'attend to self'
  * Negative off-diagonal = 'de-emphasize others'
- Could be useful for tasks requiring:
  * Self-focus (diagonal emphasis)
  * Contrast learning (positive vs negative weights)
  * Sparse attention patterns

This demonstrates how different activation functions can create fundamentally different attention behaviors, even with the same underlying Q, K, V computation. To train with one of these alternatives, the activation also needs a `gradient(x, grad_output, axis)` method giving its vector-Jacobian product; the attention layer raises an error in the backward pass if it is missing.}

\subsection{Positional Encoding Layer Test}

\loadcode{PositionalEncodingLayer}{mlai}

\code{# Test positional encoding layer (new modular approach)
pe_layer = PositionalEncodingLayer(d_model, max_length=100)
X_test = np.random.randn(2, seq_length, d_model)

X_with_pe = pe_layer.forward(X_test)

print("Positional Encoding Layer Test:")
print(f"Input shape: {X_test.shape}")
print(f"Output shape: {X_with_pe.shape}")
print(f"PE added: {np.allclose(X_test + pe_layer.pe[:seq_length], X_with_pe)}")
print(f"Layer parameters: {len(pe_layer.parameters)} (should be 0 - no trainable params)")
print("This is now a proper Layer that can be composed with other layers!")}

\subsection{Build Transformer with Layered Architecture}

\notes{A transformer block combines multi-head attention with a position-wise feed-forward network, which is the same small neural network applied separately at every position. Each of these sub-layers is wrapped in a residual connection, $\mathbf{y} = \mathbf{x} + f(\mathbf{x})$. Because $\mathbf{x}$ reaches the output by two paths, the chain rule again sums two contributions in the backward pass: $\frac{\partial \lossFunction}{\partial \mathbf{x}} = \frac{\partial \lossFunction}{\partial \mathbf{y}} + \frac{\partial \lossFunction}{\partial \mathbf{y}}\frac{\partial f}{\partial \mathbf{x}}$. Residual connections make deep stacks much easier to train because the gradient always has a direct path back to earlier layers. Full transformers also apply layer normalisation around each sub-layer, which we omit here for simplicity.}

\loadcode{ResidualLayer}{mlai}

\helpercode{def build_transformer(vocab_size, d_model=32, n_heads=4, d_ff=64):
    """A single-block causal transformer for next-token prediction."""
    from mlai import (LayeredNeuralNetwork, LinearLayer, FullyConnectedLayer, ReLUActivation,
                      PositionalEncodingLayer, MultiHeadAttentionLayer, ResidualLayer)
    return LayeredNeuralNetwork([
        LinearLayer(vocab_size, d_model),                                   # token embedding
        PositionalEncodingLayer(d_model),
        ResidualLayer(MultiHeadAttentionLayer(d_model, n_heads, causal=True)),
        ResidualLayer([FullyConnectedLayer(d_model, d_ff, ReLUActivation()),  # feed-forward network
                       LinearLayer(d_ff, d_model)]),
        LinearLayer(d_model, vocab_size),                                   # logits
    ])}

\code{transformer = build_transformer(vocab_size=20)

print("Layered Transformer Model:")
print(f"Number of layers: {len(transformer.layers)}")
print(f"Total parameters: {len(transformer.parameters)}")
print(f"Layer types: {[type(layer).__name__ for layer in transformer.layers]}")

# Forward pass on one-hot tokens
tokens = X_seq[:2]
logits = transformer.forward(np.eye(20)[tokens])
print(f"Input tokens shape: {tokens.shape}")
print(f"Output logits shape: {logits.shape}  (batch, sequence position, vocabulary)")}

\subsection{Training Layered Transformer Model}

\code{X_seq, y_seq = create_interesting_sequence_data('arithmetic')
transformer_model = build_transformer(vocab_size=20)
transformer_losses, transformer_accuracies, transformer_test_accuracy = train_sequence_model(
    transformer_model, X_seq, y_seq, n_epochs=100, learning_rate=0.05)}

\plotcode{fig, ax = plt.subplots(figsize=plot.wide_figsize)
ax.plot(transformer_losses, linewidth=2)
ax.set_xlabel('Epoch')
ax.set_ylabel('Cross-entropy loss')
plt.grid(True, alpha=0.3)

print(f"Final training loss: {transformer_losses[-1]:.4f}")

mlai.write_figure("simple-transformer-training.svg", directory="\writeDiagramsDir/deepnn/")}

\figure{\includediagram{\diagramsDir/deepnn/simple-transformer-training}{50%}}{Simple Transformer Training Progress}{simple-transformer-training}

\subsection{Compare Different Sequence Types}

\code{# Train the same transformer on different sequence types
print("Training Transformers on Different Sequence Types:")
print("=" * 60)

results = {}
for pattern_type in ['arithmetic', 'pattern', 'text']:
    print(f"\n{pattern_type}:")
    X_p, y_p = create_interesting_sequence_data(pattern_type)
    vocab_size = int(max(X_p.max(), y_p.max())) + 1
    losses_p, accuracies_p, test_accuracy_p = train_sequence_model(
        build_transformer(vocab_size), X_p, y_p, n_epochs=100, learning_rate=0.05)
    results[pattern_type] = (accuracies_p[-1], test_accuracy_p)

print("\nSummary (train accuracy, test accuracy):")
for pattern_type, (train_acc, test_acc) in results.items():
    print(f"  {pattern_type:10s}: {train_acc:.3f}, {test_acc:.3f}")}

\notes{Comparing training and test accuracy shows how well each pattern has been learned. Arithmetic sequences use a rule (add the step) that the model can apply to sequences it has not seen, so training and test accuracy are similar. The repeating patterns are made of randomly chosen tokens. To predict them on new sequences the model must find the earlier occurrence of the current token and copy whatever followed it. That copying mechanism is hard for a single small attention block to learn from 150 examples, so it partly memorises the training sequences instead, and the test accuracy is much lower than the training accuracy. This is the gap between fitting and generalising that we discussed for overparameterised models. The text-like sequences are made of letters drawn uniformly at random, separated by spaces and occasional punctuation, so most next tokens cannot be predicted from the context at all. The only learnable structure is where words are likely to end, and accuracy stays low on both training and test data. Low accuracy here reflects the data, not a failure of the model.}

\subsection{Benefits of the New Layered Architecture}

\code{# Demonstrate the benefits of the new modular layered architecture
print("Benefits of the New Layered Architecture:")
print("=" * 50)

# 1. Composable layers
from mlai import LayeredNeuralNetwork, MultiHeadAttentionLayer, PositionalEncodingLayer, LinearLayer

# Create different layer combinations
layers1 = [PositionalEncodingLayer(d_model), MultiHeadAttentionLayer(d_model, n_heads)]
layers2 = [PositionalEncodingLayer(d_model), MultiHeadAttentionLayer(d_model, n_heads),
           LinearLayer(d_model, d_model)]

model1 = LayeredNeuralNetwork(layers1)
model2 = LayeredNeuralNetwork(layers2)

print(f"Model 1 (Attention only): {len(model1.parameters)} parameters")
print(f"Model 2 (Attention + Linear): {len(model2.parameters)} parameters")
print(f"Layer types in Model 1: {[type(l).__name__ for l in layers1]}")
print(f"Layer types in Model 2: {[type(l).__name__ for l in layers2]}")

# 2. Independent layer testing
print("\nIndependent Layer Testing:")
attention_layer = MultiHeadAttentionLayer(d_model, n_heads)
pos_layer = PositionalEncodingLayer(d_model)

# Test each layer independently
X_test = np.random.randn(2, 8, d_model)
pos_output = pos_layer.forward(X_test)
attn_output = attention_layer.forward(pos_output)

print(f"Positional encoding output shape: {pos_output.shape}")
print(f"Attention output shape: {attn_output.shape}")
print("Each layer can be tested and debugged independently!")

# 3. Gradient testing
print("\nGradient Testing:")
print("Every layer's input and parameter gradients are checked against finite differences")
print("in mlai's tests (tests/unit/test_layer_parameter_gradients.py)")

# 4. Parameter management
print("\nParameter Management:")
print(f"Attention layer parameters: {len(attention_layer.parameters)}")
print(f"Positional encoding parameters: {len(pos_layer.parameters)} (should be 0)")
print("Each layer manages its own parameters with proper getter/setter methods")

print("\nThis demonstrates the power of the new modular architecture!")
print("Layers are composable, testable, and mathematically verified!")}

\notes{The new layered architecture provides several key benefits:

**1. Modularity and Composability:**
- Each layer is a self-contained unit with a consistent interface
- Layers can be composed in any order to create complex architectures
- Easy to experiment with different layer combinations

**2. Independent Testing:**
- Each layer can be tested independently using our comprehensive gradient testing
- Forward and backward passes are verified using finite differences
- Mathematical correctness is ensured through numerical verification

**3. Clean Separation of Concerns:**
- Attention logic is separate from positional encoding
- Each layer has a single responsibility
- Easy to understand and debug individual components

**4. Consistent Interface:**
- All layers implement the same `forward()`, `backward()`, and `parameters` interface
- Works seamlessly with `LayeredNeuralNetwork`
- Follows the same patterns as other neural network components

**5. Educational Clarity:**
- Students can understand each component in isolation
- Clear demonstration of how complex architectures are built from simple components
- Shows the power of composition over inheritance

This modular approach makes transformer architectures much more accessible and maintainable!}

\endif

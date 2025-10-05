\ifndef{simpleTransformerImplementation}
\define{simpleTransformerImplementation}

\editme

\subsection{Simple Transformer Implementation}

\helpercode{def create_synthetic_sequence_data(n_samples=100, seq_length=10, vocab_size=50):
    """Create synthetic sequence data for demonstration."""
    np.random.seed(42)
    
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

\subsection{Create and Test Transformer Components}

\setupcode{from mlai import MultiHeadAttention, TransformerBlock, PositionalEncoding}

\code{d_model = 64
n_heads = 4
d_ff = 128
seq_length = 8
vocab_size = 30

# Create transformer block
transformer = TransformerBlock(d_model, n_heads, d_ff, dropout=0.1)

# Test forward pass
X_test = np.random.randint(0, vocab_size, (2, seq_length))
X_embedded = np.random.randn(2, seq_length, d_model)  # Dummy embeddings

output = transformer.forward(X_embedded)

print("Transformer Test:")
print(f"Input shape: {X_embedded.shape}")
print(f"Output shape: {output.shape}")
print(f"Model parameters: {sum(p.numel() for p in transformer.parameters())}")}

\subsection{Test Attention Mechanism}

\code{# Test multi-head attention
attention = MultiHeadAttention(d_model, n_heads)

# Forward pass
X_test = np.random.randn(2, seq_length, d_model)
attn_output, attn_weights = attention.forward(X_test, X_test, X_test)

print("Attention Test:")
print(f"Input shape: {X_test.shape}")
print(f"Output shape: {attn_output.shape}")
print(f"Attention weights shape: {attn_weights.shape}")
print(f"Attention weights sum (should be 1): {attn_weights.sum(axis=-1)[0, 0]}")}

\subsection{Test Backpropagation}

\code{# Forward pass
X_test = np.random.randn(2, seq_length, d_model)
output = transformer.forward(X_test)

# Create dummy loss
loss_fn = nn.MSELoss()
target = np.random.randn(2, seq_length, d_model)
loss_value = loss_fn(output, target)

# Backward pass
loss_value.backward()

print("Backpropagation Test:")
print(f"Loss value: {loss_value.item():.4f}")
print(f"Gradient norms:")
for name, param in transformer.named_parameters():
    if param.grad is not None:
        print(f"  {name}: {param.grad.norm().item():.4f}")}

\subsection{Train Transformer for Sequence Modeling}

\helpercode{def train_transformer_sequence(X, y, n_epochs=50, learning_rate=0.001):
    """Train a transformer for sequence modeling."""
    # Create model
    d_model = 64
    n_heads = 4
    d_ff = 128
    vocab_size = 30
    
    model = TransformerBlock(d_model, n_heads, d_ff, dropout=0.1)
    optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)
    criterion = nn.CrossEntropyLoss()
    
    # Convert to embeddings (simplified)
    X_embedded = torch.randn(len(X), X.shape[1], d_model)
    y_tensor = torch.tensor(y, dtype=torch.long)
    
    # Training loop
    losses = []
    for epoch in range(n_epochs):
        optimizer.zero_grad()
        
        # Forward pass
        output = model.forward(X_embedded)
        
        # Reshape for loss computation
        output_flat = output.view(-1, d_model)
        y_flat = y_tensor.view(-1)
        
        # Compute loss (simplified)
        loss = torch.mean((output - X_embedded) ** 2)
        
        # Backward pass
        loss.backward()
        optimizer.step()
        
        losses.append(loss.item())
        
        if epoch % 10 == 0:
            print(f"Epoch {epoch:3d}: Loss = {loss.item():.4f}")
    
    return model, losses}

\code{X_seq, y_seq = create_synthetic_sequence_data(200, 8, 30)
model, losses = train_transformer_sequence(X_seq, y_seq)}

\setupplotcode{import matplotlib.pyplot as plt
import mlai.plot}

\plotcode{fig, ax = plt.subplots(figsize=plot.wide_figsize)
ax.plot(losses, linewidth=2)
ax.set_xlabel('Epoch')
ax.set_ylabel('Loss')
plt.grid(True, alpha=0.3)

print(f"Final training loss: {losses[-1]:.4f}")}

mlai.write_figure("transformer-training-progress.svg", directory="\writeDiagramsDir/deepnn")}

\figure{\includediagram{\diagramsDir/deepnn/transformer-training-progress}{50%}}{Transformer Training Progress for sequence modeling}{transformer-training-progress}

\subsection{Visualise Attention Weights}

\helpercode{def visualise_attention_weights(model, X, filename="transformer-attention.svg", directory="../diagrams"):
    """Visualise attention weights from the transformer."""
    model.eval()
    
    with torch.no_grad():
        # Get attention weights
        X_embedded = torch.randn(1, X.shape[1], model.d_model)
        _, attn_weights = model.attention.forward(X_embedded, X_embedded, X_embedded)
        
        # Convert to numpy
        attn_weights = attn_weights[0, 0].numpy()  # First head, first sample
        
        # Plot
        fig, ax = plt.subplots(figsize=plot.big_figsize)
        im = ax.imshow(attn_weights, cmap='Blues', aspect='auto')
        
        ax.set_xlabel('Key Position')
        ax.set_ylabel('Query Position')
        
        plt.colorbar(im, ax=ax)
        plt.tight_layout()
        
        mlai.write_figure(filename, directory=directory)}

\plotcode{visualize_attention_weights(model, X_seq, "transformer-attention-weights.svg", directory="\writeDiagramsDir/deepnn/")}

\figure{\includediagram{\diagramsDir/deepnn/transformer-attention-weights}{60%}}{Attention weights visualisation showing which positions the model attends to}{transformer-attention-weights}

\subsection{Test Multi-Head Attention}

\code{# Test different numbers of heads
d_model = 64
seq_length = 8

for n_heads in [1, 2, 4, 8]:
    attention = MultiHeadAttention(d_model, n_heads)
    X_test = torch.randn(2, seq_length, d_model)
    
    output, attn_weights = attention.forward(X_test, X_test, X_test)
    
    print(f"n_heads={n_heads}: output shape={output.shape}, attn shape={attn_weights.shape}")}

\subsection{Positional Encoding Test}

\code{# Test positional encoding
pe = PositionalEncoding(d_model, max_length=100)
X_test = torch.randn(2, seq_length, d_model)

X_with_pe = pe(X_test)

print("Positional Encoding Test:")
print(f"Input shape: {X_test.shape}")
print(f"Output shape: {X_with_pe.shape}")
print(f"PE added: {torch.allclose(X_test + pe.pe[:seq_length], X_with_pe)}")}

\subsection{Complete Transformer Model}

\helpercode{def create_complete_transformer(vocab_size, d_model=64, n_heads=4, d_ff=128, n_layers=2):
    """Create a complete transformer model."""
    class CompleteTransformer(nn.Module):
        def __init__(self, vocab_size, d_model, n_heads, d_ff, n_layers):
            super().__init__()
            self.d_model = d_model
            self.embedding = nn.Embedding(vocab_size, d_model)
            self.pe = PositionalEncoding(d_model)
            self.transformer_blocks = nn.ModuleList([
                TransformerBlock(d_model, n_heads, d_ff) for _ in range(n_layers)
            ])
            self.output_projection = nn.Linear(d_model, vocab_size)
            
        def forward(self, x):
            # Embedding + positional encoding
            x = self.embedding(x) * np.sqrt(self.d_model)
            x = self.pe(x)
            
            # Pass through transformer blocks
            for block in self.transformer_blocks:
                x = block.forward(x)
            
            # Output projection
            return self.output_projection(x)
    
    return CompleteTransformer(vocab_size, d_model, n_heads, d_ff, n_layers)}

\code{# Create complete model
vocab_size = 30
model = create_complete_transformer(vocab_size, d_model=64, n_heads=4, d_ff=128, n_layers=2)

# Test forward pass
X_test = torch.randint(0, vocab_size, (2, 8))
output = model(X_test)

print("Complete Transformer Test:")
print(f"Input shape: {X_test.shape}")
print(f"Output shape: {output.shape}")
print(f"Total parameters: {sum(p.numel() for p in model.parameters())}")}

\subsection{Training Complete Model}

\helpercode{def train_complete_transformer(X, y, vocab_size, n_epochs=100, learning_rate=0.001):
    """Train the complete transformer model."""
    model = create_complete_transformer(vocab_size)
    optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)
    criterion = nn.CrossEntropyLoss()
    
    losses = []
    for epoch in range(n_epochs):
        optimizer.zero_grad()
        
        # Forward pass
        X_tensor = torch.tensor(X, dtype=torch.long)
        y_tensor = torch.tensor(y, dtype=torch.long)
        
        output = model(X_tensor)
        
        # Reshape for loss
        output_flat = output.view(-1, vocab_size)
        y_flat = y_tensor.view(-1)
        
        loss = criterion(output_flat, y_flat)
        
        # Backward pass
        loss.backward()
        optimizer.step()
        
        losses.append(loss.item())
        
        if epoch % 20 == 0:
            print(f"Epoch {epoch:3d}: Loss = {loss.item():.4f}")
    
    return model, losses}

\code{X_seq, y_seq = create_synthetic_sequence_data(200, 8, 30)
complete_model, complete_losses = train_complete_transformer(X_seq, y_seq, vocab_size=30)}

\plotcode{fig, ax = plt.subplots(figsize=plot.wide_figsize)
ax.plot(complete_losses, linewidth=2)
ax.set_xlabel('Epoch')
ax.set_ylabel('Loss')
plt.grid(True, alpha=0.3)

print(f"Final training loss: {complete_losses[-1]:.4f}")}

mlai.write_figure("complete-transformer-training.svg", directory="\writeDiagramsDir/deepnn/")}

\figure{\includediagram{\diagramsDir/deepnn/complete-transformer-training}{50%}}{Complete Transformer Training Progress}{complete-transformer-training}

\endif

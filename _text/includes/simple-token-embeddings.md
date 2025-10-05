\ifndef{simpleTokenEmbeddings}
\define{simpleTokenEmbeddings}

\editme

\subsection{Simple Token Embeddings}

\setupcode{import numpy as np
import matplotlib.pyplot as plt}

\helpercode{def create_embedding_matrix(vocab_size, d_model):
    """
    Create a simple embedding matrix for educational purposes.
    
    This maps discrete token IDs to continuous d-dimensional vectors.
    
    Parameters
    ----------
    vocab_size : int
        Size of the vocabulary (number of unique tokens)
    d_model : int
        Dimension of the embedding space
        
    Returns
    -------
    embeddings : np.ndarray
        Embedding matrix of shape (vocab_size, d_model)
    """
    # Initialize with small random values
    # In practice, these would be learned during training
    np.random.seed(42)  # For reproducible results
    embeddings = np.random.normal(0, 0.1, (vocab_size, d_model))
    
    return embeddings}

\code{# Create embedding matrix
vocab_size = 20  # Small vocabulary for demonstration
d_model = 8      # 8-dimensional embeddings

embeddings = create_embedding_matrix(vocab_size, d_model)

print("Embedding Matrix:")
print(f"Shape: {embeddings.shape}")
print(f"Vocabulary size: {vocab_size}")
print(f"Embedding dimension: {d_model}")
print(f"Sample embeddings:")
print(embeddings[:5])  # Show first 5 embeddings}

\subsection{Map Tokens to Embeddings}

\helpercode{def tokenise_to_embeddings(tokens, embedding_matrix):
    """
    Convert a sequence of tokens to their corresponding embeddings.
    
    Parameters
    ----------
    tokens : list or np.ndarray
        Sequence of token IDs
    embedding_matrix : np.ndarray
        Embedding matrix of shape (vocab_size, d_model)
        
    Returns
    -------
    embedded_sequence : np.ndarray
        Sequence of embeddings of shape (seq_len, d_model)
    """
    # Convert tokens to embeddings
    embedded_sequence = embedding_matrix[tokens]
    
    return embedded_sequence}

\code{# Example: Convert tokens to embeddings
# Sample token sequence
tokens = [0, 5, 12, 3, 8]  # Example token IDs
print(f"Input tokens: {tokens}")

# Convert to embeddings
embedded = tokenise_to_embeddings(tokens, embeddings)

print(f"Embedded sequence shape: {embedded.shape}")
print(f"Embedded sequence:")
print(embedded)}

\subsection{Visualise Embedding Space}

\helpercode{def visualise_embeddings_2d(embeddings, vocab, max_tokens=10):
    """Visualise embeddings in 2D space using PCA."""
    from sklearn.decomposition import PCA
    
    # Take first max_tokens embeddings
    subset_embeddings = embeddings[:max_tokens]
    subset_vocab = {k: v for k, v in vocab.items() if v < max_tokens}
    
    # Reduce to 2D using PCA
    pca = PCA(n_components=2)
    embeddings_2d = pca.fit_transform(subset_embeddings)
    
    # Create plot
    fig, ax = plt.subplots(figsize=(10, 8))
    
    # Plot embeddings
    scatter = ax.scatter(embeddings_2d[:, 0], embeddings_2d[:, 1], 
                        c=range(len(embeddings_2d)), cmap='tab10', s=100)
    
    # Add labels
    for i, (word, token_id) in enumerate(subset_vocab.items()):
        if token_id < max_tokens:
            ax.annotate(f'{word}({token_id})', 
                       (embeddings_2d[token_id, 0], embeddings_2d[token_id, 1]),
                       xytext=(5, 5), textcoords='offset points', fontsize=8)
    
    ax.set_xlabel('First Principal Component')
    ax.set_ylabel('Second Principal Component')
    ax.set_title('Token Embeddings in 2D Space')
    ax.grid(True, alpha=0.3)
    
    plt.colorbar(scatter, label='Token ID')
    plt.tight_layout()
    
    return fig}

\code{# Create a simple vocabulary for visualisation
vocab = {'the': 0, 'quick': 1, 'brown': 2, 'fox': 3, 'jumps': 4, 
         'over': 5, 'lazy': 6, 'dog': 7, 'cat': 8, 'runs': 9}

# Create embeddings
embeddings = create_embedding_matrix(len(vocab), d_model=16)

# Visualise in 2D
fig = visualise_embeddings_2d(embeddings, vocab, max_tokens=10)
mlai.write_figure("token-embeddings-2d.svg", directory="\writeDiagramsDir/text/")}

\figure{\includediagram{\diagramsDir/text/token-embeddings-2d}{80%}}{Token embeddings visualised in 2D space showing how discrete tokens map to continuous vectors}{token-embeddings-2d}

\subsection{Sequence Embeddings}

\helpercode{def embed_sequence(tokens, embedding_matrix, seq_length=None):
    """
    Embed a sequence of tokens, handling variable lengths.
    
    Parameters
    ----------
    tokens : list or np.ndarray
        Sequence of token IDs
    embedding_matrix : np.ndarray
        Embedding matrix
    seq_length : int, optional
        Target sequence length (padding/truncation)
        
    Returns
    -------
    embedded_sequence : np.ndarray
        Embedded sequence of shape (seq_length, d_model)
    """
    # Convert to embeddings
    embedded = tokenise_to_embeddings(tokens, embedding_matrix)
    
    if seq_length is not None:
        # Pad or truncate to target length
        if len(embedded) < seq_length:
            # Pad with zeros
            padding = np.zeros((seq_length - len(embedded), embedded.shape[1]))
            embedded = np.vstack([embedded, padding])
        elif len(embedded) > seq_length:
            # Truncate
            embedded = embedded[:seq_length]
    
    return embedded}

\code{# Example: Embed sequences of different lengths
sequences = [
    [0, 1, 2],           # Short sequence
    [3, 4, 5, 6, 7],     # Medium sequence  
    [8, 9, 0, 1, 2, 3, 4, 5]  # Long sequence
]

target_length = 6  # Standardise to length 6

print("Sequence Embedding Examples:")
for i, seq in enumerate(sequences):
    embedded = embed_sequence(seq, embeddings, target_length)
    print(f"Sequence {i}: {seq} -> Shape: {embedded.shape}")
    print(f"  Padded/truncated: {embedded.shape[0]} tokens, {embedded.shape[1]} dimensions")}

\subsection{Positional Encoding}

\helpercode{def add_positional_encoding(embedded_sequence):
    """
    Add positional encoding to embedded sequence.
    
    This helps the model understand the order of tokens in the sequence.
    
    Parameters
    ----------
    embedded_sequence : np.ndarray
        Embedded sequence of shape (seq_len, d_model)
        
    Returns
    -------
    encoded_sequence : np.ndarray
        Sequence with positional encoding added
    """
    seq_len, d_model = embedded_sequence.shape
    
    # Create positional encoding matrix
    pos_encoding = np.zeros((seq_len, d_model))
    position = np.arange(seq_len).reshape(-1, 1)
    
    # Sinusoidal encoding
    div_term = np.exp(np.arange(0, d_model, 2) * 
                     (-np.log(10000.0) / d_model))
    
    pos_encoding[:, 0::2] = np.sin(position * div_term)
    pos_encoding[:, 1::2] = np.cos(position * div_term)
    
    # Add to embeddings
    return embedded_sequence + pos_encoding}

\code{# Example: Add positional encoding
tokens = [0, 1, 2, 3, 4]
embedded = embed_sequence(tokens, embeddings, seq_length=5)
positional_encoded = add_positional_encoding(embedded)

print("Positional Encoding Example:")
print(f"Original embeddings shape: {embedded.shape}")
print(f"With positional encoding: {positional_encoded.shape}")
print(f"Difference (positional encoding):")
print(positional_encoded - embedded)}

\subsection{Complete Token-to-Embedding Pipeline}

\code{# Complete pipeline: tokens -> embeddings -> positional encoding
def process_tokens_for_transformer(tokens, vocab_size, d_model, max_seq_len=10):
    """
    Complete pipeline from tokens to transformer-ready embeddings.
    
    Parameters
    ----------
    tokens : list
        Sequence of token IDs
    vocab_size : int
        Size of vocabulary
    d_model : int
        Embedding dimension
    max_seq_len : int
        Maximum sequence length
        
    Returns
    -------
    processed_embeddings : np.ndarray
        Embeddings with positional encoding, shape (max_seq_len, d_model)
    """
    # Step 1: Create embedding matrix
    embeddings = create_embedding_matrix(vocab_size, d_model)
    
    # Step 2: Convert tokens to embeddings
    embedded = embed_sequence(tokens, embeddings, max_seq_len)
    
    # Step 3: Add positional encoding
    final_embeddings = add_positional_encoding(embedded)
    
    return final_embeddings

# Example usage
tokens = [0, 1, 2, 3, 4, 5]
processed = process_tokens_for_transformer(tokens, vocab_size=20, d_model=8, max_seq_len=6)

print("Complete Pipeline:")
print(f"Input tokens: {tokens}")
print(f"Output shape: {processed.shape}")
print(f"Ready for transformer input!")}

\notes{Token embeddings are crucial for transformer models:

**Key Concepts:**
1. **Discrete to Continuous**: Tokens are integers, but neural networks need continuous values
2. **Learnable Mappings**: Embedding matrices are learned during training
3. **Positional Information**: Positional encoding adds order information
4. **Dimensionality**: Higher dimensions can capture more semantic relationships

**Important Properties:**
- **Similarity**: Similar tokens should have similar embeddings
- **Compositionality**: Embeddings can be combined (e.g., "king" - "man" + "woman" ≈ "queen")
- **Context Independence**: Same token always maps to same embedding (before attention)
- **Position Awareness**: Positional encoding preserves sequence order

This embedding layer is the first step in any transformer model, converting discrete text into continuous mathematical representations that can be processed by neural networks.}

\endif

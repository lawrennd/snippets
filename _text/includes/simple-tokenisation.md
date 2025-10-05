\ifndef{simpleTokenisation}
\define{simpleTokenisation}

\editme

\subsection{Simple Text Tokenisation}

\setupcode{import numpy as np
import re}

\helpercode{def simple_tokeniser(text, vocab_size=1000):
    """
    Simple tokeniser for educational purposes.
    
    This creates a basic vocabulary from the text and converts
    words to integer tokens.
    
    Parameters
    ----------
    text : str
        Input text to tokenise
    vocab_size : int
        Maximum vocabulary size
        
    Returns
    -------
    tokens : list
        List of integer tokens
    vocab : dict
        Word to token mapping
    """
    # Convert to lowercase and split into words
    words = re.findall(r'\b\w+\b', text.lower())
    
    # Create vocabulary (most common words)
    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1
    
    # Sort by frequency and take top vocab_size words
    sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
    vocab = {word: idx for idx, (word, _) in enumerate(sorted_words[:vocab_size])}
    
    # Add special tokens
    vocab['<UNK>'] = len(vocab)  # Unknown word token
    vocab['<PAD>'] = len(vocab)  # Padding token
    
    # Convert words to tokens
    tokens = []
    for word in words:
        if word in vocab:
            tokens.append(vocab[word])
        else:
            tokens.append(vocab['<UNK>'])
    
    return tokens, vocab}

\code{# Example text for tokenisation
text = "The quick brown fox jumps over the lazy dog. The dog was very lazy indeed."

print("Original text:")
print(text)
print()

# Tokenize the text
tokens, vocab = simple_tokeniser(text, vocab_size=20)

print("Tokenisation results:")
print(f"Number of tokens: {len(tokens)}")
print(f"Tokens: {tokens}")
print(f"Vocabulary size: {len(vocab)}")
print(f"Vocabulary: {vocab}")}

\subsection{Create Sequences for Training}

\helpercode{def create_sequences(tokens, seq_length=5):
    """
    Create input-target sequences for next token prediction.
    
    Parameters
    ----------
    tokens : list
        List of integer tokens
    seq_length : int
        Length of input sequences
        
    Returns
    -------
    X : np.ndarray
        Input sequences of shape (n_sequences, seq_length)
    y : np.ndarray
        Target sequences of shape (n_sequences, seq_length)
    """
    sequences = []
    targets = []
    
    for i in range(len(tokens) - seq_length):
        # Input sequence
        seq = tokens[i:i+seq_length]
        # Target sequence (shifted by 1)
        target = tokens[i+1:i+seq_length+1]
        
        sequences.append(seq)
        targets.append(target)
    
    return np.array(sequences), np.array(targets)}

\code{# Create sequences from our tokenised text
seq_length = 4
X, y = create_sequences(tokens, seq_length)

print("Training sequences:")
print(f"Input shape: {X.shape}")
print(f"Target shape: {y.shape}")
print()
print("Example sequences:")
for i in range(min(3, len(X))):
    print(f"Input {i}: {X[i]} -> Target {i}: {y[i]}")}

\subsection{Visualise Tokenisation Process}

\helpercode{def visualise_tokenisation(text, tokens, vocab, max_tokens=20):
    """Visualise the tokenisation process."""
    import matplotlib.pyplot as plt
    
    # Show first few tokens
    words = re.findall(r'\b\w+\b', text.lower())
    shown_tokens = min(max_tokens, len(tokens))
    
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 6))
    
    # Show word-to-token mapping
    ax1.bar(range(shown_tokens), tokens[:shown_tokens])
    ax1.set_xlabel('Position')
    ax1.set_ylabel('Token ID')
    ax1.set_title('Token IDs for First {} Words'.format(shown_tokens))
    
    # Show vocabulary
    vocab_items = list(vocab.items())[:10]  # Show first 10 vocab items
    words_vocab = [item[0] for item in vocab_items]
    token_ids = [item[1] for item in vocab_items]
    
    ax2.bar(range(len(vocab_items)), token_ids)
    ax2.set_xlabel('Vocabulary Index')
    ax2.set_ylabel('Token ID')
    ax2.set_title('Vocabulary Mapping (First 10 Words)')
    ax2.set_xticks(range(len(vocab_items)))
    ax2.set_xticklabels(words_vocab, rotation=45)
    
    plt.tight_layout()
    return fig}

\plotcode{fig = visualise_tokenisation(text, tokens, vocab)
mlai.write_figure("tokenisation-process.svg", directory="\writeDiagramsDir/deepnn/")}

\figure{\includediagram{\diagramsDir/deepnn/tokenisation-process}{80%}}{Tokenisation process showing how text is converted to integer tokens}{tokenisation-process}

\subsection{Test with Transformer}

\code{# Now we can use our tokenised data with the transformer
from mlai import Transformer

# Set up transformer parameters
vocab_size = len(vocab)
d_model = 32
n_heads = 4

# Create transformer model
transformer = Transformer(d_model=d_model, n_heads=n_heads, vocab_size=vocab_size)

print("Transformer with Tokenised Data:")
print(f"Vocabulary size: {vocab_size}")
print(f"Model dimension: {d_model}")
print(f"Number of heads: {n_heads}")
print(f"Input sequences shape: {X.shape}")

# Test forward pass
output = transformer.predict(X[:5])  # Test with first 5 sequences
print(f"Output shape: {output.shape}")
print("This shows how text flows through the transformer!")}

\subsection{Complete Text Processing Pipeline}

\code{# Complete pipeline: text -> tokens -> sequences -> transformer
def text_to_transformer_input(text, seq_length=4, vocab_size=50):
    """Complete pipeline from text to transformer input."""
    # Step 1: Tokenize
    tokens, vocab = simple_tokeniser(text, vocab_size)
    
    # Step 2: Create sequences
    X, y = create_sequences(tokens, seq_length)
    
    # Step 3: Create transformer
    transformer = Transformer(d_model=32, n_heads=4, vocab_size=len(vocab))
    
    return X, y, transformer, vocab

# Example usage
sample_text = "Hello world this is a test of our tokenisation system"
X, y, model, vocab = text_to_transformer_input(sample_text, seq_length=3, vocab_size=30)

print("Complete Pipeline Results:")
print(f"Text: '{sample_text}'")
print(f"Sequences: {X.shape}")
print(f"Vocabulary: {len(vocab)} words")
print(f"Model ready for training!")}

\notes{This tokenisation process is fundamental to transformer models:

**Key Steps:**
1. **Text Preprocessing**: Convert to lowercase, extract words
2. **Vocabulary Creation**: Build word-to-integer mapping
3. **Tokenisation**: Convert words to integer tokens
4. **Sequence Creation**: Create input-target pairs for training

**Important Concepts:**
- **Special Tokens**: `<UNK>` for unknown words, `<PAD>` for padding
- **Vocabulary Size**: Limits the number of unique words the model can handle
- **Sequence Length**: Determines how much context the model sees at once
- **Next Token Prediction**: The target is the input shifted by one position

This simple tokeniser demonstrates the core concepts, though production systems use more sophisticated approaches like BPE (Byte Pair Encoding) or WordPiece.}

\endif

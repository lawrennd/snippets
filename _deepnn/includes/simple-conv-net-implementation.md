\ifndef{simpleConvNetImplementation}
\define{simpleConvNetImplementation}

\editme

\subsection{Simple Conv Net Implementation}

\helpercode{def create_synthetic_image_data(n_samples=100, height=28, width=28, n_channels=1):
    """Create synthetic image datasets for demonstration."""
    np.random.seed(42)
    
    # Create random images
    X = np.random.randn(n_samples, height, width, n_channels)
    
    # Create target: simple pattern recognition (sum of pixels > threshold)
    y = (X.sum(axis=(1, 2, 3)) > 0).astype(float).reshape(-1, 1)
    
    return X, y}

\code{
# Create data
X_img, y_img = create_synthetic_image_data(200, 28, 28, 1)

print(f"Image data: {X_img.shape} -> {y_img.shape}")
print(f"Sample image shape: {X_img[0].shape}")
print(f"Target: {y_img[0]}")}

\subsection{Create and Test Convolutional Layer}

\setupcode{from mlai import ConvolutionalLayer, MaxPoolingLayer, ReLUActivation}

\code{input_height, input_width, input_channels = 28, 28, 1
kernel_size = 3
n_filters = 8
stride = 1
padding = 1

# Create convolutional layer
conv_layer = ConvolutionalLayer(input_channels, n_filters, kernel_size, stride, padding)

# Test forward pass
X_test = np.random.randn(2, input_height, input_width, input_channels)
output = conv_layer.forward(X_test)

print("Convolutional Layer Test:")
print(f"Input shape: {X_test.shape}")
print(f"Output shape: {output.shape}")
print(f"Kernel shape: {conv_layer.kernels.shape}")
print(f"Number of parameters: {conv_layer.kernels.size + conv_layer.biases.size}")
print(f"Weight sharing: Each kernel applied {output.shape[1] * output.shape[2]} times")}

\subsection{Test Sparse Weight Matrix}

\code{# Demonstrate sparse weight matrix structure
print("Sparse Weight Matrix Analysis:")
print("=" * 40)

# Show how convolution creates sparse connections
input_size = input_height * input_width * input_channels
output_size = output.shape[1] * output.shape[2] * n_filters

print(f"Full dense layer would need: {input_size} × {output_size} = {input_size * output_size:,} parameters")
print(f"Convolutional layer uses: {conv_layer.kernels.size + conv_layer.biases.size} parameters")
print(f"Sparsity ratio: {(conv_layer.kernels.size + conv_layer.biases.size) / (input_size * output_size):.4f}")

# Show kernel structure
print(f"\nKernel structure:")
print(f"  Shape: {conv_layer.kernels.shape}")
print(f"  Each kernel: {kernel_size}×{kernel_size} = {kernel_size**2} weights")
print(f"  Applied at {output.shape[1]}×{output.shape[2]} = {output.shape[1] * output.shape[2]} locations")
print(f"  Total applications: {n_filters} × {output.shape[1] * output.shape[2]} = {n_filters * output.shape[1] * output.shape[2]}")

# Show parameter tying
print(f"\nParameter Tying:")
print(f"  Each kernel weight is shared across {output.shape[1] * output.shape[2]} spatial locations")
print(f"  This is the key to translation invariance!")}

\subsection{Test Max Pooling}

\code{# Test max pooling layer
pool_size = 2
stride = 2

max_pool = MaxPoolingLayer(pool_size, stride)

# Forward pass through max pooling
pooled_output = max_pool.forward(output)

print("Max Pooling Test:")
print(f"Input shape: {output.shape}")
print(f"Output shape: {pooled_output.shape}")
print(f"Pooling reduces spatial dimensions by factor of {pool_size}")
print(f"Max pooling selects maximum value in each {pool_size}×{pool_size} region")}

\subsection{Test Backpropagation}

\code{# Forward pass
X_test = np.random.randn(2, 28, 28, 1)
conv_output = conv_layer.forward(X_test)
pooled_output = max_pool.forward(conv_output)

# Create dummy loss
loss_fn = MeanSquaredError()
target = np.random.randn(*pooled_output.shape)
loss_value = loss_fn.forward(pooled_output, target)

# Backward pass
loss_gradient = loss_fn.gradient(pooled_output, target)
pool_gradients = max_pool.backward(loss_gradient)
conv_gradients = conv_layer.backward(pool_gradients)

print("Backpropagation Test:")
print(f"Loss value: {loss_value:.4f}")
print(f"Input gradient shape: {conv_gradients['grad_input'].shape}")
print(f"Kernel gradient shape: {conv_gradients['grad_kernels'].shape}")
print(f"Bias gradient shape: {conv_gradients['grad_biases'].shape}")
print("Gradients flow through sparse connections and parameter tying")}

\subsection{Train Simple Conv Net}

\helpercode{def train_conv_net(X, y, n_epochs=50, learning_rate=0.01):
    """Train a simple convolutional network."""
    from mlai import MeanSquaredError
    
    # Create network components
    conv_layer = ConvolutionalLayer(1, 8, 3, 1, 1)
    max_pool = MaxPoolingLayer(2, 2)
    relu = ReLUActivation()
    
    # Loss function
    loss_fn = MeanSquaredError()
    
    # Training loop
    losses = []
    for epoch in range(n_epochs):
        # Forward pass
        conv_output = conv_layer.forward(X)
        relu_output = relu.forward(conv_output)
        pooled_output = max_pool.forward(relu_output)
        
        # Flatten for loss computation
        pooled_flat = pooled_output.reshape(pooled_output.shape[0], -1)
        y_flat = y.reshape(-1, 1)
        
        # Compute loss
        loss = loss_fn.forward(pooled_flat, y_flat)
        
        # Backward pass
        loss_gradient = loss_fn.gradient(pooled_flat, y_flat)
        loss_gradient = loss_gradient.reshape(pooled_output.shape)
        
        pool_gradients = max_pool.backward(loss_gradient)
        relu_gradients = relu.backward(pool_gradients)
        conv_gradients = conv_layer.backward(relu_gradients)
        
        # Update weights (simple gradient descent)
        conv_layer.kernels -= learning_rate * conv_gradients['grad_kernels']
        conv_layer.biases -= learning_rate * conv_gradients['grad_biases']
        
        losses.append(loss)
        
        if epoch % 10 == 0:
            print(f"Epoch {epoch:3d}: Loss = {loss:.4f}")
    
    return conv_layer, max_pool, relu, losses}

\code{X_img, y_img = create_synthetic_image_data(200, 28, 28, 1)
conv_layer, max_pool, relu, losses = train_conv_net(X_img, y_img)}

\setupplotcode{import matplotlib.pyplot as plt
import mlai.plot}

\plotcode{fig, ax = plt.subplots(figsize=plot.wide_figsize)
ax.plot(losses, linewidth=2)
ax.set_xlabel('Epoch')
ax.set_ylabel('Loss')
plt.grid(True, alpha=0.3)

print(f"Final training loss: {losses[-1]:.4f}")}

mlai.write_figure("conv-net-training-progress.svg", directory="\writeDiagramsDir/deepnn")}

\figure{\includediagram{\diagramsDir/deepnn/conv-net-training-progress}{50%}}{Convolutional Network Training Progress}{conv-net-training-progress}

\subsection{Visualise Learned Filters}

\helpercode{def visualise_learned_filters(conv_layer, filename="learned-filters.svg", directory="../diagrams"):
    """Visualise the learned convolutional filters."""
    kernels = conv_layer.kernels
    
    # Reshape kernels for visualization
    n_filters = kernels.shape[0]
    kernel_size = kernels.shape[2]
    
    # Create subplot grid
    n_cols = 4
    n_rows = (n_filters + n_cols - 1) // n_cols
    
    fig, axes = plt.subplots(n_rows, n_cols, figsize=(n_cols * 3, n_rows * 3))
    if n_rows == 1:
        axes = axes.reshape(1, -1)
    
    for i in range(n_filters):
        row = i // n_cols
        col = i % n_cols
        
        # Get kernel for this filter
        kernel = kernels[i, 0, :, :]  # First channel
        
        # Plot
        im = axes[row, col].imshow(kernel, cmap='RdBu_r', aspect='auto')
        axes[row, col].set_title(f'Filter {i+1}')
        axes[row, col].set_xticks([])
        axes[row, col].set_yticks([])
        
        # Add colorbar
        plt.colorbar(im, ax=axes[row, col])
    
    # Hide unused subplots
    for i in range(n_filters, n_rows * n_cols):
        row = i // n_cols
        col = i % n_cols
        axes[row, col].set_visible(False)
    
    plt.tight_layout()
    mlai.write_figure(filename, directory=directory)}

\plotcode{visualise_learned_filters(conv_layer, "learned-filters.svg", directory="\writeDiagramsDir/deepnn/")}

\figure{\includediagram{\diagramsDir/deepnn/learned-filters}{60%}}{Learned convolutional filters showing different feature detectors}{learned-filters}

\subsection{Test Different Kernel Sizes}

\code{# Test different kernel sizes
kernel_sizes = [1, 3, 5, 7]
input_shape = (2, 28, 28, 1)

print("Kernel Size Comparison:")
print("=" * 40)

for kernel_size in kernel_sizes:
    conv_layer = ConvolutionalLayer(1, 4, kernel_size, 1, kernel_size//2)
    X_test = np.random.randn(*input_shape)
    
    output = conv_layer.forward(X_test)
    
    print(f"Kernel size {kernel_size}:")
    print(f"  Input: {X_test.shape}")
    print(f"  Output: {output.shape}")
    print(f"  Parameters: {conv_layer.kernels.size + conv_layer.biases.size}")
    print(f"  Receptive field: {kernel_size}×{kernel_size}")
    print(f"  Spatial locations: {output.shape[1]}×{output.shape[2]}")
    print()}

\subsection{Test Different Strides}

\code{# Test different stride values
strides = [1, 2, 3, 4]
input_shape = (2, 28, 28, 1)

print("Stride Comparison:")
print("=" * 30)

for stride in strides:
    conv_layer = ConvolutionalLayer(1, 4, 3, stride, 1)
    X_test = np.random.randn(*input_shape)
    
    output = conv_layer.forward(X_test)
    
    print(f"Stride {stride}:")
    print(f"  Input: {X_test.shape}")
    print(f"  Output: {output.shape}")
    print(f"  Spatial reduction: {X_test.shape[1]}/{output.shape[1]} = {X_test.shape[1]/output.shape[1]:.1f}x")
    print(f"  Parameters: {conv_layer.kernels.size + conv_layer.biases.size}")
    print()}

\subsection{Complete Conv Net Model}

\loadcode{ConvNet}{mlai}

\code{# Create complete convolutional network
input_shape = (28, 28, 1)
n_classes = 2

conv_net = ConvNet(input_shape, n_classes)

print("Complete Conv Net Test:")
print(f"Input shape: {input_shape}")
print(f"Number of classes: {n_classes}")
print(f"Model parameters: {sum(p.size for p in conv_net.parameters())}")
print(f"Is a Model: {isinstance(conv_net, Model)}")
print(f"Has predict method: {hasattr(conv_net, 'predict')}")}

\code{# Test forward pass
X_test = np.random.randn(2, 28, 28, 1)
output = conv_net.predict(X_test)

print("Conv Net Forward Pass:")
print(f"Input shape: {X_test.shape}")
print(f"Output shape: {output.shape}")
print(f"Output represents class probabilities")}

\subsection{Training Complete Model}

\helpercode{def train_complete_conv_net(X, y, n_epochs=100, learning_rate=0.001):
    """Train the complete convolutional network."""
    from mlai import MeanSquaredError
    
    # Create model
    model = ConvNet((28, 28, 1), 2)
    
    # Loss function
    loss_fn = MeanSquaredError()
    
    losses = []
    for epoch in range(n_epochs):
        # Forward pass
        output = model.predict(X)
        
        # Compute loss
        loss = loss_fn.forward(output, y)
        
        # Backward pass
        loss_gradient = loss_fn.gradient(output, y)
        
        # Simple gradient descent update
        for layer in model.layers:
            if hasattr(layer, 'kernels'):
                layer.kernels -= learning_rate * np.mean(loss_gradient, axis=0, keepdims=True)
            if hasattr(layer, 'biases'):
                layer.biases -= learning_rate * np.mean(loss_gradient, axis=0, keepdims=True)
        
        losses.append(loss)
        
        if epoch % 20 == 0:
            print(f"Epoch {epoch:3d}: Loss = {loss:.4f}")
    
    return model, losses}

\code{X_img, y_img = create_synthetic_image_data(200, 28, 28, 1)
complete_model, complete_losses = train_complete_conv_net(X_img, y_img)}

\plotcode{fig, ax = plt.subplots(figsize=plot.wide_figsize)
ax.plot(complete_losses, linewidth=2)
ax.set_xlabel('Epoch')
ax.set_ylabel('Loss')
ax.set_title('Complete Conv Net Training Progress')
plt.grid(True, alpha=0.3)

print(f"Final training loss: {complete_losses[-1]:.4f}")}

mlai.write_figure("complete-conv-net-training.svg", directory="\writeDiagramsDir/deepnn/")}

\figure{\includediagram{\diagramsDir/deepnn/complete-conv-net-training}{50%}}{Complete Convolutional Network Training Progress}{complete-conv-net-training}

\subsection{Educational Summary}

\code{print("Convolutional Networks: Key Concepts")
print("=" * 40)
print()
print("1. SPARSE WEIGHT MATRICES:")
print("   - Dense layer: 28×28×1 × 14×14×8 = 1,232,128 parameters")
print("   - Conv layer: 8 × 3×3 = 72 parameters")
print("   - Sparsity ratio: 72/1,232,128 = 0.000058")
print("   - Massive parameter reduction!")
print()
print("2. PARAMETER TYING (Weight Sharing):")
print("   - Same kernel applied at every spatial location")
print("   - Translation invariance: same feature detector everywhere")
print("   - Each weight learned from multiple examples")
print()
print("3. SPECIAL ACTIVATIONS:")
print("   - ReLU: Non-linearity for feature detection")
print("   - Max Pooling: Spatial downsampling + translation invariance")
print("   - Max pooling selects strongest response in each region")
print()
print("4. TRANSLATION INVARIANCE:")
print("   - Same features detected regardless of position")
print("   - Crucial for image recognition")
print("   - Achieved through parameter tying")
print()
print("5. HIERARCHICAL FEATURES:")
print("   - Early layers: edges, corners, textures")
print("   - Later layers: shapes, objects, patterns")
print("   - Natural feature hierarchy")
print()
print("This is why CNNs work so well for images!")
print("They combine the power of neural networks with")
print("the structure of visual processing.")}

\endif

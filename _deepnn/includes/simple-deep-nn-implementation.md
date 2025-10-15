\ifndef{simpleDeepNnImplementation}
\define{simpleDeepNnImplementation}

\editme

\subsection{Simple Deep NN Implementation}


\helpercode{def create_synthetic_data(n_samples=100, task='regression'):
    """Create synthetic datasets for demonstration."""
    np.random.seed(42)
    
    if task == 'regression':
        # Non-linear regression: y = x1^2 + x2^2 + noise
        X = np.random.randn(n_samples, 2)
        y = (X[:, 0]**2 + X[:, 1]**2).reshape(-1, 1) + 0.1 * np.random.randn(n_samples, 1)
        return X, y
    
    elif task == 'classification':
        # Binary classification: x1^2 + x2^2 > 1
        X = np.random.randn(n_samples, 2)
        y = ((X[:, 0]**2 + X[:, 1]**2) > 1.0).astype(float).reshape(-1, 1)
        return X, y}

\code{
# Create data
X_reg, y_reg = create_synthetic_data(200, 'regression')
X_cls, y_cls = create_synthetic_data(200, 'classification')

print(f"Regression data: {X_reg.shape} -> {y_reg.shape}")
print(f"Classification data: {X_cls.shape} -> {y_cls.shape}")}



\subsection{Create and Test Neural Network}

\setupcode{from mlai.neural_networks import ReLUActivation, LinearActivation, NeuralNetwork, SigmoidActivation
from mlai.loss import MeanSquaredError, BinaryCrossEntropyLoss
from mlai.optimise import SGD, train_model}

\code{dimensions = [2, 5, 1]  # 2 inputs, 1 hidden layer (5 neurons), 1 output
activations = [ReLUActivation(), LinearActivation()]
network = NeuralNetwork(dimensions, activations)

# Test forward pass
X_test = np.array([[1.0, 2.0], [3.0, 4.0]])
y_pred = network.predict(X_test)

print("Neural Network Test:")
print(f"Input: {X_test}")
print(f"Output: {y_pred.flatten()}")
print(f"Network architecture: {dimensions}")
print(f"Number of parameters: {sum(w.size for w in network.weights) + sum(b.size for b in network.biases)}")
}


\subsection{Test Backpopagation}


\code{# Forward pass
y_pred = network.predict(X_test)
loss_fn = MeanSquaredError()
y_true = np.array([[1.0], [2.0]])

# Compute loss and gradient
loss_value = loss_fn.forward(y_pred, y_true)
loss_gradient = loss_fn.gradient(y_pred, y_true)

# Backward pass
gradients = network.backward(loss_gradient)

print("Backpropagation Test:")
print(f"Loss value: {loss_value:.4f}")
print(f"Loss gradient: {loss_gradient.flatten()}")
print(f"Weight gradients shapes: {[g.shape for g in gradients['weight_gradients']]}")
print(f"Bias gradients shapes: {[g.shape for g in gradients['bias_gradients']]}")
}

\subsection{Unified Optimisation Interface}

\loadcode{SGD}{mlai}

\code{# Demonstrate the SGD optimizer
sgd_opt = SGD(learning_rate=0.01)
print(f"SGD optimizer created with learning rate: {sgd_opt.learning_rate}")
print("SGD implements: parameters = parameters - learning_rate * gradients")}

\loadcode{train_model}{mlai}

\code{# Demonstrate the unified optimization interface with traditional NeuralNetwork
from mlai import NeuralNetwork, ReLUActivation, LinearActivation, MeanSquaredError

# Create a traditional neural network
dimensions = [2, 5, 3, 1]
activations = [ReLUActivation(), ReLUActivation(), LinearActivation()]
network = NeuralNetwork(dimensions, activations)

# Test the unified interface
X_test = np.array([[1.0, 2.0], [0.5, -1.0]])
y_test = np.array([[3.0], [1.5]])

# Forward pass
y_pred = network.predict(X_test)
print(f"Network output: {y_pred.flatten()}")

# Set up for gradient computation
loss_fn = MeanSquaredError()
loss = loss_fn.forward(y_pred, y_test)
loss_gradient = loss_fn.gradient(y_pred, y_test)
network.set_output_gradient(loss_gradient)

# Get gradients using the unified interface
gradients = network.gradients
print(f"Gradients shape: {gradients.shape}")
print(f"Parameters shape: {network.parameters.shape}")
print(f"Gradients and parameters shapes match: {gradients.shape == network.parameters.shape}")
print("This demonstrates the unified optimization interface for traditional neural networks!")}

\subsection{Train Network for Regression}

\helpercode{def train_network_regression(X, y, n_epochs=50, learning_rate=0.01):
    """Train a neural network for regression using SGD optimizer."""
    # Create network
    dimensions = [2, 10, 10, 1]
    activations = [ReLUActivation(), ReLUActivation(), LinearActivation()]
    network = NeuralNetwork(dimensions, activations)
    
    # Loss function
    loss_fn = MeanSquaredError()
    
    # Create SGD optimiser
    sgd_opt = SGD(learning_rate=learning_rate)
    
    # Use unified training interface
    losses = train_model(network, X, y, loss_fn, sgd_opt, n_epochs=n_epochs, verbose=True)
    
    return network, losses}

\code{# Train with SGD optimizer
X_reg, y_reg = create_synthetic_data(200, 'regression')
network_reg, losses = train_network_regression(X_reg, y_reg)}

\setupplotcode{import matplotlib.pyplot as plt
import mlai.plot}

\plotcode{fig, ax = plt.subplots(figsize=plot.wide_figsize)
ax.plot(losses, linewidth=2)
ax.set_xlabel('Epoch')
ax.set_ylabel('Loss')
plt.grid(True, alpha=0.3)

print(f"Final training loss: {losses[-1]:.4f}")}

mlai.write_figure("nn-regression-training-progress.svg", directory="\writeDiagramsDir/ml")
}

\figure{\includediagram{\diagramsDir/ml/nn-regression-trainng-progress"}{50%}}{Neural Network Training Progress for a regression model){nn-regression-training-progress}


\helpercode{def train_network_classification(X, y, n_epochs=500, learning_rate=0.1):
    """Train a neural network for classification using SGD optimizer."""
    # Create network
    dimensions = [2, 8, 8, 8, 8, 8, 8, 1]
    activations = [ReLUActivation(), ReLUActivation(), ReLUActivation(), ReLUActivation(), ReLUActivation(), ReLUActivation(), SigmoidActivation()]  # Sigmoid for binary classification
    network = NeuralNetwork(dimensions, activations)
    
    # Loss function
    loss_fn = BinaryCrossEntropyLoss()
    
    # Create SGD optimizer
    sgd_opt = SGD(learning_rate=learning_rate)
    
    # Training loop with custom accuracy tracking
    losses = []
    accuracies = []
    
    for epoch in range(n_epochs):
        # Forward pass
        y_pred = network.predict(X)
        loss = loss_fn.forward(y_pred, y)
        
        # Set output gradient for model
        loss_gradient = loss_fn.gradient(y_pred, y)
        network.set_output_gradient(loss_gradient)
        
        # SGD optimizer step
        sgd_opt.step(network)
        
        # Calculate accuracy
        predictions = (y_pred > 0.5).astype(float)
        accuracy = np.mean(predictions == y)
        
        losses.append(loss)
        accuracies.append(accuracy)
        
        if epoch % 10 == 0:
            print(f"Epoch {epoch:3d}: Loss = {loss:.4f}, Accuracy = {accuracy:.4f}")
    
    return network, losses, accuracies
}

\code{X_cls, y_cls = create_synthetic_data(200, 'classification')
network_cls, losses_cls, accuracies = train_network_classification(X_cls, y_cls)}

\plotcode{fig, (ax1, ax2) = plt.subplots(1, 2, figsize=plot.big_wide_figsize)

ax1.plot(losses_cls, linewidth=2, color='blue')
ax1.set_xlabel('Epoch')
ax1.set_ylabel('Loss')
ax1.grid(True, alpha=0.3)

ax2.plot(accuracies, linewidth=2, color='orange')
ax2.set_xlabel('Epoch')
ax2.set_ylabel('Accuracy')
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

print(f"Final training loss: {losses_cls[-1]:.4f}")
print(f"Final training accuracy: {accuracies[-1]:.4f}")
mlai.write_figure("classification-training.svg", directory="\writeDiagramsDir/deepnn/")}

\figure{\includediagram{\diagramsDir/deepnn/classification-training}{70%}}{Training error for the fitting of the neural network. Left is training loss, right is training accuracy}{classification-training}


\subsection{Visualise Decision Boundary}


\code{import mlai.plot
import numpy as np
import matplotlib.pyplot as plt
import mlai}

\helpercode{def plot_decision_boundary(network, X, y, filename="neural-network-decision.svg", directory="../diagrams"):
    """Plot the decision boundary of a trained neural network."""
    # Create mesh grid
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.linspace(x_min, x_max, 100),
                         np.linspace(y_min, y_max, 100))
    
    # Make predictions on mesh
    mesh_points = np.c_[xx.ravel(), yy.ravel()]
    Z = network.predict(mesh_points)
    Z = Z.reshape(xx.shape)
    
    # Plot
    plt.subplots(figsize=plot.big_figsize)
    plt.contourf(xx, yy, Z, levels=50, alpha=0.8, cmap='RdYlBu')
    plt.colorbar(label='Prediction')
    
    # Plot data points
    scatter = plt.scatter(X[:, 0], X[:, 1], c=y.flatten(), cmap='RdYlBu', 
                         edgecolors='black', linewidth=1)
    plt.colorbar(scatter, label='True Label')
    
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
	
	mlai.write_figure(filename, directory=directory)}

\plotcode{plot_decision_boundary(network_cls, X_cls, y_cls, "neural-network-decision-boundary.svg", directory="\writeDiagramsDir/deepnn/")}

\figure{\includediagram{\diagramsDir/deepnn/neural-network-decision-boundary}{50%}}{Decision boundary for the trained neural network}{neural-network-decision-boundary}

\endif

\ifndef{fromShallowToDeep}
\define{fromShallowToDeep}

\editme

\subsection{From Shallow to Deep}

\notes{A fully-connected deep network composes linear transforms and elementwise non-linearities. Under the basis-function perspective, each layer provides a new basis evaluated on the transformed inputs, then linearly combined and fed forward.}

$$
\mappingFunction(\inputVector; \mappingMatrix)  =  \mappingVector_4 ^\top\basisFunction\left(\mappingMatrix_3 \basisFunction\left(\mappingMatrix_2\basisFunction\left(\mappingMatrix_1 \inputVector\right)\right)\right).
$$

\subsection{Gradient-based optimization}

$$
\errorFunction(\mappingMatrix) = \sum_{i=1}^\numData \errorFunction(\dataVector_i, \mappingFunction(\inputVector_i; \mappingMatrix))
$$

$$
\mappingMatrix_{t+1} = \mappingMatrix_t - \eta \nabla_\mappingMatrix \errorFunction(\mappingMatrix)
$$

\subsubsection{Basic Multilayer Perceptron}

$$
\small
\mappingFunction_\numLayers(\inputVector) = \basisVector\left(\biasVector_\numLayers + \mappingMatrix_\numLayers \basisVector\left(\biasVector_{\numLayers-1} + \mappingMatrix_{\numLayers-1} \basisVector\left( \cdots \basisVector\left(\biasVector_1 + \mappingMatrix_1 \inputVector\right) \cdots \right)\right)\right)
$$

\subsubsection{Recursive MLP Definition}

\slides{\small
\begin{align}
\mappingFunction_\layerIndex(\inputVector) &= \basisVector\left(\mappingMatrix_\layerIndex \mappingFunction_{\layerIndex-1}(\inputVector) + \biasVector_\layerIndex\right),\quad l=1,\dots,\numLayers\\
\mappingFunction_0(\inputVector) &= \inputVector
\end{align}}

\subsection{Rectified Linear Unit}

\slides{
\basisVector(x) = \begin{cases}
0 & x \le 0\\
x & x > 0
\end{cases}}

\loadcode{relu_activation}{mlai}
\setupplotcode{import numpy as np
import matplotlib.pyplot as plt
import mlai
import mlai.plot as plot}

\plotcode{fig, ax = plt.subplots(figsize=plot.wide_figsize)
x = np.linspace(-3, 3, 100)
y = relu_activation(x)

ax.plot(x, y, 'b-', linewidth=3)
ax.set_xlabel('$x$')
ax.set_ylabel('$\operatorname{ReLU}(x)$')
ax.grid(True, alpha=0.3)

mlai.write_figure(filename='relu-activation.svg', directory='\writeDiagramsDir/deepnn')}

\figure{\includediagram{\diagramsDir/deepnn/relu-activation}{60%}}{The ReLU activation function: zero for negative inputs, identity for positive inputs.}{relu-activation}

\notes{Other activation functions that are used include hyperbolic tangent, sigmoid, ELU, leaky ReLU. Although ReLU is often preferred for  simplicity and fast gradient computation.}

\subsection{Shallow ReLU Networks}

\notes{A single layer ReLU network is equivalent to a generalised linear model with a ReLU basis. The difference is that we optimise over the basis function inputs.}

\slides{\small
\begin{align}
\mathbf{h}(x) &= \operatorname{ReLU}(\mathbf{w}_1 x - \mathbf{b}_1)\\
f(x) &= \mathbf{w}_2^{\top} \, \mathbf{h}(x)
\end{align}}

\notes{Each hidden unit acts as a basis function with its own kink location and slope.}

\loadcode{NeuralNetwork}{mlai}
\setupplotcode{import numpy as np
import matplotlib.pyplot as plt
import mlai
import mlai.plot as plot}

\code{x1 = np.linspace(-2, 2, 50)
x2 = np.linspace(-2, 2, 50)
X1, X2 = np.meshgrid(x1, x2)
nn = NeuralNetwork([2, 10, 1], [relu_activation, linear_activation])
X_pred = np.hstack([X1.flatten()[:, np.newaxis], X2.flatten()[:, np.newaxis]])
f_pred = nn.predict(X_pred)}

\plotcode{fig, ax = plt.subplots(figsize = plot.big_figsize)
    
levels = 30
contour = ax.contourf(X1, X2, f_pred.reshape(50, 50), levels=levels, cmap='viridis')

contour_lines = ax.contour(X1, X2, f_pred.reshape(50, 50), 
                          levels=10, colors='white', alpha=0.4, linewidths=0.5)

ax.set_xlabel('$x_1$', fontsize=12)
ax.set_ylabel('$x_2$', fontsize=12)

# Enhanced colorbar
cbar = plt.colorbar(contour, ax=ax)
cbar.set_label('Network Output', fontsize=12)

mlai.write_figure(filename='relu-network-2d.svg', directory='\writeDiagramsDir/deepnn')}

\figure{\includediagram{\diagramsDir/deepnn/relu-network-2d}{60%}}{Output of a 2D ReLU network with 3 hidden units, showing piecewise-linear regions.}{relu-network-2d}

\setupcode{import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap}


\helpercode{def visualize_relu_activations(nn, X1, X2, layer_idx=0):
    """
    Visualize which ReLU units are activated in a specific layer.
    
    :param nn: Trained neural network
    :param X1, X2: Meshgrid coordinates
    :param layer_idx: Which hidden layer to visualize (0-indexed)
    """
    # Get input data
    X_pred = np.hstack([X1.flatten()[:, np.newaxis], X2.flatten()[:, np.newaxis]])
    
    # Forward pass to get activations
    _ = nn.predict(X_pred)
    
    # Get activations for the specified layer (before activation function)
    z_layer = nn.z[layer_idx + 1]  # +1 because z[0] is input
    a_layer = nn.a[layer_idx + 1]  # Activations after ReLU
    
    n_units = z_layer.shape[1]
    n_cols = min(5, n_units)
    n_rows = (n_units + n_cols - 1) // n_cols
    
    fig, axes = plt.subplots(n_rows, n_cols, figsize=(3*n_cols, 3*n_rows))
    if n_units == 1:
        axes = [axes]
    elif n_rows == 1:
        axes = axes.reshape(1, -1)
    
    for i in range(n_units):
        row, col = i // n_cols, i % n_cols
        ax = axes[row, col] if n_rows > 1 else axes[col]
        
        # Reshape activations back to grid
        activation_grid = a_layer[:, i].reshape(X1.shape)
        
        # Create binary mask for active/inactive regions
        active_mask = activation_grid > 0
        
        # Plot with clear active/inactive distinction
        im = ax.contourf(X1, X2, activation_grid, levels=20, cmap='RdYlBu_r')
        
        # Overlay contour lines to show zero boundary
        ax.contour(X1, X2, activation_grid, levels=[0], colors='black', linewidths=2)
        
        ax.set_title(f'ReLU Unit {i+1}')
        ax.set_xlabel('$x_1$')
        ax.set_ylabel('$x_2$')
        
        # Add colorbar for each subplot
        plt.colorbar(im, ax=ax)
    
    # Hide empty subplots
    for i in range(n_units, n_rows * n_cols):
        if n_rows > 1:
            row, col = i // n_cols, i % n_cols
            axes[row, col].set_visible(False)
        elif n_cols > 1 and i < len(axes):
            axes[i].set_visible(False)
    
    plt.tight_layout()
    plt.suptitle(f'ReLU Activations - Layer {layer_idx + 1}', y=1.02, fontsize=16)
    return fig

def visualize_activation_summary(nn, X1, X2, layer_idx=0):
    """
    Create a summary visualization showing:
    1. Network output
    2. Number of active ReLUs per point
    3. Binary activation pattern
    """
    X_pred = np.hstack([X1.flatten()[:, np.newaxis], X2.flatten()[:, np.newaxis]])
    
    # Get network output and activations
    f_pred = nn.predict(X_pred)
    a_layer = nn.a[layer_idx + 1]  # Activations after ReLU
    
    # Count active units per input point
    active_count = np.sum(a_layer > 0, axis=1)
    
    fig, axes = plt.subplots(1, 3, figsize=(15, 4))
    
    # 1. Network output
    im1 = axes[0].contourf(X1, X2, f_pred.reshape(X1.shape), levels=20, cmap='viridis')
    axes[0].set_title('Network Output')
    axes[0].set_xlabel('$x_1$')
    axes[0].set_ylabel('$x_2$')
    plt.colorbar(im1, ax=axes[0])
    
    # 2. Number of active ReLUs
    im2 = axes[1].contourf(X1, X2, active_count.reshape(X1.shape), 
                          levels=np.arange(0, np.max(active_count)+2), cmap='plasma')
    axes[1].set_title('Number of Active ReLU Units')
    axes[1].set_xlabel('$x_1$')
    axes[1].set_ylabel('$x_2$')
    plt.colorbar(im2, ax=axes[1])
    
    # 3. Activation patterns (binary)
    # Create a custom colormap for binary visualization
    colors = ['darkblue', 'lightcoral']
    binary_cmap = ListedColormap(colors)
    
    # Average activation strength (normalized)
    avg_activation = np.mean(a_layer, axis=1)
    binary_mask = (avg_activation > 0).astype(int)
    
    im3 = axes[2].contourf(X1, X2, binary_mask.reshape(X1.shape), 
                          levels=[0, 0.5, 1], cmap=binary_cmap)
    axes[2].set_title('Average Activation Pattern\n(Blue=Inactive, Red=Active)')
    axes[2].set_xlabel('$x_1$')
    axes[2].set_ylabel('$x_2$')
    
    plt.tight_layout()
    return fig

def visualize_decision_boundaries(nn, X1, X2, layer_idx=0):
    """
    Visualize the linear decision boundaries created by each ReLU unit.
    """
    X_pred = np.hstack([X1.flatten()[:, np.newaxis], X2.flatten()[:, np.newaxis]])
    
    # Get pre-activation values (before ReLU)
    _ = nn.predict(X_pred)
    z_layer = nn.z[layer_idx + 1]
    
    n_units = z_layer.shape[1]
    
    fig, ax = plt.subplots(figsize=(8, 8))
    
    # Plot decision boundary for each unit
    colors = plt.cm.tab10(np.linspace(0, 1, n_units))
    
    for i in range(n_units):
        z_grid = z_layer[:, i].reshape(X1.shape)
        
        # Plot the zero-level contour (decision boundary)
        contour = ax.contour(X1, X2, z_grid, levels=[0], 
                           colors=[colors[i]], linewidths=2, alpha=0.7)
        
        # Label the contour - check if contour has any paths
        if contour.get_paths():
            ax.clabel(contour, inline=True, fontsize=10, fmt=f'Unit {i+1}')
    
    # Also show regions where network output is positive/negative
    f_pred = nn.predict(X_pred)
    ax.contourf(X1, X2, f_pred.reshape(X1.shape), levels=[-100, 0, 100], 
               colors=['lightblue', 'lightcoral'], alpha=0.3)
    
    ax.set_xlabel('$x_1$')
    ax.set_ylabel('$x_2$')
    ax.set_title('ReLU Decision Boundaries\n(Background: Network Output Sign)')
    ax.grid(True, alpha=0.3)
    
    return fig}

\plotcode{x1 = np.linspace(-2, 2, 50)
x2 = np.linspace(-2, 2, 50)
X1, X2 = np.meshgrid(x1, x2)

# Create and use network
nn = NeuralNetwork([2, 10, 1], [relu_activation, linear_activation])

# Generate visualizations
fig1 = visualize_relu_activations(nn, X1, X2, layer_idx=0)
fig2 = visualize_activation_summary(nn, X1, X2, layer_idx=0)
fig3 = visualize_decision_boundaries(nn, X1, X2, layer_idx=0)}


\slides{Complexity (1D): number of kinks $\propto$ width of network.}

\subsection{Depth vs Width: Representation Power}

\notes{ReLU networks implement piecewise-linear functions. Increasing the width of the network increases the number of linear pieces roughly linearly, increasing the depth increases them exponentially. This exponential growth in representational power with depth is what makes deep networks so powerful for complex function approximation.}

\slides{* Single hidden layer: number of kinks $\approx O(\text{width})$
* Deep ReLU networks: kinks $\approx O(2^{\text{depth}})$}

\subsection{Sawtooth Construction}

\notes{The sawtooth construction provides a concrete example of how depth leads to exponential growth in representational power. This 1D construction shows how each layer doubles the number of linear segments.}

\slides{\small
\begin{align}
\mappingFunction_l(x) &= 2\vert \mappingFunction_{l-1}(x)\vert - 2, \quad \mappingFunction_0(x) = x\\
\mappingFunction_l(x) &= 2 
  \operatorname{ReLU}(\mappingFunction_{l-1}(x)) + 2 
  \operatorname{ReLU}(-\mappingFunction_{l-1}(x)) - 2
\end{align}}

\notes{In higher dimensions, these become polyhedral regions with constant gradients inside each region. Each layer creates more complex boundaries between linear regions.}

\setupplotcode{import numpy as np
import matplotlib.pyplot as plt
import mlai
import mlai.plot as plot}

\plotcode{# Sawtooth construction visualization
def sawtooth_layer(x, layer):
    """Apply sawtooth construction for given layer"""
    if layer == 0:
        return x
    else:
        prev = sawtooth_layer(x, layer - 1)
        return 2 * np.abs(prev) - 2

# Create input data
x = np.linspace(-2, 2, 1000)

# Plot different depths
fig, axes = plt.subplots(2, 3, figsize=(15, 10))
axes = axes.flatten()

for depth in range(6):
    y = sawtooth_layer(x, depth)
    axes[depth].plot(x, y, 'b-', linewidth=2)
    axes[depth].set_title(f'Depth {depth}')
    axes[depth].set_xlabel('$x$')
    axes[depth].set_ylabel('$f_{' + str(depth) + '}(x)$')
    axes[depth].grid(True, alpha=0.3)

plt.tight_layout()
mlai.write_figure(filename='sawtooth-construction.svg', directory='\writeDiagramsDir/deepnn')}

\figure{\includediagram{\diagramsDir/deepnn/sawtooth-construction}{80%}}{Sawtooth construction showing exponential growth of linear segments with depth. Each layer doubles the number of kinks.}{sawtooth-construction}

\slides{Complexity (1D): number of kinks $\approx O(2^{\text{depth}})$.}

\subsection{Higher-dimensional Geometry}

\notes{In 2D, ReLU networks partition input space into many polygonal regions. Within each region the mapping is linear, yet globally the function is continuous because adjacent regions meet with consistent boundary values. Depth increases the number and intricacy of these regions across layers.}

\slides{* Regions: piecewise-linear, often triangular/polygonal in 2D
* Continuity arises despite stitching flat regions
* Early layers: few regions; later layers: many more}

\setupplotcode{import numpy as np
import matplotlib.pyplot as plt
import mlai
import mlai.plot as plot}

\plotcode{nn = NeuralNetwork([2, 4, 4, 1], [relu_activation, relu_activation, linear_activation])

# Create 2D input grid
x1 = np.linspace(-3, 3, 100)
x2 = np.linspace(-3, 3, 100)
X1, X2 = np.meshgrid(x1, x2)

# Deep ReLU network: 2 inputs -> 4 hidden -> 4 hidden -> 1 output
# Layer 1 weights and biases
nn.weights[0] = np.array([[1, 0.5], [0.5, 1], [-0.5, 0.5], [0.5, -0.5]])
nn.biases[0] = np.array([0, -0.5, 0.5, 0])

# Layer 2 weights and biases  
nn.weights[1] = np.array([[1, 0.5, -0.5, 0.5], [0.5, 1, 0.5, -0.5], [-0.5, 0.5, 1, 0.5], [0.5, -0.5, 0.5, 1]])
nn.biases[1] = np.array([0, -0.5, 0.5, 0])

# Layer 3 weights and biases
nn.weights[2] = np.ones((4, 1))
nn.biases[2] = np.zeros(1)

f = nn.predict(np.hstack([X1(:), X2(:)]))

# Plot the result
fig, ax = plt.subplots(figsize=plot.big_figsize)
contour = ax.contourf(X1, X2, f, levels=30, cmap='viridis')
ax.set_xlabel('$x_1$')
ax.set_ylabel('$x_2$')
plt.colorbar(contour, ax=ax)

mlai.write_figure(filename='deep-relu-2d.svg', directory='\writeDiagramsDir/deepnn')}

\figure{\includediagram{\diagramsDir/deepnn/deep-relu-2d}{60%}}{Deep ReLU network output showing complex piecewise-linear regions in 2D. Each region has constant gradient, but the overall function is continuous.}{deep-relu-2d}

\endif

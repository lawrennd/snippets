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

\setupcode{from mlai import Activation}
\loadcode{ReLUActivation}{mlai}

\setupplotcode{import numpy as np
import matplotlib.pyplot as plt
import mlai
import mlai.plot as plot}

\plotcode{fig, ax = plt.subplots(figsize=plot.wide_figsize)
x = np.linspace(-3, 3, 100)
act = ReLUActivation().forward(x)

ax.plot(x, act, 'b-', linewidth=3)
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
nn = NeuralNetwork([2, 10, 1], [ReLUActivation(), LinearActivation()])
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


\helpercode{# Cell 2: Create Synthetic Data
def create_synthetic_data(n_samples=100, task='regression'):
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
        return X, y
}

\code{x1 = np.linspace(-2, 2, 50)
x2 = np.linspace(-2, 2, 50)
X1, X2 = np.meshgrid(x1, x2)

# Create and use network
nn = NeuralNetwork([2, 10, 1], [ReLUActivation(), LinearActivation()])}

\newslide{ReLU Activations}

\plotcode{plot.visualise_relu_activations(nn, X1, X2, layer_idx=0, directory="\writeDiagramsDir/deepnn")}

\figure{\includediagram{\diagramsDir/deepnn/relu-activations}{50%}}{Decision boundaries for the ReLU network.}{relu-activations}

\newslide{Decision Boundaries}

\plotcode{plot.visualise_activation_summary(nn, X1, X2, layer_idx=0, directory="\writeDiagramsDir/deepnn")}

\figure{\includediagram{\diagramsDir/deepnn/activation-summary}{50%}}{Decision boundaries for the ReLU network.}{decision-boundaries}

\newslide{Decision Boundaries}

\plotcode{plot.visualise_decision_boundaries(nn, X1, X2, layer_idx=0, directory='\writeDiagramsDir/deepnn')}

\figure{\includediagram{\diagramsDir/deepnn/decision-boundaries}{50%}}{Decision boundaries for the ReLU network.}{decision-boundaries}

\slides{Complexity (1D): number of kinks $\propto$ width of network.}

\subsection{Depth vs Width: Representation Power}

\notes{ReLU networks implement piecewise-linear functions. Increasing the width of the network increases the number of linear pieces roughly linearly, increasing the depth increases them exponentially. This exponential growth in representational power with depth is what makes deep networks so powerful for complex function approximation.}

\slides{* Single hidden layer: number of kinks $\approx O(\text{width})$
* Deep ReLU networks: kinks $\approx O(2^{\text{depth}})$}

\subsection{Sawtooth Construction}

\notes{The sawtooth construction provides an example of how depth can to exponential growth in representational power. This 1D construction shows how each layer doubles the number of linear segments.}

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

\plotcode{nn = NeuralNetwork([2, 4, 4, 1], [ReLUActivation(), ReLUActivation(), LinearActivation()])

# Create 2D input grid
x1 = np.linspace(-3, 3, 100)
x2 = np.linspace(-3, 3, 100)
X1, X2 = np.meshgrid(x1, x2)

# Deep ReLU network: 2 inputs -> 4 hidden -> 4 hidden -> 1 output
# Layer 1 weights and biases
nn.weights[0] = np.array([[1, 0.5], [0.5, 1], [-0.5, 0.5], [0.5, -0.5]]).T
nn.biases[0] = np.array([0, -0.5, 0.5, 0])

# Layer 2 weights and biases  
nn.weights[1] = np.array([[1, 0.5, -0.5, 0.5], [0.5, 1, 0.5, -0.5], [-0.5, 0.5, 1, 0.5], [0.5, -0.5, 0.5, 1]]).T
nn.biases[1] = np.array([0, -0.5, 0.5, 0])

# Layer 3 weights and biases
nn.weights[2] = np.ones((4, 1))
nn.biases[2] = np.zeros(1)

f = nn.predict(np.hstack([X1.flatten()[:, np.newaxis], X2.flatten()[:, np.newaxis]]))

# Plot the result
fig, ax = plt.subplots(figsize=plot.big_figsize)
contour = ax.contourf(X1, X2, f.reshape(X1.shape), levels=30, cmap='viridis')
ax.set_xlabel('$x_1$')
ax.set_ylabel('$x_2$')
plt.colorbar(contour, ax=ax)

mlai.write_figure(filename='deep-relu-2d.svg', directory='\writeDiagramsDir/deepnn')}

\figure{\includediagram{\diagramsDir/deepnn/deep-relu-2d}{60%}}{Deep ReLU network output showing complex piecewise-linear regions in 2D. Each region has constant gradient, but the overall function is continuous.}{deep-relu-2d}

\endif

\ifndef{chainRuleNeuralNetwork}
\define{chainRuleNeuralNetwork}

\editme

\subsection{Chain Rule for Neural Networks}

\newslide{Neural Network Chain Rule}

\slides{* **Goal**: compute gradients for neural networks
* **Approach**: apply matrix derivative rules
* **Key**: three fundamental gradients needed}

\notes{We're now in a position to write down the chain rule for neural
networks.}

\newslide{Neural Network Structure}

\slidesmall{$$\mappingFunctionVector_\layerIndex = \mappingMatrix_\layerIndex \basisVector_{\layerIndex-1}$$}

\slidesmall{$$\basisVector_{\layerIndex} = \basisVector_{\layerIndex}(\mappingFunctionVector_{\layerIndex})$$}

\slides{* **Activations**: $\mappingFunctionVector_\layerIndex$ at layer $\layerIndex$
* **Basis functions**: applied to activations
* **Weight matrix**: $\mappingMatrix_\layerIndex$}

\notes{To make our derivations general, we will split up the neural
network in the following way. First we describe the activations at
layer $\layerIndex$, $\mappingFunctionVector_\layerIndex$ given the
basis functions from the previous layer,
$\basisVector_{\layerIndex-1}$ in terms of the weight matrix,
$\mappingMatrix_\layerIndex$.
$$
\mappingFunctionVector_\layerIndex = \mappingMatrix_\layerIndex \basisVector_{\layerIndex-1}
$$
where the basis vector at any given layer $\layerIndex$ is given by applying the basis functions to the activations,
$$
\basisVector_{\layerIndex} = \basisVector_{\layerIndex}(\mappingFunctionVector_{\layerIndex}),
$$
where $\basisVector_{\layerIndex}(\cdot)$ represents the form of the basis functions at the $\layerIndex$th layer.

Notation note: here $\mappingFunctionVector_\layerIndex$ is the *pre-activation* (affine transform of the previous layer). On the recursive MLP slide, the same letter is sometimes used for the *post-activation* output. In this section, post-activation quantities are always written $\basisVector_\layerIndex$ (or $\mathbf{h}$ at the final layer).}

\newslide{First and Final Layers}

\slidesmall{$$\mappingFunctionVector_1 = \mappingMatrix_1 \inputVector$$}

\slidesmall{$$\mathbf{\transformationFunction} = \mathbf{\transformationFunction}(\mappingFunctionVector_L)$$}

\slides{* **First layer**: $\mappingFunctionVector_1 = \mappingMatrix_1 \inputVector$
* **Final layer**: inverse link function
* **Dummy basis**: $\mathbf{h} = \basisVector_L$}

\notes{These two equations give us everything we need apart from the first layer and final layers where we have
$$
\mappingFunctionVector_1 = \mappingMatrix_1 \inputVector
$$
for the first layer. Here we are *not* showing the index on the data point $i$ to avoid cluttering the notation. In the final layer we have the output of the network given by the inverse link function, 
$$
\mathbf{\transformationFunction} = \mathbf{\transformationFunction}(\mappingFunctionVector_L).
$$
so we can assume dummy-basis functions for the output layer and take $\mathbf{h} = \basisVector_L$.}

\newslide{Limitations}

\slides{* **Skip connections**: not captured in this formalism
* **Example**: layer $\layerIndex-2$ → layer $\layerIndex$
* **Sufficient**: for main aspects of deep network gradients}

\notes{This formalism isn't fully general as it doesn't capture the possibility of skip connections where a weight matrix connects e.g. basis functions from layer $\layerIndex-2$ to the activations of layer $\layerIndex$. But it's sufficient to capture the main aspects of deep neural network gradients.}

\newslide{Three Fundamental Gradients}

\slides{* **Activation gradient**: $\frac{\text{d}\mappingFunctionVector_\layerIndex}{\text{d}\mappingVector_\layerIndex}$
* **Basis gradient**: $\frac{\text{d}\basisVector_{\layerIndex}}{\text{d} \mappingFunctionVector_{\layerIndex}}$
* **Across-layer gradient**: $\frac{\text{d}\mappingFunctionVector_\layerIndex}{\text{d}\basisVector_{\layerIndex-1}}$}

\notes{These fundamental operations now allow us to use our matrix
derivative rules to compute the gradients of the neural network with
respect to any layer of weights. To do this we need three fundamental
gradients. First the activation gradient,}

\newslide{Activation Gradient}

\slidesmall{$$\frac{\text{d}\mappingFunctionVector_\layerIndex}{\text{d}\mappingVector_\layerIndex} = \basisVector_{\layerIndex-1}^\top \otimes \eye_{\layerDim_\layerIndex}$$}

\slides{* **Size**: $\layerDim_\layerIndex \times (\layerDim_\layerIndex \layerDim_{\layerIndex-1})$
* **Input**: $\mappingFunctionVector_\layerIndex$ and $\mappingVector_\layerIndex$
* **Kronecker product**: key to the result}

\notes{$\tfrac{\text{d}\mappingFunctionVector_\layerIndex}{\text{d}\mappingVector_\layerIndex}$
where we have defined $\mappingVector_\layerIndex =
(\mappingMatrix_\layerIndex)\!:$. This gradient is between a
$\layerDim_\layerIndex$ dimensional vector,
$\mappingFunctionVector_\layerIndex$, and a $\layerDim_\layerIndex
\layerDim_{\layerIndex-1} \times 1$ dimensional vector, so it produces a matrix
that is $\layerDim_\layerIndex \times (\layerDim_\layerIndex
\layerDim_{\layerIndex-1})$,
$$
\frac{\text{d}\mappingFunctionVector_\layerIndex}{\text{d}\mappingVector_\layerIndex}
= \basisVector_{\layerIndex-1}^\top \otimes \eye_{\layerDim_\layerIndex}.  
$$
}

\newslide{Basis Gradient}

\slidesmall{$$\frac{\text{d}\basisVector_{\layerIndex}}{\text{d} \mappingFunctionVector_{\layerIndex}} = \basisMatrix^\prime$$}

\slidesmall{$$\frac{\text{d}\basisScalar_i^{(\layerIndex)}(\mappingFunctionVector_{\layerIndex})}{\text{d} \mappingFunction_j^{(\layerIndex)}}$$}

\slides{* **Size**: $\layerDim_\layerIndex \times \layerDim_\layerIndex$ matrix
* **Elements**: derivatives of basis functions
* **Diagonal**: if basis functions depend only on their own activations}

\notes{We represent the gradient 
$$
\frac{\text{d}\basisVector_{\layerIndex}}{\text{d} \mappingFunctionVector_{\layerIndex}} = \basisMatrix^\prime
$$
which is a $\layerDim_\layerIndex \times \layerDim_\layerIndex$ sized matrix whose elements are given by
$$
\frac{\text{d}\basisScalar_i^{(\layerIndex)}(\mappingFunctionVector_{\layerIndex})}{\text{d} \mappingFunction_j^{(\layerIndex)}}
$$
where
$\basisScalar_i^{(\layerIndex)}(\mappingFunctionVector_{\layerIndex})$
is the $i$th basis function from the $\layerIndex$th layer and
$\mappingFunction_j^{(\layerIndex)}$ is the $j$th activation from the
same layer. If
$\basisScalar_i^{(\layerIndex)}(\mappingFunctionVector_{\layerIndex})
= \basisScalar_i^{(\layerIndex)}(\mappingFunction^{(\layerIndex)}_i)$
then this matrix is diagonal.}

\setupcode{from mlai.neural_networks import Activation}

\loadcode{LinearActivation}{mlai.neural_networks}
\loadcode{ReLUActivation}{mlai.neural_networks}
\loadcode{SigmoidActivation}{mlai.neural_networks}
\loadcode{SoftReLUActivation}{mlai.neural_networks}

\code{x = np.linspace(-3, 3, 100)
activations = {
    'Linear': LinearActivation(),
    'ReLU': ReLUActivation(),
    'Sigmoid': SigmoidActivation(),
    'Soft ReLU': SoftReLUActivation()
}
}

\setupplotcode{import matplotlib.pyplot as plt
from mlai.utils import write_figure
from mlai import plot}
\plotcode{plt.figure(figsize=plot.big_wide_figsize)
for i, (name, activation) in enumerate(activations.items()):
    plt.subplot(2, 2, i+1)
    y = activation.forward(x)
    y_grad = activation.gradient(x)
    
    plt.plot(x, y, 'b-', linewidth=2, label=f'{name}(x)')
    plt.plot(x, y_grad, 'r--', linewidth=2, label=f"d{name}/dx")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(f'{name} Activation Function')
    plt.grid(True, alpha=0.3)

plt.tight_layout()

write_figure('activation-functions.svg', directory="\writeDiagramsDir/deepnn")}

\newslide{Activations and Gradients}

\figure{\includediagram{\diagramsDir/deepnn/activation-functions}{70%}}{Some different activation functions (solid line) and their gradients (dashed line).}{activation-functions}

\newslide{Across-Layer Gradient}

\slidesmall{$$\frac{\text{d}\mappingFunctionVector_\layerIndex}{\text{d}\basisVector_{\layerIndex-1}} = \mappingMatrix_\layerIndex$$}

\slides{* **Size**: $\layerDim_\layerIndex \times \layerDim_{\layerIndex -1}$
* **Matches**: shape of $\mappingMatrix_\layerIndex$
* **Simple**: just the weight matrix itself}

\notes{Then we have the *across layer* gradients
$$
\frac{\text{d}\mappingFunctionVector_\layerIndex}{\text{d}\basisVector_{\layerIndex-1}} = \mappingMatrix_\layerIndex,
$$
which should be a $\layerDim_\layerIndex \times \layerDim_{\layerIndex -1}$ size matrix, which matches the shape of $\mappingMatrix_\layerIndex$. 
}

\newslide{Complete Chain Rule}

\slidesmall{$$\frac{\text{d} \mappingFunctionVector_\ell}{\text{d}\mappingVector_{\ell-k}} = \left[\prod_{i=0}^{k-1} \left(\frac{\text{d} \mappingFunctionVector_{\ell - i}}{\text{d} \basisVector_{\ell - i -1}}\frac{\text{d} \basisVector_{\ell - i -1}}{\text{d} \mappingFunctionVector_{\ell - i -1}}\right)\right] \frac{\text{d} \mappingFunctionVector_{\ell-k}}{\text{d} \mappingVector_{\ell - k}}$$}

\slides{* **Product**: of all intermediate gradients ($i=0$ on the left)
* **Chain**: from layer $\ell$ back to layer $\ell-k$
* **Complete**: gradient of activations w.r.t.\ earlier weights}

\newslide{Substituted Matrix Form}

\slidesmall{$$\frac{\text{d} \mappingFunctionVector_\ell}{\text{d}\mappingVector_{\ell-k}} = \left[\prod_{i=0}^{k-1} \left(\mappingMatrix_{\ell - i} \basisMatrix^\prime_{\ell - i -1}\right)\right] \left(\basisVector_{\ell-k-1}^\top \otimes \eye_{\layerDim_{\ell-k}}\right)$$}

\slides{* **Weight matrices**: $\mappingMatrix_{\ell - i}$ for across-layer gradients
* **Basis derivatives**: $\basisMatrix^\prime_{\ell - i -1}$ for activation derivatives
* **Final term**: Kronecker product for activation gradient}

\notes{This now gives us the ability to compute the gradient of any
$\mappingMatrix_\ell$ in the model,
$$
\frac{\text{d}
\mappingFunctionVector_\ell}{\text{d}\mappingVector_{\ell-k}} =
\left[\prod_{i=0}^{k-1} \left(\frac{\text{d} \mappingFunctionVector_{\ell - i}}{\text{d} \basisVector_{\ell - i -1}}\frac{\text{d} \basisVector_{\ell - i -1}}{\text{d} \mappingFunctionVector_{\ell - i -1}}\right)\right]
\frac{\text{d} \mappingFunctionVector_{\ell-k}}{\text{d}
\mappingVector_{\ell - k}}
$$
with the product ordered so that $i=0$ appears on the left. Substituting the matrix derivatives we derived:
$$
\frac{\text{d}
\mappingFunctionVector_\ell}{\text{d}\mappingVector_{\ell-k}} =
\left[\prod_{i=0}^{k-1} \left(\mappingMatrix_{\ell - i} \basisMatrix^\prime_{\ell - i -1}\right)\right]
\left(\basisVector_{\ell-k-1}^\top \otimes \eye_{\layerDim_{\ell-k}}\right)
$$
where $\basisMatrix^\prime_{\ell - i -1}$ is the derivative matrix for the basis functions at layer $\ell - i -1$.}

\newslide{From Activations to the Loss}

\slides{* **Still need**: $\frac{\text{d}\errorFunction}{\text{d}\mappingVector}$
* **Tool**: $(\mathbf{E}:)^\top(\mathbf{F}\otimes\mathbf{G})$ identity
* **Result**: multiply on the left by $\frac{\text{d}\errorFunction}{\text{d}\mappingFunctionVector_\ell}$}

\notes{The formulae above give $\frac{\text{d}\mappingFunctionVector_\ell}{\text{d}\mappingVector_{\ell-k}}$. Training requires the loss gradient $\frac{\text{d}\errorFunction}{\text{d}\mappingVector_{\ell-k}}$. Using the stacking identity introduced earlier,
$$
(\mathbf{E}:)^{\top} (\mathbf{F} \otimes \mathbf{G}) = \bigl((\mathbf{G}^{\top} \mathbf{E} \mathbf{F}):\bigr)^{\top},
$$
we multiply on the left by the (row) gradient of the loss with respect to the layer activations. In code this left factor is the backpropagated `delta` / `output_gradient`.}

\notes{**Notes versus code.** The derivation uses column vectors and $\mappingFunctionVector_\layerIndex = \mappingMatrix_\layerIndex \basisVector_{\layerIndex-1}$ without biases. The `NeuralNetwork` implementation uses a row-vector layout, $\mathbf{z} = \boldsymbol{\phi}\,@\,\mathbf{W} + \mathbf{b}$, so its weight matrix is the transpose of $\mappingMatrix_\layerIndex$ above, and biases are included. Under that layout the Kronecker term collapses to an outer product of the layer input and the backpropagated delta — which is what `backward` and `compute_gradient_for_layer` compute.}

\subsection{Gradient Verification}

\loadcode{finite_difference_jacobian}{mlai.utils}
\loadcode{verify_gradient_implementation}{mlai.utils}

\setupcode{import numpy as np}

\code{# Test data
x = np.array([1.0, -2.0, 0.5, -0.1])
results = {}}

\code{# Test Linear Activation
linear_activation = LinearActivation()
def linear_func(x):
	return linear_activation.forward(x)

numerical_grad = finite_difference_jacobian(linear_func, x)
analytical_grad = np.diag(linear_activation.gradient(x))
results['Linear'] = verify_gradient_implementation(analytical_grad, numerical_grad)
print(f"Linear Activation: {'PASS' if results['Linear'] else 'FAIL'}")}
    
\code{# Test ReLU Activation
relu_activation = ReLUActivation()
def relu_func(x):
	return relu_activation.forward(x)

numerical_grad = finite_difference_jacobian(relu_func, x)
analytical_grad = np.diag(relu_activation.gradient(x))
results['ReLU'] = verify_gradient_implementation(analytical_grad, numerical_grad)
print(f"ReLU Activation: {'PASS' if results['ReLU'] else 'FAIL'}")}
    
\code{# Test Sigmoid Activation
sigmoid_activation = SigmoidActivation()
def sigmoid_func(x):
	return sigmoid_activation.forward(x)

numerical_grad = finite_difference_jacobian(sigmoid_func, x)
analytical_grad = np.diag(sigmoid_activation.gradient(x))
results['Sigmoid'] = verify_gradient_implementation(analytical_grad, 
numerical_grad)
print(f"Sigmoid Activation: {'PASS' if results['Sigmoid'] else 'FAIL'}")}
    
\code{# Test Soft ReLU Activation
soft_relu_activation = SoftReLUActivation()
def soft_relu_func(x):
	return soft_relu_activation.forward(x)

numerical_grad = finite_difference_jacobian(soft_relu_func, x)
analytical_grad = np.diag(soft_relu_activation.gradient(x))
results['SoftReLU'] = verify_gradient_implementation(analytical_grad, 
numerical_grad)
print(f"Soft ReLU Activation: {'PASS' if results['SoftReLU'] else 'FAIL'}")}
	
\subsection{Verify Neural Network Gradients}

\notes{Testing neural network gradients with finite differences}
    
\code{results = {}}
    
\code{# Test 1: Simple linear network
print("\nTesting simple linear network...")
dimensions = [2, 2, 1]
activations = [LinearActivation(), LinearActivation()]

# Create network
network = NeuralNetwork(dimensions, activations)
x = np.array([[1.0, 2.0]])

# Forward pass to populate z and a attributes
network.predict(x)

# Test gradient with respect to first weight matrix
def network_output_w0(w0_flat):
	w0 = w0_flat.reshape(network.weights[0].shape)
	test_network = NeuralNetwork(dimensions, activations)
	test_network.weights[0] = w0
	test_network.biases[0] = network.biases[0]
	test_network.weights[1] = network.weights[1]
	test_network.biases[1] = network.biases[1]
	return test_network.predict(x).flatten()

w0_flat = network.weights[0].flatten()
numerical_grad = finite_difference_jacobian(network_output_w0, w0_flat).flatten()

output_gradient = np.array([[1.0]])
analytical_grad = network.compute_gradient_for_layer(0, output_gradient).flatten()

results['Linear_Network'] = verify_gradient_implementation(analytical_grad, 
numerical_grad, rtol=1e-4)
print(f"Linear Network: {'PASS' if results['Linear_Network'] else 'FAIL'}")}

\code{# Test 2: Network with ReLU activation
print("\nTesting network with ReLU activation...")
dimensions = [2, 3, 1]
activations = [ReLUActivation(), LinearActivation()]
network = NeuralNetwork(dimensions, activations)

# Forward pass to populate z and a attributes
network.predict(x)

def network_output_w0_relu(w0_flat):
	w0 = w0_flat.reshape(network.weights[0].shape)
	test_network = NeuralNetwork(dimensions, activations)
	test_network.weights[0] = w0
	test_network.biases[0] = network.biases[0]
	test_network.weights[1] = network.weights[1]
	test_network.biases[1] = network.biases[1]
	return test_network.predict(x).flatten()

w0_flat = network.weights[0].flatten()
numerical_grad = finite_difference_jacobian(network_output_w0_relu, w0_flat).flatten()

analytical_grad = network.compute_gradient_for_layer(0, output_gradient).flatten()

results['ReLU_Network'] = verify_gradient_implementation(analytical_grad, 
numerical_grad, rtol=1e-4)
print(f"ReLU Network: {'PASS' if results['ReLU_Network'] else 'FAIL'}")}
    
\code{# Test Network with sigmoid activation
print("\nTesting network with sigmoid activation...")
dimensions = [2, 3, 1]
activations = [SigmoidActivation(), LinearActivation()]
network = NeuralNetwork(dimensions, activations)

# Forward pass to populate z and a attributes
network.predict(x)

def network_output_w0_sigmoid(w0_flat):
	w0 = w0_flat.reshape(network.weights[0].shape)
	test_network = NeuralNetwork(dimensions, activations)
	test_network.weights[0] = w0
	test_network.biases[0] = network.biases[0]
	test_network.weights[1] = network.weights[1]
	test_network.biases[1] = network.biases[1]
	return test_network.predict(x).flatten()

w0_flat = network.weights[0].flatten()
numerical_grad = finite_difference_jacobian(network_output_w0_sigmoid, w0_flat).flatten()

analytical_grad = network.compute_gradient_for_layer(0, output_gradient).flatten()

results['Sigmoid_Network'] = verify_gradient_implementation(analytical_grad, 
numerical_grad, rtol=1e-4)
print(f"Sigmoid Network: {'PASS' if results['Sigmoid_Network'] else 'FAIL'}")
}

\notes{The checks above only cover `compute_gradient_for_layer(0, ...)` for a single data point. The next cell verifies `backward` through the full `parameters` / `gradients` interface, including biases, deeper layers and a small batch.}

\code{# Full-parameter check: weights, biases, deeper layers, batch
from mlai.utils import finite_difference_gradient

print("\nTesting full network.gradients against finite differences...")
dimensions = [2, 4, 3, 1]
activations = [ReLUActivation(), SigmoidActivation(), LinearActivation()]
network = NeuralNetwork(dimensions, activations)
X_batch = np.array([[1.0, 2.0], [0.5, -1.0], [-0.3, 0.8]])

network.predict(X_batch)
network.set_output_gradient(np.ones((X_batch.shape[0], 1)))
analytical_grad = network.gradients

def network_sum_output(params):
	temp = NeuralNetwork(dimensions, activations)
	temp.parameters = params
	return np.sum(temp.predict(X_batch))

numerical_grad = finite_difference_gradient(network_sum_output, network.parameters)
results['Full_Parameters'] = verify_gradient_implementation(
	analytical_grad, numerical_grad, rtol=1e-4)
print(f"Full parameters (backward): {'PASS' if results['Full_Parameters'] else 'FAIL'}")
}

\endif

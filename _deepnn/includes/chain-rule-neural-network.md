\ifndef{chainRuleNeuralNetwork}
\define{chainRuleNeuralNetwork}

\editme

\subsection{Chain Rule for Neural Networks}

\notes{We're now in a position to write down the chain rule for neural
networks.}

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
where $\mappingFunctionVector_{\layerIndex}(\cdot)$ represents the form of the basis functions at the $\layerIndex$th layer. These two equations give us everything we need apart from the first layer and final layers where we have
$$
f_1 = \mappingMatrix_1 \inputVector
$$
for the first layer. Here we are *not* showing the index on the data point $i$ to avoid cluttering the notation. In the final layer we have the output of the network given by the inverse link function, 
$$
\mathbf{\transformationFunction} = \mathbf{\transformationFunction}(\mappingFunctionVector_L).
$$
so we can assume dummy-basis functions for the output layer and take $\mathbf{h} = \basisVector_L$.}

\notes{This formalism isn't fully general as it doesn't capture the possibility of skip connections where a weight matrix connects e.g. basis functions from layer $\layerIndex-2$ to the activations of layer $\layerIndex$. But it's sufficient to capture the main aspects of deep neural network gradients.}

\notes{These fundamental operations now allow us to use our matrix
derivative rules to compute the gradients of the neural network with
respect to any layer of weights. To do this we need three fundamental
gradients. First the activation gradient,
$\tfrac{\text{d}\mappingFunctionVector_\layerIndex}{\text{d}\mappingVector_\layerIndex}$
where we have defined $\mappingFunctionVector_\layerIndex =
(\mappingFunctionVector_\layerIndex)\!:$. This gradient is between a
$\layerDim_\layerIndex$ dimensional vector,
$\mappingFunctionVector_\layerIndex$, and a $(\layerDim_{\layerIndex
-1})\layerDim \times 1$ dimensional vector, so it produces a matrix
that is $\layerDim_\layerIndex \times (\layerDim_{\layerIndex-1}
\layerDim)$,
$$
\frac{\text{d}\mappingFunctionVector_\layerIndex}{\text{d}\mappingVector_\layerIndex}
= \basisVector_{\ell-1}^\top \otimes \eye_{\layerDim_\layerIndex}.  
$$
}

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

\notes{Then we have the *across layer* gradients
$$
\frac{\text{d}\mappingFunctionVector_\layerIndex}{\text{d}\basisVector_{\layerIndex-1}} = \mappingMatrix_\layerIndex,
$$
which should be a $\layerDim_\layerIndex \times \layerDim_{\layerIndex -1}$ size matrix, which matches the shape of $\mappingMatrix_\layerIndex$. 
}

\notes{This now gives us the ability to compute the gradient of any
$\mappingMatrix_\ell$ in the model,
$$
\frac{\text{d}
\mappingFunctionVector_\ell}{\text{d}\mappingVector_{\ell-k}} =
\left[\prod_{i=0}^{k-1} \frac{\text{d} \mappingFunctionVector_{\ell - i}}{\text{d} \basisVector_{\ell - i -1}}\frac{\text{d} \basisVector_{\ell - i -1}}{\text{d} \mappingFunctionVector_{\ell - i -1}}\right]
\frac{\text{d} \mappingFunctionVector_{\ell-k}}{\text{d}
\mappingVector_{\ell - k}}
$$
}

\endif

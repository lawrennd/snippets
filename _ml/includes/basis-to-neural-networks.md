\ifndef{basisToNeuralNetworksJax}
\define{basisToNeuralNetworksJax}

\editme

\subsection{From Basis Functions to Neural Networks (JAX)}

\notes{So far we have been using `numpy` for building our models. In this session we are going to make use of `JAX`.}

\setupcode{import jax
import jax.numpy as jnp
from jax import random, grad, jit, value_and_grad
from functools import partial

\setupplotcode{import matplotlib.pyplot as plt
import mlai.plot as plot}

\subsection{Linear Models as Basis + Weights}

\notes{The generalised linear models we work with allow us to create a model that is non-linear in inputs, but linear in the parameters,
$$
\mappingFunction(\inputVector_i) = \mappingVector^\top \basisFunctionVector(\inputVector_i).
$$
We defined a basis, such as the quadratic basis.}
\setupcode{import jax.numpy as jnp}

\code{def jax_quadratic(x, **kwargs):
    """Take in a vector of input values and return the design matrix associated with quadratic basis functions."""
	return jnp.hstack([jnp.ones((x.shape[0], 1)), x, x**2])}

\notes{Here we've defined the function almost identically to the `numpy` version, only we imported `jax.numpy` instead of `numpy`.}

\setupplotcode{import matplotlib
# Comment for google colab (no latex available)
matplotlib.rc('text', usetex=True)
matplotlib.rcParams['text.latex.preamble']=[r"\usepackage{amsmath}"]}

\setupplotcode{import mlai.plot as plot}
\plotcode{plot.neural_network()}

\figure{\includediagram{\diagramsDir/ml/neural-network}{70%}}{A neural network. Input nodes are shown at the bottom. The hidden layer is the result of applying an affine transformation to the input layer and placing through an activation function.}{deep-neural-network}}

\notes{We can plot the basis just like before.}

\setupplotcode{import matplotlib.pyplot as plt
import mlai.plot as plot}

\plotcode{f, ax = plt.subplots(figsize=plot.big_wide_figsize)
loc =[[0, 1.4,],
      [0, -0.7],
      [0.75, -0.2]]
text =[r'$\phi(x) = 1$',
       r'$\phi(x) = x$',
       r'$\phi(x) = x^2$']

plot.basis(jax_quadratic, x_min=-1.3, x_max=1.3, 
           fig=f, ax=ax, loc=loc, text=text,
           diagrams='\writeDiagramsDir/ml')
		   }
		   

\subsection{Parametric Basis Functions}

\notes{We define parametric basis layers: affine transforms and non-linear activations. These combine to form neural networks.}

\subsection{Multi-Layer Perceptron as Stacked Bases}

\notes{}

\subsection{Loss and Training (JAX grad/jit)}

\notes{We use squared error and train with gradient descent. JAX allows JIT compilation and automatic differentiation.}

\code{def mse_loss(params, x, y, apply_fn):
    y_pred = apply_fn(params, x)
    return jnp.mean((y_pred - y)**2)}

\code{@jit
def update(params, x, y, lr, apply_fn):
    loss, grads = value_and_grad(mse_loss)(params, x, y, apply_fn)
    # Params is a list of dicts; apply tree map-style update
    new_params = []
    for p, g in zip(params, grads):
        new_params.append({k: p[k] - lr * g[k] for k in p})
    return new_params, loss}

\subsection{Demo: Olympics Data with a Neural Network}


\subsection{Discussion}


\endif


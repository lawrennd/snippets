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

\notes{Recall $f(\mathbf{x}) = \mathbf{ w}^\top \boldsymbol{\phi}(\mathbf{x})$. In JAX, we write basis maps that take inputs and parameters and return features. A standard linear layer is a basis with $\boldsymbol{\phi}(\mathbf{x}) = \mathbf{ x}$.}

\code{def linear_features(x):
    """Identity features (no bias), expects x of shape (n, d)."""
    return x}

\code{def predict_linear(params, x, features=linear_features):
    """Linear model: w^T phi(x) + b.
    params: dict with 'W' (d->o) and optional 'b' (o,)."""
    Phi = features(x)
    y = Phi @ params['W']
    if 'b' in params:
        y = y + params['b']
    return y}

\subsection{Parametric Basis Functions}

\notes{We define parametric basis layers: affine transforms and non-linear activations. These combine to form neural networks.}

\code{def affine(params, x):
    """Affine transform: x -> xW + b."""
    return x @ params['W'] + params['b']}

\code{def relu(x):
    return jnp.maximum(0.0, x)}

\code{def tanh(x):
    return jnp.tanh(x)}

\code{def layer_apply(layer_params, x, activation=relu):
    """Apply one dense layer + activation."""
    h = affine(layer_params, x)
    return activation(h)}

\subsection{Multi-Layer Perceptron as Stacked Bases}

\notes{An MLP is a composition: $\mathbf{x} \xrightarrow{\text{affine}} \boldsymbol{ h}_1 \xrightarrow{\sigma} \xrightarrow{\text{affine}} \dots \xrightarrow{\text{affine}} \hat{\mathbf{ y}}$.}

\code{def init_dense_params(key, in_dim, out_dim, scale=0.1):
    k1, k2 = random.split(key)
    W = scale * random.normal(k1, (in_dim, out_dim))
    b = scale * random.normal(k2, (out_dim,))
    return {'W': W, 'b': b}}

\code{def init_mlp_params(key, layer_sizes, scale=0.1):
    """layer_sizes: [in, h1, h2, ..., out]"""
    keys = random.split(key, len(layer_sizes)-1)
    layers = []
    for k, (din, dout) in zip(keys, zip(layer_sizes[:-1], layer_sizes[1:])):
        layers.append(init_dense_params(k, din, dout, scale=scale))
    return layers}

\code{def mlp_apply(params, x, activation=relu):
    """Apply MLP to inputs x (n, d). Last layer linear."""
    h = x
    for layer in params[:-1]:
        h = layer_apply(layer, h, activation=activation)
    # Last layer linear (no non-linearity)
    y = affine(params[-1], h)
    return y}

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

\subsection{Demo: Fit a 1D Nonlinear Function}

\notes{We fit a simple nonlinear mapping with an MLP to illustrate stacking basis layers.}

\setupcode{key = random.PRNGKey(0)
import numpy as np}

\code{# Create synthetic 1D regression data
def make_data(n=128, noise=0.05, key=key):
    x = jnp.linspace(-3, 3, n).reshape(-1, 1)
    f = jnp.sin(x) + 0.3 * jnp.cos(2*x)
    eps = noise * random.normal(key, f.shape)
    y = f + eps
    return x, y, f}

\code{x, y, f_true = make_data(n=128, noise=0.05, key=key)}

\code{# Init MLP: 1 -> 64 -> 64 -> 1
layer_sizes = [1, 64, 64, 1]
params = init_mlp_params(key, layer_sizes, scale=0.1)}

\code{# Train
epochs = 2000
lr = 1e-2
apply_fn = partial(mlp_apply, activation=relu)

loss_trace = []
for i in range(epochs):
    params, loss = update(params, x, y, lr, apply_fn)
    if i % 100 == 0:
        loss_trace.append((i, float(loss))) }

\setupplotcode{import mlai.plot as plot}

\plotcode{fig, ax = plt.subplots(1, 2, figsize=plot.big_wide_figsize)
# Predictions
y_pred = apply_fn(params, x)
ax[0].plot(np.asarray(x).flatten(), np.asarray(y), 'r.', label='Data', alpha=0.5)
ax[0].plot(np.asarray(x).flatten(), np.asarray(f_true), 'k--', label='True f', linewidth=2)
ax[0].plot(np.asarray(x).flatten(), np.asarray(y_pred), 'b-', label='MLP fit', linewidth=2)
ax[0].legend()
ax[0].set_title('MLP Regression (JAX)')

# Loss trace
its, vals = zip(*loss_trace)
ax[1].plot(its, vals, 'g-')
ax[1].set_xlabel('Iteration')
ax[1].set_ylabel('MSE')
ax[1].set_title('Training Loss (every 100 iters)')

mlai.write_figure(filename='basis-to-nn-jax-demo.svg', directory='\writeDiagramsDir/ml')}

\figure{\includediagram{\diagramsDir/ml/basis-to-nn-jax-demo}{80%}}{From basis functions to multilayer neural networks in JAX.}{basis-to-nn-jax-demo}

\subsection{Discussion}

\notes{Each dense layer is a parametric basis mapping; stacking them with non-linearities yields universal approximators. JAX lets us compose, differentiate, and JIT-compile these computations for efficient training.}

\endif


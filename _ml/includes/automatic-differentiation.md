\ifndef{automaticDifferentiation}
\define{automaticDifferentiation}

\editme

\subsection{Evaluating Derivatives}

\notes{See also the presentation by Ferenc Huszár on the Deep Neural Network course at the University of Cambridge. Ferenc's original slides [are here](https://hackmd.io/@fhuszar/H1WZ70kl_#) and his notes on approximating with ReLU are [here](https://hackmd.io/@fhuszar/S1UdOvZe_). His notes on automatic differentiation [are here](https://hackmd.io/@fhuszar/SyHTInWeu). His Google colab notebook is [here](https://colab.research.google.com/drive/1qioPLq-dxOwudPKXU3MxpHr2s4Su3dxI?usp=sharing). He also recommended a review paper from [JMLR](https://jmlr.org/papers/v18/17-468.html) @Baydin-autodiff18 (See Figure 2).}

\notes{The chain of matrix multiplications gives us a choice about how we evaluate this system. If we want to take the derivative of the ouptut function with respect to the weights we need to compute the chain rule.}
$$
\frac{\text{d} \mappingFunctionVector_\numLayers}{\text{d} \mappingVector} = \frac{\text{d} \mappingFunctionVector_\numLayers}{\text{d} \mappingFunctionVector_{\numLayers-1}} \frac{\text{d} \mappingFunctionVector_{\numLayers-1}}{\text{d} \mappingFunctionVector_{\numLayers-2}} \frac{\text{d} \mappingFunctionVector_{\numLayers-2}}{\text{d} \mappingFunctionVector_{\numLayers-3}} \cdots \frac{\text{d} \mappingFunctionVector_3}{\text{d} \mappingFunctionVector_{2}} \frac{\text{d} \mappingFunctionVector_2}{\text{d} \mappingFunctionVector_{1}} \frac{\text{d} \mappingFunctionVector_1}{\text{d} \mappingVector} 
$$

$$
\small
\frac{\text{d} \mappingFunctionVector_\numLayers}{\text{d} \mappingVector} = \frac{\text{d} \mappingFunctionVector_\numLayers}{\text{d} \mappingFunctionVector_{\numLayers-1}} \left( \frac{\text{d} \mappingFunctionVector_{\numLayers-1}}{\text{d} \mappingFunctionVector_{\numLayers-2}} \left( \frac{\text{d} \mappingFunctionVector_{\numLayers-2}}{\text{d} \mappingFunctionVector_{\numLayers-3}} \cdots \left( \frac{\text{d} \mappingFunctionVector_3}{\text{d} \mappingFunctionVector_{2}} \left( \frac{\text{d} \mappingFunctionVector_2}{\text{d} \mappingFunctionVector_{1}} \frac{\text{d} \mappingFunctionVector_1}{\text{d} \mappingVector} \right) \right) \cdots \right) \right)
$$

\subsection{Or like this?}

$$
\frac{\text{d} \mappingFunctionVector_\numLayers}{\text{d} \mappingVector} = \frac{\text{d} \mappingFunctionVector_\numLayers}{\text{d} \mappingFunctionVector_{\numLayers-1}} \frac{\text{d} \mappingFunctionVector_{\numLayers-1}}{\text{d} \mappingFunctionVector_{\numLayers-2}} \frac{\text{d} \mappingFunctionVector_{\numLayers-2}}{\text{d} \mappingFunctionVector_{\numLayers-3}} \cdots \frac{\text{d} \mappingFunctionVector_3}{\text{d} \mappingFunctionVector_{2}} \frac{\text{d} \mappingFunctionVector_2}{\text{d} \mappingFunctionVector_{1}} \frac{\text{d} \mappingFunctionVector_1}{\text{d} \mappingVector} 
$$

$$
\small
\frac{\text{d} \mappingFunctionVector_\numLayers}{\text{d} \mappingVector} = \left( \left( \cdots \left( \left( \frac{\text{d} \mappingFunctionVector_\numLayers}{\text{d} \mappingFunctionVector_{\numLayers-1}} \frac{\text{d} \mappingFunctionVector_{\numLayers-1}}{\text{d} \mappingFunctionVector_{\numLayers-2}}  \right) \frac{\text{d} \mappingFunctionVector_{\numLayers-2}}{\text{d} \mappingFunctionVector_{\numLayers-3}} \right) \cdots \frac{\text{d} \mappingFunctionVector_3}{\text{d} \mappingFunctionVector_{2}} \right) \frac{\text{d} \mappingFunctionVector_2}{\text{d} \mappingFunctionVector_{1}} \right) \frac{\text{d} \mappingFunctionVector_1}{\text{d} \mappingVector} 
$$

\subsection{Or in a funky way?}

$$
\frac{\text{d} \mappingFunctionVector_\numLayers}{\text{d} \mappingVector} = \frac{\text{d} \mappingFunctionVector_\numLayers}{\text{d} \mappingFunctionVector_{\numLayers-1}} \frac{\text{d} \mappingFunctionVector_{\numLayers-1}}{\text{d} \mappingFunctionVector_{\numLayers-2}} \frac{\text{d} \mappingFunctionVector_{\numLayers-2}}{\text{d} \mappingFunctionVector_{\numLayers-3}} \cdots \frac{\text{d} \mappingFunctionVector_3}{\text{d} \mappingFunctionVector_{2}} \frac{\text{d} \mappingFunctionVector_2}{\text{d} \mappingFunctionVector_{1}} \frac{\text{d} \mappingFunctionVector_1}{\text{d} \mappingVector} 
$$

$$
\small
\frac{\text{d} \mappingFunctionVector_\numLayers}{\text{d} \mappingVector} = \frac{\text{d} \mappingFunctionVector_\numLayers}{\text{d} \mappingFunctionVector_{\numLayers-1}} \left( \left( \left( \frac{\text{d} \mappingFunctionVector_{\numLayers-1}}{\text{d} \mappingFunctionVector_{\numLayers-2}}  \right) \frac{\text{d} \mappingFunctionVector_{\numLayers-2}}{\text{d} \mappingFunctionVector_{\numLayers-3}} \right) \left( \left( \cdots \frac{\text{d} \mappingFunctionVector_3}{\text{d} \mappingFunctionVector_{2}} \right) \frac{\text{d} \mappingFunctionVector_2}{\text{d} \mappingFunctionVector_{1}} \right) \right)\frac{\text{d} \mappingFunctionVector_1}{\text{d} \mappingVector} 
$$

\subsection{Automatic differentiation}

*Forward-mode*

$$
\small
\frac{\text{d} \mappingFunctionVector_\numLayers}{\text{d} \mappingVector} = \frac{\text{d} \mappingFunctionVector_\numLayers}{\text{d} \mappingFunctionVector_{\numLayers-1}} \left( \frac{\text{d} \mappingFunctionVector_{\numLayers-1}}{\text{d} \mappingFunctionVector_{\numLayers-2}} \left( \frac{\text{d} \mappingFunctionVector_{\numLayers-2}}{\text{d} \mappingFunctionVector_{\numLayers-3}} \cdots \left( \frac{\text{d} \mappingFunctionVector_3}{\text{d} \mappingFunctionVector_{2}} \left( \frac{\text{d} \mappingFunctionVector_2}{\text{d} \mappingFunctionVector_{1}} \frac{\text{d} \mappingFunctionVector_1}{\text{d} \mappingVector} \right) \right) \cdots \right) \right)
$$

Cost: 
$$
\small
\layerDim_0 \layerDim_1 \layerDim_2 + \layerDim_0 \layerDim_2 \layerDim_3 + \ldots + \layerDim_0 \layerDim_{\numLayers-1} \layerDim_\numLayers = \layerDim_0 \sum_{\layerIndex=2}^{\numLayers} \layerDim_\layerIndex \layerDim_{\layerIndex-1}
$$

\newslide{Automatic Differentiation}

*Reverse-mode*

$$
\small
\frac{\text{d} \mappingFunctionVector_\numLayers}{\text{d} \mappingVector} = \left( \left( \cdots \left( \left( \frac{\text{d} \mappingFunctionVector_\numLayers}{\text{d} \mappingFunctionVector_{\numLayers-1}} \frac{\text{d} \mappingFunctionVector_{\numLayers-1}}{\text{d} \mappingFunctionVector_{\numLayers-2}}  \right) \frac{\text{d} \mappingFunctionVector_{\numLayers-2}}{\text{d} \mappingFunctionVector_{\numLayers-3}} \right) \cdots \frac{\text{d} \mappingFunctionVector_3}{\text{d} \mappingFunctionVector_{2}} \right) \frac{\text{d} \mappingFunctionVector_2}{\text{d} \mappingFunctionVector_{1}} \right) \frac{\text{d} \mappingFunctionVector_1}{\text{d} \mappingVector} 
$$

Cost:
$$
\small
 \layerDim_\numLayers \layerDim_{\numLayers-1}\layerDim_{\numLayers-2} + \layerDim_{\numLayers}d_{\numLayers-2} \layerDim_{\numLayers-3} + \ldots + \layerDim_\numLayers \layerDim_{1} \layerDim_0 = \layerDim_\numLayers \sum_{\layerIndex=0}^{\numLayers-2}\layerDim_\layerIndex \layerDim_{\layerIndex+1}
$$

\subsection{Memory cost of autodiff}

\notes{Let $d_l$ denote the output dimensionality at layer $l$. Jacobians are evaluated at intermediate activations $\mappingFunctionVector_l$.}

\subsubsection{Forward-mode}

\slides{Store only:

* current activation $\mappingFunctionVector_l$ ($d_l$)
* running JVP of size $d_0 \times d_l$
* current Jacobian $d_l \times d_{l+1}$}

\notes{Placeholder figure: forward-mode memory footprint (streaming through layers).}

\subsubsection{Reverse-mode}

\slides{Cache activations $\{\mappingFunctionVector_l\}$ so local Jacobians can be applied during backward; higher memory than forward-mode.}

\notes{Placeholder figure: reverse-mode memory footprint (cached activations reused in backward).}

\subsection{Automatic differentiation}

* in deep learning we're most interested in scalar objectives
* $d_L=1$, consequently, backward mode is always optimal
* in the context of neural networks this is *backpropagation*.
* backprop has higher memory cost than forwardprop

\subsubsection{Backprop in deep networks}

\notes{For gradients of scalar objectives ($d_L=1$), reverse-mode is computationally optimal and standard. Memory can be reduced via checkpointing/rematerialisation at extra compute cost.}

\newslide{Autodiff: Practical Details}

\slides{* *Terminology*: forward-mode = JVP; reverse-mode = VJP
* *Non-scalar outputs*: seed vector required (e.g. `backward(grad_outputs)`)
* *Stopping grads*: `.detach()`, `no_grad()` in PyTorch}

\newslide{Autodiff: Practical Details}

\slides{* *Grad accumulation*: `.grad` accumulates by default; call `zero_grad()`
* *Memory*: backprop caches intermediates; use checkpointing/rematerialisation
* *Mixed-mode*: combine forward+reverse for Hessian-vector products}

\subsection{Computational Graphs and PyTorch Autodiff}

\notes{Modern frameworks build a dynamic computational graph as you compute, then traverse it in reverse to accumulate gradients.}

\slides{* Nodes: tensors and ops; Edges: data dependencies
* Forward pass caches intermediates needed for backward
* Backward pass applies local Jacobian-vector products}

\notes{Minimal PyTorch example (CPU/GPU agnostic):}

\installcode{torch}

\setupcode{import torch as th}

\code{x = th.tensor(4.0, requires_grad=True)
y = th.tensor(2.0)
f = (x + x*y)*2
f.backward()
x.grad  # == 2*(x + x*y)*(1 + y) = 8.0}

\notes{PyTorch attaches `grad_fn` to results, constructs the graph dynamically during forward, and supports GPU execution via `.cuda()`. These conveniences, together with automatic differentiation, enable fast deep learning experimentation.}

\endif

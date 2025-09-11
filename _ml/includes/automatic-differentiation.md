\ifndef{automaticDifferentiation}
\define{automaticDifferentiation}

\editme

\subsection{Deep Function Composition}

\notes{Deep learning refers to function composition, so when we are looking to derive gradients we are interested in
$$
\frac{\text{d}\mappingFunction_L(\mappingFunction_{L-1}(\cdots \mappingFunction_1(\mappingVector)))}{\text{d} \mappingVector}
$$
This implies we should be using the *chain rule*.}

\subsection{Chain rule}

$$
\frac{\text{d} \mappingFunctionVector \mappingFunctionVector_L}{\text{d} \mappingVector} = \frac{\text{d} \mappingFunctionVector_L}{\text{d} \mappingFunctionVector_{L-1}} \frac{\text{d} \mappingFunctionVector_{L-1}}{\text{d} \mappingFunctionVector_{L-2}} \frac{\text{d} \mappingFunctionVector_{L-2}}{\text{d} \mappingFunctionVector_{L-3}} \cdots \frac{\text{d} \mappingFunctionVector_3}{\text{d} \mappingFunctionVector_{2}} \frac{\text{d} \mappingFunctionVector_2}{\text{d} \mappingFunctionVector_{1}} \frac{\text{d} \mappingFunctionVector_1}{\text{d} \mappingVector} 
$$

\subsection{How to evaluate this?}

$$
\frac{\text{d} \mappingFunctionVector_L}{\text{d} \mappingVector} = \frac{\text{d} \mappingFunctionVector_L}{\text{d} \mappingFunctionVector_{L-1}} \frac{\text{d} \mappingFunctionVector_{L-1}}{\text{d} \mappingFunctionVector_{L-2}} \frac{\text{d} \mappingFunctionVector_{L-2}}{\text{d} \mappingFunctionVector_{L-3}} \cdots \frac{\text{d} \mappingFunctionVector_3}{\text{d} \mappingFunctionVector_{2}} \frac{\text{d} \mappingFunctionVector_2}{\text{d} \mappingFunctionVector_{1}} \frac{\text{d} \mappingFunctionVector_1}{\text{d} \mappingVector} 
$$

$$
\small
\frac{\text{d} \mappingFunctionVector_L}{\text{d} \mappingVector} = \frac{\text{d} \mappingFunctionVector_L}{\text{d} \mappingFunctionVector_{L-1}} \left( \frac{\text{d} \mappingFunctionVector_{L-1}}{\text{d} \mappingFunctionVector_{L-2}} \left( \frac{\text{d} \mappingFunctionVector_{L-2}}{\text{d} \mappingFunctionVector_{L-3}} \cdots \left( \frac{\text{d} \mappingFunctionVector_3}{\text{d} \mappingFunctionVector_{2}} \left( \frac{\text{d} \mappingFunctionVector_2}{\text{d} \mappingFunctionVector_{1}} \frac{\text{d} \mappingFunctionVector_1}{\text{d} \mappingVector} \right) \right) \cdots \right) \right)
$$

\subsection{Or like this?}

$$
\frac{\text{d} \mappingFunctionVector_L}{\text{d} \mappingVector} = \frac{\text{d} \mappingFunctionVector_L}{\text{d} \mappingFunctionVector_{L-1}} \frac{\text{d} \mappingFunctionVector_{L-1}}{\text{d} \mappingFunctionVector_{L-2}} \frac{\text{d} \mappingFunctionVector_{L-2}}{\text{d} \mappingFunctionVector_{L-3}} \cdots \frac{\text{d} \mappingFunctionVector_3}{\text{d} \mappingFunctionVector_{2}} \frac{\text{d} \mappingFunctionVector_2}{\text{d} \mappingFunctionVector_{1}} \frac{\text{d} \mappingFunctionVector_1}{\text{d} \mappingVector} 
$$

$$
\small
\frac{\text{d} \mappingFunctionVector_L}{\text{d} \mappingVector} = \left( \left( \cdots \left( \left( \frac{\text{d} \mappingFunctionVector_L}{\text{d} \mappingFunctionVector_{L-1}} \frac{\text{d} \mappingFunctionVector_{L-1}}{\text{d} \mappingFunctionVector_{L-2}}  \right) \frac{\text{d} \mappingFunctionVector_{L-2}}{\text{d} \mappingFunctionVector_{L-3}} \right) \cdots \frac{\text{d} \mappingFunctionVector_3}{\text{d} \mappingFunctionVector_{2}} \right) \frac{\text{d} \mappingFunctionVector_2}{\text{d} \mappingFunctionVector_{1}} \right) \frac{\text{d} \mappingFunctionVector_1}{\text{d} \mappingVector} 
$$

\subsection{Or in a funky way?}

$$
\frac{\text{d} \mappingFunctionVector_L}{\text{d} \mappingVector} = \frac{\text{d} \mappingFunctionVector_L}{\text{d} \mappingFunctionVector_{L-1}} \frac{\text{d} \mappingFunctionVector_{L-1}}{\text{d} \mappingFunctionVector_{L-2}} \frac{\text{d} \mappingFunctionVector_{L-2}}{\text{d} \mappingFunctionVector_{L-3}} \cdots \frac{\text{d} \mappingFunctionVector_3}{\text{d} \mappingFunctionVector_{2}} \frac{\text{d} \mappingFunctionVector_2}{\text{d} \mappingFunctionVector_{1}} \frac{\text{d} \mappingFunctionVector_1}{\text{d} \mappingVector} 
$$

$$
\small
\frac{\text{d} \mappingFunctionVector_L}{\text{d} \mappingVector} = \frac{\text{d} \mappingFunctionVector_L}{\text{d} \mappingFunctionVector_{L-1}} \left( \left( \left( \frac{\text{d} \mappingFunctionVector_{L-1}}{\text{d} \mappingFunctionVector_{L-2}}  \right) \frac{\text{d} \mappingFunctionVector_{L-2}}{\text{d} \mappingFunctionVector_{L-3}} \right) \left( \left( \cdots \frac{\text{d} \mappingFunctionVector_3}{\text{d} \mappingFunctionVector_{2}} \right) \frac{\text{d} \mappingFunctionVector_2}{\text{d} \mappingFunctionVector_{1}} \right) \right)\frac{\text{d} \mappingFunctionVector_1}{\text{d} \mappingVector} 
$$

\subsection{Automatic differentiation}

*Forward-mode*

$$
\small
\frac{\text{d} \mappingFunctionVector_L}{\text{d} \mappingVector} = \frac{\text{d} \mappingFunctionVector_L}{\text{d} \mappingFunctionVector_{L-1}} \left( \frac{\text{d} \mappingFunctionVector_{L-1}}{\text{d} \mappingFunctionVector_{L-2}} \left( \frac{\text{d} \mappingFunctionVector_{L-2}}{\text{d} \mappingFunctionVector_{L-3}} \cdots \left( \frac{\text{d} \mappingFunctionVector_3}{\text{d} \mappingFunctionVector_{2}} \left( \frac{\text{d} \mappingFunctionVector_2}{\text{d} \mappingFunctionVector_{1}} \frac{\text{d} \mappingFunctionVector_1}{\text{d} \mappingVector} \right) \right) \cdots \right) \right)
$$

Cost: 
$$
\small
d_0d_1d_2 + d_0d_2d_3 + \ldots + d_0d_{L-1}d_L = d_0 \sum_{l=2}^{L}d_ld_{l-1}
$$

\subsection{Automatic differentiation}

*Reverse-mode*

$$
\small
\frac{\text{d} \mappingFunctionVector_L}{\text{d} \mappingVector} = \left( \left( \cdots \left( \left( \frac{\text{d} \mappingFunctionVector_L}{\text{d} \mappingFunctionVector_{L-1}} \frac{\text{d} \mappingFunctionVector_{L-1}}{\text{d} \mappingFunctionVector_{L-2}}  \right) \frac{\text{d} \mappingFunctionVector_{L-2}}{\text{d} \mappingFunctionVector_{L-3}} \right) \cdots \frac{\text{d} \mappingFunctionVector_3}{\text{d} \mappingFunctionVector_{2}} \right) \frac{\text{d} \mappingFunctionVector_2}{\text{d} \mappingFunctionVector_{1}} \right) \frac{\text{d} \mappingFunctionVector_1}{\text{d} \mappingVector} 
$$

Cost:
$$
\small
 d_Ld_{L-1}d_{L-2} + d_{L}d_{L-2}d_{L-3} + \ldots + d_Ld_{1}d_0 = d_L \sum_{l=0}^{L-2}d_ld_{l+1}
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
* *Stopping grads*: `.detach()`, `no_grad()` in PyTorch
* *Grad accumulation*: `.grad` accumulates by default; call `zero_grad()`
* *Memory*: backprop caches intermediates; use checkpointing/rematerialisation
* *Mixed-mode*: combine forward+reverse for Hessian-vector products}

\subsection{Computational Graphs and PyTorch Autodiff}

\notes{Modern frameworks build a dynamic computational graph as you compute, then traverse it in reverse to accumulate gradients.}

\slides{* Nodes: tensors and ops; Edges: data dependencies
* Forward pass caches intermediates needed for backward
* Backward pass applies local Jacobian-vector products}

\notes{Minimal PyTorch example (CPU/GPU agnostic):}

\code{import torch as th
x = th.tensor(4.0, requires_grad=True)
y = th.tensor(2.0)
f = (x + x*y)*2
f.backward()
x.grad  # == 2*(x + x*y)*(1 + y) = 8.0}


\notes{PyTorch attaches `grad_fn` to results, constructs the graph dynamically during forward, and supports GPU execution via `.cuda()`. These conveniences, together with autodiff, enable fast deep learning experimentation.}

\endif

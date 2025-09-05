\ifndef{automaticDifferentiation}
\define{automaticDifferentiation}

\editme

\subsection{General Deep Function Composition}

$$
f_L(f_{L-1}(\cdots f_1(\mathbb{w})))
$$

How do I calculate the derivative of $f_L(\mathbb{w})$ with respect to $\mathbb{w}$?

\subsection{Chain rule}

$$
\frac{\partial \mathbf{f}_L}{\partial \mathbb{w}} = \frac{\partial \mathbf{f}_L}{\partial \mathbf{f}_{L-1}} \frac{\partial \mathbf{f}_{L-1}}{\partial \mathbf{f}_{L-2}} \frac{\partial \mathbf{f}_{L-2}}{\partial \mathbf{f}_{L-3}} \cdots \frac{\partial \mathbf{f}_3}{\partial \mathbf{f}_{2}} \frac{\partial \mathbf{f}_2}{\partial \mathbf{f}_{1}} \frac{\partial \mathbf{f}_1}{\partial \mappingVector} 
$$

\subsection{How to evaluate this?}

$$
\frac{\partial \mathbf{f}_L}{\partial \mathbb{w}} = \frac{\partial \mathbf{f}_L}{\partial \mathbf{f}_{L-1}} \frac{\partial \mathbf{f}_{L-1}}{\partial \mathbf{f}_{L-2}} \frac{\partial \mathbf{f}_{L-2}}{\partial \mathbf{f}_{L-3}} \cdots \frac{\partial \mathbf{f}_3}{\partial \mathbf{f}_{2}} \frac{\partial \mathbf{f}_2}{\partial \mathbf{f}_{1}} \frac{\partial \mathbf{f}_1}{\partial \mappingVector} 
$$

$$
\small
\frac{\partial \mathbf{f}_L}{\partial \mathbb{w}} = \frac{\partial \mathbf{f}_L}{\partial \mathbf{f}_{L-1}} \left( \frac{\partial \mathbf{f}_{L-1}}{\partial \mathbf{f}_{L-2}} \left( \frac{\partial \mathbf{f}_{L-2}}{\partial \mathbf{f}_{L-3}} \cdots \left( \frac{\partial \mathbf{f}_3}{\partial \mathbf{f}_{2}} \left( \frac{\partial \mathbf{f}_2}{\partial \mathbf{f}_{1}} \frac{\partial \mathbf{f}_1}{\partial \mappingVector} \right) \right) \cdots \right) \right)
$$

\subsection{Or like this?}

$$
\frac{\partial \mathbf{f}_L}{\partial \mathbb{w}} = \frac{\partial \mathbf{f}_L}{\partial \mathbf{f}_{L-1}} \frac{\partial \mathbf{f}_{L-1}}{\partial \mathbf{f}_{L-2}} \frac{\partial \mathbf{f}_{L-2}}{\partial \mathbf{f}_{L-3}} \cdots \frac{\partial \mathbf{f}_3}{\partial \mathbf{f}_{2}} \frac{\partial \mathbf{f}_2}{\partial \mathbf{f}_{1}} \frac{\partial \mathbf{f}_1}{\partial \mappingVector} 
$$

$$
\small
\frac{\partial \mathbf{f}_L}{\partial \mathbb{w}} = \left( \left( \cdots \left( \left( \frac{\partial \mathbf{f}_L}{\partial \mathbf{f}_{L-1}} \frac{\partial \mathbf{f}_{L-1}}{\partial \mathbf{f}_{L-2}}  \right) \frac{\partial \mathbf{f}_{L-2}}{\partial \mathbf{f}_{L-3}} \right) \cdots \frac{\partial \mathbf{f}_3}{\partial \mathbf{f}_{2}} \right) \frac{\partial \mathbf{f}_2}{\partial \mathbf{f}_{1}} \right) \frac{\partial \mathbf{f}_1}{\partial \mappingVector} 
$$

\subsection{Or in a funky way?}

$$
\frac{\partial \mathbf{f}_L}{\partial \mathbb{w}} = \frac{\partial \mathbf{f}_L}{\partial \mathbf{f}_{L-1}} \frac{\partial \mathbf{f}_{L-1}}{\partial \mathbf{f}_{L-2}} \frac{\partial \mathbf{f}_{L-2}}{\partial \mathbf{f}_{L-3}} \cdots \frac{\partial \mathbf{f}_3}{\partial \mathbf{f}_{2}} \frac{\partial \mathbf{f}_2}{\partial \mathbf{f}_{1}} \frac{\partial \mathbf{f}_1}{\partial \mappingVector} 
$$

$$
\small
\frac{\partial \mathbf{f}_L}{\partial \mathbb{w}} = \frac{\partial \mathbf{f}_L}{\partial \mathbf{f}_{L-1}} \left( \left( \left( \frac{\partial \mathbf{f}_{L-1}}{\partial \mathbf{f}_{L-2}}  \right) \frac{\partial \mathbf{f}_{L-2}}{\partial \mathbf{f}_{L-3}} \right) \left( \left( \cdots \frac{\partial \mathbf{f}_3}{\partial \mathbf{f}_{2}} \right) \frac{\partial \mathbf{f}_2}{\partial \mathbf{f}_{1}} \right) \right)\frac{\partial \mathbf{f}_1}{\partial \mappingVector} 
$$

\subsection{Automatic differentiation}

*Forward-mode*

$$
\small
\frac{\partial \mathbf{f}_L}{\partial \mathbb{w}} = \frac{\partial \mathbf{f}_L}{\partial \mathbf{f}_{L-1}} \left( \frac{\partial \mathbf{f}_{L-1}}{\partial \mathbf{f}_{L-2}} \left( \frac{\partial \mathbf{f}_{L-2}}{\partial \mathbf{f}_{L-3}} \cdots \left( \frac{\partial \mathbf{f}_3}{\partial \mathbf{f}_{2}} \left( \frac{\partial \mathbf{f}_2}{\partial \mathbf{f}_{1}} \frac{\partial \mathbf{f}_1}{\partial \mappingVector} \right) \right) \cdots \right) \right)
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
\frac{\partial \mathbf{f}_L}{\partial \mathbb{w}} = \left( \left( \cdots \left( \left( \frac{\partial \mathbf{f}_L}{\partial \mathbf{f}_{L-1}} \frac{\partial \mathbf{f}_{L-1}}{\partial \mathbf{f}_{L-2}}  \right) \frac{\partial \mathbf{f}_{L-2}}{\partial \mathbf{f}_{L-3}} \right) \cdots \frac{\partial \mathbf{f}_3}{\partial \mathbf{f}_{2}} \right) \frac{\partial \mathbf{f}_2}{\partial \mathbf{f}_{1}} \right) \frac{\partial \mathbf{f}_1}{\partial \mathbb{w}} 
$$

Cost:
$$
\small
 d_Ld_{L-1}d_{L-2} + d_{L}d_{L-2}d_{L-3} + \ldots + d_Ld_{1}d_0 = d_L \sum_{l=0}^{L-2}d_ld_{l+1}
$$

\subsection{Memory cost of autodiff}

\notes{Let $d_l$ denote the output dimensionality at layer $l$. Jacobians are evaluated at intermediate activations $\mathbf{f}_l$.}

\subsubsection{Forward-mode}

\slides{Store only:
* current activation $\mathbf{f}_l$ ($d_l$)
* running JVP of size $d_0 \times d_l$
* current Jacobian $d_l \times d_{l+1}$}

\notes{Placeholder figure: forward-mode memory footprint (streaming through layers).}

\subsubsection{Reverse-mode}

\slides{Cache activations $\{\mathbf{f}_l\}$ so local Jacobians can be applied during backward; higher memory than forward-mode.}

\notes{Placeholder figure: reverse-mode memory footprint (cached activations reused in backward).}

\subsection{Automatic differentiation}

* in deep learning we're most interested in scalar objectives
* $d_L=1$, consequently, backward mode is always optimal
* in the context of neural networks: *backpropagation*
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

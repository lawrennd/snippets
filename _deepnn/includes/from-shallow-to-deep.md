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
\mathscr{L}(\theta) = \sum_{n=1}^N \ell(y_n, f(x_n, \theta))
$$

$$
\theta_{t+1} = \theta_t - \eta \nabla_\theta \mathcal{L}(\theta)
$$

\subsubsection{Basic Multilayer Perceptron}

$$
\small
\mappingFunction_L(x) = \basisVector\left(b_L + W_L \basisVector\left(b_{L-1} + W_{L-1} \basisVector\left( \cdots \basisVector\left(b_1 + W_1 x\right) \cdots \right)\right)\right)
$$

\subsubsection{Recursive MLP Definition}

\slides{\small
\begin{align}
\mappingFunction_l(x) &= \basisVector\big(W_l \mappingFunction_{l-1}(x) + b_l\big),\quad l=1,\dots,L\\
\mappingFunction_0(x) &= x
\end{align}}

\subsection{Rectified Linear Unit}

\slides{\small
\basisVector(x) = \begin{cases}
0 & x \le 0\\
x & x > 0
\end{cases}}

\notes{Placeholder figure: basic ReLU shape (zero for negative inputs, identity for positive).}

\notes{Other activation functions that are used include hyperbolic tangent, sigmoid, ELU, leaky ReLU. Although ReLU is often preferred for  simplicity and fast gradient computation.}

\subsection{Shallow ReLU Networks}

\notes{A single layer ReLU network is functionally equivalent to a generalised linear model with a ReLU basis. The difference is that we optimise over the basis function inputs.}

\slides{\small
\begin{align}
\mathbf{h}(x) &= \operatorname{ReLU}(\mathbf{w}_1 x - \mathbf{b}_1)\\
f(x) &= \mathbf{w}_2^{\top} \, \mathbf{h}(x)
\end{align}}

\notes{Each hidden unit acts as a basis function with its own kink location and slope.}

\tk{Placeholder figure: coloured activations of individual ReLU units vs input (different kink locations/slopes).}

\tk{Placeholder figure: final output as linear combination of ReLU basis functions; colour-coded kinks correspond to unit activations.}

\slides{Complexity (1D): number of kinks $\propto$ width of network.}

\subsection{Depth vs Width: Representation Power}

\notes{ReLU networks implement piecewise-linear functions; width increases the number of linear pieces roughly linearly, depth increases them exponentially.}

\slides{* Single hidden layer: number of kinks $\approx O(\text{width})$
* Deep ReLU networks: kinks $\approx O(2^{\text{depth}})$}

\subsection{Sawtooth Construction}

\notes{Illustrative 1D construction showing exponential growth of segments with depth.}

\slides{\small
\begin{align}
\mappingFunction_l(x) &= 2\vert \mappingFunction_{l-1}(x)\vert - 2, \quad \mappingFunction_0(x) = x\\
\mappingFunction_l(x) &= 2 
  \operatorname{ReLU}(\mappingFunction_{l-1}(x)) + 2 
  \operatorname{ReLU}(-\mappingFunction_{l-1}(x)) - 2
\end{align}}

\notes{In higher dimensions, these become polyhedral regions with constant gradients inside each region.}

\notes{Placeholder mini-figures: depth $0,1,2,3,4,5$ outputs of the sawtooth network showing doubling segments at each step.}

\slides{Complexity (1D): number of kinks $\approx O(2^{\text{depth}})$.}

\subsection{Higher-dimensional Geometry}

\notes{In 2D, ReLU networks partition input space into many polygonal regions. Within each region the mapping is linear, yet globally the function is continuous because adjacent regions meet with consistent boundary values. Depth increases the number and intricacy of these regions across layers.}

\slides{* Regions: piecewise-linear, often triangular/polygonal in 2D
* Continuity arises despite stitching flat regions
* Early layers: few regions; later layers: many more}

\notes{Placeholder figure: 2D piecewise-linear tiling (e.g., Hanin and Rolnick, 2019) with coloured regions indicating distinct linear pieces.}

\notes{Suggested visual: reuse figures showing partitioned 2D input space with coloured linear regions. If needed, include links or embed static images used in prior notes.}

\endif

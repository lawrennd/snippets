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
\mathcal{L}(\theta) = \sum_{n=1}^N \ell(y_n, f(x_n, \theta))
$$

$$
\theta_{t+1} = \theta_t - \eta \nabla_\theta \mathcal{L}(\theta)
$$

\subsubsection{Basic Multilayer Perceptron}

$$
\small
f_L(x) = \phi\left(b_L + W_L \phi\left(b_{L-1} + W_{L-1} \phi\left( \cdots \phi\left(b_1 + W_1 x\right) \cdots \right)\right)\right)
$$

\subsubsection{Recursive MLP Definition}

\slides{\small
\begin{align}
f_l(x) &= \phi\big(W_l f_{l-1}(x) + b_l\big),\quad l=1,\dots,L\\
f_0(x) &= x
\end{align}}

\subsection{Rectified Linear Unit}

\slides{\small
\phi(x) = \begin{cases}
0 & x \le 0\\
x & x > 0
\end{cases}}

\notes{Placeholder figure: basic ReLU shape (zero for negative inputs, identity for positive).}

\notes{Other activation functions exist (tanh, sigmoid, ELU, leaky ReLU). ReLU is emphasised here for simplicity and fast gradient computation.}

\subsection{Shallow ReLU Networks}

\notes{Single hidden layer with 1D input/output for illustration.}

\slides{\small
\begin{align}
\mathbf{h}(x) &= \operatorname{ReLU}(\mathbf{w}_1 x - \mathbf{b}_1)\\
f(x) &= \mathbf{w}_2^{\top} \, \mathbf{h}(x)
\end{align}}

\notes{Each hidden unit acts as a basis function with its own kink location and slope.}

\notes{Placeholder figure: coloured activations of individual ReLU units vs input (different kink locations/slopes).}

\notes{Placeholder figure: final output as linear combination of ReLU basis functions; colour-coded kinks correspond to unit activations.}

\slides{Complexity (1D): number of kinks $\propto$ width of network.}

\subsection{Depth vs Width: Representation Power}

\notes{ReLU networks implement piecewise-linear functions; width increases the number of linear pieces roughly linearly, depth increases them exponentially.}

\slides{* Single hidden layer: number of kinks $\approx O(\text{width})$
* Deep ReLU networks: kinks $\approx O(2^{\text{depth}})$}

\subsection{Sawtooth Construction}

\notes{Illustrative 1D construction showing exponential growth of segments with depth.}

\slides{\small
\begin{align}
f_l(x) &= 2\vert f_{l-1}(x)\vert - 2, \quad f_0(x) = x\\
f_l(x) &= 2 
  \operatorname{ReLU}(f_{l-1}(x)) + 2 
  \operatorname{ReLU}(-f_{l-1}(x)) - 2
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

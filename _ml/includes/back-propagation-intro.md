\ifndef{backPropagationIntro}
\define{backPropagationIntro}

\editme

\subsection{Chain Rule and Back Propgation}

\newslide{Historical Context}

\slides{* **1957**: Rosenblatt's Perceptron with multiple layers
* **Association units**: deep structure with random weights
* **Modern approach**: adjust weights to minimise error}

\notes{When Rosenblatt built his Perceptron model in 1957, he used multiple layers of units, that he called association units, to take advantage of the deep structure he gave these units random weights. In modern deep learning we adjust these weights to minimise the error.}

\newslide{Parameterised Basis Functions}

\slides{* **Basis functions**: $\basisVector(\inputVector; \mappingMatrixTwo)$
* **Adjustable parameters**: $\mappingMatrixTwo$ can be optimized
* **Non-linear models**: in both inputs and parameters}

\notes{From the basis function perspective, we have parameters in our basis function vectors, $\basisVector(\inputVector; \mappingMatrixTwo)$ that can be adjusted. They are non-linearly related to the output so that makes these models non-linear both in terms of the dependence on inputs *and* the dependence on parameters.}

\newslide{The Gradient Problem}

\slides{* **Model**: $\mappingFunction(\inputVector_i) = \mappingVector^\top \basisVector(\inputVector_i; \mappingMatrixTwo)$
* **Easy gradient**: $\frac{\text{d}\mappingFunction_i}{\text{d}\mappingVector} = \basisVector(\inputVector_i; \mappingMatrixTwo)$
* **Hard gradient**: $\frac{\text{d}\mappingFunction_i}{\text{d}\mappingMatrixTwo}$}

\notes{To compute derivatives we now need to compute the derivation of the system with respect to the basis functions.
$$
\mappingFunction(\inputVector_i) = \mappingVector^\top \basisVector(\inputVector_i; \mappingMatrixTwo).
$$
We already have the gradient with respect to $\mappingVector$, which is simply.
$$
\frac{\text{d}\mappingFunction_i}{\text{d}\mappingVector} = \basisVector(\inputVector_i; \mappingMatrixTwo),
$$}

\newslide{Chain Rule Application}

$$\frac{\text{d}\mappingFunction_i}{\text{d}\mappingMatrixTwo} = \frac{\text{d}\mappingFunction_i}{\text{d}\basisVector_i}\frac{\text{d}\basisVector_i}{\text{d} \mappingMatrixTwo}$$

\newslide{The Matrix Challenge}

\slides{* **Chain rule**: standard approach
* **New challenge**: $\frac{\text{d}\basisVector_i}{\text{d} \mappingMatrixTwo}$
* **Problem**: derivative of *vector* with respect to *matrix*}

\notes{we now need the gradient with respect to $\mappingVectorTwo$. This can be computed by the chain rule as,
$$
\frac{\text{d}\mappingFunction_i}{\text{d}\mappingMatrixTwo} = \frac{\text{d}\mappingFunction_i}{\text{d}\basisVector_i}\frac{\text{d}\basisVector_i}{\text{d} \mappingMatrixTwo}.
$$
But we have to be careful here. This is the chain rule, but it contains a new challenge, $\frac{\text{d}\basisVector_i}{\text{d} \mappingMatrixTwo}$ is the derivative of a *vector* with respect to a *matrix*. How do we deal with this?}


\endif

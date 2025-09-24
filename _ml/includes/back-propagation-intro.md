\ifndef{backPropagationIntro}
\define{backPropagationIntro}

\editme

\subsection{Chain Rule and Back Propgation}

\notes{When Rosenblatt built his Perceptron model in 1957, he used multiple layers of units, that he called association units, to take advantage of the deep structure he gave these units random weights. In modern deep learning we adjust these weights to minimise the error.}

\notes{From the basis function perspective, we have parameters in our basis function vectors, $\basisVector(\inputVector; \mappingMatrixTwo)$ that can be adjusted. They are non-linearly related to the output so that makes these models non-linear both in terms of the dependence on inputs *and* the dependence on parameters.}

\notes{To compute derivatives we now need to compute the derivation of the system with respect to the basis functions.
$$
\mappingFunction(\inputVector_i) = \mappingVector^\top \basisVector(\inputVector_i; \mappingMatrixTwo).
$$
We already have the gradient with respect to $\mappingVector$, which is simply.
$$
\frac{\text{d}\mappingFunction_i}{\text{d}\mappingVector} = \basisVector(\inputVector_i; \mappingMatrixTwo),
$$
we now need the gradient with respect to $\mappingVectorTwo$. This can be computed by the chain rule as,
$$
\frac{\text{d}\mappingFunction^L_i}{\text{d}\mappingMatrixTwo} = \frac{\text{d}\mappingFunction_i}{\text{d}\basisVector_i}\frac{\text{d}\basisVector_i}{\text{d} \mappingMatrixTwo}.
$$
But we have to be careful here. This is the chain rule, but it contains a new challenge, $\frac{\text{d}\basisVector_i}{\text{d} \mappingMatrixTwo}$ is the derivative of a *vector* with respect to a *matrix*. How do we deal with this?}


\endif

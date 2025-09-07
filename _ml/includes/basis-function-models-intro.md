\ifndef{basisFunctionModelsIntro}
\define{basisFunctionModelsIntro}

\editme

\subsection{Basis Function Models}

\notes{We are reviewing models that are *linear* in the parameters. Very often we are interested in *non-linear* predictions. We can make models that are linear in the parameters and given non-linear predictions by introducing non-linear *basis functions*. A common example is the polynomial basis.}

\include{_ml/includes/polynomial-basis.md}

\notes{The predictions from this model,
$$
\mappingFunction(\inputScalar) = \mappingScalar_0 + \mappingScalar_1 \inputScalar} + \mappingScalar_2 \inputScalar^2 + \mappingScalar_3 \inputScalar^3 + \mappingScalar_4 \inputScalar^4
$$
are *linear* in the parameters, $\mappingVector$, but *non-linear* in the input $\inputScalar^3$. Here we are showing a polynomial basis for a 1-dimensional input, $\inputScalar$, but basis functions can also be constructed for multidimensional inputs, $\inputVector$.}

\notes{In the neural network models, the "RELU function" is normally used as a basis function, but for illustration we will continue with the polynomial basis for these linear models.}

\endif

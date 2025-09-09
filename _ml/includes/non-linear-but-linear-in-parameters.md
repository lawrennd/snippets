\ifndef{nonLinearButLinearInParameters}
\define{nonLinearButLinearInParameters}

\editme

\subsection{Non-linear but Linear in the Parameters}

\notes{One rather nice aspect of our model is that whilst it is non-linear in the inputs, it is still linear in the parameters $\mappingVector$. This means that our derivations from before continue to operate to allow us to work with this model. In fact, although this is a non-linear regression it is still known as a *linear model* because it is linear in the parameters,}
\slides{* Model is non-linear, but linear in parameters}
$$
\mappingFunction(\inputVector) = \mappingVector^\top \basisVector(\inputVector)
$$
\slides{* $\inputVector$ is inside the non-linearity, but $\mappingVector$ is outside.}\notes{where the vector $\inputVector$ appears inside the basis functions, making our result, $\mappingFunction(\inputVector)$ non-linear in the inputs, but $\mappingVector$ appears outside our basis function, making our result *linear* in the parameters. In practice, our basis function itself may contain its own set of parameters,}
$$
\mappingFunction(\inputVector) = \mappingVector^\top \basisVector(\inputVector;
\mappingVectorTwo),
$$
\notes{that we've denoted here as $\mappingVectorTwo$. If these parameters appear inside the basis function then our model is *non-linear* in these parameters.}

\writeassignment{For the following prediction functions state whether
the model is linear in the inputs, the parameters or both.

(a) $\mappingFunction(\inputScalar) = \mappingScalar_1\inputScalar_1 + \mappingScalar_2$

(b) $\mappingFunction(\inputScalar) = \mappingScalar_1\exp(\inputScalar_1) + \mappingScalar_2\inputScalar_2 + \mappingScalar_3$

(c) $\mappingFunction(\inputScalar) =
\log(\inputScalar_1^{\mappingScalar_1}) + \mappingScalar_2\inputScalar_2^2 + \mappingScalar_3$

(d) $\mappingFunction(\inputScalar) = \exp(-\sum_i(\inputScalar_i - \mappingScalar_i)^2)$

(e) $\mappingFunction(\inputScalar) = \exp(-\mappingVector^\top \inputVector)$}{25}

\endif

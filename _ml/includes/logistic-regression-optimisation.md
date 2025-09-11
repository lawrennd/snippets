\ifndef{logisticRegressionOptimisation}
\define{logisticRegressionOptimisation}

\editme

\subsection{Negative Log Likelihood}

\slides{
\begin{aligned}
  - \log P(\dataVector|\mappingVector, \inputMatrix) = &
  - \sum_{i=1}^\numData \log P(\dataScalar_i|\mappingVector, \inputVector_i) \\ = &- \sum_{i=1}^\numData \dataScalar_i \log
  \pi_i \\ & - \sum_{i=1}^\numData (1-\dataScalar_i)\log (1-\pi_i)
\end{aligned}
}


\setupcode{import numpy as np}
\code{def objective(h, y):
    "Computes the objective function."
	labs = np.asarray(y, dtype=float).flatten()
    posind = np.where(labs==1)
    negind = np.where(labs==0)
    return -np.log(h[posind, :]).sum() - np.log(1-h[negind, :]).sum()}

\notes{As normal, we would like to minimise this objective. This can be done
by differentiating with respect to the parameters of our prediction
function, $\pi(\inputVector;\mappingVector)$, for optimisation. The
gradient of the likelihood with respect to
$\pi(\inputVector;\mappingVector)$ is of the form,
$$
\frac{\text{d}\errorFunction(\mappingVector)}{\text{d}\mappingVector} = -\sum_{i=1}^\numData
\frac{\dataScalar_i}{\transformationFunction\left(\mappingVector^\top
\basisVector(\inputVector)\right)}\frac{\text{d}\transformationFunction(\mappingFunction_i)}{\text{d}\mappingFunction_i}
\basisVector(\inputVector_i) +  \sum_{i=1}^\numData
\frac{1-\dataScalar_i}{1-\transformationFunction\left(\mappingVector^\top
\basisVector(\inputVector)\right)}\frac{\text{d}\transformationFunction(\mappingFunction_i)}{\text{d}\mappingFunction_i}
\basisVector(\inputVector_i)
$$
where we used the chain rule to develop the derivative in terms of
$\frac{\text{d}\transformationFunction(\mappingFunction_i)}{\text{d}\mappingFunction_i}$,
which is the gradient of the inverse link function (in our case the
gradient of the sigmoid function).}

\notes{So the objective function now depends on the gradient of the inverse
link function, as well as the likelihood depends on the gradient of
the inverse link function, as well as the gradient of the log
likelihood, and naturally the gradient of the argument of the inverse
link function with respect to the parameters, which is simply
$\basisVector(\inputVector_i)$.}

\newslide{Objective Function}

\slides{
* Probability of positive outcome for the $i$th data point 
  $$\pi_i = \transformationFunction\left(\mappingVector^\top \basisVector(\inputVector_i)\right),$$
  where $\transformationFunction(\cdot)$ is the *inverse* link function
* Objective function of the form 
  $$\begin{align*}
    E(\mappingVector) = & -  \sum_{i=1}^\numData \dataScalar_i \log
    \transformationFunction\left(\mappingVector^\top \basisVector(\inputVector_i)\right) \\& -
    \sum_{i=1}^\numData(1-\dataScalar_i)\log \left(1-\transformationFunction\left(\mappingVector^\top
    \basisVector(\inputVector_i)\right)\right).
   \end{align*}$$
}

\newslide{Minimise Objective}

\slides{
* Grdient wrt  $\pi(\inputVector;\mappingVector)$
  \begin{aligned}
  \frac{\text{d}\errorFunction(\mappingVector)}{\text{d}\mappingVector} = &
  -\sum_{i=1}^\numData \frac{\dataScalar_i}{\transformationFunction\left(\mappingVector^\top
  \basisVector(\inputVector)\right)}\frac{\text{d}\transformationFunction(\mappingFunction_i)}{\text{d}\mappingFunction_i}
  \basisVector(\inputVector_i) \\ & +  \sum_{i=1}^\numData
  \frac{1-\dataScalar_i}{1-\transformationFunction\left(\mappingVector^\top
  \basisVector(\inputVector)\right)}\frac{\text{d}\transformationFunction(\mappingFunction_i)}{\text{d}\mappingFunction_i}
  \basisVector(\inputVector_i)
  \end{aligned}
}

\notes{The only missing term is the gradient of the inverse link
function. For the sigmoid squashing function we have,
\begin{aligned}
\transformationFunction(\mappingFunction_i) &= \frac{1}{1+\exp(-\mappingFunction_i)}\\
&=(1+\exp(-\mappingFunction_i))^{-1}
\end{align*}$$
and the gradient can be computed as
$$\begin{align*}
\frac{\text{d}\transformationFunction(\mappingFunction_i)}{\text{d} \mappingFunction_i} & =
\exp(-\mappingFunction_i)(1+\exp(-\mappingFunction_i))^{-2}\\
& = \frac{1}{1+\exp(-\mappingFunction_i)}
\frac{\exp(-\mappingFunction_i)}{1+\exp(-\mappingFunction_i)} \\
& = \transformationFunction(\mappingFunction_i) (1-g(\mappingFunction_i))
\end{aligned}
so the full gradient can be written down as
$$
\frac{\text{d}\errorFunction(\mappingVector)}{\text{d}\mappingVector} = -\sum_{i=1}^\numData
\dataScalar_i\left(1-\transformationFunction\left(\mappingVector^\top \basisVector(\inputVector)\right)\right)
\basisVector(\inputVector_i) +  \sum_{i=1}^\numData
(1-\dataScalar_i)\left(\transformationFunction\left(\mappingVector^\top \basisVector(\inputVector)\right)\right)
\basisVector(\inputVector_i).
$$

\setupcode{import numpy as np}
\code{def gradient(h, Phi, y):
    "Generates the gradient of the parameter vector."
	labs = np.asarray(y, dtype=float).flatten()
    posind = np.where(labs==1)
    dw = -(Phi[posind]*(1-h[posind])).sum(0)
    negind = np.where(labs==0 )
    dw += (Phi[negind]*h[negind]).sum(0)
    return dw[:, None]}

\subsection{Optimisation of the Function}

Reorganising the gradient to find a stationary point of the function
with respect to the parameters $\mappingVector$ turns out to be
impossible. Optimisation has to proceed by *numerical
methods*. Options include the multidimensional variant of
[Newton's method](http://en.wikipedia.org/wiki/Newton%27s_method) or
[gradient based optimisation methods](http://en.wikipedia.org/wiki/Gradient_method)
like we used for optimising matrix factorisation for the movie
recommender system. We recall from matrix factorisation that, for
large data, *stochastic gradient descent* or the Robbins Munro
[@Robbins:stoch51] optimisation procedure worked best for function
minimisation.}

\newslide{Link Function Gradient}
\slides{
* Also need gradient of inverse link function wrt parameters.
\begin{aligned}
\transformationFunction(\mappingFunction_i) &= \frac{1}{1+\exp(-\mappingFunction_i)}\\
&=(1+\exp(-\mappingFunction_i))^{-1}
\end{aligned}
}
\newslide{Link Function Gradient}
\slides{
and the gradient can be computed as
\begin{aligned}
\frac{\text{d}\transformationFunction(\mappingFunction_i)}{\text{d} \mappingFunction_i} & =
\exp(-\mappingFunction_i)(1+\exp(-\mappingFunction_i))^{-2}\\
& = \frac{1}{1+\exp(-\mappingFunction_i)}
\frac{\exp(-\mappingFunction_i)}{1+\exp(-\mappingFunction_i)} \\
& = \transformationFunction(\mappingFunction_i) (1-\transformationFunction(\mappingFunction_i))
\end{aligned}
}

\newslide{Objective Gradient}
\slides{
\begin{aligned}
\frac{\text{d}E(\mappingVector)}{\text{d}\mappingVector} = & -\sum_{i=1}^\numData
\dataScalar_i\left(1-\transformationFunction\left(\mappingVector^\top \basisVector(\inputVector)\right)\right)
\basisVector(\inputVector_i) \\ & + \sum_{i=1}^\numData
(1-\dataScalar_i)\left(\transformationFunction\left(\mappingVector^\top \basisVector(\inputVector)\right)\right)
\basisVector(\inputVector_i).
\end{aligned}
}

\newslide{Optimisation of the Function}
\slides{
* Can't find a stationary point of the objective function analytically.
* Optimisation has to proceed by *numerical methods*. 
    * [Newton's method](http://en.wikipedia.org/wiki/Newton%27s_method) or 
    * [gradient based optimisation methods](http://en.wikipedia.org/wiki/Gradient_method)
	* Iterative Reweighted Least Squares
* Similarly to matrix factorisation, for large data *stochastic gradient descent*  (Robbins Munro [@Robbins:stoch51] optimisation procedure) works well.
}

\endif

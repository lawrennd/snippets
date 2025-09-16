\ifndef{logisticRegressionLogLikelihood}
\define{logisticRegressionLogLikelihood}

\editme


\subsection{Maximum Likelihood}

\slides{
* Conditional independence of data:
  $$P(\dataVector|\mappingVector, \inputMatrix) = \prod_{i=1}^\numData P(\dataScalar_i|\mappingVector,
\inputVector_i). $$
}

\notes{To obtain the parameters of the model, we need to maximise the likelihood, or minimise the objective function, normally taken to be the negative log likelihood. With a data conditional independence assumption the likelihood has the form,
$$
P(\dataVector|\mappingVector,
\inputMatrix) = \prod_{i=1}^\numData P(\dataScalar_i|\mappingVector, \inputVector_i). 
$$
which can be written as a log likelihood in the form
$$
\log P(\dataVector|\mappingVector,
\inputMatrix) = \sum_{i=1}^\numData \log P(\dataScalar_i|\mappingVector, \inputVector_i) = \sum_{i=1}^\numData
\dataScalar_i \log \pi_i + \sum_{i=1}^\numData (1-\dataScalar_i)\log (1-\pi_i)
$$
and if we take the probability of positive outcome for the $i$th data point to be given by
$$
\pi_i = \transformationFunction\left(\mappingVector^\top \basisVector(\inputVector_i)\right),
$$
where $\transformationFunction(\cdot)$ is the *inverse* link function, then this leads to an objective function of the form,
$$
\errorFunction(\mappingVector) = -  \sum_{i=1}^\numData \dataScalar_i \log
\transformationFunction\left(\mappingVector^\top \basisVector(\inputVector_i)\right) -
\sum_{i=1}^\numData(1-\dataScalar_i)\log \left(1-\transformationFunction\left(\mappingVector^\top
\basisVector(\inputVector_i)\right)\right).
$$}

\newslide{Log Likelihood}
\slides{
$$\begin{align*}
  \log P(\dataVector|\mappingVector, \inputMatrix) = &
  \sum_{i=1}^\numData \log P(\dataScalar_i|\mappingVector, \inputVector_i) \\ = &\sum_{i=1}^\numData \dataScalar_i \log
  \pi_i \\ & + \sum_{i=1}^\numData (1-\dataScalar_i)\log (1-\pi_i)
\end{align*}$$
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


\endif

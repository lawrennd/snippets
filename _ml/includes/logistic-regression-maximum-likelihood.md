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


\endif

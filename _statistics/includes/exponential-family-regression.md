\ifndef{exponentialFamilyRegression}
\define{exponentialFamilyRegression}

\editme

\subsection{Exponential Family Regression}

\notes{An important class of distribution is known as the exponential family. These distributions can be written as
$$
p(\dataVector| \naturalParameterVector) = \exp(\naturalParameterVector^\top \sufficientStatistics - \cumulantGeneratingFunction(\naturalParameterVector)) \baseMeasure(\naturalParameterVector)
$$
where $\naturalParameterVector$ is known as the \emph{natural parameters}, $\sufficientStatistics(\dataVector)$ is known as the \emph{sufficient statistics} and $\cumulantGeneratingFunction$ is the the log partition function, or the \emph{cumulant generating function} and $\baseMeasure(\cdot)$ is known as the base measure.}

\notes{For the moment we'll ignore the base measure as for several of the distributions we'll considere it's constant, so we will consider the form 
$$
p(\dataVector| \naturalParameterVector) = \exp(\naturalParameterVector^\top \sufficientStatistics - \cumulantGeneratingFunction(\naturalParameterVector)).
$$
This form yields a particularly simple likelihood function
$$
L(\naturalParameterVector) = \naturalParameterVector^\top \sufficientStatistics - \cumulantGeneratingFunction(\naturalParameterVector)
$$
and since the gradient of the cumulant generating function is the first cumulant of the sufficient statistics, the gradient of the log likelihood also has a simple form.
$$
\nabla_\naturalParameterVector L(\naturalParameterVector) = \sufficientStatistics - \expDist{\sufficientStatistics}{p(\dataVector|\naturalParameterVector)}.
$$
where $\expDist{\cdot}{p(\cdot)} denotes the expecttion under the distribution $p(\cdot)$.}

\notes{This leads to a special form of generalised linear model we call the *canonical form* where the *link function* is such that the linear function *is* the natural parameter of the distribution. For example if we have a categorical distribution with natural parameters $\naturalParameterScalar_{i,j}$, the sufficient statistic is a matrix $\dataMatrix$ where $\dataScalar_{i,j} = 1$ if the $j$th category is observed for the $i$th data point. Now if we give the natural parameters a *linear* relationship with the design matrix,
$$
\naturalParameterMatrix = \designMatrix\mappingMatrix
$$
which is equivalent to suggesting that each natural parameter is given by
$$
\naturalParameterScalar_{i,j} = \mappingVector{:, j}^\top\designVector_{i,:}.
$$
The link function that recovers this relation is known as the *canonical* link function.}

\notes{For this form the gradient of the log likelihood with respect to the model's parameters is given by 
$$
\nabla_\mappingMatrix L(\mappingMatrix) = \left(\sufficientStatistics - \expDist{\sufficientStatistics}{p(\dataVector|\naturalParameterVector)})\designMatrix.
$$
\notes{This very simple form covers all the examples we have presented so far. Let's consider their exponential family form one by one. One of the easiest to start with is the Bernoulli probability.}

\subsection{Bernoulli as Exponential Family}

\notes{The Bernoulli probability is given by
$$
P(\dataScalar) = \pi^\dataScalar(1-\pi)^(1-\dataScalar)
$$
where $\pi$ is the probability of a $\dataScalar=1$ outcome. In exponential family form the natural parameter is given by $\naturalParameterScalar = \log \frac{\pi}{1-\pi}$ and the sufficient statistics are given by $\dataScalar$. The distribution is written as
$$
P(\dataScalar|\naturalParameterScalar) = \exp(y \naturalParameterScalar - \cumualantGeneratingFunction(\naturalParameterScalar))
$$
where
$$
\cumulantGeneratingFunction(\naturalParameterScalar) = \log(1 + \exp(\naturalParameterScalar)).
$$
We can substitute back into the exponential family form to recover the original form by first recognising that
$$
\pi_i = \frac{\exp(\naturalParameterScalar)}{1+\exp(\naturalParameterScalar)}
$$
which implies that $\cumulantGeneratingFunction(\naturalParameterScalar) = - \log (1- \pi)$. Substituting this and the form of the natural parameter back into the distribution we recover
$$
P(\dataScalar|\pi) = \exp\left(\dataScalar \log \pi + (1-\dataScalar)\log (1-\pi)\right)
$$
which can be rewritten as $\pi^\dataScalar (1-\pi)^(1-\dataScalar)$ as required.}

\subsection{Categorical Distribution as Exponental Family}

\notes{The categorical distribution can be seen as a generalisation of the Bernoulli to multiple outcomes. For this distribution we have
$$
P(\dataVector) = \prod_{j=1}^C \pi_j^y_j
$$
where the $\dataVector$ is a vector of all zeros apart from the $k$th element whcih is one.}

\notes{The natural parameters are given by $\naturalParameterScalar_i = \log \pi_i$ and the sufficient statistics are just given by $\dataVector$,
$$
P(\dataVector) = \exp\left(\dataVector^\top \naturalParameterVector - \cumulantGeneratingFunction(\naturalParameterVector)\right)
$$
where $\cumulantGeneratingFunction(\naturalParameterVector) = \log \sum_{i=1}^C \exp(\naturalParameterScalar_i)$.}

\subsection{Gaussian as Exponential Family}

\notes{The natural parameters of a univariate Gaussian with mean, $\meanScalar$ and variance $\dataStd^2$,
$$
y \sim \gaussianSamp(\meanScalar, \dataStd^2)
$$
are $\naturalParameterScalar_1 = \frac{\meanScalar}{\dataStd^2}$ and $\naturalParameterScalar_2 = -\tfrac{1}{2\dataStd^2}$. This allows us to write
$$
p(y | \naturalParameterVector) = \exp(\nu_1 y + \nu_2 y^2 - \cumulantGeneratingFunction(\naturalParameterVector)
$$
where the log partition function is
$$
\cumulantGeneratingFunction(\naturalParameterScalar_1, \naturalParameterScalar_2) = \frac{\naturalParameterScalar_1^2}{4\naturalParameterScalar_2} - \frac{1}{2}\log\det{-2\naturalParameterScalar_2} - \frac{1}{2}\log 2\pi.
$$
\writeExercise{Substitute the natural parameters back into the Gaussian form to recover the standard Gaussian repesentation we've been using,
$$
p(\dataScalar | \meanScalar, \dataStd^2) = \frac{1}{\sqrt{2\pi \dataStd^2}}\exp\left(\frac{1}{2\dataStd^2}(\dataScalar-\meanScalar)^2\right).
$$
}{10}

\subsection{Poisson Distribution in Exponential Family Form}

\notes{The Poisson distribution is given by
$$
P(\dataScalar | \lambda) = \frac{\lambda^\dataScalar\exp(-\lambda)}{\dataScalar!} 
$$
natural parameter of the Poisson is $\naturalParameterScalar = \log \lambda$. The sufficient statistic is $\dataScalar$ and in the Poisson case we cannot ignore the base measure. It is given by $\baseMeasure(\dataScalar) = \frac{1}{\dataScalar!}$. The log partition function is
$$
\cumulantGeneratingFunction(\naturalParameterScalar) = \exp(\naturalParameterScalar)
$$}



\endif

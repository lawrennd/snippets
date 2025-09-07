\ifndef{exponentialFamilyRegression}
\define{exponentialFamilyRegression}

\editme

\subsection{Exponential Family Regression}

\notes{An important class of distribution is known as the exponential family. These distributions can be written as
$$
p(\dataVector| \naturalParameterVector) = \exp(\naturalParameterVector^\top \sufficientStatistics - \cumulantGeneratingFunction(\naturalParameterVector)) \baseMeasure(\naturalParameterVector)
$$
where $\naturalParameterVector$ is known as the \emph{natural parameters}, $\sufficientStatistics(\dataVector)$ is known as the \emph{sufficient statistics} and $\cumulantGeneratingFunction$ is the the log partition function, or the \emph{cumulant generating function} and $\baseMeasure(\cdot)$ is known as the base measure.}

\notes{Often the base measure can be ignored or absorbed, so we will consider the form 
$$
p(\dataVector| \naturalParameterVector) = \exp(\naturalParameterVector^\top \sufficientStatistics - \cumulantGeneratingFunction(\naturalParameterVector)).
$$
THe form yields a particularly simple likelihood function
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
\naturalParameterMatrix = \designMatrix\mappingMatrix^\top
$$
which is equivalent to suggesting that each natural parameter is given by
$$
\naturalParameterScalar_{i,j} = \mappingVector{j, :}^\top\designVector_{i,:}.
$$
The link function that recovers this relation is known as the *canonical* link function.}

\notes{For this form the gradient of the log likelihood with respect to the model's parameters is given by 
$$
\

\endif

\ifndef{theExponentialFamily}
\define{theExponentialFamily}

\editme

\subsection{The Exponential Family}

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

\endif

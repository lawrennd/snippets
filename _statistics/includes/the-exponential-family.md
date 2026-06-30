\ifndef{theExponentialFamily}
\define{theExponentialFamily}

\editme

\subsection{The Exponential Family}

\notes{An important class of distribution is known as the exponential family. These distributions can be written as
$$
p(\dataVector| \naturalParameterVector) = \exp(\naturalParameterVector^\top \sufficientStatistics - \cumulantGeneratingFunction(\naturalParameterVector)) \baseMeasure(\naturalParameterVector)
$$
where $\naturalParameterVector$ is known as the \emph{natural parameters}, $\sufficientStatistics(\dataVector)$ is known as the \emph{sufficient statistics} and $\cumulantGeneratingFunction$ is the the log partition function, or the \emph{cumulant generating function} and $\baseMeasure(\cdot)$ is known as the base measure.}

\notes{For the moment we'll ignore the base measure as for several of the distributions we'll consider it's constant, so we will consider the form 
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

\slides{
$$
p(\dataVector|\naturalParameters) = \exp\!\left(\naturalParameters^\top \sufficientStatistics(\dataVector) - \cumulantGeneratingFunction(\naturalParameters)\right)
$$

* $\naturalParameters$: natural parameters
* $\cumulantGeneratingFunction(\cdot)$: cumulant generating function 
* $G(\naturalParameters) = \nabla^2\cumulantGeneratingFunction(\naturalParameters)$: Fisher information
}

\narration{The standard exponential family is the right parameterisation for working with entropy on this configuration space. The normaliser is what machine learners would call the evidence — the cumulant generating function. The natural parameters are what you'd use to label where you are in the information geometry. The Fisher information matrix $G$ is the second derivative of the cumulant generating function with respect to the natural parameters. This is the metric on the configuration space. It tells you the local geometry of the space. And the natural gradient is the direction you move in this space that maximises entropy production most efficiently in terms of Fisher information. This becomes the core of the dynamics.}

\endif

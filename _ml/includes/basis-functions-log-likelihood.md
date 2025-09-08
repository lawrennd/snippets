\ifndef{basisFunctionsLogLikelihood}
\define{basisFunctionsLogLikelihood}

\editme

\subsection{Log Likelihood for Basis Function Model}

\notes{The likelihood of a single data point given the model parameters is given by}\slides{* The likelihood of a single data point is}
  $$
  p\left(\dataScalar_i|\inputScalar_i\right)=\frac{1}{\sqrt{2\pi\dataStd^2}}\exp\left(-\frac{\left(\dataScalar_i-\mappingVector^{\top}\basisVector_i\right)^{2}}{2\dataStd^2}\right).
  $$
\notes{and making an assumption of *conditional independence* given the parameters we can write} 
\newslide{Log Likelihood for Basis Function Model}
\slides{
* Leading to a log likelihood for the data set of}
  \begin{aligned}
  L(\mappingVector,\dataStd^2)= & -\frac{\numData}{2}\log \dataStd^2-\frac{\numData}{2}\log 2\pi \\ & -\frac{\sum_{i=1}^{\numData}\left(\dataScalar_i-\mappingVector^{\top}\basisVector_i\right)^{2}}{2\dataStd^2}.
  \end{aligned}
\notes{to give us the likelihood for the whole data set.}

\subsection{Objective Function}

\notes{Traditionally in optimization, we choose to minmize an object function (or loss function, or cost function) rather than maximizing a likelihood. For these models we *minimize the negative log likelihood*. This function takes the form,}
\slides{* And a corresponding *objective function* of the form}
$$
\errorFunction(\mappingVector,\dataStd^2)= \frac{\numData}{2}\log\dataStd^2 + \frac{\sum_{i=1}^{\numData}\left(\dataScalar_i-\mappingVector^{\top}\basisVector_i\right)^{2}}{2\dataStd^2}.
$$

\endif

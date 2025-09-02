\ifndef{otherGlmsStatsmodels}
\define{otherGlmsStatsmodels}

\editme 

\subsection{Other GLMs}

\slides{
* Logistic regression is part of a family known as *generalized linear models*
* They all take the form 
  $$g^{-1}(\mappingFunction_i(x)) = \mappingVector^\top \basisVector(\inputVector_i)$$
* Other examples include *Poisson regression*.}

\notes{We've introduced the formalism for generalised linear models. Have a think about how you might model count data using the [Poisson distribution](http://en.wikipedia.org/wiki/Poisson_distribution) and a log link function for the rate, $\lambda(\inputVector)$. If you want a data set you can try the `pods.datasets.google_trends()` for some count data.}


\endif

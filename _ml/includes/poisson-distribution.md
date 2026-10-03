\ifndef{poissonDistribution}
\define{poissonDistribution}

\editme

\subsection{Poisson Distribution}

\slides{
* Poisson distribution is used for 'count data'. For non-negative integers, $\dataScalar$, 
  $$P(\dataScalar) = \frac{\lambda^\dataScalar}{\dataScalar!}\exp(-\lambda)$$
* Here $\lambda$ is a *rate* parameter that can be thought of as the number of arrivals per unit time.
* Poisson distributions can be used for disease count data. E.g. number of incidence of malaria in a district.
}

\setupplotcode{import mlai.plot as plot}

\plotcode{plot.poisson('\writeDiagramsDir/ml/')}

\newslide{Poisson Distribution}

\figure{\includediagram{\diagramsDir/ml/poisson}{80%}}{The Poisson distribution.}{the-poisson-distribution}

\endif

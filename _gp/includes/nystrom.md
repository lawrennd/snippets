\ifndef{nystrom}
\define{nystrom}
\editme
\newslide{Nystr\"om Method}

\setupplotcode{import mlai.plot as plot}
\plotcode{plot.nystrom_covariance_approx(diagrams='\writeDiagramsDir')
plot.nystrom_covariance_approx(diagrams='\writeDiagramsDir', optimized_Z=True)}

\figure{\includediagram{\diagramsDir/cov_approx}{90%}}{Nyström approximation of a covariance: $\Kff$, the low-rank reconstruction $\Qff=\Kfu\Kuu^{-1}\Kuf$, and the factors $\Kfu$, $\Kuu$, $\Kuf$. Layout after Ed Snelson's NIPS illustration.}{cov-approx}

\notes{The Nystr\"om approximation takes the form,}
$$
\Kff \approx \Qff = \Kfu \Kuu^{-1}\Kuf
$$
\notes{The idea is that instead of inverting $\Kff$, we make a low rank (or Nyström) approximation, and invert $\Kuu$ instead.

In the original Nystr\"om method the columns to incorporate are sampled from the complete set of columns (without replacement). In a kernel matrix each of these columns corresponds to a data point. In the Nystr\"om method these points are sometimes called *landmark* points.}

\slides{
\newslide{Nystr\"om with spaced landmarks}

\figure{\includediagram{\diagramsDir/cov_approx_opt}{90%}}{Same decomposition with evenly spaced landmark inputs: $\Qff$ tracks $\Kff$ more closely.}{cov-approx-opt}
}
\endif

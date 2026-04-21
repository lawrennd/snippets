\ifndef{velocityCorrelatedSample}
\define{velocityCorrelatedSample}
\editme

\newslide{Correlation}
\slidesincremental{
* Correlation is when two variables are dependent
}

\subsection{Sampling Two Dimensional Variables}

\setupplotcode{import mlai.plot as plot}
\plotcode{plot.correlated_gaussians_sample(num_samps=8, 
                              xlabel='$v_x$',
                              ylabel='$v_y$',
                              filestub='correlated_velocities',
                              diagrams='\writeDiagramsDir/ml')}

\setupdisplaycode{import notutils as nu
from ipywidgets import IntSlider}

\displaycode{nu.display_plots('correlated_velocities{fig:0>3}.svg', 
                            directory='\writeDiagramsDir/ml', 
							fig=IntSlider(0, 0, 7, 1))}


\slides{
\define{weight}{70%}
\startanimation{correlated_velocities}{0}{7}
\newframe{\includediagram{\diagramsDir/ml/correlated_velocities000}{\width}}{correlated_velocities}
\newframe{\includediagram{\diagramsDir/ml/correlated_velocities001}{\width}}{correlated_velocities}
\newframe{\includediagram{\diagramsDir/ml/correlated_velocities002}{\width}}{correlated_velocities}
\newframe{\includediagram{\diagramsDir/ml/correlated_velocities003}{\width}}{correlated_velocities}
\newframe{\includediagram{\diagramsDir/ml/correlated_velocities004}{\width}}{correlated_velocities}
\newframe{\includediagram{\diagramsDir/ml/correlated_velocities005}{\width}}{correlated_velocities}
\newframe{\includediagram{\diagramsDir/ml/correlated_velocities006}{\width}}{correlated_velocities}
\newframe{\includediagram{\diagramsDir/ml/correlated_velocities007}{\width}}{correlated_velocities}
\endanimation
}

\notes{\figure{\includediagram{\diagramsDir/ml/correlated_velocities007}{70%}}{Samples from *correlated* Gaussian variables that represent vertical and horizontal velocity.}{correlated-velocities-7}}


\endif

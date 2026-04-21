\ifndef{velocityIndependentSample}
\define{velocityIndependentSample}
\editme

\newslide{Sampling Two Dimensional Variables}

\setupplotcode{import mlai.plot as plot}
\plotcode{plot.independent_gaussians_sample(num_samps=8, 
                               xlabel='$v_x$',
                               ylabel='$v_y$',
                               filestub="independent_velocities",
                               diagrams='\writeDiagramsDir/ml')}
							   
							
\setupdisplaycode{import notutils as nu
from ipywidgets import IntSlider}

\displaycode{nu.display_plots('independent_velocities{fig:0>3}.svg', 
                            directory='\writeDiagramsDir/ml', 
							fig=IntSlider(0, 0, 7, 1))}

\slides{
\define{width}{70%}
\startanimation{independent_velocities}{0}{7}
\newframe{\includediagram{\diagramsDir/ml/independent_velocities000}{\width}}{independent_velocities}
\newframe{\includediagram{\diagramsDir/ml/independent_velocities001}{\width}}{independent_velocities}
\newframe{\includediagram{\diagramsDir/ml/independent_velocities002}{\width}}{independent_velocities}
\newframe{\includediagram{\diagramsDir/ml/independent_velocities003}{\width}}{independent_velocities}
\newframe{\includediagram{\diagramsDir/ml/independent_velocities004}{\width}}{independent_velocities}
\newframe{\includediagram{\diagramsDir/ml/independent_velocities005}{\width}}{independent_velocities}
\newframe{\includediagram{\diagramsDir/ml/independent_velocities006}{\width}}{independent_velocities}
\newframe{\includediagram{\diagramsDir/ml/independent_velocities007}{\width}}{independent_velocities}
\endanimation
}
\notes{\figure{\includediagram{\diagramsDir/ml/independent_velocities007}{70%}}{Samples from independent Gaussian variables that represent horizontal and vertical velocities when our system is at equilibrium.}{independent-velocities-7}}

\endif

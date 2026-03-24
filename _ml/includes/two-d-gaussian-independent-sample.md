\ifndef{twoDGaussianIndependentSample}
\define{twoDGaussianIndependentSample}
\editme

\newslide{Sampling Two Dimensional Variables}

\setupplotcode{import mlai.plot as plot}
\plotcode{plot.independent_gaussians_sample(
                               mu_x=1.7, var_x=0.0225,
                               mu_y=75, var_y=36, num_samps=8,
                               xlabel='$h/m$', ylabel='$w/kg$',
                               filestub="independent_height_weight",
                               diagrams='\writeDiagramsDir/ml')}
							   
							
\setupdisplaycode{import notutils as nu
from ipywidgets import IntSlider}
\
displaycode{nu.display_plots('independent_height_weight{fig:0>3}.svg', 
                            directory='\writeDiagramsDir/ml', 
							fig=IntSlider(0, 0, 7, 1))}

\slides{
\define{width}{70%}
\startanimation{independent_height_weight}{0}{7}
\newframe{\includediagram{\diagramsDir/ml/independent_height_weight000}{\width}}{independent_height_weight}
\newframe{\includediagram{\diagramsDir/ml/independent_height_weight001}{\width}}{independent_height_weight}
\newframe{\includediagram{\diagramsDir/ml/independent_height_weight002}{\width}}{independent_height_weight}
\newframe{\includediagram{\diagramsDir/ml/independent_height_weight003}{\width}}{independent_height_weight}
\newframe{\includediagram{\diagramsDir/ml/independent_height_weight004}{\width}}{independent_height_weight}
\newframe{\includediagram{\diagramsDir/ml/independent_height_weight005}{\width}}{independent_height_weight}
\newframe{\includediagram{\diagramsDir/ml/independent_height_weight006}{\width}}{independent_height_weight}
\newframe{\includediagram{\diagramsDir/ml/independent_height_weight007}{\width}}{independent_height_weight}
\endanimation
}
\notes{\figure{\includediagram{\diagramsDir/ml/independent_height_weight007}{70%}}{Samples from independent Gaussian variables that might represent heights and weights.}{independent-height-weight-7}}

\endif

\ifndef{gpOptimizeDataFit}
\define{gpOptimizeDataFit}

\editme

\subsection{Quadratic Data Fit}

\newslide{Data Fit: $\color{\redColor}{\frac{\dataVector^\top\kernelMatrix^{-1}\dataVector}{2}}$}

\plotcode{gp_optimize_quadratic(
    lambda1=3,
    lambda2=1, 
    diagrams='\writeDiagramsDir/gp',
    fontsize=20,
    plot_width=0.6,
    generate_frames=True
)    
}

\setupdisplaycode{import notutils as nu
from ipywidgets import IntSlider}
\displaycode{nu.display_plots('gp-optimise-quadratic{sample:0>3}.svg', 
                                          directory='\writeDiagramsDir/gp', 
			                  sample=IntSlider(0, 0, 2, 1))}

\slides{\define{width}{80%}
\startanimation{gp-optimise-quadratic}{0}{2}
\newframe{\includediagram{\diagramsDir/gp/gp-optimise-quadratic000}{\width}}{gp-optimise-quadratic}
\newframe{\includediagram{\diagramsDir/gp/gp-optimise-quadratic001}{\width}}{gp-optimise-quadratic}
\newframe{\includediagram{\diagramsDir/gp/gp-optimise-quadratic002}{\width}}{gp-optimise-quadratic}
\endanimation}

\figure{\includediagram{\diagramsDir/gp/gp-optimise-quadratic002}{80%}}{The data fit term of the Gaussian process is a quadratic loss centered around zero. This has eliptical contours, the principal axes of which are given by the covariance matrix.}{gp-optimise-quadratic}

\newslide{$$\errorFunction(\parameterVector) = \color{\blueColor}{\frac{1}{2}\log\det{\kernelMatrix}}+\color{\redColor}{\frac{\dataVector^{\top}\kernelMatrix^{-1}\dataVector}{2}}$$}

\endif

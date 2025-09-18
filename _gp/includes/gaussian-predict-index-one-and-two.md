\ifndef{gaussianPredictIndexOneAndTwo}
\define{gaussianPredictIndexOneAndTwo}
\editme


\subsection{Sampling a Function}

\notes{We will consider a *multivariate Gaussian* with a particular structure of covariance matrix. We will generate a *single* sample from this 25 dimensional Gaussian density.}
\slides{**Multi-variate Gaussians**

* We will consider a Gaussian with a particular structure of covariance matrix.
* Generate a single sample from this 25 dimensional Gaussian density,}
$$
\mappingFunctionVector=\left[\mappingFunction_{1},\mappingFunction_{2}\dots \mappingFunction_{25}\right].
$$
\slides{* We will plot these points against their index.}\notes{in the figure below we plot these data on the $y$-axis against their *indices* on the $x$-axis.}


\setupcode{import numpy as np
np.random.seed(4949)}

\loadcode{Kernel}{mlai}
\loadcode{polynomial_cov}{mlai}
\loadcode{eq_cov}{mlai}

\setupplotcode{import mlai.plot as plot}
\plotcode{kernel=Kernel(function=eq_cov, lengthscale=0.5)
plot.two_point_sample(kernel.K, diagrams='\writeDiagramsDir/gp')}

\subsubsection{Sampling a Function from a Gaussian}

\setupdisplaycode{import notutils as nu
from ipywidgets import IntSlider}
\setupdisplaycode{import notutils as nu}
\displaycode{nu.display_plots('two_point_sample{sample:0>3}.svg', 
                            '\writeDiagramsDir/gp', 
							sample=IntSlider(0, 0, 8, 1))}

\slides{
\define{width}{80%}
\startanimation{two-point-sample}{9}{12}
\newframe{\includediagram{\diagramsDir/gp/two_point_sample000}{\width}}{two-point-sample}
\newframe{\includediagram{\diagramsDir/gp/two_point_sample001}{\width}}{two-point-sample}
\newframe{\includediagram{\diagramsDir/gp/two_point_sample002}{\width}}{two-point-sample}
\newframe{\includediagram{\diagramsDir/gp/two_point_sample003}{\width}}{two-point-sample}
\newframe{\includediagram{\diagramsDir/gp/two_point_sample004}{\width}}{two-point-sample}
\newframe{\includediagram{\diagramsDir/gp/two_point_sample005}{\width}}{two-point-sample}
\newframe{\includediagram{\diagramsDir/gp/two_point_sample006}{\width}}{two-point-sample}
\newframe{\includediagram{\diagramsDir/gp/two_point_sample007}{\width}}{two-point-sample}
\newframe{\includediagram{\diagramsDir/gp/two_point_sample008}{\width}}{two-point-sample}
\endanimation
}

\notes{\figure{\includediagram{\diagramsDir/gp/two_point_sample001}{80%}}{The joint Gaussian over $\mappingFunction_1$ and $\mappingFunction_2$ along with the conditional distribution of $\mappingFunction_2$ given $\mappingFunction_1$}{two-point-sample-one-two}}


\subsubsection{Joint Density of $f_1$ and $f_2$}

\setupdisplaycode{import notutils as nu
from ipywidgets import IntSlider}
\setupdisplaycode{import notutils as nu}
\displaycode{nu.display_plots('two_point_sample{sample:0>3}.svg', 
                            '\writeDiagramsDir/gp', 
							sample=IntSlider(9, 9, 12, 1))}

\newslide{Prediction of $\mappingFunction_{2}$ from $\mappingFunction_{1}$}

\slides{
\define{width}{80%}
\startanimation{two_point_sample2}{9}{12}
\newframe{\includediagram{\diagramsDir/gp/two_point_sample009}{\width}}{two_point_sample2}
\newframe{\includediagram{\diagramsDir/gp/two_point_sample010}{\width}}{two_point_sample2}
\newframe{\includediagram{\diagramsDir/gp/two_point_sample011}{\width}}{two_point_sample2}
\newframe{\includediagram{\diagramsDir/gp/two_point_sample012}{\width}}{two_point_sample2}
\endanimation
}

\notes{\figure{\includediagram{\diagramsDir/gp/two_point_sample012}{80%}}{The joint Gaussian over $\mappingFunction_1$ and $\mappingFunction_2$ along with the conditional distribution of $\mappingFunction_2$ given $\mappingFunction_1$}{two-point-sample-one-two}}

\endif

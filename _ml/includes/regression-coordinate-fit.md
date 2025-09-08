\ifndef{regressionCoordinateFit}
\define{regressionCoordinateFit}


\subsection{Regression Coordiate Fit}

\notes{Now we'll run Each frame shows:

- *Current position*: The green star indicating our current parameter estimates
- *Error contours*: The background showing the error landscape
- *Path*: The trajectory we've taken from the starting point to the current position

Watch how the algorithm follows a "staircase" path that converges towards the minimum. Note that the more correlated $m$ and $c$ are (principle axes of the ellipse contours is diagonal) the slower the convergence towards the minimum demonstrating the potential limitation of coordinate descent.}

\setupplotcode{import mlai.plot as plot}
\plotcode{num_plots = plot.regression_contour_coordinate_descent(x, y, max_iters=10, diagrams='\writeDiagramsDir/ml')}

\setupdisplaycode{import notutils as nu
from ipywidgets import IntSlider}

\displaycode{nu.display_plots('regression_coordinate_descent_contour_fit{num:0>3}.svg', directory='\writeDiagramsDir/ml', num=IntSlider(0, 0, num_plots, 1))}

\slides{
\define{width}{60%}
\startanimation{regression_coordinate_descent_contour_fit}{1}{20}
\newframe{\includediagram{\diagramsDir/ml/regression_coordinate_descent_contour_fit000}{\width}}{regression_coordinate_descent_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_coordinate_descent_contour_fit001}{\width}}{regression_coordinate_descent_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_coordinate_descent_contour_fit002}{\width}}{regression_coordinate_descent_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_coordinate_descent_contour_fit003}{\width}}{regression_coordinate_descent_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_coordinate_descent_contour_fit004}{\width}}{regression_coordinate_descent_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_coordinate_descent_contour_fit005}{\width}}{regression_coordinate_descent_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_coordinate_descent_contour_fit006}{\width}}{regression_coordinate_descent_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_coordinate_descent_contour_fit007}{\width}}{regression_coordinate_descent_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_coordinate_descent_contour_fit008}{\width}}{regression_coordinate_descent_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_coordinate_descent_contour_fit009}{\width}}{regression_coordinate_descent_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_coordinate_descent_contour_fit010}{\width}}{regression_coordinate_descent_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_coordinate_descent_contour_fit011}{\width}}{regression_coordinate_descent_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_coordinate_descent_contour_fit012}{\width}}{regression_coordinate_descent_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_coordinate_descent_contour_fit013}{\width}}{regression_coordinate_descent_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_coordinate_descent_contour_fit014}{\width}}{regression_coordinate_descent_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_coordinate_descent_contour_fit015}{\width}}{regression_coordinate_descent_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_coordinate_descent_contour_fit016}{\width}}{regression_coordinate_descent_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_coordinate_descent_contour_fit017}{\width}}{regression_coordinate_descent_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_coordinate_descent_contour_fit018}{\width}}{regression_coordinate_descent_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_coordinate_descent_contour_fit019}{\width}}{regression_coordinate_descent_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_coordinate_descent_contour_fit020}{\width}}{regression_coordinate_descent_contour_fit}
\endanimation
}

\notes{\figure{\includediagram{\diagramsDir/ml/regression_coordinate_descent_contour_fit020}{60%}}{Coordinate descent for linear regression showing the path after 20 updates between $c$ and $m$.}{regression-coordinate-descent-contour-fit20}}

\endif

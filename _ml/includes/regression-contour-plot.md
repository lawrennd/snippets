\ifndef{regressionContourPlot}
\define{regressionContourPlot}

\editme

\subsection{Contour Plot of Error Function}

* Visualise the error function surface,
create vectors of values.

\code{# create an array of linearly separated values around m_true
m_vals = np.linspace(m_true-3, m_true+3, 100) 
# create an array of linearly separated values ae
c_vals = np.linspace(c_true-3, c_true+3, 100)}

* create a grid of values to evaluate the error function in 2D.

\code{m_grid, c_grid = np.meshgrid(m_vals, c_vals)}

* compute the error function at each  combination of $c$ and $m$.

\code{E_grid = np.zeros((100, 100))
for i in range(100):
    for j in range(100):
        E_grid[i, j] = ((y - m_grid[i, j]*x - c_grid[i, j])**2).sum()}

\subsection{Contour Plot of Error}

\slides{* We can now make a contour plot.}

\setupplotcode{import mlai.plot as plot
import mlai}

\plotcode{f, ax = plt.subplots(figsize=(5,5))
plot.regression_contour(f, ax, m_vals, c_vals, E_grid)
mlai.write_figure(filename='regression_contour.svg', directory='\writeDiagramsDir/ml')}

\figure{\includediagram{\diagramsDir/ml/regression_contour}{60%}}{Contours of the objective function for linear regression by minimizing least squares.}{regression-contour}

\endif

\ifndef{regressionContourPlot}
\define{regressionContourPlot}

\editme

\subsection{Contour Plot of Error Function}

\notes{To understand how the least squares algorithm works, it's helpful to visualize the error function as a surface in parameter space. Since we have two parameters ($m$ and $c$), our error function $\errorFunction(m, c)$ defines a surface in 3D space where the height at any point represents the error for that combination of parameters.

The global minimum of this surface is given by the optimal parameter values that best fit our data according to the least squares objective. By visualising this surface through contour plots, we can gain intuition about the optimization landscape and understand why gradient-based methods work effectively for this problem.}

\notes{First, we create vectors of parameter values to explore around the true values we used to generate the data. We sample points in a range around the true parameters to see how the error function behaves in the local neighborhood.}


\code{# create an array of linearly separated values around m_true
m_vals = np.linspace(m_true-3, m_true+3, 100) 
# create an array of linearly separated values around c_true
c_vals = np.linspace(c_true-3, c_true+3, 100)}

\notes{Next, we create a 2D grid from these parameter vectors. This grid allows us to evaluate the error function at every combination of $m$ and $c$ values, giving us a complete picture of the error surface over the parameter space we're exploring.}


\code{m_grid, c_grid = np.meshgrid(m_vals, c_vals)}

\notes{Now we compute the error function at each combination of parameters. For each point in our grid, we:
1. Use the parameter values to make predictions: $\hat{y}_i = m \cdot x_i + c$  
2. Calculate the squared errors: $(y_i - \hat{y}_i)^2$
3. Sum these squared errors to get the total error for that parameter combination

This gives us the complete error surface that we can then visualize. The nested loop structure evaluates the sum of squared errors formula at each $(m, c)$ coordinate in our grid.}


\code{E_grid = np.zeros((100, 100))
for i in range(100):
    for j in range(100):
        E_grid[i, j] = ((y - m_grid[i, j]*x - c_grid[i, j])**2).sum()}

\notes{With our error surface computed, we can now create a contour plot to visualize the optimization landscape. A contour plot shows lines of equal error value, similar to elevation contours on a topographic map. 

Insights from this visualisation include:
- *Bowl-shaped surface*: For linear regression with least squares, the error surface is a smooth, convex bowl with a unique global minimum
- *Contour lines*: Each contour represents parameter combinations that yield the same error value
- *Minimum location*: The centre of the concentric ellipses shows where the error is minimized - this should be close to our true parameter values

This visualisation helps explain why least squares regression has nice mathematical properties and why optimisation algorithms converge reliably to the solution.}


\setupplotcode{import mlai.plot as plot
import mlai}

\plotcode{f, ax = plt.subplots(figsize=(5,5))
plot.regression_contour(f, ax, m_vals, c_vals, E_grid)
mlai.write_figure(filename='regression_contour.svg', directory='\writeDiagramsDir/ml')}

\figure{\includediagram{\diagramsDir/ml/regression_contour}{60%}}{Contours of the objective function for linear regression by minimizing least squares.}{regression-contour}

\notes{The contour plot reveals the characteristic elliptical shape of the least squares error surface. The concentric ellipses represent increasing levels of error as we move away from the optimal parameters. 

Key observations from this visualization:
- *Convex optimisation*: The smooth, bowl-shaped surface guarantees that any local minimum is also the global minimum
- *Parameter sensitivity*: The shape of the ellipses tells us how sensitive the error is to changes in each parameter
- *Optimization efficiency*: The regular, predictable shape means we can develop optimisation methods that will converge quickly and reliably
- *True parameter location*: The minimum should occur very close to our known true values ($m_{true} = 1.4$, $c_{true} = -3.1$)

*Warning:* This visualisation is great for giving some intuition, but can be quite misleading about how these objective funcitons look in very high dimensions. Unfortunately high dimensions are much harder to visualise.}

\endif

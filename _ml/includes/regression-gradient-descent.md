\ifndef{regressionGradientDescent}
\define{regressionGradientDescent}

\editme

\subsection{Steepest Descent}

\notes{Now that we understand the shape of the error surface from our contour plot, we need an algorithm to find the minimum. Gradient descent is one of the most fundamental optimization algorithms in machine learning.

The intuition behind gradient descent is simple: imagine you're standing on a hillside in fog and want to reach the bottom. Even though you can't see the whole landscape, you can feel the steepest downward slope at your current position. By repeatedly taking steps in the steepest downward direction, you'll eventually reach the bottom.

Mathematically, the gradient points in the direction of steepest ascent, so we move in the negative gradient direction to descend toward the minimum. The algorithm works by:
1. Starting with an initial guess for our parameters
2. Computing the gradient (slope) of the error function at that point
3. Taking a small step in the opposite direction of the gradient
4. Repeating until we converge to the minimum}

\slides{* Minimise the sum of squares error function. 
* E.g. gradient descent. 
* Initialise with a guess for $m$ and $c$ 
* update that guess by subtracting a portion of the gradient from the guess. 
* Like walking down a hill in the steepest direction of the hill to get to the
bottom.}

\subsection{Algorithm}

\notes{The first step in gradient descent is to initialise our parameters with some starting values. The choice of initial values can affect how quickly the algorithm converges, although because of the simple shape of the linear regression objective (known as a convex optimisation), any starting point should eventually reach the global minimum.

Here we're starting with $m = 0$ (no slope) and $c = -5$ (a negative intercept). These values are deliberately chosen to be different from our true values ($m_{true} = 1.4$, $c_{true} = -3.1$) so we can see the algorithm as it navigates toward the correct solution. Normally you would initialise with smaller values closer to the origin.}

\slides{* We start with a guess for $m$ and $c$.

```
m_star = 0.0
c_star = -5.0
```
}

\code{m_star = 0.0
c_star = -5.0}

\subsection{Offset Gradient}

\notes{To implement gradient descent, we need to compute the partial derivatives of our error function with respect to each parameter. We'll start with the gradient with respect to the intercept parameter $c$.

Our error function is
$$\errorFunction(m, c) = \sum_{i=1}^\numData (\dataScalar_i - m\inputScalar_i - c)^2$$

To find how the error changes with respect to $c$, we use the chain rule. Each squared term contributes to the gradient, and since $c$ appears in every term with a coefficient of $-1$, the partial derivative becomes:
$$\frac{\text{d}\errorFunction(m, c)}{\text{d} c} = -2\sum_{i=1}^\numData (\dataScalar_i - m\inputScalar_i - c)$$

The negative sign comes from differentiating the $-c$ term inside the squared expression, and the factor of 2 comes from differentiating the square.}

\slides{* Gradient of the error wrt $c$,
    $$
	\frac{\text{d}\errorFunction(m, c)}{\text{d} c} = -2\sum_{i=1}^\numData (\dataScalar_i - m\inputScalar_i - c)
	$$
}
\newslide{Compute as}

\slides{
```
c_grad = -2*(y-m_star*x - c_star).sum()
```}

\code{c_grad = -2*(y-m_star*x - c_star).sum()
print("Gradient with respect to c is ", c_grad)}

\notes{\subsection{Deriving the Gradient}}

\notes{To understand how we derived the gradient formula, let's work through the calculus step by step.

The error function has the form:
$$\errorFunction(m, c) = \sum_{i=1}^\numData (\dataScalar_i - m\inputScalar_i - c)^2$$

For the derivative with respect to $c$, note that $c$ appears in every term of the sum. For each term $(\dataScalar_i - m\inputScalar_i - c)^2$, we apply the chain rule:

1. *Outer function*: The derivative of $u^2$ is $2u$
2. *Inner function*: The derivative of $(\dataScalar_i - m\inputScalar_i - c)$ with respect to $c$ is $-1$

Combining these: $\frac{d}{dc}[(\dataScalar_i - m\inputScalar_i - c)^2] = 2(\dataScalar_i - m\inputScalar_i - c) \cdot (-1)$

Since this applies to all terms in the sum, we get:
$$\frac{\text{d}\errorFunction(m, c)}{\text{d} c} = -2\sum_{i=1}^\numData (\dataScalar_i - m\inputScalar_i - c)$$}

\subsection{Slope Gradient}

\notes{The gradient with respect to the slope parameter $m$ follows the same chain rule approach, but now $m$ appears multiplied by $\inputScalar_i$ in each term.

For the derivative with respect to $m$, each term $(\dataScalar_i - m\inputScalar_i - c)^2$ contributes:
1. *Outer function*: Still $2u$ where $u = (\dataScalar_i - m\inputScalar_i - c)$
2. *Inner function*: The derivative of $(\dataScalar_i - m\inputScalar_i - c)$ with respect to $m$ is $-\inputScalar_i$

This gives us:
$$\frac{\text{d}\errorFunction(m, c)}{\text{d} m} = -2\sum_{i=1}^\numData \inputScalar_i(\dataScalar_i - m\inputScalar_i - c)$$

Notice that each term is weighted by $\inputScalar_i$, which makes intuitive sense: data points with larger input values have more influence on the slope parameter.}


\slides{Gradient wrt $m$ is similar
$$
\frac{\text{d}\errorFunction(m, c)}{\text{d} m} = -2\sum_{i=1}^\numData \inputScalar_i(\dataScalar_i - m\inputScalar_i -
c)
$$}

\newslide{Compute as}

\slides{which can be implemented in python (numpy) as
```
m_grad = -2*(x*(y-m_star*x - c_star)).sum()
```
}
\code{m_grad = -2*(x*(y-m_star*x - c_star)).sum()
print("Gradient with respect to m is ", m_grad)}

\subsection{Update Equations}

\notes{Now that we have computed both gradients, we can update our parameter estimates. The key insight is that we don't want to simply subtract the full gradient from our current parameter values - this would likely cause us to overshoot the minimum.

Instead, we take small steps in the negative gradient direction. This is crucial because:
1. *Gradient changes*: As we move through parameter space, the gradient itself changes, so we need to recompute it frequently
2. *Overshooting*: Large steps might cause us to jump over the minimum and potentially diverge
3. *Local information*: The gradient only gives us local information about the slope, not global information about the entire surface

The size of the step we take is controlled by the learning rate, which we'll introduce shortly.}

\slides{
* Gradients with respect to $m$ and $c$.
* Can update our inital guesses for $m$ and $c$ using the gradient. 
}

\newslide{Update Equations}

\slides{
* We don't want to just subtract the gradient from $m$ and $c$, 
* We need to take a *small* step in the gradient direction. 
* Otherwise we might overshoot the minimum. 
}

\newslide{Update Equations}

\slides{
* We want to follow the gradient to get to the minimum, the gradient
changes all the time.
}

\subsection{Move in Direction of Gradient}

\notes{Let's visualize what a single gradient descent step looks like on our error surface. The plot shows our current parameter position as a green star and the direction we should move (negative gradient direction) as an arrow.

The arrow points toward lower error values, following the steepest descent path from our current location. Notice how the arrow is perpendicular to the contour lines - this is always true for gradients, which by definition point in the direction of steepest increase (and thus their negative points in the direction of steepest decrease).

The length and direction of this arrow tell us:
- *Direction*: Where to move in parameter space
- *Magnitude*: How steep the slope is (longer arrows mean steeper slopes)
- *Step size*: We scale the arrow by the learning rate to determine our actual step size}

\setupplotcode{import mlai.plot as plot}
\plotcode{f, ax = plt.subplots(figsize=plot.big_figsize)
plot.regression_contour(f, ax, m_vals, c_vals, E_grid)
ax.plot(m_star, c_star, 'g*', markersize=20)
ax.arrow(m_star, c_star, -m_grad*0.1, -c_grad*0.1, head_width=0.2)
mlai.write_figure(filename='regression_contour_step001.svg', directory='\writeDiagramsDir/ml/', transparent=True)}

\figure{\includediagram{\diagramsDir/ml/regression_contour_step001}{60%}}{Single update descending the contours of the error surface for regression.}{regression-contour-step-1}

\subsection{Update Equations}

\notes{The crucial hyperparameter in gradient descent is the learning rate $\learnRate$, which controls how big steps we take in the direction of the negative gradient. The learning rate is a balancing act:

- *Too large*: We might overshoot the minimum, potentially causing the algorithm to diverge or oscillate wildly
- *Too small*: The algorithm will converge very slowly, requiring many iterations to reach the minimum
- *Just right*: We make steady progress toward the minimum without overshooting

The update equations formally incorporate the learning rate:}

\slides{* The step size has already been introduced
* it's known as the learning rate and is denoted by $\learnRate$. 
  $$
  c_\text{new}\leftarrow c_{\text{old}} - \learnRate \frac{\text{d}\errorFunction(m, c)}{\text{d}c}
$$ 
}
\newslide{Step Size}

\slides{
* gives us an update for our estimate of $c$ and
$$
m_\text{new} \leftarrow m_{\text{old}} - \learnRate \frac{\text{d}\errorFunction(m, c)}{\text{d}m}
$$
* Giving us an update for $m$.}

\subsection{Update Code}

\notes{Let's implement the parameter updates in code. We choose a learning rate of 0.01, which is small enough to ensure stable convergence but large enough to make reasonable progress.

The code shows the before and after parameter values, demonstrating how a single gradient descent step moves us closer to the optimal solution. After this update, we would recompute the gradients at our new position and repeat the process.}

\slides{* These updates can be coded as
```
learn_rate = 0.01
c_star = c_star - learn_rate*c_grad
m_star = m_star - learn_rate*m_grad
```}

\code{print("Original m was", m_star, "and original c was", c_star)
learn_rate = 0.01
c_star = c_star - learn_rate*c_grad
m_star = m_star - learn_rate*m_grad
print("New m is", m_star, "and new c is", c_star)}

\subsection{Iterating Updates}

\notes{One gradient step only takes us partway to the minimum. The full gradient descent algorithm requires iterating these updates until convergence. The process is:

1. *Initialise* parameters with random or reasonable starting values
2. *Compute gradients* at the current position
3. *Update parameters* using the gradient and learning rate
4. *Repeat* steps 2-3 until convergence (gradients become very small or error stops decreasing)

The beauty of this algorithm is its simplicity and general applicability - the same basic approach works for many different types of models and error functions.}

\slides{* Fit model by descending gradient.}

\subsection{Gradient Descent Algorithm}

\notes{Let's run the complete gradient descent algorithm and visualize how the parameters evolve over multiple iterations. The animation will show the path taken through parameter space as the algorithm navigates toward the minimum of the error surface.

Each frame shows:

- *Current position*: The green star indicating our current parameter estimates
- *Error contours*: The background showing the error landscape
- *Path*: The trajectory we've taken from the starting point to the current position

Watch how the algorithm follows a curved path that eventually spiral into the minimum, demonstrating the iterative nature of gradient-based optimization.}

\code{num_plots = plot.regression_contour_fit(x, y, diagrams='\writeDiagramsDir/ml')}

\setupdisplaycode{import notutils as nu
from ipywidgets import IntSlider}

\displaycode{nu.display_plots('regression_contour_fit{num:0>3}.svg', directory='\writeDiagramsDir/ml', num=IntSlider(0, 0, num_plots, 1))}

\slides{
\define{width}{60%}
\startanimation{regression_contour_fit}{1}{28}
\newframe{\includediagram{\diagramsDir/ml/regression_contour_fit000}{\width}}{regression_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_contour_fit001}{\width}}{regression_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_contour_fit002}{\width}}{regression_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_contour_fit003}{\width}}{regression_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_contour_fit004}{\width}}{regression_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_contour_fit005}{\width}}{regression_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_contour_fit006}{\width}}{regression_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_contour_fit007}{\width}}{regression_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_contour_fit008}{\width}}{regression_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_contour_fit009}{\width}}{regression_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_contour_fit010}{\width}}{regression_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_contour_fit011}{\width}}{regression_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_contour_fit012}{\width}}{regression_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_contour_fit013}{\width}}{regression_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_contour_fit014}{\width}}{regression_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_contour_fit015}{\width}}{regression_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_contour_fit016}{\width}}{regression_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_contour_fit017}{\width}}{regression_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_contour_fit018}{\width}}{regression_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_contour_fit019}{\width}}{regression_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_contour_fit020}{\width}}{regression_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_contour_fit021}{\width}}{regression_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_contour_fit022}{\width}}{regression_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_contour_fit023}{\width}}{regression_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_contour_fit024}{\width}}{regression_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_contour_fit025}{\width}}{regression_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_contour_fit026}{\width}}{regression_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_contour_fit027}{\width}}{regression_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_contour_fit028}{\width}}{regression_contour_fit}
\endanimation
}

\notes{\figure{\includediagram{\diagramsDir/ml/regression_contour_fit028}{60%}}{Batch gradient descent for linear regression showing the final converged solution.}{regression-contour-fit-28}

The final frame shows the algorithm has converged to the minimum of the error surface. Notice how:

- *Path shape*: The trajectory follows the natural gradient flow, starting with larger steps when gradients are large and taking smaller steps as we approach the minimum
- *Convergence*: The final position should be very close to our true parameter values ($m_{true} = 1.4$, $c_{true} = -3.1$)
- *Efficiency*: The algorithm finds the optimal solution automatically without us needing to specify the answer ahead of time

But note the limitations of gradient-based optimisation: by following local information (the gradient), we can sometimes approach the minimum only very slowly. To improve convergence we can look to more advanced methods that consider curvature or, in neural networks, methods that use a stochastic approximation to the gradient.}

\endif

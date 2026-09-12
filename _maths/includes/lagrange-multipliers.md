\ifndef{lagrangeMultipliers}
\define{lagrangeMultipliers}

\editme

\subsection{Lagrange Multipliers}

\notes{Many problems in physics, engineering and machine learning ask us to optimise a function subject to constraints. For example, we free energy minimisation, or maximising entropy while matching observed averages.[^free-entropy] Principal component analysis can be formulated as finding directions in data of maximum variance. Each direction is constrained to be orthogonal to the previous one. Lagrange multipliers turn these constrained problems into unconstrained ones.}

\notes{[^free-entropy]: Although because total energy is given by free energy plus temperature-scaled entropy, these two optimisations are two sides of the same coin.}

\slides{
* Constrained optimisation appears throughout physics, engineering and machine learning.
* Lagrange multipliers convert constraints into terms in an auxiliary function
* At the optimum, the objective gradient is normal to the constraint surface
}

\subsection{One Equality Constraint}

\notes{If we want to find a stationary point of a function, $f(\mathbf{x})$, and we know that another function $g(\mathbf{x}) = c$ is constrained such that $g(\mathbf{x}) = c$ we 
introduce a *Lagrange multiplier*, often denoted by $\lambda$ and form the *Lagrangian*,
$$
\mathscr{L}(\mathbf{x}, \lambda) = f(\mathbf{x}) + \lambda\bigl(g(\mathbf{x}) - c\bigr).
$$
We are optimising with respect to $\mathbf{x}$ and the gradient of the Lagrangian is given by
$$
\nabla_{\mathbf{x}} \mathscr{L} = \nabla f + \lambda \nabla g,
$$
but we now also have the gradient of the Lagrangian with respect to the Lagrange multiplier,
$$
\frac{\partial \mathscr{L}}{\partial \lambda} = g(\mathbf{x}) - c.
$$
Think about what happens when we set both gradients to zero (as we would do if we were looking for a stationary point of an unconstrained function). The first equation is now
$$
\nabla f + \lambda \nabla g = \mathbf{0}
$$
which tells us that $\nabla f$ is parallel to $\nabla g$, and therefore the gradient of the objective, $\nabla f$, is perpendicular to the constraint surface.}

\slides{
**Single constraint:**
$$
\mathscr{L}(\mathbf{x}, \lambda) = f(\mathbf{x}) + \lambda\left(g(\mathbf{x}) - c\right)
$$

**Stationarity:**
$$
\nabla f + \lambda \nabla g = 0, \qquad g(\mathbf{x}) = c
$$
}
\newslide{Stationarity: parallel gradients}

\setupplotcode{import mlai.plot as plot}

\plotcode{plot.lagrange_parallel_vectors(diagrams='\writeDiagramsDir/physics/')}

\setupdisplaycode{import notutils as nu
from ipywidgets import IntSlider}
\displaycode{nu.display_plots('lagrange-parallel-vectors{sample:0>3}.svg',
                                          directory='\writeDiagramsDir/physics',
                                          sample=IntSlider(0, 0, 12, 1))}

\slides{\define{width}{70%}
\startanimation{lagrange-parallel-vectors}{0}{13}
\newframe{\includediagram{\diagramsDir/physics/lagrange-parallel-vectors000}{\width}}{lagrange-parallel-vectors}
\newframe{\includediagram{\diagramsDir/physics/lagrange-parallel-vectors001}{\width}}{lagrange-parallel-vectors}
\newframe{\includediagram{\diagramsDir/physics/lagrange-parallel-vectors002}{\width}}{lagrange-parallel-vectors}
\newframe{\includediagram{\diagramsDir/physics/lagrange-parallel-vectors003}{\width}}{lagrange-parallel-vectors}
\newframe{\includediagram{\diagramsDir/physics/lagrange-parallel-vectors004}{\width}}{lagrange-parallel-vectors}
\newframe{\includediagram{\diagramsDir/physics/lagrange-parallel-vectors005}{\width}}{lagrange-parallel-vectors}
\newframe{\includediagram{\diagramsDir/physics/lagrange-parallel-vectors006}{\width}}{lagrange-parallel-vectors}
\newframe{\includediagram{\diagramsDir/physics/lagrange-parallel-vectors007}{\width}}{lagrange-parallel-vectors}
\newframe{\includediagram{\diagramsDir/physics/lagrange-parallel-vectors008}{\width}}{lagrange-parallel-vectors}
\newframe{\includediagram{\diagramsDir/physics/lagrange-parallel-vectors009}{\width}}{lagrange-parallel-vectors}
\newframe{\includediagram{\diagramsDir/physics/lagrange-parallel-vectors010}{\width}}{lagrange-parallel-vectors}
\newframe{\includediagram{\diagramsDir/physics/lagrange-parallel-vectors011}{\width}}{lagrange-parallel-vectors}
\newframe{\includediagram{\diagramsDir/physics/lagrange-parallel-vectors012}{\width}}{lagrange-parallel-vectors}
\endanimation}

\notes{\figure{\includediagram{\diagramsDir/physics/lagrange-parallel-vectors012}{70%}}{At stationarity, $\nabla f + \lambda\nabla g = \mathbf{0}$: the objective gradient is balanced by the constraint gradient scaled by $\lambda$ (here $\lambda = -\frac{1}{2}$ in the worked example).}{lagrange-parallel-vectors-figure}}

\notes{The second condition, 
$$
g(\mathbf{x}) - c = 0,
$$
just enforces the constraint itself ($g(\mathbf{x}) = c$).}

\newslide{Geometric picture}

\notes{Picture climbing a hill (maximise $f$) while staying on a path defined by $g(\mathbf{x}) = c$. At the highest point reachable on the path, you cannot move along the path and still increase $f$. That means $\nabla f$ points off the path, normal to the constraint surface. The multiplier $\lambda$ measures how strongly the constraint must pull against the unconstrained gradient.}

\slides{
* At a constrained optimum, $\nabla f$ is normal to the constraint surface
* If $\nabla f$ had a component tangent to the surface, we could improve $f$ without leaving it
* $\lambda$ is the strength of the constraint force
}

\subsection{Several Equality Constraints}

\notes{With multiple constraints $g_k(\mathbf{x}) = c_k$ for $k = 1, \ldots, m$, introduce one multiplier $\lambda_k$ for each constraint:
$$
\mathscr{L}(\mathbf{x}, \boldsymbol{\lambda}) = f(\mathbf{x}) + \sum_{k=1}^m \lambda_k \bigl(g_k(\mathbf{x}) - c_k\bigr).
$$
Stationarity gives
\begin{align}
\nabla f + \sum_{k=1}^m \lambda_k \nabla g_k &= 0, \\
g_k(\mathbf{x}) &= c_k \quad k = 1, \ldots, m.
\end{align}
Each multiplier enforces one constraint; together they specify how far the objective gradient is rotated onto the intersection of the constraint surfaces.}

\slides{
**Several constraints:**
$$
\mathscr{L} = f(\mathbf{x}) + \sum_k \lambda_k \bigl(g_k(\mathbf{x}) - c_k\bigr)
$$

**Stationarity:**
$$
\nabla f + \sum_k \lambda_k \nabla g_k = 0, \qquad g_k(\mathbf{x}) = c_k
$$
}

\subsection{A Worked Example}

\notes{The method is clearer on a small problem before we apply it to probabilities. Minimise
$$
f(x,y) = \frac{1}{2}(x^2 + y^2)
$$
subject to the linear constraint $x + y = 1$. Geometrically, we seek the point on the line closest to the origin; physically, this is the same pattern as minimising a quadratic energy or loss while a conserved quantity remains fixed. The Lagrangian is
$$
\mathscr{L}(x,y,\lambda) = \frac{1}{2}(x^2 + y^2) + \lambda(x + y - 1).
$$
Stationarity gives $x + \lambda = 0$, $y + \lambda = 0$, and $x + y = 1$, hence $x = y = \frac{1}{2}$ and $\lambda = -\frac{1}{2}$. The gradient of $f$ at the solution is $(1,1)$, parallel to the constraint normal $(1,1)$ as required.}

\notes{The same template appears in machine learning: minimise a squared error or regulariser $\frac{1}{2}\|\mathbf{w}\|^2$ subject to a linear prediction constraint $\mathbf{w}^\top \mathbf{x} = y$. The multiplier $\lambda$ then plays the role of a Lagrange multiplier in ridge regression and support-vector margins. We do not need that full story here; the point is that one constraint adds one multiplier and reduces the problem to solving linear stationarity conditions.}

\slides{
**Example:** minimise $\frac{1}{2}(x^2+y^2)$ subject to $x+y=1$

$$
\mathscr{L} = \frac{1}{2}(x^2+y^2) + \lambda(x+y-1)
$$

**Solution:** $x = y = \frac{1}{2}$, $\lambda = -\frac{1}{2}$

*Closest point on a line; same pattern as constrained energy or $\|\mathbf{w}\|^2$ with a linear constraint*
}

\endif

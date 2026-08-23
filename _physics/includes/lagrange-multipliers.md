\ifndef{lagrangeMultipliers}
\define{lagrangeMultipliers}

\editme

\subsection{Lagrange Multipliers}

\notes{Many problems in physics and machine learning ask us to optimise a function subject to constraints. We might minimise energy while holding volume fixed, or maximise entropy while matching observed averages. Lagrange multipliers turn such constrained problems into unconstrained ones.}

\slides{
* Constrained optimisation appears throughout inference and physics
* Lagrange multipliers convert constraints into terms in an auxiliary function
* At the optimum, the objective gradient is normal to the constraint surface
}

\subsection{One Equality Constraint}

\notes{Consider
$$
\text{extremise } f(\mathbf{x}) \quad \text{subject to } g(\mathbf{x}) = c.
$$
Introduce a multiplier $\lambda$ and form the Lagrangian
$$
\mathscr{L}(\mathbf{x}, \lambda) = f(\mathbf{x}) + \lambda\bigl(g(\mathbf{x}) - c\bigr).
$$
At a constrained extremum (under standard regularity conditions) we require
\begin{align}
\nabla_{\mathbf{x}} \mathscr{L} &= \nabla f + \lambda \nabla g = 0, \\
\frac{\partial \mathscr{L}}{\partial \lambda} &= g(\mathbf{x}) - c = 0.
\end{align}
The first condition says that $\nabla f$ is parallel to $\nabla g$: the gradient of the objective is perpendicular to the constraint surface. The second condition enforces the constraint itself.}

\slides{
**Single constraint:**
$$
\mathscr{L}(\mathbf{x}, \lambda) = f(\mathbf{x}) + \lambda\bigl(g(\mathbf{x}) - c\bigr)
$$

**Stationarity:**
$$
\nabla f + \lambda \nabla g = 0, \qquad g(\mathbf{x}) = c
$$
}

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

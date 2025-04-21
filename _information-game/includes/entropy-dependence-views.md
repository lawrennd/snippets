\ifndef{entropyDependenceViews}
\define{entropyDependenceViews}

\subsection{Two Views of Entropy Dependence}

\notes{When working with entropy in the context of maximum entropy methods, there are two ways to treat the dependence of expectations on the natural parameters. This choice has important implications for how we derive gradients and analyse the system properties.}

\slides{
* Two views of entropy dependence:
  * Explicit: $\boldsymbol{\eta} = \boldsymbol{\eta}(\boldsymbol{\theta})$
  * Legendre: $\boldsymbol{\eta}$ independent
* Choice affects:
  * Gradient calculations
  * Hessian structure
  * Physical interpretation
}

\subsection{Explicit Dependence View}

\notes{In the explicit dependence view, we treat the expectations $\boldsymbol{\eta}$ as functions of the natural parameters $\boldsymbol{\theta}$. The entropy is written as,
$$
S(\boldsymbol{\theta}) = \log Z(\boldsymbol{\theta}) - \boldsymbol{\theta}^\top \boldsymbol{\eta}(\boldsymbol{\theta}),
$$
where $\boldsymbol{\eta} = \nabla_{\boldsymbol{\theta}} \log Z$. This view is crucial for dynamic analysis and variational derivations.}

\slides{
* Explicit view:
  * $S(\boldsymbol{\theta}) = \log Z(\boldsymbol{\theta}) - \boldsymbol{\theta}^\top \boldsymbol{\eta}(\boldsymbol{\theta})$
  * Full product rule in gradients
  * Complete Hessian: $-G - \sum_k \theta_k \frac{\partial G}{\partial \theta_k}$
}

\subsection{Legendre Transform View}

\notes{The Legendre transform view treats $\boldsymbol{\eta}$ as an independent variable, even though it's a function of $\boldsymbol{\theta}$. This leads to,
$$
S(\boldsymbol{\theta}, \boldsymbol{\eta}) = \log Z(\boldsymbol{\theta}) - \boldsymbol{\theta}^\top \boldsymbol{\eta},
$$
This perspective is used in information geometry and convex analysis.}

\slides{
* Legendre view:
  * $S(\boldsymbol{\theta}, \boldsymbol{\eta}) = \log Z(\boldsymbol{\theta}) - \boldsymbol{\theta}^\top \boldsymbol{\eta}$
  * Simpler Hessian: $-G(\boldsymbol{\theta})$
  * Natural for info-geometry
}

\subsection{When to Use Each View}

\notes{The choice between these views depends on the analysis being performed, we use explicit dependence for dynamic analysis, flows, and variational derivations. We can use Legendre transform view for curvature analysis and concavity proofs. Both are correct when used consistently within their context.}

\slides{
* Choose based on task:
  * Dynamics → Explicit dependence
  * Curvature → Legendre transform
* Both correct when used consistently
}


\endif 
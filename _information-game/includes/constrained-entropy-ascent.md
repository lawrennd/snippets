\ifndef{constrainedEntropyAscent}
\define{constrainedEntropyAscent}

\editme

\subsection{Constrained Entropy Ascent}

\notes{The game's dynamics are fixed by two requirements: maximise joint entropy production, and maintain the information isolation constraint $\sum_i h_i = C$ exactly. Working out the explicit equations makes transparent why the linearised flow decomposes into symmetric (dissipative) and antisymmetric (reversible) parts.}

\newslide{Entropy via the Log-Partition Function}

\notes{For a distribution $p(\mathbf{x};\boldsymbol{\theta})$ in the exponential family,
$$
p(\mathbf{x};\boldsymbol{\theta}) = \exp\!\left(\sum_k \theta_k f_k(\mathbf{x}) - \psi(\boldsymbol{\theta})\right),
$$
the log-partition function $\psi(\boldsymbol{\theta}) = \log\sum_{\mathbf{x}}\exp(\sum_k\theta_k f_k(\mathbf{x}))$ is the cumulant generating function (CGF). The moment parameters are its first derivatives,
$$
\eta_k = \frac{\partial\psi}{\partial\theta_k} = \mathbb{E}_{p_{\boldsymbol{\theta}}}[f_k(\mathbf{x})],
$$
and the Fisher information matrix is the Hessian: $G_{jk}(\boldsymbol{\theta}) = \partial^2\psi/\partial\theta_j\partial\theta_k$.

Shannon entropy is the Legendre conjugate of $\psi$:
$$
H(\boldsymbol{\theta}) = \psi(\boldsymbol{\theta}) - \boldsymbol{\theta}\cdot\nabla\psi(\boldsymbol{\theta}) = \psi(\boldsymbol{\theta}) - \boldsymbol{\theta}\cdot\boldsymbol{\eta}.
$$}

\slides{
$$H(\boldsymbol{\theta}) = \psi(\boldsymbol{\theta}) - \boldsymbol{\theta}\cdot\nabla\psi(\boldsymbol{\theta})$$

* $\psi(\boldsymbol{\theta})$: log-partition function (CGF)
* $\boldsymbol{\eta} = \nabla\psi$: moment parameters $\eta_k = \mathbb{E}[f_k]$
* $G(\boldsymbol{\theta}) = \nabla^2\psi$: Fisher information matrix
}

\newslide{Natural Gradient of Entropy}

\notes{Differentiating entropy with respect to the natural parameters:
$$
\frac{\partial H}{\partial\theta_k}
= \frac{\partial\psi}{\partial\theta_k} - \eta_k - \sum_j\theta_j\frac{\partial^2\psi}{\partial\theta_j\partial\theta_k}
= \eta_k - \eta_k - (G(\boldsymbol{\theta})\boldsymbol{\theta})_k
= -(G(\boldsymbol{\theta})\boldsymbol{\theta})_k.
$$
So $\nabla_{\!\boldsymbol{\theta}} H = -G(\boldsymbol{\theta})\boldsymbol{\theta}$.

The natural gradient (steepest ascent in the Fisher metric) is then
$$
\nabla^{\mathrm{nat}} H = G(\boldsymbol{\theta})^{-1}\nabla_{\!\boldsymbol{\theta}} H = -\boldsymbol{\theta}.
$$
Unconstrained steepest entropy ascent is simply descent in the natural parameters: $\dot{\boldsymbol{\theta}} \propto -\boldsymbol{\theta}$. This is the symmetric, dissipative part of the flow.}

\slides{
$$\nabla_{\!\boldsymbol{\theta}} H = -G(\boldsymbol{\theta})\boldsymbol{\theta}$$

Natural gradient:
$$\nabla^{\mathrm{nat}} H = G^{-1}\nabla_{\!\boldsymbol{\theta}} H = -\boldsymbol{\theta}$$

* Steepest entropy ascent $\Rightarrow$ $\dot{\boldsymbol{\theta}} \propto -\boldsymbol{\theta}$
* Descent in natural parameters — the symmetric part
}

\newslide{Constrained Natural Gradient Dynamics}

\notes{The information isolation constraint $\sum_i h_i(\boldsymbol{\theta}) = C$ introduces a Lagrange multiplier $\nu(\tau)$. The constrained natural gradient ascent is
$$
\dot{\boldsymbol{\theta}} = -\boldsymbol{\theta} + \nu(\tau) G^{-1}(\boldsymbol{\theta}) \mathbf{a}(\boldsymbol{\theta}),
$$
where $\mathbf{a}(\boldsymbol{\theta}) = \nabla_{\boldsymbol{\theta}} \sum_i h_i(\boldsymbol{\theta})$ is the constraint gradient and $G^{-1}\mathbf{a}$ is its natural gradient.

Requiring the constraint to be maintained, $\mathbf{a}(\boldsymbol{\theta})^\top\dot{\boldsymbol{\theta}} = 0$, gives
$$
\mathbf{a}^\top\left(-\boldsymbol{\theta} + \nu\,G^{-1}\mathbf{a}\right) = 0
\quad\Longrightarrow\quad
\nu(\tau) = \frac{\mathbf{a}(\boldsymbol{\theta})^\top\boldsymbol{\theta}}{\mathbf{a}(\boldsymbol{\theta})^\top G^{-1}(\boldsymbol{\theta}) \mathbf{a}(\boldsymbol{\theta})}.
$$
Substituting back gives a projected natural gradient flow:
$$
\dot{\boldsymbol{\theta}} = -\boldsymbol{\theta} + \frac{\mathbf{a}^\top\boldsymbol{\theta}}{\mathbf{a}^\top G^{-1}\mathbf{a}}\,G^{-1}\mathbf{a} = -\Pi^G_\perp \boldsymbol{\theta},
$$
where $\Pi^G_\perp = \mathbf{I} - G^{-1}\mathbf{a}\,\mathbf{a}^\top / (\mathbf{a}^\top G^{-1}\mathbf{a})$ is the projector orthogonal to the constraint gradient in the Fisher metric.}

\slides{
$$\dot{\boldsymbol{\theta}} = -\boldsymbol{\theta} + \nu(\tau)\,G^{-1}(\boldsymbol{\theta}) \mathbf{a}(\boldsymbol{\theta})$$

$\mathbf{a}(\boldsymbol{\theta}) = \nabla_{\!\boldsymbol{\theta}}\!\sum_i h_i$ — constraint gradient.

$$\nu(\tau) = \frac{\mathbf{a}^\top\boldsymbol{\theta}}{\mathbf{a}^\top G^{-1}\mathbf{a}}$$
}

\notes{Because $\nu(\boldsymbol{\theta})$ depends on $\boldsymbol{\theta}$, linearising the Lagrange multiplier term $\nu(\boldsymbol{\theta})\,G^{-1}(\boldsymbol{\theta}) \mathbf{a}(\boldsymbol{\theta})$ around $\boldsymbol{\theta}^*$ produces a contribution to the Jacobian whose antisymmetric part seeds the reversible sector $A$ of the linearised dynamics. The symmetric part of the Jacobian comes from $-\mathbf{I}$ (unconstrained natural gradient) and the symmetric part of $\nabla[\nu G^{-1}\mathbf{a}]$; the antisymmetric part is sourced by the Lagrange multiplier's $\boldsymbol{\theta}$-dependence [@Lawrence-inaccessible25].}

\endif

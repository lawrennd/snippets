\ifndef{genericLikeStructure}
\define{genericLikeStructure}

\editme

\subsection{GENERIC-like Structure}

\narration{The linearised dynamics decompose into a symmetric part and an antisymmetric part. The symmetric part is irreversible and produces entropy. The antisymmetric part is reversible — entropy-conserving rotations.}

\notes{To understand the local structure of the dynamics we linearise around any point $\boldsymbol{\theta}^*$ on the constraint manifold. Writing $\mathbf{q} = \boldsymbol{\theta} - \boldsymbol{\theta}^*$, the linearised flow is
$$
\dot{\mathbf{q}} = M\mathbf{q} + O(\|\mathbf{q}\|^2), \qquad M = S + A,
$$
where $S = \tfrac{1}{2}(M + M^\top)$ is symmetric (positive-semidefinite) and $A = \tfrac{1}{2}(M - M^\top)$ is antisymmetric. The symmetric part drives entropy production; the antisymmetric part generates entropy-conserving, rotation-like redistribution of information. This decomposition is the GENERIC (General Equation for Non-Equilibrium Reversible--Irreversible Coupling) structure of @Grmela-dynamics97 and @Ottinger-beyond05, and it emerges automatically from the constraint geometry rather than being imposed by hand [@Lawrence-inaccessible25].}

\slides{
* Linearise around $\boldsymbol{\theta}^*$
* $\mathbf{q} = \boldsymbol{\theta} - \boldsymbol{\theta}^*$
}
\newslide{Linearised Flow}

\slides{
$$\dot{\mathbf{q}} = M\mathbf{q}$$
where $M = S + A$

* $S$ is symmetric and irreversible (entropy production)
* $A$ is antisymmetric and reversible (entropy-conserving)
}

\notes{The ratio $\|A\|/\|S\|$ varies across the constraint manifold and determines the local character of the dynamics. When $\|S\| \gg \|A\|$ the system is in a thermodynamic regime: dissipation dominates and entropy is produced rapidly. When $\|A\| \gtrsim \|S\|$ the system is in a mechanical regime: conservative, rotation-like dynamics dominate. The information topography — the landscape of the Fisher information $G(\boldsymbol{\theta})$ — governs how these regimes are distributed.}

 \narration{And this structure is exactly what's called GENERIC: General Equation for Non-Equilibrium Reversible–Irreversible Coupling. It was derived by Öttinger and collaborators in a very different way — from a first-principles non-equilibrium thermodynamics perspective. What's interesting here is that this structure is being derived from the information-geometric setting of the inaccessible game, not imposed from outside. It's a consequence of maximum entropy production plus information isolation.}

\endif

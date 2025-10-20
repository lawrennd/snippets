\ifndef{informationRelaxationMep}
\define{informationRelaxationMep}

\editme

\subsection{From Information Relaxation to Maximum Entropy Production}

\notes{We've established used the conservation law $I + H = C$ to suggest a relaxation principle: systems evolve from high correlation (high $I$) to high entropy (high $H$). Now we explore the implications of this principle by deriving the explicit dynamics.}

\slides{
**Question:** How exactly does the system relax?

**Answer:** Through maximum entropy production
}

\subsection{The Direction of Time: Entropy Increases}

\notes{The second law of thermodynamics tells us that entropy increases over time. In The Inaccessible Game, this means:
$$
\dot{H} \geq 0.
$$

Since the joint entropy $H$ must increase (or at least not decrease), and we have the constraint $I + H = C$, it immediately follows that:
$$
\dot{I} \leq 0.
$$

The multi-information must decrease, i.e. the system breaks down correlations to increase entropy.

This gives us the direction of evolution, but not yet the rate or the specific form of the dynamics. For that, we need to think about how the system can maximize the rate of entropy production while respecting the conservation constraint.}

\slides{
**Second Law:**
$$
\dot{H} \geq 0
$$

**Conservation:**
$$
I + H = C
$$

**Therefore:**
$$
\dot{I} \leq 0
$$

*Correlations must decrease*
}

\subsection{Maximum Entropy Production Principle}

\notes{Among all possible dynamics that conserve marginal entropy, which path should we choose? Our answer comes from a principle that has emerged across multiple domains of physics: *maximum entropy production* (MEP).

The MEP principle states that, subject to constraints, systems evolve along the path of steepest entropy increase. This principle has been observed in:
- Non-equilibrium thermodynamics [@Ziegler:book77; @Beretta-steepest84]
- Fluid dynamics and turbulence
- Ecology and self-organization
- Climate dynamics

For The Inaccessible Game, MEP means: *of all paths that conserve $\sum h_i$, the system follows the one that maximises $\dot{H}$.* This choice of dynamics makes sense because it is uniquely determined at all times.

Note that this principle isn't one of our axioms, it's an assumption about how the relaxation dynamics should occur. }

\slides{
**Maximum Entropy Production (MEP):**

* Subject to constraints
* Maximize $\dot{H}$
* Steepest path to equilibrium

**Observed across physics:**

* Thermodynamics (Beretta, Ziegler)
* Fluid mechanics
* Self-organising systems
}

\subsection{Natural Parameters and the Entropy Gradient}

\notes{To make MEP concrete, we need coordinates. Recall from Lecture 1 that exponential families have natural parameters $\boldsymbol{\theta}$ where the geometry is particularly elegant. In natural parameters, the entropy gradient has a beautiful form.

For an exponential family $p(\mathbf{x}|\boldsymbol{\theta}) = \exp(\boldsymbol{\theta}^T T(\mathbf{x}) - \mathcal{A}(\boldsymbol{\theta}))$, the joint entropy is:
$$
H(\boldsymbol{\theta}) = \mathcal{A}(\boldsymbol{\theta}) - \boldsymbol{\theta}^T \nabla \mathcal{A}(\boldsymbol{\theta}).
$$

Taking the gradient with respect to $\boldsymbol{\theta}$:
$$
\nabla_{\boldsymbol{\theta}} H = -\boldsymbol{\theta}^\top \nabla^2 \mathcal{A}(\boldsymbol{\theta}) = -G(\boldsymbol{\theta})\boldsymbol{\theta},
$$
where $G(\boldsymbol{\theta}) = \nabla^2 \mathcal{A}(\boldsymbol{\theta})$ is the Fisher information matrix.

This gradient points in the direction of steepest entropy increase.}

\slides{
**Entropy in Natural Parameters:**
$$
H(\boldsymbol{\theta}) = \mathcal{A}(\boldsymbol{\theta}) - \boldsymbol{\theta}^\top \nabla \mathcal{A}(\boldsymbol{\theta})
$$

**Gradient (steepest increase):**
$$
\nabla_{\boldsymbol{\theta}} H = -G(\boldsymbol{\theta})\boldsymbol{\theta}
$$

*Fisher information emerges*
}

\subsection{The MEP Dynamics}

\notes{Maximum entropy production, in its simplest form, says: **move in the direction of the entropy gradient**. In natural parameters, this gives:
$$
\dot{\boldsymbol{\theta}} = \nabla_{\boldsymbol{\theta}} H = -G(\boldsymbol{\theta})\boldsymbol{\theta}.
$$

This is *gradient ascent on entropy*. But we must be careful: this dynamics must also preserve the constraint $\sum h_i = C$.

For the moment, we will focus on systems where we assume that this simple gradient flow preserves marginal entropies. This would require the Fisher information matrix $G$ and the conservation constraint have compatible structure, both arising from the same geometric structure of the probability manifold. 

Later (especially Lecture 4) we'll see how to handle more general constraints through Lagrangian methods, where we explicitly enforce the conservation through multipliers. For now, the key insight is: **MEP naturally leads to gradient flow in entropy**.}

\slides{
**MEP Dynamics:**
$$
\dot{\boldsymbol{\theta}} = -G(\boldsymbol{\theta})\boldsymbol{\theta}
$$

* Gradient ascent on entropy
* Fisher metric determines the flow
* Automatically preserves $\sum h_i$ (for right structure)

*Natural dynamics from information geometry*
}

\subsection{Why This Is the Unique Dynamics}

\notes{The MEP dynamics $\dot{\boldsymbol{\theta}} = -G(\boldsymbol{\theta})\boldsymbol{\theta}$ has several interesting properties.

1. **Steepest ascent**: This follows the Euclidean gradient $\nabla_{\boldsymbol{\theta}} H$ in parameter space. The Fisher information $G$ appears because of the structure of exponential families ($\nabla H = -G\boldsymbol{\theta}$), not because we're using it as a Riemannian metric. Note: *natural gradients* would be $G^{-1}\nabla H$, we are *not* following the natural gradients here.

2. **Maximizes entropy production**: Among all dynamics preserving the constraint, this produces entropy fastest.

3. **Conserves marginal entropies**: For systems with the exchangeable structure we've assumed, this flow keeps $\sum h_i$ constant.

4. **Connects to thermodynamics**: This is exactly the "steepest entropy ascent" dynamics explored e.g. in non-equilibrium thermodynamics by Beretta  [@Beretta-steepest84].

The information relaxation principle—that systems evolve from correlation to entropy—combined with MEP, uniquely determines these dynamics.}

\slides{
**Why This Dynamics?**

1. Steepest ascent (Euclidean, *not* natural gradient)
2. Maximizes entropy production rate
3. Conserves marginal entropies (special case)
4. Matches thermodynamic steepest ascent

*Determined by information relaxation + MEP*
}

\subsection{The Information Relaxation Picture}

\notes{Let's put it all together. The Inaccessible Game dynamics can be understood as:

**Initial state**: High correlation, low entropy
- Multi-information $I$ is large (variables tightly coupled)
- Joint entropy $H$ is small (distribution is concentrated)

**Evolution**: Maximum entropy production
- System follows gradient flow $\dot{\boldsymbol{\theta}} = -G(\boldsymbol{\theta})\boldsymbol{\theta}$
- Entropy $H$ increases at maximum rate
- Multi-information $I$ decreases correspondingly
- Marginal entropies $h_i$ remain constant (external observer learns nothing)

**Final state**: Low correlation, high entropy
- Multi-information $I$ is small (variables nearly independent)
- Joint entropy $H$ is large (distribution is spread out)
- Equilibrium: $\dot{H} = 0$, maximum entropy subject to constraints

This is information relaxation: the system "relaxes" from a tense, correlated state to a loose, uncorrelated state, just as a stretched elastic relaxes to its natural length.}

\slides{
**Information Relaxation:**

*Start:* High $I$, low $H$ (correlated, tense)

↓ $\dot{\boldsymbol{\theta}} = -G\boldsymbol{\theta}$ (MEP)

*End:* Low $I$, high $H$ (independent, relaxed)

**Throughout:** $\sum h_i = C$ (inaccessible to observer)
}

\subsection{Connection to Physical Intuition}

\notes{The information relaxation picture has a direct physical analogy. Consider a room full of gas molecules:

**Initial state**: All molecules are in one corner (high correlation - if you know where one molecule is, you have a good guess about others; low entropy - the distribution over positions is concentrated).

**Evolution**: Molecules diffuse according to the laws of thermodynamics, spreading out to fill the room. This is maximum entropy production—the fastest route to equilibrium.

**Final state**: Molecules are uniformly distributed throughout the room (low correlation - knowing where one molecule is tells you nothing about others; high entropy - maximum uncertainty about positions).

In both cases, we have:
- A conservation law (total energy for gas, marginal entropy for information)
- A relaxation from structured to unstructured states
- Maximum entropy production as the governing principle

The Inaccessible Game applies this same physics to abstract probability distributions.}

\slides{
**Physical Analogy: Gas Diffusion**

| Gas Molecules | Information System |
|---------------|-------------------|
| Concentrated in corner | High correlation ($I$) |
| Diffuse throughout room | Entropy increases ($H ↑$) |
| Uniform distribution | Low correlation (independent) |
| Conservation: energy | Conservation: $\sum h_i$ |

*Same principle, different space*
}

\subsection{Preview: Constrained Gradient Flow}

\notes{The simple gradient flow $\dot{\boldsymbol{\theta}} = -G(\boldsymbol{\theta})\boldsymbol{\theta}$ is the starting point, but real systems often have additional constraints beyond marginal entropy conservation. In Lecture 4, we'll see how to incorporate these constraints using Lagrangian methods, leading to:
$$
\dot{\boldsymbol{\theta}} = -G(\boldsymbol{\theta})(\boldsymbol{\theta} + \lambda \nabla C),
$$
where $\lambda$ is a Lagrange multiplier and $C$ represents the constraint.

The key insight remains: **information relaxation through maximum entropy production** is the fundamental principle. Constraints modify the path, but not the underlying logic.}

\slides{
**Next Steps:**

* Lecture 4: Adding Lagrangian constraints
* Lecture 5: Poisson structure (conservation)
* Lecture 8: Full GENERIC framework

*MEP + constraints = complete dynamics*
}

\addreading{@Beretta-steepest84}{Steepest entropy ascent in thermodynamics}
\addreading{@Ziegler:book77}{Thermomechanics and variational principles}

\endif


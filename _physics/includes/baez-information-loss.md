\ifndef{baezInformationLoss}
\define{baezInformationLoss}

\editme

\subsection{Baez et al.: Axioms for Information Loss}

\notes{Shannon introduced entropy as a measure of information derived from probability through five axioms. More recently, Baez et al. [@Baez-characterisation11] took a different approach: they showed that entropy can be derived through category theory as a way of measuring *information loss* in a process.

Without invoking probability, they showed that the Shannon entropy emerges from three axioms about how information should be lost when we apply transformations. This provides our justification for why entropy is the "right" measure of information.}

\slides{
**Baez et al. Approach:**
* Shannon: probability → entropy (5 axioms)
* Baez: information loss → entropy (3 axioms)
* Category theory perspective
* Justifies entropy as measure of information
}

\subsubsection{The Three Axioms}

\notes{Consider a process $f: p \rightarrow q$ that transforms one probability distribution $p$ into another $q$. Let $F(f)$ denote the information lost in this process. Baez et al. proposed three axioms that $F$ should satisfy:

**Axiom 1: Functoriality** (Information loss is additive)

If we perform a process in two stages, the total information lost should be the sum of the information lost at each stage:
$$
F(f \circ g) = F(f) + F(g)
$$
where $\circ$ represents composition of processes.

This says: information loss accumulates. If we first apply process $g$, then process $f$, the total loss is the sum of individual losses. There's no "recovery" of information in the second stage.}

\slides{
**Axiom 1: Functoriality**
$$
F(f \circ g) = F(f) + F(g)
$$
* Two-stage process
* Total loss = sum of losses
* Information doesn't recover
* Additive accumulation
}

\newslide{Axiom 2: Convex Linearity}

\notes{**Axiom 2: Convex Linearity** (Probabilistic mixing)

If we flip a biased coin (probability $\lambda$) to decide whether to do process $f$ or process $g$, the expected information lost should be the weighted average:
$$
F(\lambda f \oplus (1-\lambda)g) = \lambda F(f) + (1-\lambda)F(g)
$$

This says: if we randomly choose between two processes, the expected information loss is just the probabilistic mixture of the individual losses. There's no "interaction term" between different processes.}

\slides{
**Axiom 2: Convex Linearity**
$$
F(\lambda f \oplus (1-\lambda)g) = \lambda F(f) + (1-\lambda)F(g)
$$
* Flip $\lambda$-coin to choose process
* Expected loss = weighted average
* No interaction between processes
* Linear in probabilities
}

\newslide{Axiom 3: Continuity}

\notes{**Axiom 3: Continuity** (Small changes → small effects)

If we change a process slightly, the information lost should change only slightly:
$$
F(f) \text{ is a continuous function of } f
$$

This is a regularity condition: information loss shouldn't have sudden jumps or discontinuities. Smooth changes to the process lead to smooth changes in information loss.}

\slides{
**Axiom 3: Continuity**
$$
F(f) \text{ continuous in } f
$$
* Small change in process
* → Small change in loss
* No sudden jumps
* Regularity condition
}

\subsection{The Main Result}

\notes{From these three axioms alone, Baez et al. proved:

> There exists a constant $c \geq 0$ such that for any process $f: p \rightarrow q$,
> $$
> F(f) = c(H(p) - H(q))
> $$

where $H(\cdot)$ is the Shannon entropy.

In other words, given these three axioms, *information loss must be measured by entropy difference*. The three axioms uniquely determine that entropy (up to a scaling constant $c$) is the right measure. This provides a deep justification for using entropy in information theory, independent of Shannon's original probabilistic approach.}

\slides{
**Main Result:**
$$
F(f) = c(H(p) - H(q))
$$
* Three axioms → uniquely determine entropy
* $H(\cdot)$ = Shannon entropy
* $c \geq 0$ = scaling constant
* Information loss = entropy difference
* Deep justification for entropy
}

\newslide{Why This Matters}

\notes{This result is powerful because:

1. **Justification**: It shows entropy isn't arbitrary, it's the *unique* measure satisfying natural axioms about information loss.

2. **Category Theory**: The functoriality axiom comes from category theory, providing a geometric/structural understanding of information.

3. **Foundation for TIG**: Baez's three axioms justify using entropy as the measure of information. The fourth axiom then applies this to marginal entropies with an exchangeability structure. 

4. **Process-Oriented**: It focuses on *processes* and *transformations*, which is natural for thinking about dynamics.

The constant $c$ can be set to 1 by choice of units, so we typically work with:
$$
F(f) = H(p) - H(q)
$$}

\slides{
**Why This Matters:**
* Unique characterization of entropy
* Category theory foundation
* Justifies using entropy in dynamics
* Process-oriented viewpoint
* Foundation for fourth axiom

*Usually set $c=1$ by choice of units*
}

\subsection{Connection to Exponential Families}

\notes{Recall from Lecture 1 that for exponential families, entropy has the particularly clean form:
$$
H(\boldsymbol{\theta}) = \mathcal{A}(\boldsymbol{\theta}) - \boldsymbol{\theta}^\top \boldsymbol{\mu}
$$
where $\mathcal{A}$ is the log partition function.

Baez's result tells us that when we transform from one exponential family distribution to another, the information lost is exactly the difference in these entropies. This will be crucial when we study information dynamics, because processes that transform distributions will naturally involve entropy gradients.}

\slides{
**With Exponential Families:**
$$
H(\boldsymbol{\theta}) = \mathcal{A}(\boldsymbol{\theta}) - \boldsymbol{\theta}^\top \boldsymbol{\mu}
$$
* Information loss = entropy difference
* Natural for studying dynamics
* Entropy gradients drive evolution
* Clean form in natural parameters
}

\subsection{The Fourth Axiom Preview}

\notes{Baez et al. gave us three axioms about *information loss*. The Inaccessible Game adds a fourth axiom about *information conservation*. The three axioms justify measuring information loss by entropy differences. The fourth axiom will constrain the *total* information in the system.

Think of it like physics:
- Baez axioms: "How should we measure information loss?" → Entropy differences
- Fourth axiom: "What if information is conserved?" → New constraint

This combination leads to constrained dynamics where information can flow between variables but the total remains constant.}

\slides{
**Preview: Fourth Axiom**

*Baez axioms (review):*
* How to measure information loss
* → Entropy differences

*Fourth axiom (next):*
* Information conservation
* → New constraint on system

*Together:* Constrained dynamics
}
\endif

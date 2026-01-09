\ifndef{informationConservationAxiom}
\define{informationConservationAxiom}

\editme

\subsection{The Fourth Axiom: Information Conservation}

\notes{Baez et al.'s three axioms tell us how to measure information loss. Now we add a new constraint: what if information is *conserved* in an isolated system?

In physics, isolated chambers conserve mass and energy. In The Inaccessible Game, we consider what it would mean for information to be conserved. This gives us the fourth axiom.}

\slides{
**Physical Analogy:**
* Isolated chamber
* Mass conserved: $\sum m_i = \text{const}$
* Energy conserved: $\sum E_i = \text{const}$
* *Information conserved?*
}

\subsubsection{Statement of the Axiom}

\notes{**Axiom 4: Information Conservation**

For any finite sub-group of $N$ variables, the sum of marginal entropies $\{h_i\}_{i=1}^{N}$ equals a constant $C$:
$$
\sum_{i=1}^N h_i = C
$$

This says the total amount of information in the system is conserved. Information can flow between variables, but the total remains constant.}

\slides{
**Axiom 4: Information Conservation**
$$
\sum_{i=1}^N h_i = C
$$
* $h_i$ = marginal entropy of variable $i$
* $C$ = conservation constant
* Total information conserved
* Information can redistribute
}

\newslide{Why Marginal Entropies?}

\notes{A crucial choice: we conserve the *sum of marginal entropies*, not the joint entropy $H(\mathbf{x})$.

Recall the relationship:
$$
H(\mathbf{x}) = \sum_{i=1}^N h_i - I(\mathbf{x})
$$
where $I(\mathbf{x})$ is the multi-information (total correlation):
$$
I(\mathbf{x}) = \sum_{i=1}^N h_i - H(\mathbf{x}) \geq 0
$$

If we conserve $\sum h_i = C$, then:
- The multi-information $I$ can change
- The joint entropy $H$ can change
- Variables can become correlated or decorrelated
- But the "total information capacity" $\sum h_i$ stays fixed

Why marginal? The exchangeability principle: we want a constraint that applies to any finite subset of variables. Marginal entropies allow this flexibility. Also, conserving $\sum h_i$ (rather than joint $H$) allows the correlation structure $I$ to vary, giving the system freedom to organise.}

\slides{
**Why Marginal?**
$$
H(\mathbf{x}) = \sum_{i} h_i - I(\mathbf{x})
$$
* Conserve: $\sum h_i = C$
* $I$ (multi-information) can change
* $H$ (joint entropy) can change
* Variables can correlate/decorrelate
* *Total capacity* $\sum h_i$ fixed
}

\newslide{Exchangeability}

\notes{The conservation constraint is imposed in an *exchangeable* form across the marginal entropies. This means we can consider any finite partition of variables from a total that could be countably infinite.

The exchangeability ensures:
1. We can focus on any finite subset of variables
2. The constraint applies equally to all variables
3. No variable has a "special" role
4. The system can have infinitely many degrees of freedom

This is inspired by, but differs from, the usual notion of exchangeability in Bayesian non-parametric probability (de Finetti, Aldous, Bernardo & Smith). Here, exchangeability refers to the *constraint structure*, not the probability distribution itself.}

\slides{
**Exchangeability:**
* Consider any finite subset
* Constraint applies equally to all
* No special variables
* Can handle infinite systems
* Different from Bayesian exchangeability
}

\subsection{Physical Interpretation}

\notes{Think of the system as an isolated information chamber:

**Marginal entropy $h_i$**: The "information content" or "information capacity" of variable $i$. High marginal entropy means the variable can take on many states.

**Conservation $\sum h_i = C$**: Total capacity is fixed. Like a fixed amount of "space" to store information.

**Multi-information $I$**: The "structure" or "correlation" between variables. This can grow or shrink.

As the system evolves:
- Information can flow between variables (changing individual $h_i$)
- Correlations can form or break (changing $I$)
- But the total capacity $\sum h_i = C$ remains constant

Since $H + I = C$, increasing joint entropy $H$ (second law) means decreasing multi-information $I$. The system breaks down correlations to increase entropy. It's like having a fixed amount of "information capacity" $C$ that gets redistributed between joint entropy (disorder) and correlation structure.}

\slides{
**Physical Picture:**
* $h_i$ = information capacity of variable $i$
* $\sum h_i = C$ = total fixed capacity
* $I$ = correlation/structure (can vary)
* Information flows but total conserved
* Can "buy correlations" with capacity
}

\newslide{Why This Creates "Inaccessibility"}

\notes{Now we see why the game is "inaccessible": an external observer cannot learn anything about the system.

Recall Baez's result: information gained from observing a process $f: p \rightarrow q$ is measured by the entropy change:
$$
F(f) = H(p) - H(q)
$$

But if marginal entropies are conserved ($\sum h_i = C$), then an external observer sees:
- Before observation: $\sum h_i = C$
- After observation: $\sum h_i = C$
- Information gained: $\Delta(\sum h_i) = 0$

The observer learns nothing! The system is informationally isolated. Internal variables can correlate and decorrelate (changing $I$ and $H$), but the total marginal entropy, what an external observer can access through Baez's measurement framework, remains constant.

This is "inaccessibility": the system's internal dynamics are hidden from external observation because there's no net information flow to the outside. The conservation constraint creates an information barrier.

Mathematically, this leads to dynamics constrained to a manifold $\sum h_i = C$, which we'll formalize with Lagrange multipliers in Lecture 3.}

\slides{
**Creates "Inaccessibility":**

*Baez:* Info gained = entropy change

*Conservation:* $\sum h_i = C$ (constant)

*Observer:* $\Delta(\sum h_i) = 0$ → learns nothing!

* Internal dynamics hidden
* Information barrier
* System informationally isolated
* → Constrained dynamics (L3)
}

\subsection{The Four Axioms Together}

\notes{We now have four axioms for The Inaccessible Game:

1. **Functoriality** (Baez): Information loss is additive across compositions
2. **Convex Linearity** (Baez): Probabilistic mixing is linear  
3. **Continuity** (Baez): Small changes have small effects
4. **Information Conservation** (New): $\sum_{i=1}^N h_i = C$

The first three axioms (Baez) justify measuring information by entropy differences. The fourth axiom constrains the total information. Together, they define an information-theoretic "chamber" where:
- Information content is measured by entropy (axioms 1-3)
- Total information is conserved (axiom 4)
- Dynamics must respect this conservation

From these four axioms, we will derive (in Lecture 3) a constrained dynamical system that evolves to maximize entropy production subject to conservation.}

\slides{
**Four Axioms Together:**

*Baez (1-3):*
* Functoriality
* Convex linearity  
* Continuity
* → Entropy measures information

*New (4):*
* Information conservation: $\sum h_i = C$
* → Constrained dynamics

*Next (L3):* Derive dynamics from axioms
}

\endif
\endif

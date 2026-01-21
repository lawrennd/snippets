\ifndef{informationIsolationSelected}
\define{informationIsolationSelected}

\editme

\subsection{Information Isolation: Selected, Not Assumed}

\notes{In our earlier presentation [@Lawrence-inaccessible25], we introduced information isolation $\sum_i h_i = C$ as a fourth independent axiom. But more recent work suggests this is better understood as **selected by the no-barber principle** rather than assumed.}

\slides{
**Earlier:** Fourth axiom (assumed)

**Now:** Selected by no-barber principle

*Not independent assumption*
}

\subsection{Why This Selection?}

\notes{Among all possible entropy-related constraints, marginal entropy conservation $\sum_i h_i = C$ is the **strongest nontrivial constraint** that can be formulated without external structure.}

\notes{Consider the alternatives:

**Partial conservation** (only some $h_i$ constrained):
- Requires specifying *which* variables are isolated
- Privileges those variables over others
- Needs external criterion to select them

**Time-varying** $C(t)$:
- Requires an external time parameter $t$
- Who defines this time?
- Violates no-barber principle

**Observer-relative** isolation:
- Isolated *from what observer*?
- Requires external reference point
- Smuggles in external structure

**Probabilistic** isolation (holds in expectation):
- Requires external probability space
- Who defines the measure?
- Again violates no-barber}

\slides{
**Alternatives Violate No-Barber:**

* Partial conservation → privileges variables
* Time-varying $C(t)$ → needs external clock
* Observer-relative → needs external observer
* Probabilistic → needs external measure

*All require external structure*
}

\newslide{The Unique Internal Choice}

\notes{The constraint $\sum_i h_i = C$ (constant) has special properties:

1. **Exchangeable:** Treats all subsystems identically (depends only on marginal entropies)
2. **Extensive:** Scales linearly with system size
3. **Internal:** Definable from reduced descriptions alone
4. **No external time:** $C$ is a constant, not time-dependent
5. **No external observer:** Isolation is absolute, not relative}

\notes{These properties make it the unique choice that satisfies both:
- Strong enough to constrain dynamics
- Weak enough to avoid external reference}

\slides{
**Why $\sum h_i = C$?**

Properties:
* Exchangeable across subsystems
* Extensive (scales with $n$)
* Internal (reduced descriptions only)
* Time-independent (constant $C$)
* Observer-independent (absolute)

*Strongest constraint without external structure*
}

\subsection{Implication: Not "Just Another Axiom"}

\notes{This reframing changes how we understand the game's foundation. We're not arbitrarily adding a fourth axiom—we're **discovering** that internal adjudicability forces this specific constraint.}

\notes{The three Baez-Fritz-Leinster axioms tell us information loss is measured by entropy. The no-barber principle then tells us that the only admissible global constraint on a collection of subsystems is marginal entropy conservation.}

\slides{
**Conceptual Shift:**

Not: "Here's a fourth axiom"

But: "Internal adjudicability forces this"

$$\text{No-barber principle} \Rightarrow \sum_i h_i = C$$

*Derived necessity, not arbitrary choice*
}

\notes{This is a stronger foundation. We're not asking "what happens if we add this constraint?" but rather "what must be true if we forbid external reference?" The answer turns out to be marginal entropy conservation.}

\endif

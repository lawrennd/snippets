\ifndef{shannonOriginImpossibility}
\define{shannonOriginImpossibility}

\editme

\subsection{Classical Obstruction at the Origin}

\notes{The information relaxation dynamics suggest that the game begins at the origin: the state of maximum multi-information, $I = C$, with zero joint entropy, $H = 0$. Playing forward, multi-information is relaxed and joint entropy increases until $H = C$ and $I = 0$.

This natural starting point — zero joint entropy with positive marginal entropies — cannot be represented by classical Shannon entropy. The problem is the *non-negativity of conditional Shannon entropy*: for any two classical random variables $X_1$ and $X_2$,
$$
H_{X_1|X_2} = H_{1,2} - H_2 \geq 0,
$$
because conditional entropy measures residual uncertainty after conditioning, which cannot be negative. This constraint has an immediate consequence for multi-information.}

\slides{
* Boundary Condition
$$
I = C, \quad H = 0
$$
* Conditional Shannon entropies always $\geq 0$.
* Prohibits $H=0$ with positive marginals.
}

\notes{For a two-variable system, multi-information is
$$
I_{1,2} = H_1 + H_2 - H_{1,2} = H_1 - H_{1|2},
$$
using the chain rule $H_{1|2} = H_{1,2} - H_2$. Since $H_{1|2} \geq 0$ we get $I_{1,2} \leq H_1$, and by symmetry $I_{1,2} \leq \min(H_1, H_2)$.

At the origin we need $H_{1,2} = 0$, which gives $I_{1,2} = H_1 + H_2$. But this would require $I_{1,2} > H_1$ whenever $H_2 > 0$, contradicting the bound. The only escape is $H_1 = H_2 = 0$, i.e.\ all marginals are zero — but then $C = 0$ and there is no game.

More generally, for $N$ variables the Shannon conditional entropy constraint forces: *zero joint entropy is only possible when all marginal entropies are also zero*.

The Baez--Fritz--Leinster axioms (functoriality, convex linearity, continuity) uniquely select Shannon entropy [@Baez-characterisation11], but Shannon entropy structurally forbids the game's natural origin [@Lawrence-origin26].}

\subsection{Von Neumann Entropy Resolution}

\notes{The resolution is to replace Shannon entropy with von Neumann entropy. For a bipartite quantum system with density matrix $\rho$, the von Neumann conditional entropy $S_{A|B} = S_{AB} - S_B$ *can be negative* when the subsystems are entangled. A globally pure entangled state has $S(\rho) = 0$ while its marginal states $\rho_A$ and $\rho_B$ may each have positive entropy — precisely the configuration the game needs at its origin.

An analogous axiomatic characterisation of information loss via von Neumann entropy is provided by @Parzygnat-functorial22. This extends the Baez--Fritz--Leinster framework from classical stochastic maps to quantum channels (unital completely positive maps on finite-dimensional $C^*$-algebras). Adopting the Parzygnat axioms resolves the origin paradox.}

\slides{
* Entanglement leads to negative conditional entropy.

* Pure entangled state:
$$
S(\rho_{AB}) = 0, \quad S(\rho_A) > 0, \quad S(\rho_B) > 0
$$
}
\newslide{Information Loss Axioms}
\slides{
* Provided by @Parzygnat-functorial22 (quantum analogue of BFL)
}

\endif

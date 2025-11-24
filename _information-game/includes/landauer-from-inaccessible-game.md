\ifndef{landauerFromInaccessibleGame}
\define{landauerFromInaccessibleGame}

\editme

\subsection{Landauer's Principle from the Inaccessible Game}

\notes{The GENERIC-like structure and energy-entropy equivalence provide a natural framework for deriving Landauer's principle [@Landauer-irreversibility61], which states that erasing information requires dissipating at least $k_BT\log 2$ of energy per bit.}

\subsubsection{Information Erasure as a Process}

\notes{Consider erasing one bit: a memory variable $x_i \in \{0,1\}$ is reset to a standard state (say $x_i = 0$), destroying the stored information. From an ensemble perspective—considering many such erasure operations where the initial value is random—the marginal entropy of this variable decreases:
$$
\Delta h(X_i) = -\log 2.
$$}

\slides{
**Bit Erasure:**
* Variable $x_i \in \{0,1\}$
* Reset to standard state: $x_i \rightarrow 0$
* Ensemble perspective: initial state random
* Marginal entropy decreases: $\Delta h(X_i) = -\log 2$
}

\subsection{Conservation Requires Redistribution}

\notes{For a system obeying $\sum_i h_i = C$, this decrease must be compensated by increases elsewhere:
$$
\sum_{j \neq i} \Delta h(X_j) = +\log 2.
$$}

\notes{The antisymmetric (conservative) part $A$ of our GENERIC dynamics preserves both $H$ and $\sum_i h_i$. It can only shuffle entropy reversibly between variables. But such reversible redistribution doesn't truly erase the information—it merely moves it to other variables, from which it could in principle be recovered.}

\slides{
**Conservation Constraint:**
$$\sum_{j \neq i} \Delta h(X_j) = +\log 2$$

**Antisymmetric Part $A$:**
* Reversible shuffling only
* Moves information to other variables
* Not true erasure!
}

\newslide{True Erasure Requires Dissipation}

\notes{True irreversible erasure requires increasing the total joint entropy $H$ (second law) while maintaining $\sum_i h_i = C$. Since $I = \sum_i h_i - H$, this means decreasing multi-information:
$$
\Delta I < 0.
$$}

\notes{This reduction of correlations is precisely what the dissipative part $S$ achieves. It increases $H$ through entropy production while the constraint forces redistribution of marginal entropies. **The erasure process thus necessarily involves the dissipative dynamics**, not just conservative reshuffling.}

\slides{
**True Erasure:**

Must increase $H$ (2nd law) with $\sum h_i = C$

$$\Rightarrow \Delta I = \Delta(\sum h_i) - \Delta H < 0$$

* Breaks correlations
* Requires dissipative part $S$
* Cannot be purely reversible
}

\subsection{Energy Cost from Energy-Entropy Equivalence}

\notes{In the thermodynamic limit with energy-entropy equivalence (Section 5 of the paper), the gradients $\nabla(\sum_i h_i)$ and $\nabla E$ become parallel along the order-parameter direction. Near thermal equilibrium at inverse temperature $\beta = \tfrac{1}{k_BT}$, this implies:
$$
\beta \langle E \rangle \approx \sum_i h_i + \text{const}.
$$}

\notes{Therefore, erasing one bit requires:
$$
\Delta(\beta \langle E \rangle) \approx \Delta h(X_i) = -\log 2,
$$
giving an energy change:
$$
\Delta \langle E \rangle \approx -\frac{\log 2}{\beta} = -k_BT \log 2.
$$}

\slides{
**Energy-Entropy Equivalence:**

In thermodynamic limit: $\beta \langle E \rangle \approx \sum_i h_i$

**Erasure Cost:**
$$\Delta \langle E \rangle = -\frac{\log 2}{\beta} = -k_BT\log 2$$

Energy must be removed from system
}

\subsection{Dissipation Bound}

\notes{Since the system must dissipate this energy via the symmetric part $S$, and entropy production is non-negative, we obtain Landauer's bound
$$
Q_{\text{dissipated}} \geq k_BT\log 2.
$$}

\notes{This derivation shows that Landauer's principle emerges from:
1. **Marginal entropy conservation** $\sum_i h_i = C$
2. **GENERIC-like structure** distinguishing conservative redistribution ($A$) from dissipative entropy production ($S$)  
3. **Energy-entropy equivalence** in the thermodynamic limit

The insight is that erasure requires both redistributing marginal entropy (to maintain the constraint) and increasing total entropy $H$ (second law), which necessarily reduces multi-information $I$ and invokes dissipation.}

\slides{
**Landauer's Principle Emerges From:**

1. Marginal entropy conservation
2. GENERIC structure ($S$ vs $A$)
3. Energy-entropy equivalence

$$\boxed{Q_{\text{dissipated}} \geq k_BT\log 2}$$

}

\notes{The information-theoretic constraint provides the foundation, with thermodynamic energy appearing as its dual in the large-system limit. This reverses the usual derivation where information bounds follow from thermodynamics --- here thermodynamic bounds follow from information theory.}

\endif


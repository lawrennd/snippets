\ifndef{noBarberFavoursNcfinprob}
\define{noBarberFavoursNcfinprob}
\editme

\subsection{Two Candidates for Information Loss}

\notes{The inaccessible game uses a formal notion of information loss to impose information isolation. Two category-theoretic characterisations exist. @Baez-characterisation11 work in the classical category $\textsf{FinProb}$ of finite probability spaces and measure-preserving functions, characterising information loss via Shannon entropy. @Parzygnat-functorial22 work in the noncommutative category $\textsf{NCFinProb}$ of finite-dimensional quantum probability spaces and unital completely positive maps, characterising information loss via von Neumann entropy. Both give rigorous accounts of information loss, but they differ in what kind of state space they presuppose. In the classical case, a probability measure is defined over a finite set of distinguishable alternatives. In the noncommutative case, a density operator is not a measure over a basis-independent outcome space; classical outcomes appear only relative to a chosen measurement context.}

\slidesincremental{
* Two characterisations of information loss:
  * @Baez-characterisation11: $\textsf{FinProb}$, Shannon entropy
  * @Parzygnat-functorial22: $\textsf{NCFinProb}$, von Neumann entropy
* Which is the right internal language for the game?
}

\newslide{Baez-Fritz-Leinster: $\textsf{FinProb}$}

\notes{In $\textsf{FinProb}$, probability distributions live on finite outcome spaces and information loss is characterised by the decrease in Shannon entropy. The result of @Baez-characterisation11 is that suitable axioms (functoriality, convex linearity, and continuity) pin down information loss as proportional to the entropy difference $H(p)-H(q)$ along the relevant probability-preserving process.}

\notes{The outcome space should be understood as external structure relative to the game's intended internal perspective. Formally, a finite probability space includes both a finite set of outcomes and a probability measure on that set. But the set of outcomes presents the uncertainty from outside: it names the alternatives over which the measure ranges. If the game is meant to enforce information isolation, then admitting this named outcome space as internal data already imports an external individuation of possibilities.}

\notes{Once that external individuation is admitted internally, copying follows as a secondary problem. The elements of the outcome space can be treated as classical data: they can be compared, recorded, and duplicated. Thus the diagonal $x \mapsto (x,x)$ is not caused by the probability measure itself, but by allowing the externally specified outcome space to function as internal syntax.}

\slidesincremental{
* Three axioms $\rightarrow$ $F(f) = c(H(p) - H(q))$ uniquely
* A classical measure is defined over a named outcome space
* That outcome space individuates possibilities from an external perspective
* If admitted internally, outcomes become classical data
* Classical data can be copied: $x \mapsto (x,x)$
}

\newslide{Parzygnat: $\textsf{NCFinProb}$}

\notes{In $\textsf{NCFinProb}$, states are density matrices on finite-dimensional Hilbert spaces and channels are unital completely positive maps. @Parzygnat-functorial22 characterises information loss via von Neumann entropy with the analogous result.}

\notes{A density operator is also a state, but it is not a probability measure over a basis-independent set of pre-existing outcomes. To obtain classical outcomes one must choose a measurement context, observable, or basis. Thus the native noncommutative structure does not provide copyable outcomes as primitive internal data. There is no natural copying map $A \to A \otimes A$; any such operation would require imposing extra classical structure.}

\slidesincremental{
* Analogous axioms $\rightarrow$ $F(f) = c(S(\rho) - S(\sigma))$ via von Neumann entropy
* A density operator is a state, but not a measure over fixed outcomes
* Classical outcomes require a measurement context
* No basis-independent copying: $A \to A \otimes A$ not available
}

\subsection{Applying the No-Barber Principle}

\notes{@Lawvere-diagonal69 showed that Russell's barber paradox shares a common categorical structure with Gödel's incompleteness theorem, Turing's halting problem, and Cantor's theorem. The structure requires five ingredients: rules, a universal evaluator, internalisation of syntax, self-application, and a twist. The self-application step requires feeding the same object into two slots simultaneously. Categorically, this requires a copying operation.}

\notes{In the classical case, the relevant outcome structure is already presupposed by the form of a probability measure: probabilities are assigned to distinguishable alternatives. This does not mean that the Baez--Fritz--Leinster information-loss theorem itself supplies a diagonal. But if the game's internal language is allowed to refer to those alternatives as outcomes, then they become copyable classical data, and the self-application step becomes available.}

\notes{In the noncommutative case, the state is not given as a measure over a fixed outcome space. Classical outcomes arise only through a chosen measurement context. Without making such a choice internal, there is no basis-independent copying operation and hence no native self-application step of the Lawvere kind.}

\slidesincremental{
* Lawvere diagonalisation needs: self-application $\equiv$ copying
* The issue is not probability measure vs no measure
* Classical measures presuppose distinguishable outcomes
* If those outcomes are internal, they are copyable data
* Noncommutative states do not expose basis-independent outcomes
}

\newslide{What the No-Barber Principle Constrains}

\notes{The no-barber principle does not select between $\textsf{FinProb}$ and $\textsf{NCFinProb}$ merely as categories, nor does it argue against the Baez--Fritz--Leinster characterisation of information loss. It constrains the internal language of the game. The problematic structure is a copyable space of classical outcomes. A classical probability measure presupposes such a space; the no-barber issue arises if that space is admitted internally as data that the game can inspect and duplicate.}

\notes{$\textsf{NCFinProb}$ avoids this not because it has no state, but because its states are not measures over a basis-independent set of outcomes. Classical outcomes appear only after a measurement context is chosen. Thus the no-barber principle favours an internal language in which outcome-selection and copying are not primitive. This is independent of but consistent with the selection in @Lawrence-origin26, where von Neumann entropy is independently required because the game's origin demands zero joint entropy with positive marginal entropies — a configuration achievable via entanglement but impossible under Shannon entropy.}

\slides{
> The no-barber principle constrains the game's internal access to outcomes,
> not the information-loss theorem itself.

* The measure is not the culprit
* A classical measure presupposes distinguishable outcomes
* If those outcomes are internal, they become copyable data
* Copyable data enables Lawvere self-application
* Noncommutative states do not expose basis-independent outcomes
* The selection is operational: no primitive outcome-copying
}

\endif

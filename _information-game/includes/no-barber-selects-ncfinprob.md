\ifndef{noBarberSelectsNcfinprob}
\define{noBarberSelectsNcfinprob}
\editme

\subsection{Two Candidates for Information Loss}

\notes{The inaccessible game uses formal notion of information loss in order to impose information isolation. Two category-theoretic characterisations exist. @Baez-characterisation11 work in the classical category $\textsf{FinProb}$ of finite probability spaces and stochastic maps, characterising information loss via Shannon entropy. @Parzygnat-functorial22 work in the noncommutative category $\textsf{NCFinProb}$ of finite-dimensional quantum probability spaces and unital completely positive maps, characterising information loss via von Neumann entropy. Both give rigorous accounts of information loss, but they correspond to very different underlying mathematical structures.}

\slidesincremental{
* Two characterisations of information loss:
  * @Baez-characterisation11: $\textsf{FinProb}$, Shannon entropy
  * @Parzygnat-functorial22: $\textsf{NCFinProb}$, von Neumann entropy
* Which is the right internal language for the game?
}

\newslide{Baez-Fritz-Leinster: $\textsf{FinProb}$}

\notes{In $\textsf{FinProb}$, probability distributions live on finite sets and information loss is characterised by the decrease in Shannon entropy. The result of @Baez-characterisation11 is that three axioms (functoriality, convex linearity, and continuity) pin down information loss as proportional to the entropy difference $H(p) - H(q)$ along a stochastic map $p \to q$.}

\notes{$\textsf{FinProb}$ is a \emph{cartesian} category. This means every object $A$ is equipped with a canonical diagonal map $\Delta_A : A \to A \times A$. Such a map duplicates its input freely, with no additional postulates required.}

\slidesincremental{
* Three axioms $\rightarrow$ $F(f) = c(H(p) - H(q))$ uniquely
* $\textsf{FinProb}$ is *cartesian*
* Canonical copying: $\Delta_A : A \to A \times A$ available for free
}

\newslide{Parzygnat: $\textsf{NCFinProb}$}

\notes{In $\textsf{NCFinProb}$, states are density matrices on finite-dimensional Hilbert spaces and channels are unital completely positive maps. @Parzygnat-functorial22 characterises information loss via von Neumann entropy with the analogous result.}

\notes{$\textsf{NCFinProb}$ is a \emph{symmetric monoidal} category. The tensor product $\otimes$ combines systems, but there is no canonical copying map $A \to A \otimes A$. Any duplication must be explicitly postulated — it cannot arise from the categorical structure alone. This is the mathematical expression of the quantum no-cloning theorem.}

\slidesincremental{
* Analogous axioms $\rightarrow$ $F(f) = c(S(\rho) - S(\sigma))$ via von Neumann entropy
* $\textsf{NCFinProb}$ is *symmetric monoidal*
* No canonical copying: $A \to A \otimes A$ not available by default
* This is the quantum *no-cloning* property
}

\subsection{Applying the No-Barber Principle}

\notes{@Lawvere-diagonal69 showed that Russell's barber paradox shares a common categorical structure with Gödel's incompleteness theorem, Turing's halting problem, and Cantor's theorem. The structure requires five ingredients: rules, a universal evaluator, internalisation of syntax, self-application, and a twist. The self-application step requires feeding the same object into two slots simultaneously. In categorical terms this is precisely the diagonal map $A \to A \times A$.

In a cartesian category this map exists for free, making the paradox constructible internally. In a symmetric monoidal category with no canonical copying map, self-application cannot be formed without additional non-standard structure. The Lawvere diagonalisation — and with it the class of impredicative paradoxes it generates — cannot be derived internally.}

\slidesincremental{
* Lawvere diagonalisation needs: self-application $\equiv$ canonical copying
* *$\textsf{FinProb}$ (cartesian):* copying available $\to$ paradox constructible $\to$ external adjudication required
* *$\textsf{NCFinProb}$ (symmetric monoidal):* no canonical copying $\to$ diagonalisation blocked $\to$ no-barber satisfied
}

\newslide{The No-Barber Selection}

\notes{The no-barber principle requires that the internal language of the game does not permit constructions whose resolution requires external adjudication. $\textsf{FinProb}$, being cartesian, admits the diagonal constructions that can generate impredicative circularity. $\textsf{NCFinProb}$, lacking canonical copying, blocks those constructions at the structural level.}

\notes{The no-barber principle selects $\textsf{NCFinProb}$ over $\textsf{FinProb}$ as the foundational language for information loss in the game. This is independent of but consistent with the selection in @Lawrence-origin26, where von Neumann entropy is independently required because the game's origin demands zero joint entropy with positive marginal entropies (a configuration achievable via entanglement but impossible under Shannon entropy).}

\slides{
> The no-barber principle selects $\textsf{NCFinProb}$ over $\textsf{FinProb}$.

* FinProb: cartesian $\rightarrow$ copying $\rightarrow$ Lawvere $\rightarrow$ paradox $\rightarrow$ external adjudication
* NCFinProb: monoidal $\rightarrow$ no-cloning $\rightarrow$ diagonalisation blocked $\rightarrow$ internally adjudicable
* Independently consistent with @Lawrence-origin26
* Information loss $\equiv$ von Neumann entropy decrease
}

\endif

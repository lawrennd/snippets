\ifndef{lawvereDiagonalisation}
\define{lawvereDiagonalisation}

\editme

\subsection{Lawvere Diagonalisation}

\notes{Russell's barber paradox is one instance of a broader class of impossibility results that share a common category-theoretic structure. \citet{Lawvere-diagonal69} showed that Russell's paradox, Cantor's theorem [@Cantor-elementare91], Gödel's incompleteness theorem [@Godel-incompleteness31], Turing's halting problem [@Turing-computable36], and Tarski's undefinability theorem [@Tarski-warhheitsbegriff36] all arise through the same mechanism: a *five-move recipe* for constructing a self-referential contradiction.}

\slides{
**Impossibility results sharing a structure:**

* Russell's paradox
* Cantor's theorem
* Gödel incompleteness
* Turing's halting problem
* Tarski's undefinability

*Unified by Lawvere diagonalisation* [@Lawvere-diagonal69]
}

\newslide{The Five-Move Recipe}

\notes{We treat rules as elements of an internal language whose evaluation is represented by morphisms in a chosen category; the structural properties of that category determine which constructions are available. Lawvere's diagonalisation can be summarised as a five-move recipe.

1. **Rules.** The system consists of *rules* which are a collection of operations that take inputs to outputs.
2. **Universal evaluator.** There must be a universal evaluator operation that can execute a rule on any input.
3. **Internalisation of syntax.** For every rule it must be possible to *internalise the syntax*: the system should be able to identify all its operations internally.
4. **Self-application.** The rules should allow for *self-application*, so that any rule-code can be fed in as an input.
5. **Twist.** There should be a *twist* transformation that can negate or complement outputs.

When all five moves are available, one can construct the diagonal rule: $g(x) = \text{Twist}(\text{Apply}(x, x))$. Through internalisation of syntax, there must exist some internal code $r_0$ such that $g(x) = \text{Apply}(r_0, x)$ for all $x$. Evaluating at $x = r_0$ gives the fixed point $\text{Apply}(r_0, r_0) = \text{Twist}(\text{Apply}(r_0, r_0))$, a contradiction for appropriate choices of twist such as negation.}

\slides{
**Lawvere's Five-Move Recipe:**

1. Rules: operations from inputs to outputs
2. Universal evaluator: run any rule on any input
3. Internalise syntax: rules can reference all operations
4. Self-application: rules can serve as their own input
5. Twist: negate or complement outputs

*When all five hold: contradiction is derivable*
}

\newslide{The Barber Paradox as Lawvere Diagonalisation}

\notes{The barber paradox maps cleanly onto these five moves. Let $P$ be the set of people in the village and $R$ the set of shaving rules, $R : P \to \{\text{yes},\text{no}\}$. Combining a rule with a person produces a shaver object $x = (R, p) \in R \times P$. The universal evaluator is $\text{shaves}((R,q),p) = R(p)$.

Each person $p$ carries a rule $R_p$ describing their shaving behaviour (internalisation of syntax). This enables self-application $R_p(p)$. The twist rule is $T(p) = \neg R_p(p)$, selecting exactly those people who do not shave themselves. Suppose a person $b$ whose shaving behaviour follows $T$: this is the barber $B = (T, b)$. Evaluating the barber on themselves gives $\text{shaves}(B,b) = \neg\text{shaves}(B,b)$—the contradiction.}

\slides{
**Barber as Lawvere:**

| Step | Barber interpretation |
|------|----------------------|
| Rules | shaving rules $R$ |
| Evaluator | $\text{shaves}((R,p),q)$ |
| Internalisation | each person $p$ carries rule $R_p$ |
| Self-application | $R_p(p)$ |
| Twist | $T(p) = \neg R_p(p)$ |

$\Rightarrow$ contradiction: $\text{shaves}(B,b) = \neg\text{shaves}(B,b)$
}

\newslide{Blocking Diagonalisation by Blocking Copying}

\notes{The key observation is that self-application (step 4) requires feeding a rule-code in as its own input, which internally corresponds to *duplicating* that input: the same object must appear simultaneously as both the rule and its argument. This requires a diagonal map
$$
\Delta : P \to P \times P, \qquad \Delta(p) = (p,p),
$$
which duplicates the input. Without such a cloning operation, the twist rule $T(p)$ could not be defined, and the diagonal contradiction would not arise.

In a *cartesian* category every object has a canonical diagonal map $A \to A \times A$ by the universal property of the product. In a *symmetric monoidal* category the product is replaced by a tensor $\otimes$ representing combination of independent resources; there is no universal property forcing a copying map $A \to A \otimes A$ to exist. Moving from a cartesian to a symmetric monoidal setting therefore removes free copying from the internal language.

**Proposition (informal).** In any internal language lacking a canonical copying map $A \to A \otimes A$, the self-application step required for Lawvere diagonalisation cannot be formed without additional, non-standard structure. Consequently, the standard Lawvere-style fixed-point contradiction, including the barber paradox and related diagonal arguments, cannot be derived internally.}

\slides{
**Blocking the Construction:**

Self-application requires *cloning*:
$$\Delta : A \to A \times A, \quad \Delta(a) = (a,a)$$

* **Cartesian category**: canonical $\Delta$ exists — Lawvere diagonalisation possible
* **Symmetric monoidal category**: no canonical $\Delta$ — self-application step fails

*Removing free copying blocks the diagonal construction*
}

\newslide{Linear Logic and No-Cloning}

\notes{This connection between copying and diagonalisation has two natural instantiations. Girard's linear logic makes the hidden structural rules of classical reasoning explicit by removing them: in linear logic, assumptions behave like resources that cannot in general be duplicated or discarded [@Girard-linear87]. Categorically this corresponds to moving from a Cartesian world to a merely symmetric monoidal world $(\otimes, I)$.

Quantum probability fits naturally into this resource-sensitive picture. In a noncommutative setting there is no state-independent way to duplicate an arbitrary unknown state—the quantum no-cloning theorem. The shift from classical to noncommutative probability is analogous to replacing ordinary Boolean logic by a compositional, resource-sensitive logic.

The no-barber principle therefore has a concrete categorical implementation: any internal language that admits canonical copying maps also admits Lawvere-style diagonalisation and is incompatible with self-adjudication. This motivates symmetric monoidal categories—and hence von Neumann entropy over Shannon entropy—as the appropriate setting for self-adjudicating dynamical systems.}

\slides{
**Two programmes that block copying:**

**Linear logic** [@Girard-linear87]:
* Assumptions are resources — can't duplicate freely
* Cartesian $\to$ symmetric monoidal

**Quantum probability (no-cloning)**:
* No canonical $A \to A \otimes A$ for unknown states
* Noncommutative $C^*$-algebras replace Boolean event spaces

*Both satisfy the no-barber constraint for independent reasons*
}

\endif

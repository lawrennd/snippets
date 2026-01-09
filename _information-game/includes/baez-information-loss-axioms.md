\ifndef{baezInformationLossAxioms}
\define{baezInformationLossAxioms}

\editme

\subsection{Baez-Fritz-Leinster Characterization of Information Loss}

\notes{Before introducing our fourth axiom, we need to understand how information loss is measured. @Baez-characterisation11 showed that entropy emerges naturally from category theory as a way of measuring information loss in measure-preserving functions. They derived Shannon entropy from three axioms, without invoking probability directly.}

\slides{
**@Baez-characterisation11:**
* Entropy from category theory
* Three axioms uniquely determine information loss
* No probability needed initially
}

\subsubsection{The Three Axioms}

\notes{Let $F(f)$ denote the information lost by a process $f$ that transforms one probability distribution to another. The three axioms constrain the functional form of $F$.}

\notes{**Axiom 1: Functoriality** suggests that given a process consisting of two stages, the amount of information lost in the whole process is the sum of the amounts lost at each stage:
$$
F(f \circ g) = F(f) + F(g),
$$
where $\circ$ represents composition.}

\slides{
**Axiom 1: Functoriality**
$$F(f \circ g) = F(f) + F(g)$$

* Information loss is additive
* Compose processes → add losses
}

\newslide{Convex Linearity}

\notes{**Axiom 2: Convex Linearity** suggests that if we flip a probability-$\lambda$ coin to decide whether to do one process or another, the information lost is $\lambda$ times the information lost by the first process plus $(1-\lambda)$ times the information lost by the second:
$$
F(\lambda f \oplus (1-\lambda)g) = \lambda F(f) + (1-\lambda)F(g).
$$}

\slides{
**Axiom 2: Convex Linearity**
$$F(\lambda f \oplus (1-\lambda)g) = \lambda F(f) + (1-\lambda)F(g)$$

* Probabilistic mixture of processes
* Linear in probability weights
}

\newslide{Continuity}

\notes{**Axiom 3: Continuity** suggests that if we change a process slightly, the information lost changes only slightly, i.e. $F(f)$ is a continuous function of $f$.}

\slides{
**Axiom 3: Continuity**

* Small change in process
* Small change in information loss
* $F(f)$ continuous in $f$
}

\subsection{The Main Result}

\notes{The main result of @Baez-characterisation11 is that these three axioms uniquely determine the form of information loss. There exists a constant $c\geq 0$ such that for any $f: p \rightarrow q$:
$$
F(f) = c(H(p) -H(q))
$$
where $F(f)$ is the information loss in process $f: p\rightarrow q$ and $H(\cdot)$ is the Shannon entropy measured before and after the process is applied to the system.}

\slides{
**Theorem:**

Three axioms $\Rightarrow$ unique form:
$$F(f) = c(H(p) - H(q))$$

* Information loss = scaled entropy difference
* Shannon entropy emerges from axioms
* No other measure satisfies all three
}

\notes{This provides a foundational justification for using entropy as our measure of information. It's not just a convenient choice, it's the unique measure that satisfies natural requirements for measuring information loss.}

\endif
\endif

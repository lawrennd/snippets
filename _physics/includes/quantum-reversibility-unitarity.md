\ifndef{quantumReversibilityUnitarity}
\define{quantumReversibilityUnitarity}

\editme

\subsection{Quantum Preview: Reversibility Forces Unitarity}

\notes{So far, the course has largely lived in a \emph{commutative} setting. In a commutative setting we can talk about random variables, joint distributions, and entropies of those distributions.

The new TIG paper makes a sharper point: the ``origin'' configuration we want (max multi-information with zero joint entropy, i.e. globally pure but locally maximally uncertain) is \emph{forbidden} in the classical/Shannon setting because classical conditional entropy is nonnegative.

A clean resolution is to move to \emph{noncommutative probability}: keep expectations as the primitive notion, but allow observables that do not commute. This forces a different representation of ``state'' and (crucially for today's lecture) it forces a different notion of \emph{reversible} dynamics.}

\subsubsection{Expectation-first view (state = expectation functional)}

\notes{In noncommutative probability, the observables are Hermitian operators (matrices) $A$.

A \emph{state} is not a point in phase space; it is an \emph{expectation functional} $\omega$ which assigns an expectation value $\omega(A)$ to each observable $A$.

In finite dimensions, every such state can be represented by a \emph{density matrix} $\rho$ so that
\[
\omega(A) = \text{tr}(\rho A),\qquad \rho\succeq 0,\quad \text{tr}(\rho)=1.
\]
Intuitively: the density matrix is the object that lets you take consistent expectations when there is no underlying joint sample space.}

\slides{
**Noncommutative probability:**

- observables: Hermitian operators $A$
- state: expectation functional $\omega(A)$
- finite-dim representation: $\omega(A)=\text{tr}(\rho A)$
}

\subsubsection{Reversible transformations (no information loss)}

\notes{What does it mean for a transformation to be \emph{reversible}?

In the information-loss framing, reversible means: it preserves information (equivalently, it preserves von Neumann entropy for all states).

This is a real shift from normal (commutative) probability. Classically, if you have a sample space $\Omega$ and random variables are functions $\Omega\to\mathbb{R}$, then a reversible transformation is (morally) an invertible relabelling $\phi:\Omega\to\Omega$ that preserves probabilities; observables are pushed forward/pulled back by composition, and you really can think in terms of ``moving points around'' in $\Omega$.

In noncommutative probability there is \emph{no underlying joint sample space} when observables don't commute. So ``reversibility'' can't mean a pointwise relabelling of outcomes; instead it means an isomorphism of the \emph{observable algebra} (a $*$-isomorphism) that preserves the expectation structure. In finite dimensions, for \emph{closed systems}, those algebra isomorphisms are implemented by unitary (or antiunitary) conjugation.

For closed finite-dimensional quantum systems, the reversible transformations are exactly the ones implemented by unitary conjugation:
\[
\rho \mapsto U\rho U^\dagger,\qquad U^\dagger U = I.
\]
This is not an additional modelling assumption; it is the structural notion of ``symmetry'' compatible with noncommutative probability. (Open systems with dissipation require the broader class of completely positive trace-preserving maps; unitary is the reversible special case.)}

\slides{
**Reversible (closed system) ⇒ unitary:**

$\rho \mapsto U\rho U^\dagger$

(Open systems: CPTP maps; unitary = reversible case)
}

\subsubsection{Infinitesimal form: commutator dynamics}

\notes{The paper's perspective is that \emph{expectations are primitive}. So we should describe reversible time evolution in a way that is \emph{consistent} with invariance of expectations.

Let $\mathcal{A}$ be our observable algebra (think: matrices) and let a state be an expectation functional $\omega:\mathcal{A}\to\mathbb{R}$.

\textbf{Reversible dynamics} are implemented by a one-parameter family of algebra automorphisms $\alpha_t$ (in finite dimensions: $\alpha_t(A)=U(t)^\dagger A U(t)$). This is the Heisenberg-style statement: observables are transformed, and expectations are preserved by pulling the state back.

Define the time-evolved state by
$$
\omega_t(A) \coloneq \omega_0 \big(\alpha_t(A)\big).
$$
This definition makes the invariance principle explicit: we are not changing the meaning of expectation-taking; we are composing with an automorphism of the observable algebra.

If $\alpha_t$ is smooth, we can look at the \emph{infinitesimal} change it induces. Define the generator $\delta$ by
$$
\frac{\text{d}}{\text{d}t}\alpha_t(A)\big\rvert_{t=0}=\delta(A).
$$
What does this mean concretely? In finite dimensions we can take
$$
U(t)=e^{-itH}\qquad\text{with $H$ Hermitian,}
$$
so that $\alpha_t(A)=U(t)^\dagger A U(t) = e^{itH} A e^{-itH}$.
Differentiate this expression at $t=0$ and you get
$$
\delta(A)= i[H,A].
$$
Here are the steps, written out:
$$
\alpha_t(A)=e^{itH} A e^{-itH}.
$$
Use the product rule
$$
\frac{\text{d}}{\text{d}t}\alpha_t(A)
=\left(\frac{\text{d}}{\text{d}t}e^{itH}\right)Ae^{-itH}
+e^{itH}A\left(\frac{\text{d}}{\text{d}t}e^{-itH}\right).
$$
Now use the standard derivative identities (valid for constant $H$):
$$
\frac{\text{d}}{\text{d}t}e^{itH} = iH e^{itH},\qquad
\frac{\text{d}}{\text{d}t}e^{-itH} = -iH e^{-itH}.
$$
Substitute them
$$
\frac{\text{d}}{\text{d}t}\alpha_t(A)
= iHe^{itH}Ae^{-itH}-e^{itH}AiHe^{-itH}.
$$
Finally evaluate at $t=0$ (so $e^{itH}=I$):
$$
\delta(A)=\frac{\text{d}}{\text{d}t}\alpha_t(A)\Big\rvert_{t=0}
= iHA-iAH=i[H,A].
$$

This is the Heisenberg form: the observable evolves by a commutator. If you have not seen commutators before, you can read $[H,A]=HA-AH$ as "apply $H$ then $A$ minus apply $A$ then $H$".

Now translate this to the density-matrix representation. If $\omega_t(A)=\text{tr}(\rho(t)A)$ represents the same expectation functional, then consistency for \emph{all} observables $A$ forces
$$
\text{tr}(\dot\rho A) = \frac{\text{d}}{\text{d}t} \omega_t(A) = \omega_0 \big(\delta(A)\big)=\text{tr}(\rho i[H,A]).
$$
Using cyclicity[^trace_cyclicity] of trace, $\text{tr}(\rho i[H,A])=\text{tr}((-i[H,\rho])A)$, 
so we must have
$$
\dot\rho = -i[H,\rho].
$$
This is exactly the paper's point: the commutator form is the concrete finite-dimensional equation whose job is to implement the \emph{invariance/consistency of expectation-taking} under reversible evolution.

[^trace_cyclicity]: For compatible matrices, $\text{tr}(AB)=\text{tr}(BA)$, and more generally $\text{tr}(ABC)=\text{tr}(BCA)=\text{tr}(CAB)$.
}

\slides{
**Infinitesimal unitary evolution:**

$$\dot\rho=-i[H,\rho]$$
}

\subsubsection{Commutative sanity check: diagonals recover classical probability}

\notes{Fix a basis and restrict attention to the \emph{commutative (diagonal) subalgebra} of observables. Concretely, take observables of the form
$$
A=\text{diag}(a_1,\dots,a_d)
$$
and restrict to diagonal density matrices
$$
\rho=\text{diag}(p_1,\dots,p_d),\qquad p_i\ge 0,\ \sum_i p_i=1.
$$
Then the expectation functional becomes ordinary probability:
$$
\omega(A)=\text{tr}(\rho A)=\sum_{i=1}^d p_i a_i.
$$
So ``noncommutative probability'' collapses to classical probability on the finite sample space $\Omega=\{1,\dots,d\}$.

Structural note: the diagonal matrices form a \emph{maximal abelian subalgebra}—the only matrices that commute with all diagonal matrices are themselves diagonal. So restricting to commuting observables isn't just a convenience; it's the structural reason why classical probability sits inside quantum probability as a special case.}

Now look at reversible transformations. If we want to stay inside the diagonal algebra, the allowed unitaries are permutations of the basis.
Let $U_\pi$ be the permutation matrix for a bijection $\pi:\Omega\to\Omega$. Then conjugation gives
$$
\alpha_\pi(A)=U_\pi^\dagger A U_\pi = \text{diag}(a_{\pi(1)},\dots,a_{\pi(d)}),
$$
which is literally ``relabel the outcomes''.

On states,
$$
\rho^\prime = U_\pi\rho U_\pi^\dagger = \text{diag}(p_{\pi^{-1}(1)},\dots,p_{\pi^{-1}(d)}),
$$
which is the same relabelling acting on the probability vector.

Note what disappears in the commuting restriction: if both $H$ and $\rho$ are diagonal, then $[H,\rho]=H \rho - \rho H=0$ and the commutator dynamics is trivial. The only reversible transformations that preserve diagonality are discrete relabellings (permutations), whereas general unitaries give you the genuinely noncommutative ``rotation'', i.e.\ basis-change behaviour.}

\slides{
**Commutative sanity check (diagonals):**

- $\rho=\text{diag}(p)$, $A=\text{diag}(a)$
- $\omega(A)=\text{tr}(\rho A)=\sum_i p_i a_i$ (classical expectation)
- Diagonal-preserving unitaries $\approx$ permutations $U_\pi$
- $U_\pi^\dagger A U_\pi$ permutes outcomes (pure relabelling)
}

\subsubsection{Bridge back: Poisson brackets as the commutative shadow}

\notes{Why does this belong in today's Poisson-bracket lecture?

Because Poisson brackets are the \emph{commutative limit} of commutators:
\[
\frac{1}{i\hbar}[\hat f,\hat g] \;\longrightarrow\; \{f,g\}
\]
(heuristically, as $\hbar\to 0$ and operators become classical observables).

So today's classical message

- ``antisymmetry $\Rightarrow$ conservation''

is the shadow of a deeper structural message:

- ``noncommutativity + reversibility $\Rightarrow$ unitarity $\Rightarrow$ commutator flow''.

We will now develop Poisson brackets as a concrete, classical calculus for this reversible sector.}

\endif


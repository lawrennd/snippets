\ifndef{originParadoxShannonVonNeumann}
\define{originParadoxShannonVonNeumann}

\editme

\subsection{The Origin Paradox: Shannon vs von Neumann}

\notes{The inaccessible game wants a very specific kind of ``origin'' state:

- maximal multi-information ($I=C$), but
- zero joint entropy ($H=0$).

Informally: the system is globally fully specified (no global uncertainty), but every subsystem looks maximally uncertain on its own.

In classical probability (commutative setting), this origin is impossible. The obstruction is not a technicality — it is a structural inequality: classical conditional entropy is nonnegative.

The quantum (noncommutative) resolution is equally structural: von Neumann conditional entropy can be negative for entangled states, and those are exactly the configurations that look ``locally maximally uncertain'' while remaining globally pure.}

\slides{
**Origin target:**

- $I=C$
- $H=0$

**Classical obstruction:** $H(X|Y)\ge 0$

**Quantum resolution:** $\mathsf{H}(A|B)$ can be negative
}

\subsubsection{Why the classical origin is impossible}

\notes{Consider two variables $X,Y$ (the same idea scales).
Recall
$$
I(X;Y)=H(X)+H(Y)-H(X,Y).
$$
If $H(X,Y)=0$ then the joint distribution puts all mass on a single outcome $(x^\star,y^\star)$, which forces $H(X)=H(Y)=0$ as well. So you cannot have $H(X,Y)=0$ while keeping $H(X)+H(Y)$ positive.

Another way to say the same thing is through conditional entropy:
$$
H(X|Y)=H(X,Y)-H(Y)\ge 0.
$$
If $H(X,Y)=0$ but $H(Y)>0$, then $H(X|Y)=-H(Y)<0$, contradicting $H(X|Y)\ge 0$.

So the origin condition "globally pure but locally uncertain" is forbidden in the commutative/Shannon world.}

\subsubsection{von Neumann entropy changes the rules}

\notes{In noncommutative probability, the joint system is described by a density matrix $\rho_{AB}$ and subsystems by reduced density matrices $\rho_A=\text{tr}_B(\rho_{AB})$, $\rho_B=\text{tr}_A(\rho_{AB})$.

The von Neumann entropy is
$$
\textsf{H}(\rho)=-\text{tr}(\rho\log\rho).
$$
We can define conditional entropy by the same formal identity:
$$
\textsf{H}(A|B)=\textsf{H}(\rho_{AB})-\textsf{H}(\rho_B).
$$
But now $\textsf{H}(A|B)$ can be \emph{negative}. That is not a bug: it is exactly how entanglement shows up as "more-than-classical correlation".}

\slides{
**von Neumann entropy:**

$$\textsf{H}(\rho)=-\text{tr}(\rho\log\rho)$$

**Conditional:**

$$\textsf{H}(A|B)=\textsf{H}(AB)-\textsf{H}(B) \text{ (can be < 0)}$$
}

\subsubsection{Worked toy example: Bell state}

\notes{Take two qubits and the Bell state
$$
\ket{\Phi^+}=\frac{1}{\sqrt 2}(\ket{00}+\ket{11}),
\qquad \rho_{AB}=\ket{\Phi^+}\bra{\Phi^+}.
$$
This is a \emph{pure} joint state, so
$$
\textsf{H}(\rho_{AB})=0.
$$
But each marginal is maximally mixed:
$$
\rho_A=\rho_B=\frac{1}{2}I,
\qquad \textsf{H}(\rho_A)=\textsf{H}(\rho_B)=\log 2.
$$
Therefore
$$
\textsf{H}(A|B)=\textsf{H}(AB)-\textsf{H}(B)=0-\log 2=-\log 2<0.
$$
This is exactly the pattern TIG wants at the origin:

- globally pure ($\textsf{H}(AB)=0$),
- locally maximally uncertain ($\textsf{H}(A),\textsf{H}(B)$ maximal).

So the quantum/noncommutative formalism makes the origin \emph{representable} without changing the goal — only changing the structural notion of "information loss".}

\slides{
**Bell state:**

- $\textsf{H}(AB)=0$
- $\textsf{H}(A)=\textsf{H}(B)=\log 2$
- $\textsf{H}(A|B)=-\log 2$
}

\subsubsection{Connection back to TIG}

\notes{This is why the paper pivots to von Neumann entropy:

- It preserves the “information as entropy difference” intuition.
- It removes the classical origin obstruction.
- It forces an expectation-first, noncommutative probability framing.

From here, the next question is: once expectations are primitive, what are the reversible transformations that preserve this expectation structure? That leads into the unitary/commutator story.}

\endif


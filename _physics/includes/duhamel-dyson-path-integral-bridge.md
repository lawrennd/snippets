\ifndef{duhamelDysonPathIntegralBridge}
\define{duhamelDysonPathIntegralBridge}

\editme

\subsection{How Duhamel Connects to Dyson Series and Path Integrals}

\notes{Students often see a lot of different-looking formulas in quantum/statistical physics:

- Duhamel integrals for differentiating operator exponentials,
- time-ordered exponentials and Dyson series,
- Trotter product formulas,
- and path integrals (often as a limit of time-slicing).

These are not disconnected tricks. They are different faces of the same underlying issue:

\begin{center}
\emph{when operators do not commute, you cannot manipulate exponentials as if they were scalars.}
\end{center}

The role of Duhamel-type formulas is to give a \emph{controlled} way to move derivatives or perturbations through a noncommuting exponential.}

\slides{
**Unifying obstacle:** noncommutativity

Operator exponentials $\neq$ scalar exponentials

Duhamel / Dyson / Trotter / path integrals = ways to cope
}

\subsubsection{Two "Duhamel" ideas}

\notes{The word “Duhamel” gets used in two closely related contexts.

\textbf{(A) Duhamel for derivatives of exponentials (ordering parameter).}

If $K(\theta)$ is an operator and $F_i=\partial K/\partial\theta_i$, then
$$
\partial_i e^{K(\theta)}
=\int_0^1 e^{(1-s)K(\theta)} F_i e^{sK(\theta)} \text{d}s.
$$
Here $s\in[0,1]$ is an \emph{ordering parameter} that tells you where the derivative is inserted inside the exponential.

\textbf{(B) Duhamel for splitting a generator (time parameter).}

If you want to compare the exponential of a sum to the exponential of a part, e.g.
$$
e^{t(A+B)} \quad \text{vs} \quad e^{tA},
$$
then a Duhamel formula expresses their difference as an integral involving $B$. This is the backbone of perturbation expansions in time evolution.}

\subsubsection{From Duhamel to Dyson (time-ordered exponential)}

\notes{In quantum dynamics, you often split a Hamiltonian into "easy + perturbation":
$$
H=H_0+V.
$$
In the interaction picture one defines an interaction operator
$$
V_I(t)=e^{i t H_0} V e^{-i t H_0},
$$
and the exact propagator can be written as a \emph{time-ordered exponential}
$$
U(t)=\mathcal{T}\exp \left(-i\int_0^t V_I(\tau) \text{d}\tau\right).
$$

Expanding the time-ordered exponential gives the Dyson series:
$$
U(t)=I+\sum_{n\ge 1}(-i)^n\int_{0\le \tau_n\le\cdots\le \tau_1\le t}
V_I(\tau_1)\cdots V_I(\tau_n) \text{d}\tau_1 \cdots \text{d}\tau_n.
$$

Conceptually: this is “Duhamel(B)” iterated. Each integral insertion accounts for the fact that $H_0$ and $V$ do not commute, so you must keep track of operator order in time.}

\slides{
**Dyson series:**

$U(t)=\mathcal{T}\exp(-i\int_0^t V_I)$

Expands into ordered integrals (time-ordering = noncommutativity bookkeeping)
}

\subsubsection{From Dyson/Trotter to path integrals (time slicing)}

\notes{Path integrals can be introduced as a computational method by time-slicing (Trotterisation).

The Trotter product formula states:
$$
e^{t(A+B)}
=\lim_{n\to\infty}\left(e^{tA/n}\,e^{tB/n}\right)^n
$$
for suitable operators $A$ and $B$ (e.g., bounded operators, or self-adjoint with appropriate domain conditions).

**Error analysis:** The simple splitting above has error $O(t^2/n)$. For practical time-stepping, symmetric (Strang) splitting $e^{tA/(2n)}e^{tB/n}e^{tA/(2n)}$ gives error $O(t^3/n^2)$. There is a large literature on higher-order splittings for numerical simulation.

For example, in (imaginary-time) statistical mechanics:
$$
e^{-\beta(H_0+V)}
=\lim_{n\to\infty}\left(e^{-\beta H_0/n}\,e^{-\beta V/n}\right)^n.
$$
In real time one has an analogous statement for $e^{-it(H_0+V)}$.

Now insert resolutions of the identity between the factors (e.g. position eigenstates for particles, spin basis for spins). In the limit of many slices, the product becomes an integral over intermediate configurations: that limiting object is the (Euclidean or real-time) path integral.

So the path integral is another way to cope with noncommutativity: it replaces a hard operator exponential with a limit of many small steps where the ordering is explicit.}

\subsubsection{How this relates to our Duhamel parameter $s\in[0,1]$}

\notes{In our TIG quantum exponential-family calculations, the Duhamel integral involves an $s\in[0,1]$ ordering parameter:
$$
\partial_i e^{K}=\int_0^1 e^{(1-s)K}F_i e^{sK} \text{d}s.
$$

This is not a physical time variable. It is the same kind of bookkeeping device as:

- the time-ordering operator $\mathcal{T}$ in Dyson expansions, and
- the slice index in Trotter/path-integral constructions.

All three enforce one principle: \emph{when things do not commute, "where you insert an operator" matters.}}

\slides{
**Key moral:**

ordering matters

$s$ (Duhamel) / $\mathcal{T}$ (Dyson) / time-slices (path integral)
}

\endif


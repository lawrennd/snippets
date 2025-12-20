\ifndef{exponentialFamilyClassicalToQuantum}
\define{exponentialFamilyClassicalToQuantum}

\editme

\subsection{From Classical to Quantum Exponential Families}

\notes{If you know classical exponential families and information geometry, you already have the right conceptual framework for quantum statistical mechanics. The move to quantum is not a wholesale replacement; it is a \emph{minimal extension} to handle one new feature: observables that do not commute.

This section maps the familiar classical objects to their quantum counterparts, highlights exactly what breaks (and why), and previews the computational fix (Duhamel calculus).}

\slides{
**For ML + info-geometry folks:**

Classical exponential families → quantum exponential families

Same structure, one new obstacle (noncommutativity)
}

\subsubsection{The classical exponential family (what you already know)}

\notes{In classical statistics, an exponential family has the form
$$
p(\mathbf{x};\theta) = \exp\!\big(\theta^\top \mathbf{F}(\mathbf{x}) - \psi(\theta)\big),
$$
where:

- $\mathbf{x}$ is a sample from some space $\mathcal{X}$,
- $\mathbf{F}(\mathbf{x})=(F_1(\mathbf{x}),\dots,F_d(\mathbf{x}))$ are sufficient statistics,
- $\theta\in\mathbb{R}^d$ are natural parameters,
- $\psi(\theta)=\log\int_{\mathcal{X}} e^{\theta^\top \mathbf{F}(\mathbf{x})}\,\text{d}\mu(\mathbf{x})$ is the log-partition function.

Key properties you rely on:

1. **Expectations from $\psi$**: $\mathbb{E}_\theta[F_i]=\partial_i\psi(\theta)$.
2. **Fisher information metric**: $G_{ij}(\theta)=\partial_i\partial_j\psi(\theta)=\text{Cov}_\theta(F_i,F_j)$.
3. **Geometry**: $G$ is the Riemannian metric on the parameter space; it controls local linear response and natural gradient descent.
4. **Differentiating the exponential**: $\partial_i e^{\theta^\top \mathbf{F}} = F_i e^{\theta^\top \mathbf{F}}$ (scalars commute).
}

\slides{
**Classical exponential family:**

$$p(\mathbf{x};\theta)=\exp(\theta^\top \mathbf{F}-\psi(\theta))$$

- $\mathbb{E}[F_i]=\partial_i\psi$
- Fisher metric: $G_{ij}=\partial_i\partial_j\psi$
- Differentiate exponential: $\partial_i e^{\theta^\top \mathbf{F}}=F_i e^{\theta^\top \mathbf{F}}$ (scalars commute)
}

\subsubsection{The quantum exponential family (same structure, different representation)}

\notes{In quantum statistical mechanics, a state is represented by a \emph{density matrix} $\rho$, which is a positive semidefinite matrix with trace 1. Observables are Hermitian matrices $A$, and the expectation is $\langle A\rangle=\text{tr}(\rho A)$.

A quantum exponential family has exactly the same form:
$$
\rho(\theta) = \exp\!\big(K(\theta) - \psi(\theta)\big),
$$
where:

- $K(\theta)=\sum_i \theta_i F_i$ is a Hermitian matrix (the "Hamiltonian" in statistical-mechanics language),
- $F_i$ are Hermitian "sufficient statistic" operators,
- $\psi(\theta)=\log\text{tr}\,e^{K(\theta)}$ is the log-partition function (now a trace over operator exponential),
- $\rho(\theta)$ is the density matrix (analogous to the probability density $p$).

(Physics often writes $K=-\beta H$ with a minus sign; here we absorb signs into the $\theta_i$ parameters.)

\textbf{What stays the same:}

1. **Expectations from $\psi$**: $\langle F_i\rangle=\text{tr}(\rho F_i)=\partial_i \psi(\theta)$. Noncommutativity complicates $\partial_i e^K$, but trace cyclicity plus Duhamel still yields this identity.
2. **Fisher-like metric**: $G_{ij}(\theta)=\partial_i\partial_j\psi(\theta)$ is the Bogoliubov–Kubo–Mori (BKM) metric, one canonical quantum analog of Fisher information, and the one that naturally appears in thermodynamic linear response.
3. **Geometry**: $G$ is still a Riemannian metric governing local linear response.
4. **$\psi$ is still a scalar function** of real parameters $\theta\in\mathbb{R}^d$.

\textbf{What breaks:}

**Matrices do not commute**, so $\partial_i e^{K(\theta)} \neq F_i e^{K(\theta)}$ in general.

This is the \emph{only} obstacle, but it requires new calculus.}

\slides{
**Quantum exponential family:**

$$\rho(\theta)=\exp(K(\theta)-\psi(\theta)),\quad K=\sum_i\theta_i F_i$$

(Physics: $K=-\beta H$; we absorb signs into $\theta$)

**What stays the same:**

- $\langle F_i\rangle=\partial_i\psi$ (trace cyclicity + Duhamel preserves this)
- $G_{ij}=\partial_i\partial_j\psi$ (BKM metric—canonical quantum Fisher)
- $\psi$ is still a scalar real-valued function

**What breaks:**

- Matrices don't commute: $\partial_i e^K \neq F_i e^K$
}

\subsubsection{Side-by-side comparison}

\notes{Here is the structural mapping:

| **Classical** | **Quantum** |
|---------------|-------------|
| Sample space $\mathcal{X}$ | Hilbert space $\mathcal{H}$ (dim $d$) |
| Probability density $p(\mathbf{x})$ | Density matrix $\rho$ ($d\times d$ positive, trace 1) |
| Random variable $F:\mathcal{X}\to\mathbb{R}$ | Observable (Hermitian operator) $F$ |
| Expectation $\mathbb{E}_p[F]=\int F(\mathbf{x})p(\mathbf{x})\,\text{d}\mu$ | Expectation $\langle F\rangle=\text{tr}(\rho F)$ |
| Exponential family $p=e^{\theta^\top \mathbf{F}-\psi}$ | Quantum exp. family $\rho=e^{K-\psi}$ |
| Log-partition $\psi=\log\int e^{\theta^\top \mathbf{F}}\,\text{d}\mu$ | Log-partition $\psi=\log\text{tr}\,e^K$ |
| Fisher metric $G_{ij}=\partial_i\partial_j\psi$ | BKM metric $G_{ij}=\partial_i\partial_j\psi$ |
| $\partial_i e^{\theta^\top \mathbf{F}}=F_i e^{\theta^\top \mathbf{F}}$ (scalars) | $\partial_i e^K=\int_0^1 e^{(1-s)K}F_i e^{sK}\,\text{d}s$ (Duhamel) |

The top six rows are \emph{structurally identical}. The last row is where noncommutativity forces new calculus.}

\slides{
| Classical | Quantum |
|-----------|---------|
| $p(\mathbf{x})$ (probability) | $\rho$ (density matrix) |
| $F:\mathcal{X}\to\mathbb{R}$ (r.v.) | $F$ (Hermitian op.) |
| $\mathbb{E}[F]=\int Fp\,\text{d}\mu$ | $\langle F\rangle=\text{tr}(\rho F)$ |
| $p=e^{\theta^\top \mathbf{F}-\psi}$ | $\rho=e^{K-\psi}$ |
| $\psi=\log\int e^{\theta^\top \mathbf{F}}$ | $\psi=\log\text{tr}\,e^K$ |
| $G_{ij}=\partial_i\partial_j\psi$ | $G_{ij}=\partial_i\partial_j\psi$ (BKM) |
| $\partial_i e^{\theta^\top \mathbf{F}}=F_i e^{\theta^\top \mathbf{F}}$ | $\partial_i e^K=$ **Duhamel integral** |
}

\subsubsection{Why noncommutativity matters (and what Duhamel fixes)}

\notes{In the classical case, when you differentiate the exponential in $\psi(\theta)=\log\int e^{\theta^\top \mathbf{F}(\mathbf{x})}\,\text{d}\mu$, you can "pull down" the sufficient statistic:
$$
\partial_i e^{\theta^\top \mathbf{F}} = F_i(\mathbf{x})\, e^{\theta^\top \mathbf{F}(\mathbf{x})}.
$$
This is because $\theta^\top \mathbf{F}(\mathbf{x})$ is a scalar for each $\mathbf{x}$.

In the quantum case, $K(\theta)=\sum_j\theta_j F_j$ is a \emph{matrix}, and the $F_i$ are matrices. In general, $F_i K \neq K F_i$ (they do not commute), so you cannot write $\partial_i e^K = F_i e^K$.

The \textbf{Duhamel formula} is the correct way to differentiate a matrix exponential:
$$
\frac{\partial}{\partial\theta_i} e^{K(\theta)}
= \int_0^1 e^{(1-s)K(\theta)}\, F_i\, e^{sK(\theta)}\,\text{d}s.
$$

You can read $s\in[0,1]$ as "where you insert the derivative inside the exponential". It is an \emph{ordering parameter}, not a physical time.

Once you have Duhamel, all the familiar exponential-family calculations go through:

- differentiate $\psi$ to get expectations,
- differentiate again to get the Fisher-like metric (BKM),
- and everything else (natural parameters, duality, convexity) works as before.

\textbf{Bottom line for ML folks:} Quantum exponential families are the same probabilistic modeling framework you already know, plus one new computational layer (Duhamel) to handle the fact that operators are matrices.}

\slides{
**Why Duhamel:**

Classical: $\partial_i e^{\theta^\top \mathbf{F}}=F_i e^{\theta^\top \mathbf{F}}$ (scalars commute)

Quantum: $F_i K \neq K F_i$ in general (matrices don't commute)

**Fix:** Duhamel integral

$$\partial_i e^K=\int_0^1 e^{(1-s)K}F_i e^{sK}\,\text{d}s$$

($s$ = ordering parameter, not time)

Then all exponential-family calculus works!
}

\subsubsection{What comes next in the course}

\notes{Now that you see the structural parallel, the rest of the quantum development is:

1. **Reversible dynamics** (analogous to measure-preserving maps): in quantum, these are unitary transformations $\rho\mapsto U\rho U^\dagger$, which preserve von Neumann entropy (the quantum analog of Shannon entropy).

2. **Infinitesimal reversible dynamics**: these are generated by commutators $\dot\rho=-i[H,\rho]$, which is the quantum analog of Hamiltonian flow (Poisson brackets).

3. **Computation layer**: when you need to linearize dynamics or compute Fisher-like metrics, you use Duhamel/Kubo–Mori calculus to handle the derivatives of operator exponentials.

4. **Applications**: quantum natural gradient, variational inference on quantum states, reversible quantum neural networks, etc.

The punchline: if you know exponential families + Fisher information + natural gradients, you already understand the quantum story—you just need Duhamel to handle the matrix algebra.}

\slides{
**Course roadmap (for ML folks):**

1. Reversible dynamics → unitary $U\rho U^\dagger$
2. Infinitesimal form → commutator $\dot\rho=-i[H,\rho]$
3. Computation layer → Duhamel/Kubo–Mori for derivatives
4. Applications → quantum natural gradient, variational inference, etc.

**If you know exp. families + Fisher info, you're 90% there.**
}

\endif



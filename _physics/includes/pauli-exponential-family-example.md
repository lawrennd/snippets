\ifndef{pauliExponentialFamilyExample}
\define{pauliExponentialFamilyExample}

\editme

\subsection{Concrete Example: 2×2 Pauli Exponential Family}

\notes{To make the quantum exponential family concrete, let's work through the simplest nontrivial case: a 2-level system (qubit) using Pauli matrices.

This example shows exactly where noncommutativity appears, why the classical derivative formula fails, and how Duhamel fixes it.}

\slides{
**Concrete 2×2 example:**

Pauli matrices (qubit sufficient statistics)
}

\subsubsection{The Pauli basis}

\notes{The Pauli matrices are
$$
\sigma_x = \begin{pmatrix}0&1\\1&0\end{pmatrix},\quad
\sigma_z = \begin{pmatrix}1&0\\0&-1\end{pmatrix}.
$$

These are Hermitian, traceless, and \emph{do not commute}:
$$
\sigma_x \sigma_z = \begin{pmatrix}0&-1\\1&0\end{pmatrix},\quad
\sigma_z \sigma_x = \begin{pmatrix}0&1\\-1&0\end{pmatrix},
$$
so $[\sigma_x,\sigma_z]=\sigma_x\sigma_z-\sigma_z\sigma_x = 2i\sigma_y \neq 0$.

We'll use these as sufficient statistics $F_1=\sigma_x$, $F_2=\sigma_z$.}

\slides{
**Pauli matrices:**

$$\sigma_x = \begin{pmatrix}0&1\\1&0\end{pmatrix},\quad \sigma_z = \begin{pmatrix}1&0\\0&-1\end{pmatrix}$$

**Key property:** $[\sigma_x,\sigma_z]\neq 0$ (noncommuting)
}

\subsubsection{Quantum exponential family for a qubit}

\notes{Define a 2-parameter exponential family:
$$
\rho(\theta_1,\theta_2) = \frac{1}{Z(\theta)} \exp(\theta_1 \sigma_x + \theta_2 \sigma_z),
$$
where
$$
K(\theta)=\theta_1\sigma_x+\theta_2\sigma_z,\qquad Z(\theta)=\text{tr}\,e^{K(\theta)},\qquad \psi(\theta)=\log Z(\theta).
$$

The density matrix $\rho$ is $2\times 2$, Hermitian, positive semidefinite, with trace 1.

**Question:** How do we compute $\partial_1\psi$ (the expectation of $\sigma_x$)?}

\slides{
**Qubit exponential family:**

$$\rho(\theta)=\frac{1}{Z(\theta)}e^{\theta_1\sigma_x+\theta_2\sigma_z}$$

$$\psi(\theta)=\log\text{tr}\,e^{\theta_1\sigma_x+\theta_2\sigma_z}$$

Goal: compute $\partial_1\psi = \langle \sigma_x\rangle$
}

\subsubsection{Why the classical formula fails}

\notes{In the classical case, we would write $\psi=\log\int e^{\theta^\top \mathbf{F}} \text{d}\mu$ and differentiate:
$$
\partial_1 e^{\theta_1 F_1+\theta_2 F_2} = F_1 e^{\theta_1 F_1+\theta_2 F_2}.
$$
This works because scalars commute.

In the quantum case, $F_1$ and $F_2$ are matrices ($\sigma_x$ and $\sigma_z$), and they don't commute. So
$$
\partial_1 e^{\theta_1\sigma_x+\theta_2\sigma_z} \neq \sigma_x e^{\theta_1\sigma_x+\theta_2\sigma_z}.
$$

To see this concretely, note that $\sigma_x K(\theta) \neq K(\theta)\sigma_x$ in general (try it with $\theta_1=\theta_2=1$ for a numerical check).

So we cannot "pull down" $\sigma_x$ from inside the exponential naively.}

\slides{
**Classical:** $\partial_1 e^{\theta_1 F_1+\theta_2 F_2} = F_1 e^{\theta_1 F_1+\theta_2 F_2}$ ✓

**Quantum:** $\partial_1 e^{\theta_1\sigma_x+\theta_2\sigma_z} \neq \sigma_x e^{\theta_1\sigma_x+\theta_2\sigma_z}$ ✗

(because $\sigma_x$ and $\sigma_z$ don't commute)
}

\subsubsection{Duhamel formula fixes it}

\notes{The correct derivative formula is the Duhamel integral (Fréchet derivative):
$$
\partial_1 e^{K(\theta)} = \int_0^1 e^{(1-s)K(\theta)} \sigma_x e^{sK(\theta)}\,\text{d}s.
$$

**Computational note:** In practice, you'd compute this using the block-matrix trick:
$$
L_{\exp}(K,\sigma_x)=\exp\begin{pmatrix}K&\sigma_x\\0&K\end{pmatrix}_{(1,2)},
$$
where the subscript means "take the upper-right $2\times 2$ block" of the $4\times 4$ exponential. This is how autodiff frameworks implement gradients through `expm`.

Now compute $\partial_1\psi$:
$$
\partial_1\psi = \frac{1}{Z(\theta)}\,\text{tr}\left(\partial_1 e^{K(\theta)}\right)
= \frac{1}{Z(\theta)}\int_0^1 \text{tr}\!\left(e^{(1-s)K}\sigma_x e^{sK}\right)\text{d}s.
$$

Use cyclicity of trace: $\text{tr}(ABC)=\text{tr}(CAB)$, so
$$
\text{tr}\!\left(e^{(1-s)K}\sigma_x e^{sK}\right) = \text{tr}\!\left(e^{K}\sigma_x\right).
$$
(The $s$-dependence cancels!)

Thus
$$
\partial_1\psi = \frac{1}{Z}\,\text{tr}(e^K \sigma_x) = \text{tr}(\rho\,\sigma_x) = \langle \sigma_x\rangle.
$$

So the expectation identity $\partial_i\psi=\langle F_i\rangle$ holds, but only after using Duhamel plus trace cyclicity.}

\slides{
**Duhamel formula:**

$$\partial_1 e^K = \int_0^1 e^{(1-s)K}\sigma_x e^{sK}\,\text{d}s$$

**Key trick:** trace cyclicity makes $s$ disappear:

$$\text{tr}(e^{(1-s)K}\sigma_x e^{sK})=\text{tr}(e^K\sigma_x)$$

**Result:** $\partial_1\psi=\langle\sigma_x\rangle$ ✓
}

\subsubsection{The BKM metric (quantum Fisher information)}

\notes{The Hessian $G_{ij}=\partial_i\partial_j\psi$ gives the Bogoliubov–Kubo–Mori metric.

For our qubit family,
$$
G_{11}=\partial_1^2\psi,\quad G_{12}=\partial_1\partial_2\psi,\quad G_{22}=\partial_2^2\psi.
$$

In the classical exponential family, the Fisher metric equals the covariance matrix of sufficient statistics:
$$
G_{ij}^\text{classical}=\text{Cov}(F_i,F_j).
$$

In the quantum case, the BKM metric is \emph{not} simply the covariance of $\sigma_x$ and $\sigma_z$. Instead, it involves operator orderings (Kubo–Mori inner product). The difference arises precisely because the operators don't commute.

For $\theta=0$ (the maximally mixed state $\rho=I/2$), the BKM metric simplifies and you can compute it explicitly:
$$
G_{ij}(0)=\frac{1}{2}\text{tr}(\sigma_i\sigma_j)=\frac{1}{2}\delta_{ij}.
$$
(This uses $\text{tr}(\sigma_i\sigma_j)=2\delta_{ij}$ and the fact that at $\theta=0$, the state is maximally mixed.)

Away from $\theta=0$, the metric is state-dependent and reflects the curvature of the quantum state space (the Bloch sphere).}

\slides{
**BKM metric (quantum Fisher):**

$$G_{ij}=\partial_i\partial_j\psi$$

**Classical:** $G_{ij}=\text{Cov}(F_i,F_j)$

**Quantum:** $G_{ij}$ involves operator orderings (Kubo–Mori), not just covariance

At $\theta=0$: $G_{ij}(0)=\frac{1}{2}\delta_{ij}$
}

\subsubsection{Summary: what noncommutativity changes}

\notes{This 2×2 example makes concrete what happens when you extend exponential families to the quantum setting:

1. **Structure stays the same**: You still have $\rho=e^{K-\psi}$, with $K=\sum_i\theta_i F_i$.
2. **Expectations from $\psi$ still work**: $\partial_i\psi=\langle F_i\rangle$, but the proof requires Duhamel + trace cyclicity.
3. **Derivatives of exponentials need Duhamel**: You can't pull $F_i$ down naively because $[F_i,K]\neq 0$.
4. **The metric is more subtle**: The BKM metric involves operator orderings, not just classical covariance.

For ML practitioners: if you can compute matrix exponentials and traces, you can work with quantum exponential families using exactly the same conceptual framework.}

\slides{
**Take-home from 2×2 example:**

1. Structure: $\rho=e^{K-\psi}$ (same as classical)
2. Expectations: $\partial_i\psi=\langle F_i\rangle$ (with Duhamel + trace trick)
3. Derivatives: need Duhamel (can't pull $F_i$ down naively)
4. Metric: BKM $\neq$ covariance (operator orderings matter)

If you can do matrix exp + trace, you can do quantum exp families!
}

\endif



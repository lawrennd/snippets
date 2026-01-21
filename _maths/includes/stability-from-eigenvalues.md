\ifndef{stabilityFromEigenvalues}
\define{stabilityFromEigenvalues}

\editme

\subsection{Stability Analysis from Eigenvalues}

\notes{For the linearised system $\dot{q} = Mq$, the stability of the equilibrium is completely determined by the eigenvalues of $M$.

**Recall:** The solution is $q(t) = e^{Mt} q(0)$, and if $M$ has eigendecomposition $M = V\Lambda V^{-1}$ with eigenvalues $\{\lambda_k\}$, then
$$
q(t) = \sum_k c_k e^{\lambda_k t} v_k,
$$
where $v_k$ are the eigenvectors and $c_k$ depend on initial conditions.

The behaviour depends on the **real part** of each eigenvalue

- $\text{Re}(\lambda_k) < 0$: Mode $k$ decays exponentially $\rightarrow$ **stable**
- $\text{Re}(\lambda_k) > 0$: Mode $k$ grows exponentially $\rightarrow$ **unstable**  
- $\text{Re}(\lambda_k) = 0$: Mode $k$ neither grows nor decays $\rightarrow$ **marginal**

For the equilibrium $\boldsymbol{\theta}^\ast$ to be **stable**, ALL eigenvalues must have negative real parts.}

\slides{
**Linearised Dynamics: $\dot{q} = Mq$**

Solution: $q(t) = e^{Mt}q(0)$

**Eigenvalue criterion:**

* $\text{Re}(\lambda_k) < 0$ $\rightarrow$ decay (stable)
* $\text{Re}(\lambda_k) > 0$ $\rightarrow$ growth (unstable)
* $\text{Re}(\lambda_k) = 0$ $\rightarrow$ marginal

**Stable equilibrium:** All $\text{Re}(\lambda_k) < 0$
}

\subsection{Types of Eigenvalues}

\notes{The structure of the eigenvalues tells us about the nature of the dynamics:

**Real eigenvalues**

- Pure exponential growth/decay
- No oscillations
- From symmetric matrices

**Complex eigenvalues** (come in conjugate pairs $\lambda, \bar{\lambda}$)

- Oscillatory behavior
- Frequency $\omega = |\text{Im}(\lambda)|$
- Decay/growth rate $\gamma = \text{Re}(\lambda)$
- From matrices with antisymmetric components

**Purely imaginary eigenvalues** ($\lambda = \pm i\omega$)

- Undamped oscillations
- From purely antisymmetric matrices
- Conservative (Hamiltonian) dynamics}

\slides{
**Eigenvalue Types**

**Real:** 
* Pure exponential
* From symmetric part

**Complex:** 
* Oscillations
* From antisymmetric part

**Imaginary:** 
* Undamped oscillations
* Pure Hamiltonian
}

\subsection{Connection to $S + A$ Decomposition}

\notes{For our GENERIC decomposition $M = S + A$ where $S$ is symmetric and $A$ is antisymmetric:

**Symmetric part $S$**

- Has real eigenvalues: $\lambda_k^{(S)} \in \mathbb{R}$
- Controls stability (growth vs decay)
- Negative eigenvalues $\rightarrow$ dissipation

**Antisymmetric part $A$**  

- Has purely imaginary eigenvalues: $\lambda_k^{(A)} \in i\mathbb{R}$
- Controls oscillation frequency
- Zero real part $\rightarrow$ no dissipation

**Combined system** $M = S + A$

- Eigenvalues are generally complex: $\lambda_k = \sigma_k + i\omega_k$
- Real part $\sigma_k$ from $S$ (dissipation)
- Imaginary part $\omega_k$ from $A$ (oscillation)
- Result: damped or growing oscillations

This enables the decomposition to cleanly separate the stability (real part) from the oscillatory behavior (imaginary part).}

\slides{
**$M = S + A$ Eigenvalues**

From $S$ (symmetric)

* Real eigenvalues
* Stability/dissipation

From $A$ (antisymmetric)

* Imaginary eigenvalues  
* Oscillation frequency

Combined

* Complex eigenvalues $\lambda = \sigma + i\omega$
* $\sigma$ from $S$, $\omega$ from $A$
* Damped oscillations
}

\subsection{Example: Damped Harmonic Oscillator}

\notes{The classic damped harmonic oscillator provides intuition
$$
\ddot{x} + 2\gamma\dot{x} + \omega_0^2 x = 0
$$
As a first-order system with $q = (x, \dot{x})^\top$:
$$
\dot{q} = \begin{pmatrix} 0 & 1 \\ -\omega_0^2 & -2\gamma \end{pmatrix} q = \underbrace{\begin{pmatrix} 0 & 0 \\ 0 & -2\gamma \end{pmatrix}}_{S} + \underbrace{\begin{pmatrix} 0 & 1 \\ -\omega_0^2 & 0 \end{pmatrix}}_{A} q
$$

Eigenvalues: $\lambda = -\gamma \pm \sqrt{\gamma^2 - \omega_0^2}$

**Three regimes**

- Underdamped ($\gamma < \omega_0$): $\lambda = -\gamma \pm i\sqrt{\omega_0^2 - \gamma^2}$ (damped oscillations)
- Critically damped ($\gamma = \omega_0$): $\lambda = -\gamma$ (fastest decay, no oscillation)
- Overdamped ($\gamma > \omega_0$): Two negative real eigenvalues (slow decay, no oscillation)

The antisymmetric part provides the oscillation frequency $\omega_0$, while the symmetric part provides the damping $\gamma$.}

\slides{
**Damped Oscillator**

$$
M = \underbrace{\begin{pmatrix} 0 & 0 \\ 0 & -2\gamma \end{pmatrix}}_{S} + \underbrace{\begin{pmatrix} 0 & 1 \\ -\omega_0^2 & 0 \end{pmatrix}}_{A}
$$

Eigenvalues: $\lambda = -\gamma \pm \sqrt{\gamma^2 - \omega_0^2}$

* Underdamped: Complex (oscillations)
* Critical: Real double (fastest decay)
* Overdamped: Two real (slow decay)
}

\notes{**Summary:** Eigenvalue analysis provides a complete picture of near-equilibrium behavior. The GENERIC decomposition $M = S + A$ makes the physical meaning transparent: $S$ controls stability through real parts, $A$ controls oscillations through imaginary parts.}
\endif

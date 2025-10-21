\ifndef{symmetricAntisymmetricDecomposition}
\define{symmetricAntisymmetricDecomposition}

\editme

\subsection{Matrix Decomposition: Symmetric and Antisymmetric Parts}

\notes{Any square matrix $M$ can be uniquely decomposed into symmetric and antisymmetric parts
$$
M = S + A
$$
where $S^\top = S$ (symmetric) and $A^\top = -A$ (antisymmetric or skew-symmetric).

**Unique decomposition:** Given $M$, the decomposition is unique:
$$
S = \frac{1}{2}(M + M^\top), \quad A = \frac{1}{2}(M - M^\top)
$$

**Verification:** 
$$
S + A = \frac{1}{2}(M + M^\top) + \frac{1}{2}(M - M^\top) = M \quad \checkmark
$$

**Symmetry check:**
$$
S^\top = \frac{1}{2}(M^\top + M) = S \quad \checkmark
$$
$$
A^\top = \frac{1}{2}(M^\top - M) = -\frac{1}{2}(M - M^\top) = -A \quad \checkmark
$$
}

\slides{
**Matrix Decomposition**

Any matrix $M = S + A$ where:

* $S = \frac{1}{2}(M + M^\top)$ (symmetric)
* $A = \frac{1}{2}(M - M^\top)$ (antisymmetric)

**Properties:**

* Unique decomposition
* $S^\top = S$, $A^\top = -A$
* Orthogonal in Frobenius inner product
}

\subsection{Physical Interpretation}

\notes{Why do we care about this decomposition? In dynamics $\dot{x} = Mx$, the two parts represent different aspects of the system.

**Symmetric part $S$:**
- Represents dissipation or gradient flow
- Changes the "energy" of the system: $\frac{\text{d}}{\text{d}t}(x^\top x) = 2x^\top Sx$
- Can increase or decrease norms
- Has real eigenvalues
- Example: Damping in mechanical systems

**Antisymmetric part $A$:**
- Represents conservative/Hamiltonian flow
- Preserves "energy": $x^\top A x = 0$ for all $x$
- Rotates without dissipation
- Has purely imaginary eigenvalues
- Example: Undamped oscillations

**Combined dynamics:**
The full system $\dot{x} = (S + A)x$ exhibits both:
- Dissipation (from $S$)
- Conservative rotation/oscillation (from $A$)

This is the essence of many physical systems: damped oscillators, thermodynamics, non-equilibrium dynamics.}

\slides{
**Physical Meaning**

For $\dot{x} = Mx = (S+A)x$:

**Symmetric $S$:**
* Dissipation/gradient flow
* Changes energy: $\frac{\text{d}}{\text{d}t}(\|x\|^2) \sim x^\top S x$
* Real eigenvalues

**Antisymmetric $A$:**
* Conservative/Hamiltonian flow
* Preserves energy: $x^\top A x = 0$
* Imaginary eigenvalues

**Together:** Damped oscillations + rotation
}

\subsection{Example: 2D System}

\notes{Consider a 2D matrix
$$
M = \begin{pmatrix} -1 & 2 \\ 0 & -1 \end{pmatrix}
$$
Decompose
$$
S = \frac{1}{2}\left(\begin{pmatrix} -1 & 2 \\ 0 & -1 \end{pmatrix} + \begin{pmatrix} -1 & 0 \\ 2 & -1 \end{pmatrix}\right) = \begin{pmatrix} -1 & 1 \\ 1 & -1 \end{pmatrix}
$$
$$
A = \frac{1}{2}\left(\begin{pmatrix} -1 & 2 \\ 0 & -1 \end{pmatrix} - \begin{pmatrix} -1 & 0 \\ 2 & -1 \end{pmatrix}\right) = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}
$$

**Interpretation:**
- $S$: Dissipative flow (eigenvalues: $0, -2$)
- $A$: Rotation matrix (eigenvalues: $\pm i$)
- Combined: Damped spiral toward origin}

\slides{
**2D Example**

$$
M = \begin{pmatrix} -1 & 2 \\ 0 & -1 \end{pmatrix} = \begin{pmatrix} -1 & 1 \\ 1 & -1 \end{pmatrix} + \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}
$$

* $S$: Dissipation (eigenvalues $0, -2$)
* $A$: Rotation (eigenvalues $\pm i$)
* Result: Damped spiral
}

\subsection{Inner Product Orthogonality}

\notes{An important property: $S$ and $A$ are orthogonal in the Frobenius inner product.

**Frobenius inner product:**
$$
\langle M_1, M_2 \rangle_F = \text{tr}(M_1^\top M_2) = \sum_{ij} [M_1]_{ij} [M_2]_{ij}
$$

**Orthogonality:**
$$
\langle S, A \rangle_F = \text{tr}(S^\top A) = \text{tr}(SA) = \text{tr}(-SA) = -\text{tr}(SA)
$$
Therefore $\text{tr}(SA) = 0$, so $\langle S, A \rangle_F = 0$.

This means the symmetric and antisymmetric parts contribute independently to the Frobenius norm
$$
\|M\|_F^2 = \|S\|_F^2 + \|A\|_F^2.
$$
This orthogonality is key to understanding how energy/information flows in dynamical systems.}

\slides{
**Orthogonality**

Frobenius inner product: $\langle M_1, M_2 \rangle_F = \text{tr}(M_1^\top M_2)$

**Key result:** $\langle S, A \rangle_F = 0$

Therefore:
$$
\|M\|_F^2 = \|S\|_F^2 + \|A\|_F^2
$$

* Independent contributions
* Fundamental for energy analysis
}

\notes{**Summary:** Every matrix splits uniquely into symmetric (dissipative) and antisymmetric (conservative) parts. This decomposition is fundamental in physics, where it separates irreversible processes (entropy production) from reversible ones (Hamiltonian dynamics).}

\endif



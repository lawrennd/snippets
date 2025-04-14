\ifndef{minimalEntropyDensityMatrixIntro}
\define{minimalEntropyDensityMatrixIntro}

\editme

\subsection{Variational Derivation of the Initial Curvature Structure}

\notes{We will determine constraints on the Fisher Information Matrix $G(\boldsymbol{\theta})$ that are consistent with the system's unfolding rules and internal information geometry. We follow Jaynes [@Jaynes-information57] in solving a variational problem that captures the allowed structure of the system's origin (minimal entropy) state.}

\newslide{Variational Derivation}
\slides{
- Determine constraints on Fisher Information Matrix $G(\boldsymbol{\theta})$
- Follow Jaynes' approach to solve variational problem
- Capture structure of system's minimal entropy state
}

\notes{@Hirschman-entropy57 established a connection between entropy and the Fourier transform, showing that the entropy of a function and its Fourier transform cannot both be arbitrarily small. This result, known as the Hirschman uncertainty principle, was later strengthened by Beckner [@Beckner-fourier75] who derived the optimal constant in the inequality. @Bialynicki-uncertainty75 extended these ideas to derive uncertainty relations for information entropy in wave mechanics

\notes{From these results we know that there are fundamental limits to how we express the entropy of position and its conjugate space simultaneously. These limits inspire us to focus on the *von Neumann entropy* so that our system respects the Hirschman uncertainty principle.}

\newslide{Uncertainty Principles}
\slides{
- Hirschman uncertainty principle: entropy of function and Fourier transform
- Beckner strengthened the inequality with optimal constant
- Bialynicki extended to information entropy in wave mechanics
- System respects these limits via von Neumann entropy
}

\notes{A density matrix has the form
$$
\rho(\boldsymbol{\theta}) = \frac{1}{Z(\boldsymbol{\theta})} \exp\left( \sum_i \theta_i H_i \right)
$$
where $Z(\boldsymbol{\theta}) = \mathrm{tr}\left[\exp\left( \sum_i \theta_i H_i \right)\right]$ and $\boldsymbol{\theta} \in \mathbb{R}^d$, $H_i$ are Hermitian observables.}

\newslide{Density Matrix Form}
\slides{
- $\rho(\boldsymbol{\theta}) = \frac{1}{Z(\boldsymbol{\theta})} \exp\left( \sum_i \theta_i H_i \right)$
- $Z(\boldsymbol{\theta}) = \mathrm{tr}\left[\exp\left( \sum_i \theta_i H_i \right)\right]$
- $\boldsymbol{\theta} \in \mathbb{R}^d$, $H_i$ are Hermitian observables
}

\notes{The von Neumman entropy is given by
$$
S[\rho] = -\text{tr} (\rho \log \rho)
$$
}
\notes{We now derive the minimal entropy configuration inspired by Jaynes's *free-form* variational approach. This enables us to derive the form of the *density matrix* directly from information-theoretic constraints [@Jaynes-information63].}

\newslide{Von Neumann Entropy}
\slides{
- $S[\rho] = -\text{tr} (\rho \log \rho)$
- Minimal entropy configuration via Jaynes' variational approach
- Derive density matrix from information-theoretic constraints
}

\endif 

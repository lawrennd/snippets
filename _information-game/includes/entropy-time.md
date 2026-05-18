\ifndef{entropyTime}
\define{entropyTime}

\editme

\subsection{Entropy Time}

\notes{The natural parameter space carries a preferred affine parameter, game time $\tau$, which tracks progress along the constrained flow. However, as the system approaches the LME origin, the natural parameters diverge ($\|\boldsymbol{\theta}\|\to\infty$) and the entropy production rate with respect to game time tends to zero. The origin is at infinite affine distance. This creates a degenerate parametrisation: infinite game time elapses while the system covers a finite range of entropy values.

The resolution is an *axiomatically distinguished reparametrisation*. An external clock is forbidden by information isolation. But there is one quantity internal to the game that provides a natural measure of progress: the entropy itself. We define *entropy time* $t$ by the condition that entropy production is constant [@Lawrence-origin26].}

\slidesincremental{
* Game time $\tau$: affine parameter, degenerates at origin
* $\|\boldsymbol{\theta}\|\to\infty$, entropy production $\to 0$
* Infinite game time to cover finite entropy range
* Need: an *internal* clock — external clocks forbidden by isolation
}

\subsection{Entropy Time}

\notes{Entropy time $t$ is defined by the condition
$$
\frac{\text{d}S}{\text{d}t} = c,
$$
for a fixed constant $c > 0$, where $S = -\mathrm{tr}(\rho\log\rho)$ is the von Neumann entropy. Different choices of $c$ correspond to affine rescalings of $t$ and leave the integral curves unchanged.

This is much stronger than entropy being monotonically increasing. Here the time parameter *is defined by* entropy production: one unit of $t$ corresponds to $c$ nats of entropy produced. $t$ is the unique reparametrisation (up to affine shift) for which entropy grows linearly.

The relationship to game time is
$$
\frac{\text{d}\tau}{\text{d}t} = \frac{c}{\boldsymbol{\theta}^\top G(\boldsymbol{\theta})\Pi_{\mathrm{marg}}(\boldsymbol{\theta})\boldsymbol{\theta}},
$$
which diverges as the origin is approached ($\boldsymbol{\theta}\to\infty$, metric degenerates), mapping the infinite affine-time approach to the boundary into a *finite* entropy-time interval [@Lawrence-origin26].}

\slides{
$$\frac{\text{d}S}{\text{d}t} = c \quad \text{(constant entropy production)}$$

* 1 unit of $t$ = $c$ nats of entropy produced
* Unique reparametrisation (up to affine shift) with this property
* External clock forbidden by isolation — entropy provides the clock
* Finite entropy-time interval replaces infinite affine-time approach
}

\subsection{Entropy Time is Axiomatically Distinguished}

\notes{The entropy time parametrisation is axiomatically distinguished in the sense of the inaccessible game: it is uniquely identifiable from within the game's axioms, without introducing any additional external choice. Information isolation forbids a background Newtonian time, a temperature scale, spatial coordinates, or a Hamiltonian. Entropy time requires none of these — it is defined purely by the constrained information dynamics and the BFL/Parzygnat information-loss functionals.

Crucially, the game does not assume an external time and then derive that entropy increases monotonically. Instead, it singles out a preferred parametrisation of the information flow in which the irreversible (dissipative) sector is uniformised. This is Jaynes's programme taken to its logical conclusion [@Jaynes-information57a,@Jaynes-minimum80]: take the conservation law exact, let the dynamics emerge, and measure progress by the entropy produced.}

\slidesincremental{
* No external clock, temperature, or Hamiltonian needed
* Axiomatically distinguished: uniquely specifiable from within the game
* Uniformises the irreversible (dissipative) sector
* Resolves the boundary degeneration of natural-parameter flow
* *Progress measured by entropy produced, not by an external tick*
}

\endif

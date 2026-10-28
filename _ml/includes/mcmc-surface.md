\ifndef{mcmcSurface}
\define{mcmcSurface}

\editme

\subsection{Sampling on a GP Energy Surface}

\notes{Metropolis--Hastings and Hamiltonian Monte Carlo both target a density
$p(\mathbf{q})\propto e^{-E(\mathbf{q})}$.  Here the energy $E$ is itself a draw
from a Gaussian process on $\mathbb{R}^2$, so the landscape is multimodal and
not a simple bowl.  That makes the contrast between a random-walk proposal and
a gradient-informed leapfrog proposal visible in the plane.}

\notes{The covariance is the product of an exponentiated quadratic and a
degree-2 polynomial (quadratic) kernel,
$$
k(\mathbf{x},\mathbf{x}')
=
\sigma_{\mathrm{eq}}^{2}\,
\exp\!\Bigl(-\tfrac{1}{2}\ell^{-2}\|\mathbf{x}-\mathbf{x}'\|^{2}\Bigr)
\cdot
\alpha\bigl(\mathbf{x}^{\top}\Sigma\mathbf{x}'+b\bigr)^{2},
$$
with correlated quadratic metric
$\Sigma=\begin{bmatrix}1&\rho\\\rho&1\end{bmatrix}$.
The off-diagonal $\rho$ tilts the quadratic feature geometry, so valleys in
$E$ are not axis-aligned.  The surface shown is one sample from
$\mathcal{GP}(0,k)$ on a fine inducing grid, bilinearly interpolated for the
samplers.}

\slides{MH vs HMC on $E\sim\mathcal{GP}(0,\,k_{\mathrm{EQ}}\times k_{\mathrm{quad}})$.}

\slidesincremental{
* Target $p(\mathbf{q})\propto e^{-E(\mathbf{q})}$; $E$ drawn from a GP
* $k = $ exponentiated quadratic $\times$ correlated quadratic
* MH: isotropic random-walk proposals
* HMC: leapfrog on $H=E+K$, Metropolis correction on $\Delta H$
}

\newslide{}

\figure{\html{
<div style="width:100%;max-width:820px;font-family:sans-serif;font-size:0.82em">
<div style="display:flex;gap:14px;flex-wrap:wrap;align-items:flex-start">

<div style="flex:1 1 420px;min-width:0">
<canvas id="mcmc-surface-canvas" width="560" height="560"
  style="border:1px solid #444;display:block;width:100%;height:auto;border-radius:4px;background:#1a1a2e"></canvas>
<div id="mcmc-surface-status" style="margin-top:4px;color:#888;font-size:0.85em">Initialising…</div>
<div id="mcmc-surface-stats" style="margin-top:2px;font-family:monospace;font-size:0.8em;color:#bbb"></div>
</div>

<div style="flex:0 1 260px;min-width:200px;display:flex;flex-direction:column;gap:8px">

<div>
<strong>Algorithm</strong>
<div style="display:flex;gap:12px;margin-top:4px">
<label style="cursor:pointer"><input type="radio" name="mcmc-surface-alg" id="mcmc-surface-alg-mh" checked> Metropolis–Hastings</label>
<label style="cursor:pointer"><input type="radio" name="mcmc-surface-alg" id="mcmc-surface-alg-hmc"> HMC</label>
</div>
</div>

<div style="display:flex;flex-wrap:wrap;gap:4px">
<button id="mcmc-surface-play">Play</button>
<button id="mcmc-surface-step">Step</button>
<button id="mcmc-surface-reset">Reset chain</button>
<button id="mcmc-surface-resample">New energy</button>
</div>

<label>Seed
<input type="number" id="mcmc-surface-seed" value="42" style="width:5em;margin-left:6px">
</label>

<label>Quadratic correlation ρ
<span id="mcmc-surface-rho-val" style="float:right;font-family:monospace">0.60</span>
<input type="range" id="mcmc-surface-rho" min="-0.9" max="0.9" step="0.05" value="0.6" style="width:100%">
</label>

<label>EQ lengthscale ℓ
<span id="mcmc-surface-ell-val" style="float:right;font-family:monospace">0.90</span>
<input type="range" id="mcmc-surface-ell" min="0.3" max="2.0" step="0.05" value="0.9" style="width:100%">
</label>

<label>MH proposal σ
<span id="mcmc-surface-mh-sigma-val" style="float:right;font-family:monospace">0.15</span>
<input type="range" id="mcmc-surface-mh-sigma" min="0.02" max="0.8" step="0.01" value="0.15" style="width:100%">
</label>

<label>HMC step size ε
<span id="mcmc-surface-hmc-eps-val" style="float:right;font-family:monospace">0.060</span>
<input type="range" id="mcmc-surface-hmc-eps" min="0.005" max="0.2" step="0.005" value="0.06" style="width:100%">
</label>

<label>HMC leapfrog steps L
<span id="mcmc-surface-hmc-L-val" style="float:right;font-family:monospace">20</span>
<input type="range" id="mcmc-surface-hmc-L" min="1" max="40" step="1" value="20" style="width:100%">
</label>

<label>Steps per frame
<span id="mcmc-surface-speed-val" style="float:right;font-family:monospace">2</span>
<input type="range" id="mcmc-surface-speed" min="1" max="20" step="1" value="2" style="width:100%">
</label>

<div style="font-size:0.78em;color:#888;line-height:1.35;margin-top:4px">
White trail: accepted positions.  For HMC, green/red curves are leapfrog
proposals (accepted / rejected).  Dark / purple is low energy (preferred by
$e^{-E}$); yellow is high energy.
</div>

</div>
</div>

\include{_scripts/includes/mcmc-surface-js.md}
</div>
}}{Interactive Metropolis--Hastings and Hamiltonian Monte Carlo on a 2D
energy surface drawn from a Gaussian process with covariance
$k_{\mathrm{EQ}}\times k_{\mathrm{quad}}$ (correlated quadratic).  Toggle the
algorithm, adjust $\rho$ and $\ell$, and resample the energy to see how
random-walk MH and leapfrog HMC explore the same target.}{mcmc-gp-surface}

\notes{Metropolis--Hastings proposes a local isotropic Gaussian step and
accepts with probability $\min(1,e^{-\Delta E})$.  On a rough GP energy it
mixes slowly across ridges.  HMC invents momentum, integrates Hamilton's
equations with leapfrog for $L$ steps of size $\varepsilon$, and corrects
discretisation error with a Metropolis test on the Hamiltonian
$H=E+K$.  Trajectories follow level structure of $E$ and typically move farther
per accepted proposal when gradients are informative --- the same teaching
point as in the loss-to-Hamiltonian development, now on a non-quadratic
surface.}

\endif

\ifndef{jointMarginalEntropy}
\define{jointMarginalEntropy}

\editme

\subsection{Joint and Marginal Entropy}

\notes{Each particle in the billiard gas carries two velocity components, $v_x$ and $v_y$.  We can describe the state of the gas at three levels of detail:

* **Marginal entropy $H(v_x)$** — how much uncertainty is there about a single particle's horizontal velocity, ignoring its vertical velocity entirely?
* **Marginal entropy $H(v_y)$** — likewise for the vertical velocity.
* **Joint entropy $H(v_x, v_y)$** — how much uncertainty is there about a particle's full velocity vector?

The joint entropy is never smaller than either marginal, but it can be less than their sum.  Precisely, Shannon's *subadditivity* inequality states
$$
H(v_x, v_y) \leq H(v_x) + H(v_y),
$$
with equality if and only if $v_x$ and $v_y$ are statistically independent.

The gap is the **mutual information**
$$
I(v_x;\, v_y) = H(v_x) + H(v_y) - H(v_x,\, v_y) \geq 0,
$$
which measures how much knowing one velocity component reduces uncertainty about the other.

The gas starts with all particles moving straight down at the same speed (identical to the entropy-billiards initialisation), so both marginal and joint entropy begin near zero.  A tiny random horizontal perturbation breaks the symmetry so that collisions gradually thermalise the gas and entropy rises.

Notice what is and is not conserved.  The *mean kinetic energy* $\langle v^2 \rangle = \langle v_x^2 + v_y^2 \rangle$ is conserved by elastic collisions, while $H(v_x) + H(v_y)$ is *not* conserved, it climbs from zero to its equilibrium value.  At equilibrium the joint distribution factorises as $p(v_x,v_y)=p(v_x) p(v_y)$, so $I(v_x;v_y) \to 0$ and $H(v_x,v_y) \to H(v_x)+H(v_y)$.}

\slides{
**Joint vs Marginal Entropy:**

$$
H(v_x, v_y) \leq H(v_x) + H(v_y)
$$

* Equality ↔ $v_x \perp v_y$ (statistical independence)
* Mutual information $I(v_x;v_y) = H(v_x)+H(v_y)-H(v_x,v_y)$
* Start: all balls same velocity $\rightarrow$ all entropies near zero
* Equilibrium: $I \to 0$, entropies rise to Maxwell–Boltzmann values

**What is conserved?**

* Kinetic energy $\langle v^2 \rangle$  by elastic collisions
* $H(v_x) + H(v_y)$ — no, rises from zero to equilibrium
* Connection: in the thermodynamic limit, energy conservation \(\parallel\) marginal entropy conservation
}

\figure{
<div style="width:100%;max-width:800px">
<canvas id="jointentropy-canvas" width="800" height="450" style="border:1px solid black;display:block;width:100%"></canvas>
<table style="width:100%;margin-top:8px;border-collapse:collapse;font-family:monospace;font-size:0.9em">
<tr><td style="padding:3px 8px">\(H(v_x)\) marginal (bits):</td><td><output id="jointentropy-hx">0.000</output></td></tr>
<tr><td style="padding:3px 8px">\(H(v_y)\) marginal (bits):</td><td><output id="jointentropy-hy">0.000</output></td></tr>
<tr style="border-top:1px solid #ccc"><td style="padding:3px 8px">\(H(v_x) + H(v_y)\) (bits):</td><td><output id="jointentropy-hxphy">0.000</output></td></tr>
<tr><td style="padding:3px 8px">\(H(v_x,\,v_y)\) joint (bits):</td><td><output id="jointentropy-hxy">0.000</output></td></tr>
<tr style="border-top:1px solid #ccc;font-weight:bold"><td style="padding:3px 8px">\(I(v_x;\,v_y)\) mutual info (bits):</td><td><output id="jointentropy-mi">0.000</output></td></tr>
<tr style="border-top:1px solid #ccc"><td style="padding:3px 8px">Mean KE per ball (conserved):</td><td><output id="jointentropy-ke">0.000</output></td></tr>
</table>
<div style="margin-top:6px;display:flex;gap:4px">
<button id="jointentropy-newball">Reset</button>
<button id="jointentropy-pause">Pause / Resume</button>
<button id="jointentropy-skip">Skip 1000s</button>
</div>
</div>

\include{_scripts/includes/jointentropy-js.md}}{The billiard gas starts with all particles moving in the same direction (maximally correlated, near-zero entropy).  Elastic collisions thermalise the gas: watch all entropies rise while the mean kinetic energy stays flat.  At equilibrium the mutual information \(I(v_x;v_y)\) falls to zero and the joint entropy equals the sum of the marginals.  Kinetic energy is conserved; marginal entropy sum is not — they only become equivalent in the thermodynamic limit.}{joint-marginal-entropy-js}

\endif

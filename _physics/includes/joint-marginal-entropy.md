\ifndef{jointMarginalEntropy}
\define{jointMarginalEntropy}

\editme

\subsection{Joint and Marginal Entropy}

\notes{Each particle in the billiard gas carries two velocity components, \(v_x\) and \(v_y\).  We can describe the state of the gas at three levels of detail:

* **Marginal entropy \(H(v_x)\)** — how much uncertainty is there about a single particle's horizontal velocity, ignoring its vertical velocity entirely?
* **Marginal entropy \(H(v_y)\)** — likewise for the vertical velocity.
* **Joint entropy \(H(v_x, v_y)\)** — how much uncertainty is there about a particle's full velocity vector?

The joint entropy is never smaller than either marginal, but it can be less than their sum.  Precisely, Shannon's *subadditivity* inequality states
$$
H(v_x, v_y) \leq H(v_x) + H(v_y),
$$
with equality if and only if \(v_x\) and \(v_y\) are statistically independent.

The gap is the **mutual information**
$$
I(v_x;\, v_y) = H(v_x) + H(v_y) - H(v_x,\, v_y) \geq 0,
$$
which measures how much knowing one velocity component reduces uncertainty about the other.

The billiard gas below starts with all particles moving in a circle — every particle has the same speed but a different direction.  The velocity components \(v_x = r\sin\theta\) and \(v_y = r\cos\theta\) are therefore strongly correlated (they lie on a circle in velocity space), so \(I(v_x; v_y)\) is initially large.

As elastic collisions randomise the velocities the distribution relaxes toward the Maxwell–Boltzmann equilibrium, where the joint distribution factorises as \(p(v_x,v_y)=p(v_x)\,p(v_y)\).  Watch \(I(v_x;v_y)\) fall toward zero while \(H(v_x,v_y)\) climbs toward \(H(v_x) + H(v_y)\).}

\slides{
**Joint vs Marginal Entropy:**

$$H(v_x, v_y) \leq H(v_x) + H(v_y)$$

* Equality ↔ \(v_x \perp v_y\) (statistical independence)
* Mutual information \(I(v_x;v_y) = H(v_x)+H(v_y)-H(v_x,v_y)\)
* Billiards: correlated start → \(I\) large; equilibrium → \(I \to 0\)
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
</table>
<div style="margin-top:6px;display:flex;gap:4px">
<button id="jointentropy-newball">Reset</button>
<button id="jointentropy-pause">Pause / Resume</button>
<button id="jointentropy-skip">Skip 1000s</button>
</div>
</div>

\include{_scripts/includes/jointentropy-js.md}}{The billiard gas starts with circularly-distributed velocities so that \(v_x\) and \(v_y\) are correlated.  As elastic collisions thermalise the gas the mutual information \(I(v_x;v_y)\) falls toward zero, demonstrating that at equilibrium the velocity components become statistically independent and the joint entropy equals the sum of the marginals.}{joint-marginal-entropy-js}

\endif

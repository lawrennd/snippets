\ifndef{multigameEntropy}
\define{multigameEntropy}

\editme

\subsection{Thermalisation from Different Initial Conditions}

\notes{This simulation places exactly nine billiard balls on a 3×3 grid, each
coloured according to its position.  The **3×3 histogram grid** tracks, for
each ball, the cumulative 2-D velocity distribution $(v_x, v_y)$ it has
visited since the last reset.

The **entropy** $H(v_x, v_y)$ for each ball is shown in the top-left of
its panel.  At the start, when all balls move identically, every panel shows
a single bright dot near zero entropy.  As elastic collisions redistribute
energy the dots spread outward, tracing the Maxwell–Boltzmann circle, and
entropy climbs toward its maximum.

The coloured dot in the top-right corner of each panel matches the ball's
colour on the main canvas, making it easy to follow individual balls.

Use the **Display** dropdown to switch between the 2D joint distribution
$p(v_x, v_y)$ (heatmap) and the two 1D marginals $p(v_x)$ and $p(v_y)$
overlaid as bar charts.  Both marginals are expected to converge to the same
symmetric distribution; the coloured bars show $p(v_x)$ (ball colour) and
the dark outline shows $p(v_y)$.  The entropy labels $H_x$ and $H_y$ confirm
that the two components thermalise at the same rate.

Use the **Initialisation** dropdown to choose how the balls start:

| Option | Description |
|---|---|
| From top ↓ | All balls move downward at the same speed |
| From bottom ↑ | All balls move upward |
| From left → | All balls move rightward |
| From right ← | All balls move leftward |
| Clockwise ↻ | Each ball moves tangentially clockwise around the canvas centre |
| Counter-CW ↺ | Each ball moves tangentially counter-clockwise |

For the four directional cases all nine histograms start at the same point,
yet rapidly diverge and then converge to the same circular distribution.
For the propellor cases adjacent balls start with very different velocity
directions — the corner and edge balls even start at nearly opposite
velocities — and yet all nine panels converge to the same equilibrium blob.

This is a direct demonstration of **ergodicity**: the long-run distribution
of each ball's velocity is independent of the initial conditions and identical
for all balls, even though the *path* to equilibrium differs.}

\slides{**Thermalisation from Different Initial Conditions**

* 9 balls on a 3×3 grid; each histogram tracks one ball's velocity history
* Entropy $H(v_x, v_y)$ per ball: near zero → equilibrium value
* **Ergodicity**: all 9 panels converge to the same Maxwell–Boltzmann circle
* Propellor init: adjacent balls start with opposite velocities, yet equilibrate}

\figure{
<div style="width:100%;max-width:1020px">
<div style="display:flex;gap:8px;flex-wrap:wrap;align-items:flex-start">
<div style="flex:1 1 260px">
<canvas id="multigame-canvas" width="500" height="360"
  style="border:1px solid black;display:block;width:100%"></canvas>
</div>
<div style="flex:1 1 260px">
<canvas id="multigame-grid" width="480" height="480"
  style="border:1px solid #bbb;display:block;width:100%"></canvas>
</div>
</div>
<div style="margin-top:8px;display:flex;gap:6px;align-items:center;flex-wrap:wrap">
<button id="multigame-reset">Reset</button>
<button id="multigame-pause">Pause / Resume</button>
<button id="multigame-skip">Skip 1000s</button>
<span style="font-family:sans-serif;font-size:0.9em;margin-left:6px">
Initialisation:
<select id="multigame-init">
<option value="top">From top ↓</option>
<option value="bottom">From bottom ↑</option>
<option value="left">From left →</option>
<option value="right">From right ←</option>
<option value="cw">Clockwise ↻</option>
<option value="ccw">Counter-CW ↺</option>
</select>
</span>
<span style="font-family:sans-serif;font-size:0.9em;margin-left:6px">
Display:
<select id="multigame-display">
<option value="2d">2D joint p(vₓ,vᵧ)</option>
<option value="1d">1D marginals p(vₓ) &amp; p(vᵧ)</option>
</select>
</span>
</div>
</div>

\include{_scripts/includes/multigame-js.md}}{Nine billiard balls on a 3×3 grid.
The histogram grid tracks each ball's cumulative $(v_x, v_y)$ velocity
distribution.  Entropy per ball rises from near zero (single bright dot at
the initial velocity) to the Maxwell–Boltzmann value as collisions
thermalise the gas.  Use the Initialisation dropdown to compare directional
starts (all balls move the same way) with propellor starts (adjacent balls
move in opposite directions): all initial conditions converge to the same
equilibrium, demonstrating ergodicity.}{multigame-entropy}

\endif

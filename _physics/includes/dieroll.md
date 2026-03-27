\ifndef{dieroll}
\define{dieroll}

\editme

\subsection{Die Roll Simulation}

\notes{This simulation illustrates the maximum entropy principle through Jaynes' dice
example [@Jaynes-information57]. A fair die has expected outcome 3.5; the
*Jaynes example* asks: if we know only that the average outcome is 4.5, what
probability distribution $P_n$ over the six faces should we assign?}

\notes{The answer is the maximum-entropy distribution subject to the constraint
$\sum_{n=1}^6 n P_n = 4.5$, which belongs to the exponential family:
\begin{align}
P_n = \frac{e^{\lambda n}}{Z(\lambda)}, \qquad Z(\lambda) = \sum_{n=1}^6 e^{\lambda n}
\end{align}
where $\lambda > 0$ is chosen so the mean constraint is satisfied.  This
avoids any unwarranted assumption beyond the available data.}

\slides{
* Click the die (or Roll button) to sample outcomes
* Histogram shows empirical vs theoretical frequencies
* Adjust outcome weights to explore non-uniform distributions
* **Jaynes preset**: max-entropy distribution with mean 4.5
}

\newslide{}

\figure{
<div style="width:100%;max-width:780px;font-family:sans-serif;font-size:0.82em">
<div style="display:flex;gap:16px;flex-wrap:wrap;align-items:flex-start">

<div style="display:flex;flex-direction:column;align-items:center;gap:6px;min-width:160px">
<canvas id="dieroll-die" width="150" height="150"
 style="display:block;cursor:pointer"></canvas>
<div style="font-size:0.75em;color:#888;text-align:center">click die or button to roll</div>
<div style="display:flex;gap:6px">
<button id="dieroll-roll">Roll</button>
<button id="dieroll-roll100">Roll ×100</button>
</div>
<div style="text-align:center;line-height:1.6;font-size:0.85em">
Rolls: <strong id="dieroll-count">0</strong><br>
Sample mean: <span id="dieroll-mean">—</span><br>
H(p): <span id="dieroll-entropy" style="color:#2ecc71">—</span>
</div>
<button id="dieroll-reset">Reset history</button>
</div>

<div style="flex:1;min-width:280px">
<canvas id="dieroll-hist" width="500" height="210"
style="display:block;width:100%;height:auto;border-radius:6px"></canvas>
<div style="margin-top:6px">
<div style="font-style:italic;margin-bottom:6px;color:#888">
Outcome weights (auto-normalised to probabilities)
</div>
<div id="dieroll-sliders"></div>
<div style="margin-top:8px;display:flex;gap:6px;flex-wrap:wrap">
<button id="dieroll-uniform">Uniform (mean 3.5)</button>
<button id="dieroll-jaynes">Jaynes: mean 4.5</button>
<button id="dieroll-low">Low-biased: mean 2</button>
</div>
</div>
</div>

</div>
</div>

\include{_scripts/includes/dieroll-js.md}}{Interactive die-roll simulation.
Click the die or press Roll to sample from the configured distribution.
The histogram shows empirical relative frequencies (coloured bars) overlaid
on the theoretical probabilities (dashed outlines).  Use the sliders to set
arbitrary outcome weights, or click a preset to load the uniform distribution
(mean 3.5), the Jaynes maximum-entropy distribution (mean 4.5), or a
low-biased distribution (mean 2).}{dieroll-simulation}

\endif

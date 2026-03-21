\ifndef{maxwellsDemonShort}
\define{maxwellsDemonShort}

\editme

\subsection{Maxwell's Demon}

\figure{\includediagramclass{\diagramsDir/physics/maxwells-demon}{100%}}{Maxwell's demon opens and closes a door which allows fast particles to pass from left to right and slow particles to pass from right to left. This makes the left hand side colder than the right.}{maxwells-demon}

\newslide{}

\figure{
<div style="display:flex;flex-wrap:wrap;gap:8px;align-items:flex-start">
  <div style="flex:1 1 400px;min-width:0">
    <canvas id="maxwell-canvas" width="700" height="500" style="border:1px solid black;display:block;width:100%"></canvas>
  </div>
  <div style="flex:0 1 280px;min-width:0">
    <div>Velocity-bin entropy: <output id="maxwell-entropy"></output></div>
    <div id="maxwell-histogram-canvas" style="width:100%;height:250px"></div>
  </div>
</div>
<div style="margin-top:4px;display:flex;flex-wrap:wrap;gap:4px">
<button id="maxwell-newball">New Ball</button>
<button id="maxwell-pause">Pause</button>
<button id="maxwell-skip">Skip 1000s</button>
<button id="maxwell-histogram">Histogram</button>
</div>

\include{_scripts/includes/maxwell-js.md}
}{Maxwell's Demon. The demon decides balls are either cold (blue) or hot (red) according to their velocity. Balls are allowed to pass the green membrane from right to left only if they are cold, and from left to right only if they are hot. The displayed entropy is the Shannon entropy of the velocity histogram (a coarse-grained proxy, not full thermodynamic entropy).}{maxwells-demon}

\endif
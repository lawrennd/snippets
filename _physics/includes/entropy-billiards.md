\ifndef{entropyBilliards}
\define{entropyBilliards}

\editme

\subsection{Entropy Billiards}

\figure{
<div style="display:flex;flex-wrap:wrap;gap:8px;align-items:flex-start">
  <div style="flex:1 1 400px;min-width:0">
    <canvas id="multiball-canvas" width="700" height="500" style="border:1px solid black;display:block;width:100%"></canvas>
  </div>
  <div style="flex:0 1 280px;min-width:0;display:flex;flex-direction:column;gap:6px">
    <div>Velocity-bin entropy: <output id="multiball-entropy"></output></div>
    <div id="multiball-histogram-canvas" style="width:100%;height:250px"></div>
    <div style="display:flex;flex-wrap:wrap;gap:4px">
      <button id="multiball-newball">New Ball</button>
      <button id="multiball-pause">Pause</button>
      <button id="multiball-skip">Skip 1000s</button>
      <button id="multiball-histogram">Histogram</button>
    </div>
  </div>
</div>

\include{_scripts/includes/multiball-js.md}}{Bernoulli's simple kinetic models of gases assume that the molecules of air operate like billiard balls. The displayed entropy is the Shannon entropy of the observed velocity histogram (a coarse-grained proxy, not full thermodynamic entropy).}{entropy-billiards-js}


\endif

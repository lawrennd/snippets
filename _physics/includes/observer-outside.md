\ifndef{observerOutside}
\define{observerOutside}

\editme

\subsection{The Observer Outside the System}

\notes{In classical physics the observer stands *outside* the system and watches.
The act of watching is passive: the observer gathers information without
disturbing the gas.  Here we make that observer explicit — a single eye that
tracks the centroid of all nine balls.  Its gaze follows the collective motion
of the gas, but it changes nothing inside the box.}

\notes{Notice how the pupil drifts quietly from side to side as the balls
thermalise.  Early on, when all nine balls move together in the same direction,
the eye makes a decisive sweep across the canvas.  As collisions disperse the
balls the centroid settles near the centre and the eye barely moves — the gas
has become, in a sense, *uninteresting* to the observer.  High entropy means
the observer has nothing much to track.}

\slides{**The Observer Outside**

* Classical observer watches without disturbing the gas.
* Pupil tracks the centroid of all balls.
* As entropy rises, the centroid stills — nothing left to follow.
}

\newslide{}
\figure{
<div style="width:100%;max-width:1020px">
<div style="display:flex;gap:8px;flex-wrap:wrap;align-items:flex-start">
<div style="flex:1 1 260px">
<canvas id="observer-outside-canvas" width="500" height="360"
  style="border:1px solid black;display:block;width:100%"></canvas>
</div>
<div style="flex:1 1 260px">
<canvas id="observer-outside-eye" width="480" height="480"
  style="border:1px solid #bbb;display:block;width:100%"></canvas>
</div>
</div>
<div style="margin-top:8px;display:flex;gap:6px;align-items:center;flex-wrap:wrap">
<button id="observer-outside-reset">Reset</button>
<button id="observer-outside-pause">Pause / Resume</button>
<button id="observer-outside-skip">Skip 1000s</button>
<span style="font-family:sans-serif;font-size:0.9em;margin-left:6px">
Initialisation:
<select id="observer-outside-init">
<option value="top">From top ↓</option>
<option value="bottom">From bottom ↑</option>
<option value="left">From left →</option>
<option value="right">From right ←</option>
<option value="cw">Clockwise ↻</option>
<option value="ccw">Counter-CW ↺</option>
</select>
</span>
</div>
</div>

\include{_scripts/includes/observer-outside-js.md}}{Nine billiard balls with a classical observer eye to the right.  The
pupil tracks the ball centroid: ordered initial conditions give a decisive
sweep of the gaze; thermalised equilibrium leaves it nearly motionless.  The
observer watches without perturbing the gas.}{observer-outside}

\endif

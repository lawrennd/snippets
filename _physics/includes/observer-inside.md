\ifndef{observerInside}
\define{observerInside}

\editme

\subsection{The Observer Inside the System}

\notes{What happens if we put the observer *inside* the box?  In classical
mechanics the answer is simple: the observer becomes part of the system.  The
gas molecules no longer pass freely — they bounce off the observer just like
they bounce off the walls.  The observer is now a *physical object* that the
system interacts with.}

\notes{The eye in the centre of the box is no longer passive.  Balls collide
with it, transfer momentum, and scatter in new directions.  The observer's
presence reshapes the entire trajectory of the gas.  Yet the eye still tries
to track the ball centroid — watch the pupil dart nervously as balls come
flying in from all directions.}

\notes{This is, of course, a joke — but a pointed one.  The moment the observer
enters the system, measurement and dynamics become inseparable.  The observer
cannot help but disturb what it is trying to observe.  This is the origin of
the *measurement problem* that troubles quantum mechanics: in quantum theory,
unlike in classical mechanics, there is no principled way to draw a clean
boundary between observer and observed.}

\slides{**The Observer Inside**

* Observer enters the box — becomes a physical obstacle.
* Balls bounce off the eye; pupil tracks the centroid nervously.
* *Moral:* once inside, the observer cannot help but disturb the system.
}

\newslide{}
\figure{
<div style="width:100%;max-width:700px">
<canvas id="observer-inside-canvas" width="640" height="420"
  style="border:1px solid black;display:block;width:100%"></canvas>
<div style="margin-top:8px;display:flex;gap:6px;align-items:center;flex-wrap:wrap">
<button id="observer-inside-reset">Reset</button>
<button id="observer-inside-pause">Pause / Resume</button>
<span style="font-family:sans-serif;font-size:0.9em;margin-left:6px">
Initialisation:
<select id="observer-inside-init">
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

\include{_scripts/includes/observer-inside-js.md}}{Nine billiard balls with the observer eye placed as an obstacle in the
centre of the box.  Balls bounce off the eye elastically.  The pupil tracks
the ball centroid — and flinches as they arrive.  The observer is no longer
passive: its presence changes the trajectories of everything it was trying to
watch.}{observer-inside}

\endif

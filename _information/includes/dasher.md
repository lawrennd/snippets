\ifndef{dasher}
\define{dasher}

\editme

\subsection{Dasher: Arithmetic Coding as Interface}

\notes{Dasher is a writing interface invented by David MacKay [@MacKay-dasher98]
that makes the connection between arithmetic coding and character prediction
viscerally concrete.  The key insight: if we arrange a character set
vertically with each character occupying space proportional to its
probability, then *selecting a character* is equivalent to *zooming into
its interval* in the arithmetic code.

Moving the mouse to the right zooms toward whichever letter the cursor
is pointing at.  Because common letters (e, t, a, space) have large
probability, they occupy large screen area — they are easy to aim at.
Rare letters (q, z, x) have tiny probability, occupy tiny screen area,
and are correspondingly hard to hit.  Ease of selection equals
low information content, which equals efficiency.

After typing "th", notice how 'e' swells to dominate the display;
after "q", 'u' fills almost the entire screen.  The visualisation makes
the language model's predictions tangible.}

\slides{
* Letters sized by P(char | context) — large target = common = cheap
* Move pointer **right** of centre: boxes enlarge and stream **left**
* Move pointer **left** of centre to zoom out / unwrite
* Character written when its box crosses the centre crosshair
* *Ease of selection ∝ probability ∝ 1 / information cost*
}

\newslide{}

\figure{\html{
<div style="width:100%;font-family:'Courier New',monospace;font-size:0.85em">

<div style="display:flex;justify-content:space-between;align-items:center;gap:8px;
            padding:6px 14px;background:#131320;border-bottom:1px solid #2a2a3e">
  <div style="display:flex;align-items:center;gap:12px;min-width:0;flex:1">
    <span style="color:#4ecdc4;letter-spacing:3px;font-size:14px">DASHER</span>
    <span style="color:#404068;font-style:italic;font-size:10px;
                 overflow:hidden;text-overflow:ellipsis;white-space:nowrap">
      screen height ∝ probability · boxes stream left across the crosshair
    </span>
  </div>
  <div style="display:flex;flex-wrap:wrap;gap:6px;flex-shrink:0">
    <button id="dasher-pause"
      style="background:#1a1a2e;border:1px solid #2a2a3e;color:#505080;
             padding:3px 10px;cursor:pointer;font-family:inherit;font-size:11px;
             border-radius:3px">Go</button>
    <button id="dasher-copy"
      style="background:#1a1a2e;border:1px solid #2a2a3e;color:#505080;
             padding:3px 10px;cursor:pointer;font-family:inherit;font-size:11px;
             border-radius:3px">Copy</button>
    <button id="dasher-reset"
      style="background:#1a1a2e;border:1px solid #2a2a3e;color:#505080;
             padding:3px 10px;cursor:pointer;font-family:inherit;font-size:11px;
             border-radius:3px">Reset</button>
  </div>
</div>

<div style="display:flex;align-items:center;gap:12px;padding:5px 14px;
            background:#0f0f1e;border-bottom:1px solid #1e1e32;min-height:34px">
  <div style="font-size:9px;color:#404068;flex-shrink:0">TYPED:</div>
  <div id="dasher-text"
    style="font-size:16px;color:#4ecdc4;letter-spacing:2px;flex:1;
           overflow:hidden;text-overflow:ellipsis;white-space:nowrap">▋</div>
  <div style="display:flex;flex-wrap:wrap;gap:6px;flex-shrink:0">
    <span style="background:#131320;border:1px solid #2a2a3e;border-radius:3px;
                 padding:2px 7px;font-size:11px;color:#505080;white-space:nowrap">
      bits: <span id="dasher-bits" style="color:#ffd93d">0.0</span></span>
    <span style="background:#131320;border:1px solid #2a2a3e;border-radius:3px;
                 padding:2px 7px;font-size:11px;color:#505080;white-space:nowrap">
      avg: <span id="dasher-avgbits" style="color:#ffd93d">—</span> b/ch</span>
    <span style="background:#131320;border:1px solid #2a2a3e;border-radius:3px;
                 padding:2px 7px;font-size:11px;color:#505080;white-space:nowrap">
      H(next): <span id="dasher-entropy" style="color:#ffd93d">—</span></span>
  </div>
</div>

<div style="position:relative;width:min(100%,480px);height:480px;margin:0 auto;
            cursor:crosshair;overflow:hidden">
  <canvas id="dasher-canvas" width="480" height="480"
    style="display:block;width:100%;height:100%"></canvas>
</div>

<div style="padding:5px 14px;background:#0f0f1e;border-top:1px solid #1e1e32;
            font-size:9px;color:#303055;text-align:center">
  <strong style="color:#4ecdc460">Click</strong> or <strong style="color:#4ecdc460">Space</strong>
  to Go/Pause ·
  <strong style="color:#4ecdc460">Copy</strong> extracts text ·
  pointer right zooms · left zooms out ·
  Backspace unwrites · Escape resets
</div>

</div>

\include{_scripts/includes/dasher-js.md}}}{Dasher: continuous-zoom arithmetic coding interface.
Move the pointer right of centre — boxes enlarge and stream left across
the crosshair.  Character height is proportional to P(char | context).
Try "th": after 't' and 'h', 'e' swells to dominate the display.}{dasher-visualisation}

\endif

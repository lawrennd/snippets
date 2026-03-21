\ifndef{maxwellsDemon}
\define{maxwellsDemon}

\editme 

\subsection{Maxwell's Demon}

\notes{Maxwell's demon is a thought experiment described by James Clerk Maxwell in his book, *Theory of Heat* [@Maxwell-theory71] on page 308.}

\notes{
> But if we conceive a being whose faculties are so sharpened that he can follow every molecule in its course, such a being, whose attributes are still as essentially finite as our own, would be able to do what is at present impossible to us. For we have seen that the molecules in a vessel full of air at uniform temperature are moving with velocities by no means uniform, though the mean velocity of any great number of them, arbitrarily selected, is almost exactly uniform. Now let us suppose that such a vessel is divided into two portions, A and B, by a division in which there is a small hole, and that a being, who can see the individual molecules, opens and closes this hole, so as to allow only the swifter molecules to pass from A to B, and the only the slower ones to pass from B to A. He will thus, without expenditure of work, raise the temperature of B and lower that of A, in contradiction to the second law of thermodynamics.
>
> James Clerk Maxwell in *Theory of Heat* [@Maxwell-theory71] page 308
}

\notes{He goes onto say:}

\notes{
> This is only one of the instances in which conclusions which we have draw from our experience of bodies consisting of an immense number of molecules may be found not to be applicable to the more delicate observations and experiments which we may suppose made by one who can perceive and handle the individual molecules which we deal with only in large masses
}


\figure{\includegooglebook{0p8AAAAAMAAJ}{PA308}}{Maxwell's demon was designed to highlight the statistical nature of the second law of thermodynamics.}{maxwells-demon}

\newslide{}

\figure{
<div style="display:flex;flex-wrap:wrap;gap:8px;align-items:flex-start">
  <div style="flex:1 1 400px;min-width:0">
    <canvas id="maxwell-canvas" width="700" height="500" style="border:1px solid black;display:block;width:100%"></canvas>
  </div>
  <div style="flex:0 1 280px;min-width:0;display:flex;flex-direction:column;gap:6px">
    <div>Velocity-bin entropy: <output id="maxwell-entropy"></output></div>
    <div id="maxwell-histogram-canvas" style="width:100%;height:250px"></div>
    <div style="display:flex;flex-wrap:wrap;gap:4px">
      <button id="maxwell-newball">New Ball</button>
      <button id="maxwell-pause">Pause</button>
      <button id="maxwell-skip">Skip 1000s</button>
      <button id="maxwell-histogram">Histogram</button>
    </div>
  </div>
</div>

\include{_scripts/includes/maxwell-js.md}
}{Maxwell's Demon. The demon decides balls are either cold (blue) or hot (red) according to their velocity. Balls are allowed to pass the green membrane from right to left only if they are cold, and from left to right only if they are hot. The displayed entropy is the Shannon entropy of the velocity histogram (a coarse-grained proxy, not full thermodynamic entropy).}{maxwells-demon}


\notes{Maxwell's demon allows us to connect thermodynamics with information theory (see e.g. @Hosoya-demon15;@Hosoya-maxwell11;@Bub-maxwell01;@Brillouin-maxwell51;@Szilard-intelligenter29). The connection arises due to a fundamental connection between information erasure and energy consumption @Landauer-irreversibility61.}

\notes{@Alemi-therml18}

\endif

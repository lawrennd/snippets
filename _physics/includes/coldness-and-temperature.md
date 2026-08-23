\ifndef{coldnessAndTemperature}
\define{coldnessAndTemperature}

\editme

\subsection{Coldness and Temperature}

\notes{The Boltzmann occupation can be written in two ways,
$$
p_i = \frac{e^{-E_i/kT}}{Z}
= \frac{e^{-\beta E_i}}{Z},
\qquad
\beta = \frac{1}{kT}.
$$
The mathematics is the same, but the emphasis is different.}

\slidesincremental{
* $T$: the bath, the thermometer
* $\beta = 1/kT$: coldness
* Same occupation; entropy sits in a different place
}

\notes{$T$ is the variable of the bath. It is what a thermometer reports, and it is the intensive parameter in the Helmholtz accounting $F = U - TS$. In that representation energy comes first and entropy is the correction: $TS$ is the cut the second law takes from $U$.}

\notes{$\beta$ is *coldness*. It is the variable conjugate to energy. In that representation entropy comes first: you maximise $S$ (or write a generating function in $\beta$) and energy is the constraint. Temperature is then a derived reading, $T = 1/k\beta = (\partial S/\partial U)^{-1}$.}

\newslide{Two Representations}

\slidesincremental{
* $T$-first: $F = U - TS$
* $\beta$-first: $Z(\beta)$, then $U = -\partial_\beta\log Z$
* Week 4: $\beta$ is the Lagrange multiplier
}

\notes{We will use both. Weeks 1--2 keep $T$ in view so the bath is familiar, and they already compute in $\beta$ because that is the natural argument of $Z$. Week 4 makes the $\beta$-first order honest: the Lagrange multiplier on a mean-energy constraint *is* coldness, and it is the natural parameter of the exponential family. Weeks 5--6 then treat $\beta$ as a coordinate on that family. A student who still hears $\beta$ as ``one over the thermometer'' will miss why the geometry is written in those coordinates.}

\endif

\ifndef{gaussianQuadraticFreeEnergy}
\define{gaussianQuadraticFreeEnergy}

\editme

\subsection{Gaussian: Expected Quadratic Energy}

\notes{We've already introduced the univariate Gaussian as an energy-based model with quadratic energy. We also looked at animations of elastic collisions and argued that the velocities were given by the Maxwell-Boltzmann distribution that has the form of a Gibbs distribution. We can apply the Helmholtz split to this system in closed form. Take
$$
E(x)=\frac{x^2}{2}
$$
and a bath at inverse temperature $\beta$ (here $k_B=1$, so $T=1/\beta$). The Gibbs density is
$$
p(x)=\frac{e^{-\beta x^2/2}}{Z}=\sqrt{\frac{\beta}{2\pi}}\,\exp\Bigl(-\beta\frac{x^2}{2}\Bigr),
$$
which is $\mathcal{N}(0,T)$. The partition function is the Gaussian integral
$$
Z=\int_{-\infty}^{\infty}e^{-\beta x^2/2}\,\mathrm{d}x=\sqrt{\frac{2\pi}{\beta}}.
$$}

\newslide{A Quadratic Energy}

\slides{
$$
E(x)=\frac{x^2}{2},\qquad p(x)=\sqrt{\frac{\beta}{2\pi}}\,e^{-\beta x^2/2}
$$
}

\slidesincremental{
* Week 1: Gaussian as $p\propto e^{-E}$ with a parabolic well
* Now: the same $E$, in contact with a bath at $T=1/\beta$
* $p=\mathcal{N}(0,T)$ --- variance *is* temperature ($k_B=1$)
}

\speakernotes{Callback to the height-Gaussian parabola from week 1. One quadratic degree of freedom, not a covariance model. Equipartition is the headline: $U=T/2$.}

\newslide{Inner Energy is Equipartition}

\slides{
$$
U=\expSamp{E}=\expSamp{\frac{x^2}{2}}=\frac{T}{2}
$$
}

\slidesincremental{
* $\expSamp{x^2}=T$ because $p=\mathcal{N}(0,T)$
* One quadratic degree of freedom holds $k_BT/2$
* Maxwell's kinetic energy $\tfrac32 k_BT$ is three copies of this
}

\notes{The inner energy is the expectation of the quadratic,
$$
U=\expSamp{E}=\int p(x)\,\frac{x^2}{2}\,\mathrm{d}x=\frac{1}{2}\expSamp{x^2}.
$$
Under $p=\mathcal{N}(0,T)$ we have $\expSamp{x^2}=T$, so $U=T/2$. That is the equipartition theorem for a single quadratic degree of freedom: each such term in the energy contributes $k_BT/2$ at equilibrium. Maxwell's three Cartesian components --- a few slides back --- are three independent copies of this quadratic. Kinetic energy $\tfrac32 k_BT$ is $d=3$. The Jacobian that produces *speed* is why the speed density is not itself Gaussian.}

\newslide{Free Energy and Entropy, Closed Form}

\slides{
$$
F=-T\log Z=-\frac{T}{2}\log(2\pi T),\qquad S=\frac{1}{2}+\frac{1}{2}\log(2\pi T)
$$
}

\slidesincremental{
* $Z=\sqrt{2\pi T}$, so $F$ is immediate
* $S=(U-F)/T$ recovers the Gaussian differential entropy
* Check: $F+TS=T/2=U$
}

\notes{The free energy is the generating-function term from the derivation,
$$
F=-T\log Z=-T\log\sqrt{2\pi T}=-\frac{T}{2}\log(2\pi T).
$$
Entropy follows from $S=(U-F)/T$,
$$
S=\frac{1}{2}+\frac{1}{2}\log(2\pi T).
$$
That is the differential entropy of $\mathcal{N}(0,T)$, in nats, with $k_B=1$. Here $S$ is simply the name we gave to $-k_B\expSamp{\log p}$ when we took the expectation of $E(x)$. The continuous functional can be negative and is not invariant to a change of units. The algebra we need is already visible:
$$
F+TS=-\frac{T}{2}\log(2\pi T)+T\Bigl(\frac{1}{2}+\frac{1}{2}\log(2\pi T)\Bigr)=\frac{T}{2}=U.
$$
The $\tfrac12$ in $U$ and the $\tfrac12$ sitting in $T\cdot\tfrac12$ --- the $e$ inside $\tfrac12\log(2\pi e T)$ --- cancel, leaving $F=-T\log Z$. Spreading the Gaussian (raising $T$) does not change the *shape* of the well $E(x)=x^2/2$; it changes how far the occupation climbs the walls, and therefore how much of $U$ is locked in $TS$.}

\setupplotcode{import numpy as np
import matplotlib.pyplot as plt
import mlai}

\plotcode{T = np.linspace(0.15, 3.0, 400)
U = T / 2.0
S = 0.5 + 0.5 * np.log(2.0 * np.pi * T)
TS = T * S
F = -0.5 * T * np.log(2.0 * np.pi * T)
fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(T, U, label=r'$U=T/2$')
ax.plot(T, TS, label=r'$TS$')
ax.plot(T, F, label=r'$F=-T\log Z$')
ax.axhline(0.0, color='#666', ls=':', lw=1)
ax.set_xlabel(r'$T$ ($k_B=1$)')
ax.legend()
ax.set_title(r'Quadratic $E(x)=x^2/2$: $U=F+TS$')
mlai.write_figure('gaussian-quadratic-thermo.svg', directory='\writeDiagramsDir/ml')

xs = np.linspace(-4.0, 4.0, 400)
Ex = 0.5 * xs ** 2
fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(xs, Ex, 'k', lw=2, label=r'$E(x)=x^2/2$')
for Tval, colour in [(0.3, '#4C72B0'), (1.0, '#DD8452'), (2.5, '#55A868')]:
    ax.axhline(Tval / 2.0, color=colour, ls='--', lw=1.5,
               label=rf'$\langle E\rangle=T/2$ at $T={Tval:.1f}$')
ax.set_xlabel(r'$x$')
ax.set_ylabel(r'$E(x)$')
ax.set_ylim(0.0, 4.0)
ax.legend()
ax.set_title(r'Occupation climbs the well as $T$ rises')
mlai.write_figure('gaussian-quadratic-well.svg', directory='\writeDiagramsDir/ml')}

\newslide{The Well, and the Expectation}

\figure{\includediagram{\diagramsDir/ml/gaussian-quadratic-well}{70%}}{The energy is the same parabola at every temperature. Raising $T$ spreads $p=\mathcal{N}(0,T)$ and the occupation climbs the walls: $\expSamp{E}=T/2$ rises linearly.}{gaussian-quadratic-well}

\newslide{The Decomposition versus $T$}

\figure{\includediagram{\diagramsDir/ml/gaussian-quadratic-thermo}{75%}}{Closed form for $E(x)=x^2/2$ with $k_B=1$. Inner energy $U=T/2$ is the straight line; $TS$ takes a growing cut; $F=U-TS$ is negative and decreases.}{gaussian-quadratic-thermo}

\setupcode{import numpy as np}

\code{def gaussian_quadratic_thermo(T):
    """U, S, F for $E(x)=x^2/2$ at temperature $T$ ($k_B=1$)."""
    U = T / 2.0
    Z = np.sqrt(2.0 * np.pi * T)
    F = -T * np.log(Z)
    S = (U - F) / T
    return U, S, F

T = 1.0
U, S, F = gaussian_quadratic_thermo(T)
U, S, F, np.isclose(U, F + T * S)}

\newslide{$d$ Quadratic Degrees of Freedom}

\slides{
$$
E(\mathbf{x})=\frac{1}{2}\sum_{i=1}^{d} x_i^2
\qquad\Longrightarrow\qquad
U=\frac{d\,T}{2}
$$
}

\slidesincremental{
* $Z=(2\pi T)^{d/2}$, so $F=-(d T/2)\log(2\pi T)$
* Independent coordinates: the one-dimensional split, $d$ times
* Maxwell's three velocity components were this with $d=3$
}

\notes{If the energy is a sum of independent quadratics, $E(\mathbf{x})=\tfrac12\sum_{i=1}^d x_i^2$, the partition function factors and
$$
U=\frac{d\,T}{2},\qquad
Z=(2\pi T)^{d/2},\qquad
F=-\frac{d T}{2}\log(2\pi T).
$$
Each coordinate contributes its own $T/2$ to the inner energy and its own $\tfrac12\log(2\pi e T)$ to the entropy. That is why an ideal gas of $N$ particles in three dimensions has kinetic energy $\tfrac32 N k_BT$: $3N$ quadratic terms in the Hamiltonian, each holding $k_BT/2$. The derivation did not change. We took the expectation of a bigger $E$.}

\newslide{The Air Thermometer?}

\slides{Gay-Lussac's vanishing volume is not this well. It is the same $T$.}

\slidesincremental{
* Three velocity components: $U_{\mathrm{kin}}=\tfrac32 T$ per particle --- done
* A box, not a well: positions contribute a factor $V$ to $Z$, not another Gaussian
* Helmholtz: $\displaystyle P=-\bigl(\partial F/\partial V\bigr)_T = NT/V$
}

\speakernotes{Do not derive Sackur--Tetrode or Gibbs $G$. Kinetic Gaussians are done. Name $V$ in $Z$, name the Helmholtz derivative, sit down. Charles's law is $PV=NT$ at fixed $P$.}

\notes{The air thermometer is a bulb of gas whose *volume*, at constant pressure, is the reading. Thomson already had Gay-Lussac's wall: if that volume is linear in temperature it vanishes at about $-273^\circ$. The quadratic well we just split has no box, so it cannot be that thermometer. Maxwell's three Cartesian components *are* three copies of $E=v_i^2/2$: the kinetic half of an ideal-gas particle is already on the board. What is missing is the configuration integral. A free particle in a container of volume $V$ has, up to constants of mass and $h$ that we do not need,
$$
Z_1 = V\,(2\pi T)^{3/2}.
$$
The Gaussian integrals we just evaluated are the momentum half; $V$ is the position half. For $N$ particles, $Z \propto V^N T^{3N/2}$, so $F=-T\log Z$ depends on $V$. Pressure is a Helmholtz derivative, not a new potential:
$$
P=-\Bigl(\frac{\partial F}{\partial V}\Bigr)_{T,N}=\frac{NT}{V}.
$$
At constant $P$, $V\propto T$. Gay-Lussac's wall is $T=0$ on the same scale whose variance we just read off Maxwell's Gaussians. Thomson in 1848 treated $-273^\circ$ as an accident of air. After Joule it is the floor of the engine scale; after Maxwell it is also the temperature at which those Gaussians have collapsed to a delta, and a finite pressure would require zero volume.

We do not need the Gibbs free energy $G=F+PV$ for this. $G$ is the potential when *pressure* is the control variable. Charles's law is already in $PV=NT$. Coupled multivariate Gaussians are not required either: independent coordinates suffice, and that is what Maxwell wrote. The one extra Helmholtz fact is the derivative with respect to $V$. We name it. We do not compute Stirling, $h^3$, or chemical potential today.}

\endif

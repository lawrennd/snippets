\ifndef{freeEnergyDecomposition}
\define{freeEnergyDecomposition}

\editme

\subsection{Free Energy Decomposition}

\notes{Once the Gibbs occupation
$$
p(x)=\frac{e^{-\beta E(x)}}{Z},\qquad Z=\sum_x e^{-\beta E(x)}
$$
is given, we can derive the macroscopic formulae that characterise the gas. They come to us from Helmholtz. We can compute them through the expectation of that occupation of the given energies, taken at equilibrium. The relationship between energy and probability is $p_i\propto e^{-\beta E_i}$. Here we will identify the "inner energy" or "total energy" with $\expSamp{E}$ and read off $F=U-TS$. $Z$ is German: it comes from Boltzmann, the sum of states, Summe der Zustände. That is why it is $Z$, because it is a sum. If the system were continuous, a Gaussian, $Z$ would be an integral.}

\newslide{From Occupation to Accounting}

\slides{From Gibbs distribution to energy bookkeeping.}

\slidesincremental{
* $p(x)=e^{-\beta E(x)}/Z$
* Equilibrium: inner energy is an *expectation*, $U=\expSamp{E}$
* Algebra then *defines* $F$ and $S$
}

\speakernotes{LO1. Board the occupation with $Z$, name Summe der Zustände, take the log, take the expectation. Watch the signs. Why the exponential: equilibrium. What $\log Z$ is: available energy, the work you can get out. Do not invoke MaxEnt --- that is week 5. The occupation is given; we are reading it.}

\newslide{Take the Logarithm}

\slides{
$$
\log p(x) = -\beta E(x) - \log Z
$$
}

\slidesincremental{
* Solve for the microscopic score: $E(x)=-k_BT\log p(x)-k_BT\log Z$
* $1/\beta=k_BT$ converts coldness back to the bath's temperature
}

\notes{Start from the occupation and take the logarithm,
$$
\log p(x)=-\beta E(x)-\log Z.
$$
Note that nothing statistical has happened here, this is an identity for every probability that is a member of the exponential family, which in physics we think of as the Gibbs distribution. It's valid for every configuration $x$ that the Gibbs distribution supports. If we solve for the energy of that configuration we can restore temperature through recognising that $\beta=1/(k_BT)$,
$$
E(x)=-k_BT\log p(x)-k_BT\log Z.
$$
Note that the first term on the right (the surprisal multiplied by the temperature and Boltzmann's constant) still depends on $x$. The second does not: $-k_BT\log Z$ is a property of the whole ensemble, not of a particular microstate.}

\newslide{Equilibrium Identifies $U$ with $\expSamp{E}$}

\slides{
$$
U \equiv \expSamp{E} = \sum_x p(x)\, E(x)
$$
}

\slidesincremental{
* $E(x)$ is a score on configurations
* $U$ is what a calorimeter would call the energy of the *system*
* The move is the ensemble: replace a number by an expectation
}

\notes{At equilibrium the macroscopic inner energy can be related to the expectation of the microscopic score under the same distribution,
$$
U\equiv\expSamp{E}=\sum_x p(x)\,E(x).
$$
This is where the *ensemble* is entering in physics. The ensemble that comes to us from Boltzmann, Maxwell, Gibbs, and Einstein. The idea is that the system is not in one configuration. When we coarse-grain this room we are not going to look at the actual energy of every particle. There are of order $10^{23}$ of them; at that scale the variance around the expectation does not show. That expected energy becomes, at this scale, the total energy of the gas in the room. The index $i$ is the *space* --- discrete energy levels, which is one of the challenges Boltzmann received: what *is* this discrete space? That is where the phase-volume arguments come from. We will just assume it is discrete; an expectation is a sum or an integral. Substitute the identity for $E(x)$,
\begin{align}
U
&= \sum_x p(x)\bigl(-k_BT\log p(x)-k_BT\log Z\bigr) \nonumber\\
&= -k_BT\sum_x p(x)\log p(x) - k_BT\log Z.
\end{align}
The second term comes out of the sum because $\log Z$ does not depend on $x$, and $\sum_x p(x)=1$.}

\newslide{Name the Two Remaining Terms}

\slides{
$$
U = \underbrace{-k_BT\log Z}_{F} + T\underbrace{\bigl(-k_B\sum_x p(x)\log p(x)\bigr)}_{S}
$$
}

\slidesincremental{
* Helmholtz free energy: $F=-k_BT\log Z$
* Boltzmann entropy: $S=-k_B\sum_x p(x)\log p(x)=k_B H$
* Hence $U=F+TS$, or $F=U-TS$
}

\speakernotes{Board $F=U-TS$ and $U=F+TS$ as the same equation. Helmholtz wrote $A=U-TS$ ($A$ for *Arbeit*). We use $F$ because week 5 needs $A(\theta)$ for the log-partition.}

\notes{The two remaining pieces already have names. The configuration-independent term is the *Helmholtz free energy*,
$$
F=-k_BT\log Z,
$$
it is often known as the "free energy" or "available energy". It is the energy that we can use for work. The average of $-\log p$ is the dimensionless Shannon functional $H=-\sum_x p(x)\log p(x)$. Multiplying by Boltzmann's constant produces physical entropy, $S=k_B H$, with units of energy per degree. Then
$$
U=F+TS\qquad\text{or}\qquad F=U-TS.
$$
Helmholtz originally wrote $A=U-TS$, with $A$ for *Arbeit*, the work still available. This module uses $F$ for the same quantity, because week 5 needs $A(\boldsymbol{\theta})$ for the log-partition of an exponential family. But Helmholtz's $A$ and our $F$ are the same object; $U$ is the inner energy $\expSamp{E}$, not a free energy. The fact that they are different is down to energy that is stored as entropy. It's in this term that we can find Black's latent heat.

From the physics and thermodynamics perspective $U$ is the energy in the system, $TS$ is the "cut" that entropy takes from that total energy. It is tied up in the uncertainty of the occupation, unavailable as work. Then $F$ is what the thermodynamic bath still allows you to do. Given the Gibbs occupation, the macroscopic split $F=U-TS$ is an identity.

The point of the derivation, boarded, is that inner energy is composed of the entropy plus the available energy. Entropy is now your bookkeeping device for why you cannot get all the work back out of the heat. You can convert all your work into heat and produce the inner energy with your motion. Then the motion is going in different directions. The energy is still there at the particle level. Maxwell's demon is an attempt to reverse that by seeing where the particles are. The scale we have just written assumes an ensemble. Dive into the ensemble and play with it, and you cross levels of coarse graining. That is easy to do in modelling, and it is what goes on in a lot of Maxwell's-demon arguments. It is not always clear at which point you are allowed to cross. Week 4 is the treatment; here it is the warning.

Watch the signs on the board. Boltzmann's constant is of order $10^{-23}\,\mathrm{J\,K}^{-1}$. There is a $10^{-23}$ scaling on these numbers, and then of order $10^{23}$ particles, so you get back to joules. The units of $k_B$ are joules per kelvin --- joules per degree. $S=k_B H$ takes a dimensionless functional of a probability and converts it into the units we speak about. If you think of $H$ as the more fundamental object, coldness $\beta$ is the more natural parameter than $T$. The reason we usually write it the other way around is that it was discovered in Clausius's way: energy first, then entropy times temperature.}

\newslide{Two Temperatures, One Identity}

\slidesincremental{
* $T$-first: $F=U-TS$ --- energy, then entropy's cut
* $\beta$-first: $F=-\beta^{-1}\log Z$, then $U=-\partial_\beta\log Z$
* Same numbers; week 5 makes $\beta$ a Lagrange multiplier
}

\notes{The $T$-first reading puts energy first and treats entropy as a correction. The $\beta$-first reading treats $\log Z$ as a generating function: $U=-\partial_\beta\log Z$ and $S=\beta(U-F)$, which we compute from $Z$ later. Both are the identity just derived. Later we will derive the occupation from MaxEnt and identify $\beta$ as the Lagrange multiplier on the mean-energy constraint; until then the occupation is given, and we are reading it.}

\notes{If you have a process whose entropy has not changed, inner energy and available energy are the same. That is a reversible system: you have not taken work and converted it into inner energy. Along a reversible path the heat relation is $\mathrm{d}Q_{\mathrm{rev}}=T\,\mathrm{d}S$, or $\mathrm{d}S=k_B\beta\,\mathrm{d}Q_{\mathrm{rev}}$. It comes from $\mathrm{d}U=T\,\mathrm{d}S-p\,\mathrm{d}V$, not from the Helmholtz split. The thing they were measuring the flow of, when they talked about conservation, was entropy. That is the caloric they thought was conserved. If the entropy is conserved you are looking at a reversible system, which is what Carnot was trying to look at, and why his engine is the most efficient you can be.}

\notes{A short history-of-science aside, boarded before the algebra. A lot of the *practice* of science in this period --- what we might call engineering --- is in Birmingham, Glasgow, Aberdeen, driven by application. Late nineteenth century, a rising capability in Germany. After the Great Exhibition of 1851 there was a royal commission to ask why Oxford and Cambridge had contributed so little. The result of that inquiry was the Cavendish Laboratory (1870) and the Natural Sciences Tripos. Maxwell is the scientist this thread is heading towards; we skip him for a moment.}

\setupplotcode{import numpy as np
import matplotlib.pyplot as plt
import mlai}

\plotcode{energies = np.array([0.0, 1.0, 3.0])
beta = np.linspace(0.05, 2.5, 200)
Z = np.sum(np.exp(-beta[:, None] * energies), axis=1)
p = np.exp(-beta[:, None] * energies) / Z[:, None]
U = (p * energies).sum(axis=1)
S = -np.sum(p * np.log(p + 1e-300), axis=1)
F = U - S / beta
F_check = -np.log(Z) / beta
fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(beta, U, label=r'$U(\beta)$')
ax.plot(beta, S, label=r'$S(\beta)$ (nats, $k_B=1$)')
ax.plot(beta, F, label=r'$F(\beta)$')
ax.plot(beta, F_check, 'k--', alpha=0.5, label=r'$-\ln Z/\beta$')
ax.set_xlabel(r'$\beta$')
ax.legend()
ax.set_title(r'Three-state system: energies $E\in\{0,1,3\}$')
mlai.write_figure('three-state-thermo.svg', directory='\writeDiagramsDir/ml')}

\newslide{Three-State Check}

\figure{\includediagram{\diagramsDir/ml/three-state-thermo}{75%}}{$U$, $S$, and $F$ for the Worksheet 1 three-state system ($k_B=1$). The dashed curve is $-\log Z/\beta$; it sits on $F$, which is the identity just derived.}{three-state-thermo}

\notes{The Worksheet 1 three-state system, $E\in\{0,1,3\}$, is a numerical check of the same algebra with $k_B=1$. Compute $p_i=e^{-\beta E_i}/Z$, then $U=\sum_i p_i E_i$ and $S=-\sum_i p_i\log p_i$. The two expressions for free energy, $F=U-S/\beta$ and $F=-\log Z/\beta$, overlie. If they do not, the signs in the derivation are wrong.}

\setupcode{import numpy as np}

\code{def gibbs_thermo(energies, beta):
    """U, S, F from a discrete Gibbs occupation ($k_B=1$)."""
    e = np.asarray(energies, dtype=float)
    weights = np.exp(-beta * e)
    Z = weights.sum()
    p = weights / Z
    U = np.sum(p * e)
    S = -np.sum(p * np.log(p))
    F = -np.log(Z) / beta
    return U, S, F, U - S / beta

U, S, F, F_from_US = gibbs_thermo([0.0, 1.0, 3.0], beta=1.0)
U, S, F, F_from_US}

\slidesincremental{
* Prescription: $p(x)=e^{-\beta E(x)}/Z$
* Accounting: $F=U-TS$ with $U=\expSamp{E}$
}

\endif

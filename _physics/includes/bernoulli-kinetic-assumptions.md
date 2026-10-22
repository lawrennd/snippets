\ifndef{bernoulliKineticAssumptions}
\define{bernoulliKineticAssumptions}

\editme

\subsection{What Bernoulli Assumes}

\slides{*Hydrodynamica* (1738) already treats a gas as many tiny bodies in motion.}

\slidesincremental{
* Many corpuscles, small compared with the vessel
* Motion is swift and disordered; collisions transfer momentum
* Pressure on a wall is the rain of impacts, not a static push
* Idealisation: elastic billiard-like encounters, no lingering forces
}

\speakernotes{Board the assumptions as modelling choices. The billiards canvas makes them literal. Flag what is *not* assumed: chemical identity of atoms, quantum mechanics, or a finished thermodynamic entropy.}

\notes{Daniel Bernoulli's kinetic chapter in *Hydrodynamica* [@Mikhailov:hydrodynamica05] asks what pressure *is* if air is a swarm of particles. The modelling assumptions are severe and productive:
\begin{enumerate}
\item the gas is a large number of minute bodies, each negligible in size next to the container;
\item those bodies move rapidly; what we call pressure is the momentum they impart when they strike the walls;
\item encounters are brief and mechanical --- the billiard-ball ideal that the simulation below takes literally;
\item one does not need the chemical story of atoms, only a corpuscular mechanics that can be calculated.
\end{enumerate}
Conservation of mechanical effect (energy in later language) lets him relate microscopic motion to macroscopic push. That is an extraordinary claim for 1738. It is also an *idealisation*: real molecules attract and vibrate; Bernoulli's gas is a coarse mechanical cartoon chosen so that Newton's laws have something to act on.}

\newslide{Assumptions Are Already Coarse}

\slides{Bernoulli does not track Laplace's curve for every particle --- he summarises a swarm.}

\slidesincremental{
* Individual trajectories are discarded
* What remains is a mechanical story for *pressure*
* Next: make the discarded detail a probability --- the ensemble
}

\notes{Even at the birth of kinetic theory, the useful object is not the full list of paths. Bernoulli averages. He is not tracking Laplace's curve for every particle --- he predates Laplace --- but he is summarising a swarm of motion. Individual trajectories are discarded, and what remains is a mechanical story for pressure. That pressure is macroscopic and measurable: when a vessel explodes, it is the pressure we are talking about, and that is a function of particles hitting the walls. There is a great deal of energy stored in that.

The statistical physicists who follow --- Maxwell, Boltzmann, Gibbs --- will turn that averaging into an explicit probability over microstates. The billiard simulation is Bernoulli's assumption made visible; the Shannon entropy of the velocity histogram is already a coarse-grained proxy for how much velocity detail we are keeping.

I think Bernoulli is probably the first person to start doing this move that we are going to see throughout the course. It sits at the heart of entropy, and at the heart of intelligence. The move is coarse-graining.}

\endif

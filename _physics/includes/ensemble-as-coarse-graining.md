\ifndef{ensembleAsCoarseGraining}
\define{ensembleAsCoarseGraining}

\editme

\subsection{From Paths to an Ensemble}

\slides{Laplace's gremlin says we cannot follow every curve. The ensemble is how we *live with that*.}

\slidesincremental{
* Microstate: positions and velocities of all particles (Laplace's curves)
* Macrostate: a few numbers --- $N$, $V$, $E$ or $T$, $P$
* Ensemble: a probability over the microstates compatible with the macrostate
}

\speakernotes{Name coarse-graining without measure theory. Billiard histogram bins are a toy coarse-graining; $T,V,P$ are the physicist's. Do not derive MaxEnt. Die grouping waits for week 3.}

\notes{We ignore some portion of the detail and summarise it with its macroscopic statistics. In physics, that is what Gibbs called the ensemble.

A *microstate* is the curve of the simple molecule of air --- the positions and velocities of all the particles. A *macrostate* is how we summarise it: particle number, volume, energy, temperature, pressure. An *ensemble* is the probability of the microstates compatible with the macrostate.

Bernoulli never looked at it as probabilities. He looked at it as we might do in fluid flow today, drawing a box around a subsection of the flow. Gibbs comes a little after Boltzmann. I do not think Boltzmann used the term, but Boltzmann was doing the same thing.

This maps directly into the way we model in machine learning. If I say the noise is Gaussian, I am doing the same thing: I look at it with its mean and its variance. When we include noise in a machine learning model, we are allowing the model to abstract. We are allowing it to ignore some of the underlying process. In physics they typically prove that that is the case. In machine learning we assume it and try to fit the model.}

\newslide{Extensive and Intensive}

\slides{Some macrostate properties scale with the size of the system. Some do not.}

\slidesincremental{
* Extensive: $N$, $V$, energy --- scale with the system
* Intensive: temperature --- does not
* Entropy is extensive: $N$ independent copies $\Rightarrow$ $N$ times the entropy
}

\speakernotes{Ask the room: is entropy intensive or extensive? One route: you can calculate one thermodynamic quantity from another, so they must scale roughly the same way. The other: entropy just increases as I increase the state space.}

\notes{Physicists distinguish extensive from intensive. An extensive property is a macrostate property that scales with the size of the system. An intensive property does not. Temperature is intensive. $N$ is extensive. Volume scales extensively. Energy tends to increase with the system.

Is entropy intensive or extensive? One route is that we can calculate one thermodynamic quantity from another, so they must scale in roughly the same way. Another is that entropy increases as I increase the state space. If I have $N$ independent variables from the same distribution, the total entropy is $N$ times each variable's entropy. Entropy therefore scales extensively. That is also why, later, $TS$ having units of energy tells us that entropy must be extensive.}

\newslide{A Hurricane Is Not in the Equations}

\slides{There is no variable "hurricane" in Navier--Stokes.}

\slidesincremental{
* Just air, water, land --- particles moving around
* We still all agree hurricanes exist
* Right level of abstraction is how we decide
}

\speakernotes{Niall Robinson, formerly Met Office, now NVIDIA: to find a hurricane in a simulation you write a list of things (wind speed above a threshold, location). Contrast a chair --- computer vision struggled for years to write logical rules. Gas/liquid/solid is cleaner. Do not mark students wrong for disagreeing: this is speculation.}

\notes{I think coarse-graining sits at the heart of entropy and at the heart of intelligence. Bernoulli does not track Laplace's curve for every particle. He summarises a swarm of motion. In that summarisation we lose information, because we are no longer tracking everything that is going on, but we convert the summary into something operational on the level above.

That move is common in physics. As we go into the material, into the atom, these summarisations occur multiple times. In advanced physics we meet renormalisation. Why do objects pop out at certain scales? Why are there levels at which particles appear? That is at the heart of what is going on in physics.

My argument is that something similar happens in intelligence. Which part of this is a table, and which part is not? We think about causal relationships between the table and the piece of paper; about what is a mug and what is not. What is the relationship between the physical summarisation going on here, and the summarisation we perform when we interact with the world? For me that is one of the critical things about our intelligence: how we abstract objects.

My preferred example is a hurricane. A colleague, Niall Robinson, worked at the Met Office on large-scale simulations and on data coming out of Navier--Stokes. He had to define what a hurricane is. There is no variable "hurricane" in Navier--Stokes. There is a load of particles moving around. To identify a hurricane in the simulation you write a list of things: wind speeds above a threshold, the storm in a certain place. You take our sense of a hurricane and convert it into criteria.

From the equations' perspective there is not an object. It is air moving around and interacting with water and land. I think we would all agree that hurricanes exist. That is an abstraction. When we talk about a fluid we are doing the same thing. It is really a bunch of molecules moving around together; then we think of its properties at a higher level.

A hurricane is comparatively clean --- Niall could define it quite well --- unlike a chair. People struggled for years in computer vision to write logical rules that define a chair. It is not as sharp as gas, liquid, solid.

What this abstraction buys us is that we can summarise the gas in the room by its temperature, pressure and volume, instead of by the movement of every particle. Similarly, I can talk about what we do when a hurricane is approaching New Orleans. I do not have to talk about all the bits and pieces moving in the hurricane. I can make decisions at a different level of abstraction. Operating at the right level of abstraction seems to me a key part of intelligent decision making.

I will not mark you wrong for disagreeing. That claim is my speculation, not settled science. It is a route I find worth taking.}

\newslide{The Table Is Not Maximum Entropy}

\slides{Some of a table's properties look like macrostates. The rest is structure.}

\slidesincremental{
* Volume and temperature: gas-like summaries
* Grain, chains in the wood: correlations we are not throwing away
* The table is not in a maximum-entropy state
}

\notes{Some of this table's properties are clearly macrostates of the system, such as its volume and its temperature. Then there are other things where the relationship is no longer so tight. That is where my notion of abstraction breaks away from the kinetic story. We cannot summarise the table as some simple distribution. There are correlations inside it. There is structure --- chains within the wood --- complex things going on in the states of the table that are not true of the gas around us. The table is not in a maximum-entropy state, in that sense.

The gas around us is noise. There is energy in what is going on there, but there is no correlation or structure in it. That is why we can summarise it by the temperature, the pressure and the volume. Independence is also a property of maximum entropy. If there were correlation, it would not be maximum entropy.}

\newslide{Coarse-Graining Is a Choice of Description}

\slides{Temperature and pressure are sufficient statistics of the swarm}

\slidesincremental{
* Histogram bins: keep some velocity detail, discard the rest
* Thermodynamics: keep $T$, $V$, $P$; discard which molecule was which
* The uncertainty we write as entropy lives at the chosen grain
}

\notes{We can look at the same system and coarse-grain at different levels. That is again what physicists are doing when they increase the energy in a particle accelerator. They are looking at things that are around us, but they are increasing the energy.

When I histogram the bins, I am keeping some of the velocity detail and discarding the rest. Different bin widths would have given a different entropy. That choice is a coarse-graining choice, and it affects the entropies we see.

Thermodynamics is a coarse-graining choice to keep the temperature, the volume and the pressure. The merit of that choice is that we know the form of the residual we are losing: it is a maximum entropy. I do not think that is quite true of the residual if I am histogramming.

The uncertainty we are calling entropy lives at that chosen grain. When we make these choices, we are discarding something and creating entropy. A choice of discretisation triggers an entropy loss.}

\newslide{Discretisation Produces Entropy}

\slides{Finer grain: discard less entropy, compute more.}

\slidesincremental{
* Exact only if you track the continuous thing
* UK weather: cells of about 800 metres --- why not a millimetre?
* Slow engines are more efficient and less powerful. Is that the same trade-off?
}

\speakernotes{Francisco Vargas, Schrödinger--Föllmer sampler: exact only if the diffusion is run continuously; discretise and you produce entropy. Student may offer higher-order integrators (trapezoid vs Euler): that is mechanism, not the entropic bound --- same split as Maxwell's demon. Do not prove anything. Ask: is the trade-off fundamental, or a coincidence?}

\notes{This came up with a student, Francisco Vargas, working on Schrödinger's bridge. He had a sampling approach, the Schrödinger--Föllmer sampler, billed as an exact sampler. In Bayesian inference we want to sample from the posterior, and normally we do that approximately. His sampler was exact only if the diffusion it was based on ran continuously. There is a nonlinear diffusion that has to be solved numerically. As soon as you discretise that diffusion, you produce entropy, and the sample is no longer exact. The coarser the discretisation, the more entropy you produce, and the worse the approximation.

What stops us discretising infinitely? Assume a numerical mathematician has solved stability for us. Why would we not discretise infinitely? Why, when we do weather, do we not go down to millimetres? UK weather predictions currently use cells of about 800 metres. Halve the grid size and you quadruple the computational cost. Discretising more means we have to make more computations.

If I coarse-grain more finely, I discard less entropy, but I have to compute more. Is that trade-off fundamental, or a coincidence? In the thermodynamics of engines we claim that the trade-off is fundamental. An engine that stays closer to equilibrium can be more efficient; if it moves slowly, it is more efficient and less powerful.

There is an entropic argument, and then there is an argument about how you are doing it. That is also what I claimed is problematic in Maxwell's demon: one argument is entropic, and then there is another --- how is the demon doing it?}

\newslide{Bridge to Maxwell, Boltzmann, Gibbs}

\slides{They turn Bernoulli's swarm and Laplace's ignorance into a calculus.}

\slidesincremental{
* Maxwell: velocity statistics of the ideal gas
* Boltzmann: $S$ linked to probability over microstates
* Gibbs: ensembles as the systematic language
}

\notes{What follows historically is the bookkeeping that makes the ensemble usable. Gibbs--Boltzmann occupation, free energy $F=U-TS$, and the bath that justifies fixing $T$ wait for the next lecture. The molecular hypothesis wins historically, but today we need the *abstraction*: we replace ignorance of the path with a distribution on the set of paths, and the cost of that move is how much uncertainty the macro description throws away.}

\endif

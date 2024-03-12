\ifndef{simulationScales}
\define{simulationScales}

\editme

\subsection{Abstraction and Emergent Properties}

\figure{\includediagram{\diagramsDir/physics/simulation-scales}{90%}}{A scale of different simulations we might be interested in when modelling the physical world. The scale is $\log_{10}$ meters. The scale reflects something about the level of granularity where we might choose to know "all positions of all items of which nature is composed".}{simulation-scales} 

\newslide{Abstraction}

\slides{* We often abstract smaller scales away e.g. in statistical mechanics.
* When we're abstracting finer length scales we can introduce uncertainties.
    * E.g. Maxwell-Boltzmann distribution for ideal Gas.}

\notes{Unfortunately, even if such an equation were to exist, we would be unlikely to know "all positions of all items of which nature is composed". A good example here is computational systems biology. In that domain we are interested in understanding the underlying function of the cell. These systems sit somewhere between the two extremes that Laplace described: "the movements of the greatest bodies of the universe and those of the smallest atom".}

\notes{When the smallest atom is considered, we need to introduce uncertainty. We again turn to a different work of Maxwell, building on Bernoulli's kinetic theory of gases we end up with probabilities for representing the location of the 'molecules of air'. Instead of a deterministic location for these particles we represent our belief about their location in a distribution.}

\newslide{Emergence}

\slides{* But fine scale local-laws also lead to emergent properties.
* Some of these properties exist at large scale.
* In particular, when there are complex interactions between molecules.}

\speakernotes{Ideal gas is a model where interaction between molecules is relatively simple. If this interaction is more complex (e.g. through quantum interactions of their bonded electrons, more structure exists.}

\notes{Computational systems biology is a world of micro-machines, built of three dimensional foldings of strings of proteins. There are spindles (stators) and rotors (e.g. [ATP Synthase](https://en.wikipedia.org/wiki/ATP_synthase)), there are small copying machines (e.g. [RNA Polymerase](https://en.wikipedia.org/wiki/RNA_polymerase)) there are sequence to sequence translators ([Ribosomes](https://en.wikipedia.org/wiki/Ribosome)). The cells store information in DNA but have an ecosystem of structures and messages being built and sent in proteins and RNA. Unpicking these structures has been a major preoccupation of biology. That is knowing where the atoms of these molecules are in the structure, and how the parts of the structure move when these small micro-machines are carrying out their roles.} 

\notes{We understand most (if not all) of the physical laws that drive the movements of these molecules, but we don't understand all the actions of the cell, nor can we intervene reliably to improve things. So, even in the case where we have a good understanding of the physical laws, Laplace's gremlin emerges in our knowledge of "the positions of all items of which nature is composed".}

\subsection{Molecular Dynamics Simulations}

\notes{By understanding and simulating the physics, we can recreate operations that are happening at the level of proteins in the human cell. [V-ATPase](https://en.wikipedia.org/wiki/V-ATPase) is an enzyme that pumps protons.  But at the microscopic level it's a small machine. It produces ATP in response to a proton gradient. A paper in *Science Advances* [@Roh-cryo-em20] simulates the functioning of these proteins that operate across the cell membrane. This makes these proteins difficult to crystallize, the response to this challenge is to use a simulation which (somewhat) abstracts the processes. You can also check this [blog post](https://www6.slac.stanford.edu/news/2020-10-07-first-detailed-look-how-molecular-ferris-wheel-delivers-protons-cellular-factories) from the paper's press release.}

\figure{\includegif{\diagramsDir/sysbio/rotary_proton_sv_pump_anim_final}{40%}}{The V-ATPase enzyme pumps proteins across membranes. This molecular dynamics simulation was published in *Science Advances* [@Roh-cryo-em20]. The scale is roughly $10^{-8} m$.}{v-atp-ase}

\speakernotes{Those complex interactions can also be modelled, but we can no longer summarize with the Maxwell-Boltzmann distribution. We need molecular dynamics simulations which can be combined with imaging using electron microscopes operating at extremely cold temperatures.}

\subsection{Quantum Mechanics}

\notes{Alternatively, we can drop down a few scales and consider simulation of the Schrödinger equation. Intractabilities in the many-electron Schrödinger equation have been addressed using deep neural networks to speed up the solution enabling simulation of chemical bonds [@Pfau-abinitio20]. The [PR-blog post is also available](https://deepmind.com/blog/article/FermiNet). The paper uses a neural network to model the quantum state of a number of electrons.}

\figure{\includegif{\diagramsDir/physics/many-electron-schroedinger}{40%}}{The many-electron Schrödinger equation is important in understanding how Chemical bonds are formed.}{many-electron-schroedinger}

\notes{Each of these simulations have the same property of being based on a set of (physical) rules about how particles interact. But one of the interesting characteristics of such systems is how the properties of the system are emergent as the dynamics are allowed to continue. 

These properties cannot be predicted without running the physics, or the equivalently the equation. Computation is required. And often the amount of computation that is required is prohibitive.}

\endif

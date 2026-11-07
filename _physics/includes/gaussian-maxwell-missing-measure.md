\ifndef{gaussianMaxwellMissingMeasure}
\define{gaussianMaxwellMissingMeasure}

\editme

\subsection{Gaussian, Maxwell--Boltzmann, and the Missing Measure}

\speakernotes{Composition wrapper only. Children carry the figures. As taught: open from Harry's speed-peak question and the anthropomorphic bridge, then histogram arithmetic, then the velocity-space shell before the 3D Maxwell pair. Stop before MaxEnt / Lagrange / the die.}

\notes{Entropy depends on which degrees of freedom you count. Jaynes, following Wigner, called that the anthropomorphic character of entropy: a given physical system corresponds to many thermodynamic systems, according to which variables you choose to control [@Jaynes-gibbs65]. Steam-table entropy omits degrees of freedom that the tables do not treat (nuclear spins are the classic unused reservoir). Two observers who neglect different parts of the uncertainty can still share a consistent account of what they *do* measure, because the same functional form of $H$ sits underneath. That is the bridge into Harry's question. Each Cartesian velocity component peaks at zero; the speed histogram of the three-dimensional system does not. The disagreement is not only a change of the underlying measure: it is a change of variable, a grouping of directions, and a change of measure.}

\include{_physics/includes/gaussian-histogram-discrete-entropy.md}
\include{_physics/includes/velocity-vs-modulus-1d.md}
\include{_physics/includes/velocity-space-shell-2d.md}
\include{_physics/includes/velocity-vs-speed-3d.md}
\include{_physics/includes/pushed-bins-same-entropy.md}
\include{_information/includes/log-delta-divergence.md}
\include{_physics/includes/maxwell-speed-histogram-entropy.md}
\include{_physics/includes/mb-uniform-vs-pushed-discretisation.md}
\include{_information/includes/discrete-jacobian-radon-nikodym.md}
\include{_information/includes/radon-nikodym-density-ratio.md}
\include{_physics/includes/jaynes-limiting-density.md}

\endif

\ifndef{f1SimulationFidelity}
\define{f1SimulationFidelity}

\editme

\subsection{F1 and Fidelity}

\notes{Formula 1 race simulations contain assumptions that derive from physics but don't directly encode the physical laws. For example, if one car is stuck behind another, in any given lap, it might overtake. A typical race simulation will look at the lap speed of each car and the top speed of each car (as measured in 'speed traps' that are placed on the straight). It will assume a probability of overtake for each lap that is a function of these values. Of course, underlying that function is the physics of how cars overtake each other, but that can be abstracted away into a simpler function that the Race Strategy Engineer defines from their knowledge and previous experience.}

\notes{Many simulations have this characteristic: major parts of the simulation are the result of encoding expert knowledge in the code. But this can lead to challenges. I once asked a strategy engineer, who had completed a new simulation, how it was going. He replied that things had started out well, but over time its performance was degrading. We discussed this for a while and over time a challenge of mis-specified granularity emerged.}


\slides{* Simulations work at different fidelities
    * F1 Race Strategy vs Aerodynamics
* Must maintain consistent granularity
* Adding detail can degrade performance}


\notes{The engineer explained how there'd been a race where the simulation had suggested that their main driver *shouldn't* pit because he would have emerged behind a car with a slower lap speed, but a high top-speed. This would have made that car difficult to overtake. However, the driver of that slower car was also in the team's 'development program', so everyone in the team knew that the slower car would have moved aside to let their driver through. Unfortunately, the simulation didn't know this. So, the team felt the wrong stategy decision was made. After the race, the simulation was updated to include a special case for this situation. The new code checked whether the slower car was a development driver, making it 'more realistic'.

Over time there were a number of similar changes, each of which should have improved the simulation, but the reality was the code was now 'mixing granularities'. The formula for computing the probability of overtake as a function of speeds is one that is relatively easy to verify. It ignores the relationships between drivers, whether a given driver is a development driver, whether one bears a grudge or not, whether one is fighting for their place in the team. That's all assimilated into the equation. The original equation is easy to calibrate, but as soon as you move to a finer granularity and consider more details about individual drivers, the model seems more realistic, but it becomes difficult to specify, and therefore performance degrades.}

\notes{Simulations work at different fidelities, but as the Formula 1 example shows you must be very careful about mixing fidelities within the same simulation. The appropriate fidelity of a simulation is strongly dependent on the question being asked of it. On the context. For example, in Formula 1 races you can also simulate the performance of the car in the wind tunnel and using computational fluid dynamics representations of the Navier-Stokes equations. That level of fidelity *is* appropriate when designing the aerodynamic components of the car, but inappropriate when building a strategy simulation.}

\notes{The original overtaking probability calculations were clean and verifiable. But by mixing in team politics and driver relationships, they created a model that was harder to specify correctly.

The same team also uses highly detailed aerodynamics simulations with computational fluid dynamics for car design. This different fidelity is appropriate there - but mixing fidelities within a single simulation often causes more problems than it solves. The key is maintaining consistent granularity appropriate to the specific question being asked.}

\endif

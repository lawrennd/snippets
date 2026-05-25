\ifndef{classicalObserverVelocities}
\define{classicalObserverVelocities}
\editme


\subsection{The Classical Observer}

\figure{\includediagramclass{\diagramsDir/physics/observer-composite-independent}{90%}}{Here the observer is monitoring the movements of the particles. We've plotted the velocities alongside the 1 standard deviation contour of their theoretical distribution.}{observer-composite-independent}

\subsection{The Classical Observer - Correlated}

\figure{\includediagramclass{\diagramsDir/physics/observer-composite-correlated}{90%}}{Again the observer is monitoring the movements of the particles, but here their motion is correlated ($\rho=0.95$).}{observer-composite-correlated}

\subsection{The Classical Observer - Anti-correlated}

\figure{\includediagramclass{\diagramsDir/physics/observer-composite-anti-correlated}{90%}}{Here the observer is monitoring the movements of the particles, but here their motion is anti-correlated ($\rho=-0.95$).}{observer-composite-anti-correlated}

\narration{Conceptually, imagine a classic physics setup where you can see inside a box: there are a number of particles moving around, sampled from random Gaussians. If you plot their velocities, they sit within a circle. In this case, the marginal $h_i$ would be their velocity in each direction. The marginal distribution in each direction is Gaussian. Now, if the particles are correlated — everything tending to move in one diagonal direction — interestingly, the marginal entropies are the same. Although these are correlated, I'm not saying anything about the correlation when I conserve the marginal entropies, because if you look at the marginal distribution in each direction, it's the same as in the uncorrelated case. And if they're anti-correlated, it's the same again. So I'm not making any statements about independence with this constraint.}

\endif

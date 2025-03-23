\ifndef{entropyGameIntroduction}
\define{entropyGameIntroduction}

\editme

\section{The Entropy Game}

\notes{The Entropy Game is a framework for understanding efficient uncertainty reduction. To start think of finding the optimal strategy for identifying an unknown entity by asking the minimum number of yes/no questions.}

\slides{
* Intelligence as optimal uncertainty reduction
  * 20 Questions game as intuitive example
  * Binary search exemplifies optimal strategy
* Information gain measures question quality
  * Wordle as a more complex example
}

\subsection{The 20 Questions Paradigm}

\notes{In the game of 20 Questions player one (Alice) thinks of an object, player two (Bob) must identify it by asking at most 20 yes/no questions. The optimal strategy is to divide the possibility space in half with each question. The binary search approach ensures maximum information gain with each inquiry and can access $2^20$ or abou a million different objects.}

\figure{\includediagram{\diagramsDir/information/binary-search-tree}{70%}}{The optimal strategy in the Entropy Game resembles a binary search, dividing the search space in half with each question.}{binary-search-tree}

\subsection{Entropy Reduction as Intelligence}

\notes{From an information-theoretic perspective, intelligence can be viewed as the capacity to efficiently reduce entropy - the uncertainty about the state of the world. Each observation or action an intelligent agent takes should maximize expected information gain, optimally reducing uncertainty given available resources.}

\slides{
* Entropy before question: $S(X)$
* Entropy after answer: $S(X|M)$
* Information gain: $I(X;M) = S(X) - S(X|M)$
* Intelligent systems maximize $I(X;M)$ per unit cost
}
\notes{The entropy before the question is $S(X)$. The entropy after the question is $S(X|M)$. The information gain is the difference between the two, $I(X;M) = S(X) - S(X|M)$. Intelligent systems maximize this information gain per unit cost.}

\notes{This framework helps explain why both biological and artificial intelligence systems appear to behave as if they're performing active inference - constantly generating predictions and updating models to minimize surprise and uncertainty. The entropy game reveals intelligence as a process of efficiently navigating information landscapes.}

\subsection{Thermodynamic Parallels}

\notes{The entropy game connects to thermodynamics through the concept of work. In thermodynamics, extracting work from a system requires reducing its entropy. Similarly, meaningful intelligent action requires reducing uncertainty about the environment. Both processes can be understood as converting free energy into useful work - whether physical work or informational value.}

\slides{
* Intelligence requires work to reduce uncertainty
* Thermodynamic work reduces physical entropy
* Both operate under resource constraints
* Both bound by fundamental efficiency limits
}

\notes{This perspective suggests a profound connection: intelligence might be understood as a special case of systems that efficiently extract, process, and utilize free energy from their environments, with thermodynamic principles setting fundamental constraints on what's possible.}

\subsection{Jaynes' World: An Entropy Game}

\notes{Jaynes' World is a zero-player game that implements a version of the entropy game. The dynamical system is defined by a distribution, $\rho(Z)$, over a state space $Z$. The state space is partitioned into observable variables $X$ and memory variables $M$. The memory variables are considered to be in an *information resevoir*, a thermodynamic system that maintains information in an ordered state (see e.g. Barato-stochastic14).}

\notes{Our system evolves mathematically according to gradient ascent on the entropy, $S(Z)$. This entropy is bounded from above by $N$ and below by 0.}

\notes{As a thought experiment we can imagine both the start point and end point of the system. The start point should be minimal entropy, and the end point should be maximal entropy. This allows us to conclude that the system must belong to the exponential family. As Jaynes has shown [@Jaynes-information57], the stationary points of a free-form optimisation of the distribution form are given by the *expoential family*.}
$$
\rho(Z) = \exp(\boldsymbol{\theta}^\top T(Z) - A(\boldsymbol{\theta})),
$$
where $T(Z)$ are sufficient statistics, $A(\boldsymbol{\theta})$ is the log-partition function, $\boldsymbol{\theta}$ are the *natural parameters*.

In exponential family distributions, the entropy gradient relates directly to Fisher information:

$\nabla_{\boldsymbol{\theta}}S = I(\boldsymbol{\theta})(\boldsymbol{\theta}_0 - \boldsymbol{\theta})$

The Fisher information matrix $I(\boldsymbol{\theta})$ defines the natural geometry of the parameter space:

$I(\boldsymbol{\theta}) = \nabla^2_{\boldsymbol{\theta}} A(\boldsymbol{\theta}) = \text{Cov}[T(Z)]$

\subsection{Fourier Duality}

\notes{One challenge is how to parameterise our exponential family. We've mentioned that the variables $Z$ are partitioned into observable variables $X$ and memory variables $M$. Given the minimal entropy initial state, the obvious initial choice is that at the origin all variables, $Z$, should be in the information reservoir, $M$. This implies that they are well determined and present a sensible choice for the source of our parameters, we define a mapping,  $\boldsymbol{\theta}(M)$ that maps the information resevoir to natural parameters and we assume that the entropy of these parameters $S(\boldsymbol{\theta})$ is so low as to be neglibible. allowing us to rewrite the distribution in a conditional form.}


   - $c(M)$: Maps to high-entropy capacity variables

- *Parameter-Capacity Uncertainty*: $\Delta\boldsymbol{\theta}(M) \cdot \Delta c(M) \geq k$



Parameters $\boldsymbol{\theta}(M)$ and capacity variables $c(M)$ form a Fourier-dual pair,
$$
c(M) = \mathcal{F}[\boldsymbol{\theta}(M)],
$$
This duality is particularly important at saddle points where direct gradient ascent stalls.

\subsection{Markovian Decomposition}

\notes{Now $X$ is further divided into past/present $X_0$ and future $X_1$. The entropy can be decomposed into a Markovian componen, where $X_0$ and $X_1$ are conditionally independent given $M$ and a non-Markovian component. The conditional mutual information is 
$$
I(X_0; X_1 | M) =,
$$

\subsection{System Evolution}

\subsection{Start State (origin, turn 0)}

- Low entropy, near lower bound
- Highly structured information in $M$
- Strong temporal dependencies (high non-Markovian component)
- Precise parameters, uncertain capacity (per uncertainty principle)

\subsection{End State}

- Maximum entropy, approaching upper bound $N$
- Parameter saturation where $\nabla_{\boldsymbol{\theta}}S \approx 0$
- Primarily Markovian dynamics
- Steady state with no further entropy increase possible

\section{Information Geometry}

\subsection{Fisher Information}



\subsection{Saddle Point}

\notes{Saddle points represent critical transitions where}

\notes{
- Gradient $\nabla_{\boldsymbol{\theta}}S \approx 0$
- The Fisher information matrix $I(\boldsymbol{\theta})$ has eigenvalues with significantly different magnitudes
- The system must leverage Fourier duality to continue entropy production
- Phase transitions occur between parameter-dominated and capacity-dominated regimes
}


\subsection{Variable Transitions}

\notes{How do the $z_i$ variables transitoin between $X$ and $M$? We need an approach to identifing when the character of the variables has changed.}

\notes{We introduce the moment generating function (MGF) to help identify transition candidates,}
$$
M_Z(t) = E[e^{t \cdot Z}] = \exp(A(\boldsymbol{\theta}+t) - A(\boldsymbol{\theta}))
$$
\notes{Variables transition when their contribution to cumulants changes significantly.}

\subsection{Saddle Point Seeking Behaviour}

\notes{The use of the exponential family would allow us to ascend the *natural gradient* instead of the steepest ascent direction.}

\subsection{Conceptual Framework}

\notes{The entropy game illustrates fundamental principles of information dynamics.}

\notes{
1. *Information Conservation*: Total information remains constant but redistributes between structure and randomness

2. *Uncertainty Principle*: Precision in parameters trades off with entropy capacity

3. *Self-Organization*: The system autonomously navigates toward maximum entropy while maintaining necessary structure
}

\notes{The zero-player game provides a mathematical model for studying how complex systems evolve when they instantaneously maximize entropy production.}

\endif 
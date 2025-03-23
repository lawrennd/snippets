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

\subsection{Entropy Reduction and Decisions}

\notes{From an information-theoretic perspective, decisions can be taken in a way that efficiently reduces entropy - our the uncertainty about the state of the world. Each observation or action an intelligent agent takes should maximize expected information gain, optimally reducing uncertainty given available resources.}

\slides{
* Entropy before question: $S(X)$
* Entropy after answer: $S(X|M)$
* Information gain: $I(X;M) = S(X) - S(X|M)$
* Intelligent systems maximize $I(X;M)$ per unit cost
}
\notes{The entropy before the question is $S(X)$. The entropy after the question is $S(X|M)$. The information gain is the difference between the two, $I(X;M) = S(X) - S(X|M)$. Optimal decision making systems maximize this information gain per unit cost.}

\subsection{Thermodynamic Parallels}

\notes{The entropy game connects decision making to thermodynamics.}

\slides{
* Intelligence requires work to reduce uncertainty
* Thermodynamic work reduces physical entropy
* Both operate under resource constraints
* Both bound by fundamental efficiency limits
}

\notes{This perspective suggests a profound connection: intelligence might be understood as a special case of systems that efficiently extract, process, and utilize free energy from their environments, with thermodynamic principles setting fundamental constraints on what's possible.}

\subsection{Jaynes' World: A Different Type of Entropy Game}

\notes{Jaynes' World is a zero-player game that implements a version of the entropy game. The dynamical system is defined by a distribution, $\rho(Z)$, over a state space $Z$. The state space is partitioned into observable variables $X$ and memory variables $M$. The memory variables are considered to be in an *information resevoir*, a thermodynamic system that maintains information in an ordered state (see e.g. Barato-stochastic14). The entropy of the whole system is bounded below by 0 and above by $N$. So the entropy forms a *compact manifold* with respect to its parameters.}

\notes{Unlike the animal game, where decisions are made by reducing entropy at each step, our system evovles mathematically by maximising the instantaneous entropy production. Conceptually we can think of this as *ascending* the gradient of the entropy, $S(Z)$. }

\notes{In the animal game the questioner starts with maximum uncertainty and targets minimal uncertainty. Jaynes' world starts with minimal uncertainty and aims for maximum uncertainty.}

\notes{We can phrase this as a thought experiment. Imagine you are in the game, at a given turn. You want to see where the game came from, so you look back across turns. The direction the game came from is now the direction of steepest descent. Regardless of where the game actually started it looks like it started at a minimal entropy configuration that we call the *origin*. Similarly, wherever the game is actually stopped there will nevertheless appear to be an end point we call *end* that will be a configuration of maximal entropy, $N$.}

\notes{This speculation allows us to impose the functional form of our proability distribution. As Jaynes has shown [@Jaynes-information57], the stationary points of a free-form optimisation (minimum or maximum) will place the distribution in the, $\rho(Z)$ in the *expoential family*,}
$$
\rho(Z) = h(Z) \exp(\boldsymbol{\theta}^\top T(Z) - A(\boldsymbol{\theta})),
$$
where $h(Z)$ is the base measure, $T(Z)$ are sufficient statistics, $A(\boldsymbol{\theta})$ is the log-partition function, $\boldsymbol{\theta}$ are the *natural parameters* of the distribution.}

\notes{This constraint to the exponential family is highly convenient as we will rely on it heavily for the dynamics of the game. In particular, by focussing on the *natural parameters* we find that we are optimising within an *information geometry* [@Amari-geometry]. In exponential family distributions, the entropy gradient is given by,
\[
\nabla_{\boldsymbol{\theta}}S(Z)  = \mathbf{g} = 
\]
And the Fisher information matrix, $G(\boldsymbol{\theta})$, is also the *Hessian* of the manifold,
\[
G(\boldsymbol{\theta}) = \nabla^2_{\boldsymbol{\theta}} A(\boldsymbol{\theta}) = \text{Cov}[T(Z)].
\]
Traditionally, when optimising on an information geometry we take *natural gradient* steps, equivalen to a Newton minimisation step,
\[
\Delta \boldsymbol{\theta} = - G(\boldsymbol{\theta})^{-1} \mathbf{g},
\]
but this is not the direction that gives the instantaneious maximisation of the entropy production, instead our gradient step is tiven by 
\[
\Delta \boldsymbol{\theta} = \eta \mathbf{g},
\]
where $\eta$ is a 'learning rate'.}

\subsection{Fourier Duality}

\notes{One challenge is how to parameterise our exponential family. We've mentioned that the variables $Z$ are partitioned into observable variables $X$ and memory variables $M$. Given the minimal entropy initial state, the obvious initial choice is that at the origin all variables, $Z$, should be in the information reservoir, $M$. This implies that they are well determined and present a sensible choice for the source of our parameters.}

\notes{We define a mapping, $\boldsymbol{\theta}(M)$, that maps the information resevoir to a set of values that are equivalent to the *natural parameters*. If the entropy of these parameters is low, and the distribution $\rho(\boldsymbol{\theta})$ is sharply peaked then we can move from treating the memory mapping, $\boldsymbol{\theta}(\cdot)$, as a random processe to an assumption that it is a deterministic function. We can then follow gradients with respect to these $\boldsymbol{\theta}$ values.}

\notes{This allows us to rewrite the distribution over $Z$ in a conditional form,
$$
\rho(X|M) = h(X) \exp(\boldsymbol{\theta}(M)^\top T(X) - A(\boldsymbol{\theta}(M))).
$$
}
\notes{A word of warning here, this assumption implies that $\boldsymbol{\theta}(\cdot)$ is a delta function, and our representation as a compact manifold (bounded below by $0$ and above by $N$) does not admit any singularities. To see the direct challenges this approximation brings we'll now consider a Markovian decomposition of our system.}

then we can expand around the values $\boldsymbol{\theta}$  and we assume that the entropy of these parameters $S(\boldsymbol{\theta})$ is so low as to be neglibible. allowing us to rewrite the distribution in a conditional form.
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

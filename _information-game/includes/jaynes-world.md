\ifndef{jaynesWorld}
\define{jaynesWorld}

\editme

\subsection{Jaynes' World}

\notes{Jaynes' World is a zero-player game that implements a version of the entropy game. The dynamical system is defined by a distribution, $\rho(Z)$, over a state space $Z$. The state space is partitioned into observable variables $X$ and memory variables $M$. The memory variables are considered to be in an *information resevoir*, a thermodynamic system that maintains information in an ordered state (see e.g. Barato-stochastic14). The entropy of the whole system is bounded below by 0 and above by $N$. So the entropy forms a *compact manifold* with respect to its parameters.}

\notes{Unlike the animal game, where decisions are made by reducing entropy at each step, our system evovles mathematically by maximising the instantaneous entropy production. Conceptually we can think of this as *ascending* the gradient of the entropy, $S(Z)$. }

\notes{In the animal game the questioner starts with maximum uncertainty and targets minimal uncertainty. Jaynes' world starts with minimal uncertainty and aims for maximum uncertainty.}

\notes{We can phrase this as a thought experiment. Imagine you are in the game, at a given turn. You want to see where the game came from, so you look back across turns. The direction the game came from is now the direction of steepest descent. Regardless of where the game actually started it looks like it started at a minimal entropy configuration that we call the *origin*. Similarly, wherever the game is actually stopped there will nevertheless appear to be an end point we call *end* that will be a configuration of maximal entropy, $N$.}

\notes{This speculation allows us to impose the functional form of our proability distribution. As Jaynes has shown [@Jaynes-information57], the stationary points of a free-form optimisation (minimum or maximum) will place the distribution in the, $\rho(Z)$ in the *expoential family*,}
$$
\rho(Z) = h(Z) \exp(\boldsymbol{\theta}^\top T(Z) - A(\boldsymbol{\theta})),
$$
where $h(Z)$ is the base measure, $T(Z)$ are sufficient statistics, $A(\boldsymbol{\theta})$ is the log-partition function, $\boldsymbol{\theta}$ are the *natural parameters* of the distribution.}

\notes{This constraint to the exponential family is highly convenient as we will rely on it heavily for the dynamics of the game. In particular, by focussing on the *natural parameters* we find that we are optimising within an *information geometry* [@Amari-information16]. In exponential family distributions, the entropy gradient is given by,
$$
\nabla_{\boldsymbol{\theta}}S(Z) = \mathbf{g} = \nabla^2_\boldsymbol{\theta} A(\boldsymbol{\theta}(M))
$$
And the Fisher information matrix, $G(\boldsymbol{\theta})$, is also the *Hessian* of the manifold,
$$
G(\boldsymbol{\theta}) = \nabla^2_{\boldsymbol{\theta}} A(\boldsymbol{\theta}) = \text{Cov}[T(Z)].
$$
Traditionally, when optimising on an information geometry we take *natural gradient* steps, equivalen to a Newton minimisation step,
$$
\Delta \boldsymbol{\theta} = - G(\boldsymbol{\theta})^{-1} \mathbf{g},
$$
but this is not the direction that gives the instantaneious maximisation of the entropy production, instead our gradient step is given by 
$$
\Delta \boldsymbol{\theta} = \eta \mathbf{g},
$$
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

\subsection{Markovian Decomposition}

\notes{Now $X$ is further divided into past/present $X_0$ and future $X_1$. The entropy can be decomposed into a Markovian component, where $X_0$ and $X_1$ are conditionally independent given $M$ and a non-Markovian component. The conditional mutual information is 
$$
I(X_0; X_1 | M) = \sum_{x_0,x_1,m} p(x_0,x_1,m) \log \frac{p(x_0,x_1|m)}{p(x_0|m)p(x_1|m)},
$$
which measures the remaining dependency between past and future given the memory state. This leads to a key insight about memory capacity: effective information reservoirs must minimize this conditional mutual information while maintaining minimal entropy.}

\notes{When $I(X_0; X_1 | M) = 0$, the system becomes perfectly Markovian - the memory variables capture all dependencies between past and future. However, achieving this perfect Markovianity while maintaining minimal entropy in $M$ will create a fundamental tension that drives an *uncertainty principle*.}

\subsection{System Evolution}

\notes{We are now in a position to summarise the start state and the end state of our system, as well as to speculate on the nature of the transition between the two states.}

\subsection{Start State}

\notes{The *origin configuration* is a low entropy state, with value near the lower bound of 0. The information is highly structured, by definition we place all variables in $M$, the information resevoir at this time. The uncertainty principle is present to handle the competeing needs of precision in parameters (giving us the near-singular form for $\boldsymbol{\theta}(M)$, and capacity in the information channel that $M$ provides (the capacity $c(\boldsymbol{\theta})$ is upper bounded by $S(M)$.}  

\slides{
- Low entropy, near lower bound
- Highly structured information in $M$
- Strong temporal dependencies (high non-Markovian component)
- Precise values for $\boldsymbol{\theta}$ uncertainty in other parameter characteristics.
}

\subsection{End State}

\notes{The *end configuration* is a high entropy state,
}

\slides{
- Maximum entropy, approaching upper bound $N$
- Zeno's paradox:  $\nabla_{\boldsymbol{\theta}}S \approx 0$
- Primarily Markovian dynamics
- Steady state with no further entropy increase possible
}

\endif

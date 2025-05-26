\ifndef{provocationQuestions}
\define{provocationQuestions}


\section{The Information Game and Conservation}

\subsection{Exercise 1: System Setup}

\notes{Imagine a game across $N$ variables, $Z$. The variables are separated as *latent*, $M$, or *active*, $X$ and the sum of marginal entropy of variables is constrained
$$
\sum_{i=1}^N S(z_i) = N\log 2.
$$

The latent variable's marginal entropy is given by
$$
S(m_i) = \log 2,
$$
whereas an active variable's marginal entropy is given by the Shannon entropy,
$$
S(x_i) = -\sum_j p_j \log p_j.
$$
The only parameters of this system are $N$, which will always be fixed, and what variables are partitioned as latent and what variables are partitioned as active which we will allow to vary.

*Task*: Show that for this system the sum of the joint entropy $S(Z)$ and  the multi information $I(Z)$ is also conserved.}

\subsection{Exercise 2: Initial Conditions}

\notes{In many physical systems we associate increases in entropy, $S(Z)$, with the arrow of time. We assume that the game proceeds at each turn by adjusting the partition to maximise instantaneous entropy production in the system.

This implies that wherever we are in the game, if we look back across turns eventually we arrive at the game *origin* point where $S(Z)$ should be zero. 

*Task*: (i) Show that at the origin point we face a paradoxical situation where the sum of marginal entropies is $N \log 2$ but the joint entropy is zero. 

(ii) Draw a parallel with a maximally entangled quantum pure state to provide an existence proof that this paradox can be resolved.

(iii) Show that these constraints are sufficient to provide a unique mathematical solution for the origin where all variables are partitioned into as latent $M$ an the joint entropy of $M$ is given by the von Neumann entropy of a density matrix.

(iv) Due to the under specification of this maximum mutual information state, this formulation has a gauge symmetry. Argue that the mathematical complexity of the gauge symmetry arises from the "under specification" of the initial constraints.}

\subsection{Exercise 3: Quantifying the Latent Activation}

\notes{As turns proceed in the game  entropy is produced by variables moving from the latent $M$ partition to the active $X$ partition. 

*Task*: By considering a single variable, and recalling that each turn maximises entropy production, show how the probabilities of the active variable $X$, $p_j$, relate to the density matrix, $\rho$.


\subsection{Exercise 4: Exchangeability in the Game}

\notes{The simple structure of this system hints that the game may have an exchangeability property reminiscient of de Finetti's. 

*Task*: Show that this is indeed the case and explain how this leads to the apparent paradox that fully entangled variables, $M$, can emit active variables that seem to be distrubuted identically and independently.} 

\subsection{Exercise 5: Hierarchical Partition and the Exponential Family}

\notes{*Task* (i) As variables transit from $M$ to $X$ motivate why this might trigger a further dynamic partition between latent variables, $M_p$ and $M_d$ where $M_p$ remains relatively stable across a long series of turns. 

(ii) Show that across the timescale where such effective parameters remained stable they would trigger local conservation laws where the entropy and multi informations are now conditioned on $M_p$.

(iii) Recalling our maximisation of instantaneous entropy production argue why it's the case that in these circumstances the active variables, $X$, will always be governed by a distribution in the exponential family.

(iv) Show that the resulting joint entropy of $S(Z)$ will be dependent on a set of natural parameters that correspond to the effective parameters, $\theta(M_p)$.

(v) Explain how any invariances in this function will lead to further symmetries in the resulting effective physics and what Noether's theorem tells us about how these invariances would manifest in the game's physics.}

\subsection{Exercise 6: Action Principles and Information Dynamics}

\notes{Action principles allow us to derive dynamical equations through Lagrangian's formed from kinetic and potential energies under the assumption that the sum of the two are conserved. By viewing the multi-information, $I(X, M_d| \theta(M_p))$ as analogous to potential energy and the entropy, $S(X, M_d|\theta(M_p))$.

An information action principle that is consistent with our game,
$$
\mathcal{S} = \int\left[S(X, M_d|\theta(M_p)) - I(X, M_d|\theta(M_p))\right]\text{d} \tau
$$
where turns are indexed by $\tau$.

Recall Frieden's Extreme Physical Information principle, which relates *bound* and *free* Fisher information, where *bound* is not available to the observer and *free* is available. 

*Task*: (i) By equating the bound term to the multi-information and the free term to the joint entropy explain the philosophical difference between the approaches.

(ii) Given we have already shown that the entropy is based on a exponential family/density matrix form, show how expanding around the equilibrium leads to an action principle that is equivalent to EPI.

(iii) Show that a unified form of the two actions can be given by
$$
\mathcal{S} = \int G_ij(\theta(M_p)) \frac{\text{d}\theta_i(M_p)}{\text{d}\tau}\frac{\text{d}\theta_j(M_p)}{\text{d}\tau} - I(X, M_d|\theta(M_p)) \text{d}\tau
$$
where EPI is recovered when $\frac{\text{d}\theta(M_p)}{\text{d}\tau} = 0$.}

\endif
Can you produce my series of questions that prompted you in a markdown form?​​​​​​​​​​​​​​​​

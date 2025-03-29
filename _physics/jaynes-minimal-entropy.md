\ifndef{jaynesMinimalEntropy}
\define{jaynesMinimalEntropy}

\editme

\subsection{From Maximum to Minimal Entropy}

\notes{Jaynes formulated his principle in terms of maximizing entropy, we can also view certain problems as minimizing entropy under appropriate constraints. The duality becomes apparent when we consider the relationship between entropy and information.}

\slides{
* Maximum entropy = minimum assumptions
* Minimal entropy = maximum structure/information
* Same mathematical framework, different constraints
}

\notes{The maximum entropy principle finds the distribution that is maximally noncommittal given certain constraints. Conversely, we can seek the distribution that minimizes entropy subject to different constraints - this represents the distribution with maximum structure or information.}

\notes{Consider the uncertainty principle. When we seek states that minimize the product of position and momentum uncertainties, we are  seeking minimal entropy states subject to the constraint of the uncertainty principle.}

\notes{The mathematical formalism remains the same, but with different constraints and optimization direction,
\begin{align}
\text{Minimize } S_I &= -\sum_{i} p_i \log p_i \\
\text{subject to } \sum_{i} p_i &= 1 \\
\text{and } g_k(p_1, p_2, \ldots, p_n) &= G_k \quad k=1,2,\ldots,r,
\end{align}
where $g_k$ are functions representing constraints different from simple averages.}

\notes{The solution still takes the form of an exponential family,
\begin{align}
p_i = \frac{1}{Z}\exp\left(-\sum_{k=1}^r \mu_k \frac{\partial g_k}{\partial p_i}\right),
\end{align}
where $\mu_k$ are Lagrange multipliers for the constraints.}

\subsection{Minimal Entropy States in Quantum Systems}

\notes{The pure states of quantum mechanics are those that minimize von Neumann entropy $S = -\text{Tr}(\rho \log \rho)$ subject to the constraints of quantum mechanics.}

\notes{For example, coherent states minimize the entropy subject to constraints on the expectation values of position and momentum operators. These states achieve the minimum uncertainty allowed by quantum mechanics.}

\endif 
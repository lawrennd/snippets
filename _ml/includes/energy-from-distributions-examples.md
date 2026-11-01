\ifndef{energyFromDistributionsExamples}
\define{energyFromDistributionsExamples}
\editme

\subsection{Energies from Distributions You Already Know}

\notes{The map $p\propto e^{-E}$ runs both ways. Given a distribution we already introduced, set
$$
E_i = -\log p_i
$$
(up to an additive constant that cancels in the normalisation). High probability is low energy. For each classic family we plot $P$ (or $p$) beside $E=-\log P$, then overlay the two on twin axes.}

\newslide{From $p$ to $E$: Four Outcomes}

\slides{Tabulate $-\log P(y)$ for a four-outcome distribution. Those values *are* energies.}

\slides{
$y$               |   1   |   2   |   3   |   4
------------------|-------|-------|-------|-------
$P(y)$            |  0.3  |  0.2  |  0.1  |  0.4
$E(y)=-\log P(y)$ | 1.204 | 1.609 | 2.302 | 0.916
}

\slidesincremental{
* Most probable outcome $y=4$ has the *lowest* energy
* Rarest $y=3$ has the *highest* energy
* Shannon entropy is $\mathbb{E}[E(y)] = 1.280$ nats --- average energy under $p$
}

\notes{Exponentiating recovers the distribution (natural units): $p(y)=e^{-E(y)}$ already normalises here because we took $E=-\log p$ exactly. In general one writes $p_i = e^{-E_i}/Z$ with $Z=\sum_j e^{-E_j}$. Shannon entropy of this table is therefore also an average energy.}

\speakernotes{Do not recompute; only rename $-\log p$ as $E$.}

\newslide{Bernoulli / Fair Coin}

\slides{A coin with $P(H)=p$, $P(T)=1-p$ is a two-state energy model.}

\include{_ml/includes/bernoulli-energy-from-distribution.md}

\notes{A fair coin has equal energies on heads and tails; uncertainty is maximal. A biased coin tilts the energy landscape. The same grammar appears as a two-level thermal system: fix energies $E_0,E_1$ and coldness $\beta$, then
$$
p_1 = \frac{e^{-\beta E_1}}{e^{-\beta E_0}+e^{-\beta E_1}},
$$
which is Bernoulli with that success probability. Week 2 returns to the two-state occupation.}

\newslide{Poisson: Count Energy}

\slides{A Poisson($\lambda$) is the same map $E=-\log P$ on the non-negative integers.}

\include{_ml/includes/poisson-energy-from-distribution.md}

\newslide{Gaussian: Quadratic Energy}

\slides{The univariate Gaussian we wrote earlier is already an energy-based model.}

\slides{
$$
p(y)\propto \exp\!\left(-\frac{(y-\mu)^2}{2\sigma^2}\right)
\quad\Longleftrightarrow\quad
E(y)=\frac{(y-\mu)^2}{2\sigma^2}
$$
}

\include{_ml/includes/gaussian-energy-from-distribution.md}

\notes{Reading the Gaussian density as $p\propto e^{-E}$ makes the link to regression immediate: minimising $\sum_n(y_n-\mathbf{w}^\top\mathbf{x}_n)^2$ is minimising a sum of quadratic energies, which is maximum likelihood under independent Gaussian noise. The continuous normaliser plays the role of $Z$.}

\speakernotes{One look at the parabola under the height Gaussian is enough. Then jump to the least-squares slide with recognition rather than a new idea.}

\endif

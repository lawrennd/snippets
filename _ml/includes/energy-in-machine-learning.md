\ifndef{energyInMachineLearning}
\define{energyInMachineLearning}
\editme

\subsection{Energy in Machine Learning}

\notes{An *energy* in machine learning is a scalar score on a configuration: parameters, predictions, or binary states. Lower is preferred. An *energy-based model* turns that score into a distribution by the same exponential map used in statistical physics: $p(x)\propto e^{-E(x)}$. Training often amounts to shaping $E$ so that observed configurations sit in low-energy valleys. The examples below are familiar losses rewritten in that language --- not new algorithms.}

\newslides{Energy as a Score}

\slides{In ML, an *energy* is a scalar assigned to a configuration: lower means preferred.}

\slidesincremental{
* Losses are energies over parameters or predictions
* Energy-based model: $p(x)\propto e^{-E(x)}$ --- same grammar as Boltzmann
* Minimising $E$ is the zero-temperature / MAP limit
}

\newslides{Quadratic Energy (Regression)}

\slides{
$$
E(\mathbf{w})=\sum_n\left(y_n-\mathbf{w}^\top\mathbf{x}_n\right)^2
$$
}

\slidesincremental{
* Least squares = energy of the residual
* Gaussian negative log-likelihood (up to additives and scale)
* Gauss already linked this quadratic energy to the normal density
}

\notes{Under $y_n=\mathbf{w}^\top\mathbf{x}_n+\varepsilon_n$ with $\varepsilon_n\sim\gaussianSamp{0}{\sigma^2}$, the negative log-likelihood is $\frac{1}{2\sigma^2}E(\mathbf{w})$ plus constants. So ordinary least squares *is* maximum likelihood for a Gaussian or equivalently, minimising a quadratic energy.}

\newslides{Cross-Entropy Energy (Classification)}

\slides{
$$
E=-\sum_c y_c\log\hat{y}_c
$$
}

\slidesincremental{
* Cross-entropy / log-loss scores the predictive distribution
* Softmax: $\hat{y}_c\propto e^{-E_c}$ --- class scores as energies
* Same arithmetic as $\mathbb{E}[-\log p]$ (Shannon entropy of a model)
}

\notes{When $y$ is a one-hot label and $\hat{y}$ a categorical prediction, cross-entropy is the energy of that pair. Softmax turns a vector of class energies (or logits) into a distribution. The functional $-\log\hat{y}_c$ is the same one that appears in Shannon entropy $\mathbb{E}[-\log P(y)]$, applied to a *model* distribution rather than the data distribution.}

\newslides{Boltzmann Machine: Pairwise Energy}

\slides{
$$
E(\mathbf{s})=-\sum_i b_i s_i-\sum_{i<j}W_{ij}s_i s_j
$$
}

\slidesincremental{
* Binary units $s_i\in\{0,1\}$ or $\{\pm 1\}$
* Biases plus pairwise couplings --- classic BM has no triple terms
* $p(\mathbf{s})\propto e^{-E(\mathbf{s})/T}$: a learnable Gibbs distribution
}

\speakernotes{Name only. No contrastive divergence. Hopfield is the fixed-weight cousin: recall as energy descent.}

\notes{Ackley, Hinton and Sejnowski [@Ackley-boltzmann85] made the couplings $W_{ij}$ learnable; Hopfield [@Hopfield:neural82] used a similar pairwise energy for associative memory with fixed weights. When a Boltzmann or Gibbs occupation is written $p\propto e^{-\beta E}$, the symbol $E$ is the same kind of object minimised in regression and classification --- a score over configurations, exponentiated into a distribution.}

\addreading{@Ackley-boltzmann85}{Boltzmann machines (optional colour)}
\addreading{@Hopfield:neural82}{Hopfield networks (optional colour)}

\endif

\ifndef{commonDistributionsEntropy}
\define{commonDistributionsEntropy}
\editme

\subsection{Entropy of Common Distributions}

\newslide{Entropy, Distribution by Distribution}

\slides{For each named family from the probability review: plot $P$, plot $-\log_2 P$, and form the summands $-P\log_2 P$.}

\ifdef{energyFromDistributionsExamples}
\slidesincremental{
* Left: the distribution itself --- same families as the energy overlays
* Middle: surprisal $-\log_2 P$ --- the energy $E=-\log P$ in *bits* ($E_{\mathrm{bits}}=E_{\mathrm{nats}}/\log 2$)
* Right: $-P\log_2 P$ --- average energy under $P$, i.e. Shannon entropy $H$
}

\notes{Shannon entropy is an expectation of surprisal: $H=\mathbb{E}[-\log_2 P(X)]$. When the energy-from-distribution examples are already on the board, the middle panel is the same object as $E=-\log P$, only in bits; the right-hand panel is the average energy that those overlays did not yet form. We walk Bernoulli, binomial, Poisson, multinomial/categorical, and Gaussian so each entropy sits next to its distribution (and, where we plotted it, its energy).}

\speakernotes{Callback to the energy overlays. Do not re-derive $E=-\log P$; only change units and take the expectation.}
\else
\slidesincremental{
* Left: the distribution itself
* Middle: surprisal $-\log_2 P$ (not called energy here)
* Right: $-P\log_2 P$ --- these are what sum (or integrate) to $H$
}

\notes{Shannon entropy is an expectation of surprisal: $H=\mathbb{E}[-\log_2 P(X)]$. The right-hand panel makes that literal. We walk the same five families as the probability review --- Bernoulli, binomial, Poisson, multinomial/categorical, Gaussian --- so the entropy of each object sits next to the object itself.}

\speakernotes{One visual grammar for every family. Keep the middle panel as ``surprisal'' / ``$-\log P$''; reserve ``energy'' for the ML / Boltzmann block.}
\endif

\newslide{Bernoulli and Binomial}

\slidesincremental{
* Bernoulli($p$): binary entropy $-p\log_2 p-(1-p)\log_2(1-p)$
* Binomial($n,p$): no elementary closed form; same three-panel sum
* Fair coin: $H=1$ bit
}

\include{_information/includes/bernoulli-entropy.md}
\include{_information/includes/binomial-entropy.md}

\newslide{Poisson and Multinomial}

\slidesincremental{
* Poisson($\lambda$): numerical sum over $k$; $\approx\tfrac12\log_2(2\pi e\lambda)$ for large $\lambda$
* Categorical / one multinomial trial: $H=-\sum_k p_k\log_2 p_k$
* Uniform on $K$ symbols: $H=\log_2 K$
}

\include{_information/includes/poisson-entropy.md}
\include{_information/includes/multinomial-entropy.md}

\newslide{Gaussian}

\slidesincremental{
* Differential entropy $h=-\int p\log_2 p\,\mathrm{d}y$
* Univariate Gaussian: $h=\tfrac12\log_2(2\pi e\sigma^2)$ bits
* Can be negative; not the same object as discrete $H$
}

\include{_information/includes/gaussian-entropy.md}

\endif

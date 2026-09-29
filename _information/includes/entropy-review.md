\ifndef{entropyReview}
\define{entropyReview}
\editme

\subsection{Entropy Review}

\include{_ml/includes/expectation-entropy-example.md}

\newslides{Uncertainty as a Number}

\slides{Shannon entropy turns a distribution into a scalar measure of uncertainty.}

\slidesincremental{
* Discrete: $H(p) = -\sum_i p_i \log p_i$
* Base 2: bits; natural log: nats
* Fair coin: $H=1$ bit; certain outcome: $H=0$
}

\notes{This is a *review* of the definition, not an axiomatic derivation. Enough fluency is needed to talk about entropy without confusing the symbol $H$ with heat, and to ask whether a claim is about uncertainty, coding length, or thermodynamic irreversibility. The expectations example above already computed $H$ as $\mathbb{E}[-\log P(y)]$.}

\newslides{What $H$ Is Not (Yet)}

\slidesincremental{
* Not yet Clausius's thermodynamic entropy — same formula, different job
* Not yet a channel-capacity theorem
* Operational split: entropy often *forbids*; probability *prescribes*
}

\notes{Thermodynamic entropy $S$ and Shannon $H$ share a functional form; in equilibrium statistical mechanics one often writes $S = kH$. Here, treat $H$ as uncertainty of a discrete distribution. When someone says "entropy," ask: entropy of *what*, under *which* operational reading?}

\newslides{Joint, Conditional, Chain Rule (Names Only)}

\slidesincremental{
* $H(X,Y)$ joint uncertainty
* $H(X\mid Y)$ residual uncertainty after observing $Y$
* Chain rule: $H(X,Y)=H(X)+H(Y\mid X)$
}

\speakernotes{Do not prove the chain rule here. Name it so later discussion can use the vocabulary.}

\endif

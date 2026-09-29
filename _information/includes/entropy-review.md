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

\notes{This is a *review* of the definition, not the axiomatic derivation (that is week 3 / LO2). You need enough fluency to ask an LLM about entropy without confusing the symbol $H$ with heat, and to probe whether a claim is about uncertainty, coding length, or thermodynamic irreversibility. The expectations example above already computed $H$ as $\mathbb{E}[-\log P(y)]$.}

\newslides{What $H$ Is Not (Yet)}

\slidesincremental{
* Not yet Clausius's thermodynamic entropy — same formula, different job
* Not yet a channel-capacity theorem
* Operational split for this course: entropy often *forbids*; probability *prescribes*
}

\notes{Thermodynamic entropy $S$ and Shannon $H$ will be connected formally in week 3 ($S = kH$ in equilibrium statistical mechanics). Today, treat $H$ as uncertainty of a discrete distribution. When an LLM says "entropy," ask: entropy of *what*, under *which* operational reading?}

\newslides{Joint, Conditional, Chain Rule (Names Only)}

\slidesincremental{
* $H(X,Y)$ joint uncertainty
* $H(X\mid Y)$ residual uncertainty after observing $Y$
* Chain rule: $H(X,Y)=H(X)+H(Y\mid X)$
}

\speakernotes{Do not prove the chain rule today. Name it so Worksheet 1 probes can use the vocabulary.}

\endif

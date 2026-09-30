\ifndef{entropyReview}
\define{entropyReview}
\editme

\subsection{Entropy Review}

\include{_ml/includes/expectation-entropy-example.md}

\newslides{Uncertainty as a Number}

\slides{Shannon entropy turns a distribution into a *scalar* measure of uncertainty.}

\slidesincremental{
* Discrete: $H(p) = -\sum_i p_i \log p_i$
* Base 2: bits; natural log: nats
* Fair coin: $H=1$ bit; certain outcome: $H=0$
}

\notes{Under Shannon's definition, entropy is dimensionless. It is the expectation of the negative log surprisal, $-\expSamp{\log P(\dataScalar)}$.}

\newslide{Shannon's definition is not yet ...}

\slidesincremental{
* ... Clausius's thermodynamic entropy (same formula, different motivation)
* ... a channel-capacity theorem
}

\newslide{Entropy: physical and anthropomorphic}

\slidesincremental{
}

\notes{Thermodynamic entropy $S$ and Shannon $H$ have a shared functional form, in equilibrium we can write $S = k_BH$, where $k_B$ is Boltzmann's constant, $k_B = 1.380649 \times 10^{-23} \tfrac{\text{kg}\text{m}^2 }{\text{s}^2 \text{K}}$. So there are two parts to a thermodynamic entropy, one is the uncertainty of a (discrete) distribution. The other translates that into units of work ($\text{J} = \tfrac{\text{kg}\text{m}^2 }{\text{s}^2}$) per Kelvin ($\tfrac{text{J}}{\text{K}}$). Boltzmann's constant makes entropy physical. When we multiply $S$ by temperature $T$ (in degrees Kelvin) we recover energy. But this also implies that there is a *choice*. @Jaynes-gibbs65 refers to this as the '"anthropomorphic" nature of entropy". A remark he credits to Eugene Wigner. He gives the example of thermodynamic steam tables.}

\notes{> If we work with a \emph{thermodynamic} system of \emph{n} degrees of freedom,
> the experimental entropy is a function $S_{0}(X_{1}\ldots X_{n})$ of
> $n$ independent variables. But the \emph{physical} system has any
> number of additional degrees of freedom $X_{n + 1},\ X_{n + 2}$, etc.
> We have to understand that these additional degrees of freedom are not
> to be tampered with during the experiments on the $n$ degrees of
> interest; otherwise one could easily produce *apparent violations of the
> second law.* @Jaynes-gibbs65 (my emphasis)
}

\notes{He goes on to give an example from entropy of steam (which is very important in the design of steam engines and power plants).

> For example, the engineers have their "steam tables," which give
> measured values of the entropy of superheated steam at various
> temperatures and pressures. But the H$_2$0 molecule has a
> large electric dipole moment; and so the entropy of steam depends
> appreciably on the electric field strength present. It must always be
> understood implicitly (because it is never stated explicitly) that this
> extra thermodynamic degree of freedom was not tampered with during the
> experiments on which the steam tables are based; which means, in this
> case, that the electric field was not inadvertently varied from one
> measurement to the next.
}

\notes{This leads him to a conclusion that is worth bearing in mind when we're talking about the physical meaning of entropy.}

\notes{
> Recognition that the "entropy of a physical system" is not meaningful
> without further qualifications is important in clarifying many questions
> concerning irreversibility and the second law. For example, I have been
> asked several times whether, in my opinion, a biological system, say a
> cat, which converts inanimate food into a highly organized structure and
> behavior, represents a violation of the second law. The answer I always
> give is that, until we specify the set of parameters which define the
> *thermodynamic state* of the cat, no definite question has been
> asked!
}

\notes{Returning to the mathematical form of entropy, the fact that it is based on probability means that many of the properties of probability carry across to entropy. But the use of the logarithm means that they manifest as additions instead of multiplications.}

\notes{For example the joint entropy of two variables, 
$$
H(X, Y) = - \sum_{X, Y} P(X, Y) \log P(X, Y),
$$
can be decomposed as the entropy of the marginal and the entropy of the conditional,
$$
H(X, Y) = H(X \mid Y) + H(Y)
$$
where 
$$
H(Y \mid X) = - \sum_{X, Y} P(X, Y) \log P(X \mid Y) 
$$
and
$$
H(Y) = - \sum_{Y} P(Y) \log P(Y).
$$
This is known as the *chain rule* of entropy. And it follows from the product rule.

The equivalent of Bayes' rule is 
$$
H(Y \mid X) = H(X \mid Y) + H(Y) - H(X).
$$}

\newslide{Joint, Conditional, Chain Rule (Names Only)}

\slidesincremental{
* $H(X,Y)$ joint uncertainty
* $H(X\mid Y)$ residual uncertainty after observing $Y$
* Chain rule: $H(X,Y)=H(X\mid Y) + H(Y)$
}


\endif

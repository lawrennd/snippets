\ifndef{entropyReview}
\define{entropyReview}
\editme

\subsection{Entropy Review}

\include{_ml/includes/expectation-entropy-example.md}

\newslide{Uncertainty as a Number}

\slides{Shannon entropy turns a distribution into a *scalar*. That number must compose across nested coarse-grainings.}

\slidesincremental{
* Discrete: $H(p) = -\sum_i p_i \log p_i$ --- expected surprisal
* Base 2: bits; natural log: nats
* Nested grains (this room, then the planet) must add consistently
}

\speakernotes{Fair yes/no questions under optimal play is the operational reading --- week 3 with the information game. What you argued today is composition: otherwise information loss at one grain is inconsistent with the grain above.}

\notes{Under Shannon's definition, entropy is dimensionless. It is the expectation of the negative log surprisal, $-\expSamp{\log P(\dataScalar)}$. In machine learning we might call that the energy or the objective function. It returns uncertainty as a single number.

That number has to compose correctly. If I am choosing to ensemble the gas in this room, someone outside is ensembling this room and the people in it, and someone on another planet is looking at us and summarising the whole planet, I would like the calculus of my entropy to work across that composition. As we coarse-grain, I would like entropy to reflect the loss that occurs at every grain.

That compositional property is one of the things that gives you this functional form. If it did not look like that, I could coarse-grain at this level, record my information loss, then coarse-grain at the level above, and the losses would be inconsistent. That is the mathematical motivation for the Shannon form. The information game and MacKay's balance --- the operational reading as fair yes/no questions --- wait for week 3.}

\include{_information/includes/common-distributions-entropy.md}

\newslide{Shannon's definition is not yet ...}

\slidesincremental{
* ... Clausius's thermodynamic entropy (same formula, different motivation)
* ... a channel-capacity theorem
}

\notes{We are not yet giving Shannon's channel-capacity theorem, which many would say is the sophisticated piece of his work. Philosophically, this part of the construction is doing something else. It explicitly takes away mechanism. I am not sure that he highlighted this; it is the bit I want to keep. He does not say what your coding system has to be. He does not want to talk about your mechanism for doing the actual integral. He is saying: you are going to lose entropy if you discretise in that way.

When we go into the thermodynamic entropy I will tend to use $S$ for the physical entropy and $H$ for Shannon's entropy.}

\newslide{Entropy: physical and anthropomorphic}

\slidesincremental{
* Thermodynamic $S$ and Shannon $H$: same form; in equilibrium $S = k_B H$
* $k_B$ gives physical units (J/K); $TS$ has units of energy
* Which degrees of freedom you count is a *choice* (Jaynes / Wigner: "anthropomorphic")
* Steam tables: untampered extras (e.g.\ electric field) or apparent second-law violations
}

\notes{Thermodynamic entropy $S$ and Shannon $H$ have a shared functional form, in equilibrium we can write $S = k_BH$, where $k_B$ is Boltzmann's constant, $k_B = 1.380649 \times 10^{-23} \tfrac{\text{kg}\text{m}^2 }{\text{s}^2 \text{K}}$. 

So there are two parts to a thermodynamic entropy, one is the uncertainty of a (discrete) distribution. The other translates that entropy into units of 'work' i.e. ($\text{J} = \tfrac{\text{kg}\,\text{m}^2 }{\text{s}^2}$) per Kelvin ($\tfrac{\text{J}}{\text{K}}$). Boltzmann's constant makes entropy physical. When we multiply $S$ by temperature $T$ (in degrees Kelvin) we recover a term that has units of energy. That $TS$ has units of energy is also why entropy must be extensive: if I have $N$ independent copies, $H$ scales with $N$, and so does $TS$.

I feel that this object is mathematically more fundamental than any notion of energy. You can imagine a world in which it is the other way round: you start by deriving entropy, and then you look at things in the other direction. Why is that not this world? Because no one can measure entropy. You do not measure it directly. There is no way, in an empirical science, that you would see this entropy production going on. You only start realising it is happening when you have missing quantities to explain. A physicist would say there is no way of measuring entropy directly --- although we will look at situations where entropy reduction is immediate, as when I tell you the result of a coin toss and a reduction of one bit has occurred. That is coming because we know what the probabilities were.

But the dependence of entropy on the states of a distribution, or the probability across those states, also implies that there is a *choice* in terms of which states we consider. In classical mechanics we have states like position and velocity (or momentum). But quantum mechanics also leads to other properties of materials such as the *spin* of an electron. Choice of which variables you consider when computing e.g. the entropy of an electron, was referred to as the '"anthropomorphic" nature of entropy' by @Jaynes-gibbs65. He credits this remark originally to Eugene Wigner. One example that Jaynes gives is thermodynamic steam tables.}

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

\notes{This leads him to a conclusion that is worth bearing in mind when we talk about the physical meaning of entropy. Once you have those steam tables, you can make a better steam engine or a better steam turbine. They were not measuring the entropy of the spin in the electrons, or whatever else is going on in the atomic physics, when they created the tables. That is what Jaynes means by anthropomorphic.

If I talk about the entropy of a die, you will probably assume I am talking about a fair die with six pips on it. You do not assume I am talking about the entropy of the underlying fabric of that die. So it is contextual. In physics they are trying to make sure that choice is valid in an objective way. In machine learning and AI that choice is subjective: it depends on who you are, what time frame you are operating over, what you are trying to achieve, what senses you have. From my perspective it makes no sense to talk about intelligence without this context --- cuttlefish, crows, whether large language models have some form of embodiment because they have learnt it from us.}

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

\newslide{Joint, Conditional, Chain Rule}

\slidesincremental{
* $H(X,Y)$ joint uncertainty
* $H(X\mid Y)$ residual uncertainty after observing $Y$
* Chain rule: $H(X,Y)=H(Y)+H(X\mid Y)$
* Grouping: $H(X)=H(G)+H(X\mid G)$ when $G$ is a function of $X$
}

\speakernotes{Composition of nested grains is the story from earlier today; the die board that makes grouping $G=g(X)$ explicit waits for week 3. Do not prove Khinchin. Worksheet 1 probes can already use joint / conditional / chain-rule vocabulary.}


\endif

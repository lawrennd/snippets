\ifndef{probabilisticProgramming}
\define{probabilisticProgramming}

\editme

\subsection{Probabilistic Programming}
\slides{* Dates back to BUGS
* Modern descendent (same spirit) is Stan
* Also languages like pyro (based on PyTorch)
}

\notes{Probabilistic programming is an idea that, from our perspective, can be summarized as follows. What if, when constructing your simulator, or your model, you used a programming language that was aware of the state variables and the probability distributions. What if this language could 'compile' the program into code that would automatically compute the Bayesian posterior for you?}

\notes{This is the objective of probabilistic programming. The idea is that you write your model in a language, and that language is automatically converted into the different modelling codes you need to perform Bayesian inference.}

\notes{The ideas for probabilistic programming originate in [BUGS](https://www.mrc-bsu.cam.ac.uk/software/bugs/). The software was developed at the MRC Biostatistics Unit here in Cambridge in the early 1990s, by among others, [Sir David Spiegelhalter](https://en.wikipedia.org/wiki/David_Spiegelhalter). Carl Henrik covered in last week's lecture some of the approaches for approximate inference. BUGS uses Gibbs sampling. Gibbs sampling, however, can be slow to converge when there are strong correlations in the posterior between variables.}

\endif
\ifndef{abcInference}
\define{abcInference}

\editme

\subsection{Approximate Bayesian Computation}

\notes{We reintroduced Gaussian processes at the start of this lecture by sampling from the Gaussian process and matching the samples to data, discarding those that were distant from our observations. This approach to Bayesian inference is the starting point for *approximate Bayesian computation* or ABC.}

\notes{The idea is straightforward, if we can measure 'closeness' in some relevant fashion, then we can sample from our simulation, compare our samples to real world data through 'closeness measure' and eliminate samples that are distant from our data. Through appropriate choice of closeness measure, our samples can be viewed as coming from an approximate posterior.}

\notes{My Sheffield colleague, Rich Wilkinson, was one of the pioneers of this approach during his PhD in the Statslab here in Cambridge. You can hear Rich talking about ABC at NeurIPS in 2013 here.}

\figure{\includeyoutube{sssbLkn2JjI}{600}{450}}{Rich Wilkinson giving a Tutorial on ABC at NeurIPS in 2013. Unfortunately, they've not synchronised the slides with the tutorial. You can find the slides [separately here](http://media.nips.cc/Conferences/2013/Video/Tutorial2B.pdf).}{rich-wilkinson-abc}

\endif
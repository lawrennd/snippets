\ifndef{uqSamplingHistoryDoe}
\define{uqSamplingHistoryDoe}

\editme

\subsection{Uncertainty Quantification and Design of Experiments}

\slides{* History of interest, see e.g. @McKay-selecting79
* The review:
    * Random Sampling
    * Stratified Sampling
    * Latin Hypercube Sampling
* As approaches for Monte Carlo estimates
}
\notes{We're introducing you to the optimization and analysis of real-world models through emulation, a domain that is part of the broader field known as surrogate modelling. This involves creating simplified models that approximate more complex systems, allowing for efficient exploration and analysis.}

\notes{Although we're approaching this from the machine learning perspective, with a computer-scientist's approach, you won't be surprised to hear that this field is not new. There are diverse research communities, including statisticians and engineers, who have long been interested in these methods.}

\notes{Our focus has been on *active* experimental design, where we sequentially select points to run our simulation based on previous results, optimizing the process iteratively.}

\notes{Now, we pause to explore *passive* experimental design approaches. In passive design, we select initial points to 'seed' the emulator without running the simulator. This is crucial for setting up the emulator effectively.}

\notes{The challenge of determining where to run simulations to obtain the necessary answers is longstanding. A seminal paper by @McKay-selecting79 reviews three foundational methods for designing these inputs: *random sampling*, *stratified sampling*, and *Latin hypercube sampling*. These methods provide structured ways to explore the input space and are essential for effective experimental design.}

\newslide{Random Sampling}

\slides{* Samples selected randomly across input domain
* Can be uniform or based on assumed distribution
* Simple but may miss important regions}

\notes{Random sampling is the default approach, where samples are selected randomly across the input domain of interest. This can be done uniformly or based on an assumed underlying distribution. It is straightforward but may not always provide comprehensive coverage of the input space.}

>  Let the input values $\inputVector_1, \dots, \inputVector_\numData$
> be a random sample from $f(\inputVector)$. This method of sampling
> is perhaps the most obvious, and an entire body of statistical
> literature may be used in making inferences regarding the
> distribution of $Y(t)$.

\newslide{Stratified Sampling}

\slides{* Divides input space into sub-populations (strata)
* Ensures sampling from each stratum
* Better coverage than random sampling
* Example: Covid-19 tracking by age groups}

\notes{Stratified sampling involves dividing a population into sub-populations, or strata, before sampling. This ensures that all sub-populations are represented in the sample. For instance, in Covid-19 tracking, stratifying by age groups ensures coverage across all ages, which might be missed in simple random sampling.}

\notes{In emulation, similar principles apply. The input domain can be divided into areas of particular interest. For example, when testing an F1 car component, you might focus on performance in different track sections, ensuring comprehensive data collection across varied conditions.}

> Using stratified sampling, all
> areas of the sample space of $\inputVector$ are represented by
> input values. Let the sample space $S$ of $\inputVector$ be partitioned into $I$ disjoint strata $S_t$. Let $\pi = P(\inputVector \in S_i)$
> represent the size of $S_i$. Obtain a random sample $\inputVector_{ij}$, $j
> = 1, \dots, n$ from $S_i$. Then of course the $n_i$ sum to $\numData$.
> If $I = 1$, we have random sampling over the entire
> sample space.

\newslide{Latin Hypercube Sampling}

\slides{* Advanced form of stratified sampling
* Divides each input dimension into equal probability bins
* One sample per row/column in each dimension
* Ensures full coverage of marginal distributions}

\notes{Latin hypercube sampling is an advanced form of stratified sampling. It ensures that each input variable's distribution is fully represented by dividing the input space into $M$ rows and columns, with samples taken such that each row and column contains only one sample. This method extends to multiple dimensions, providing a comprehensive sampling strategy.}

> The same reasoning that led to stratified sampling, ensuring that
> all portions of $S$ were sampled, could lead further. If we wish
> to ensure also that each of the input variables $\inputVector_k$ has
> all portions of its distribution represented by input values, we can
> divide the range of each $\inputVector_k$ into $\numData$ strata of
> equal marginal probability $1/\numData$, and sample once from each
> stratum. Let this sample be $\inputVector_{kj}$, $j = 1, \dots,
> \numData$. These form the $\inputVector_k$ component, $k = 1, \dots
> , K$, in $\inputVector_i$, $i = 1, \dots, \numData$. The components
> of the various $\inputVector_k$'s are matched at random. This method
> of selecting input values is an extension of quota sampling
> (Steinberg 1963), and can be viewed as a $K$-dimensional extension of
> Latin square sampling (Raj 1968).

\notes{The paper's rather dated reference to "Output from a Computer Code" highlights the historical context of these methods, which remain relevant today. [Tony O'Hagan](http://www.tonyohagan.co.uk/academic/), who was a colleague in Sheffield when I first arrived there, was a pioneer in Gaussian process models, and has contributed significantly to this field, including work on managing uncertainty in computational models [@Kennedy-bayesian01]. More information can be found in the [technical reports](https://web.archive.org/web/20220308104727/http://mucm.ac.uk/Pages/Dissemination/TechnicalReports.html) from the EPSRC funded project [http://www.mucm.ac.uk/](https://web.archive.org/web/20220526104923/http://mucm.ac.uk/).}

\notes{Another key group is the "MASCOT-NUM Research Group" in France and it's follow on RT-UQ, <https://uq.math.cnrs.fr/>, which unites statisticians, applied mathematicians, and engineers to tackle these complex problems.}

\endif

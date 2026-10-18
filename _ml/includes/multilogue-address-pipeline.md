\ifndef{multilogueAddressPipeline}
\define{multilogueAddressPipeline}

\editme

\subsection{Multilogue Address Pipeline}

\notes{Multilogue packages the reusable *Address* method for public-dialogue studies that follow Access $\to$ Assess $\to$ Address. Access supplies corpus-agnostic units of text. Assess is work you can do without the research question in mind --- size, coverage, vocabulary. Address is where the question enters: extract phrases, embed them into a shared topic space, weight documents fairly, optionally soften framing lenses, compare document topic profiles, and measure sensitivity across a multiverse of analytic choices. The library holds the shared machinery; consumers supply corpora, prompts, and headline metrics $\ell$.}

\slides{
* Multilogue $=$ shared *Address* method for dialogue studies
* Access $\to$ Assess $\to$ Address (Fynesse)
* Assess: no question in mind; Address: question enters
* Library: extract, embed, cluster, weight, soft lenses, distance, multiverse
* Consumers: corpora, prompts, metric $\ell$
}

\newslide{Address Stages}

\notes{The Address path is a sequence of explicit stages. *Extract* pulls kind-keyed phrases with checkpoints and optional quote verification. *Cluster* embeds phrases and runs $k$-means with frozen assignments when the phrase set is unchanged, plus blind labels and framing lenses. *Weight* averages shares at document level so long documents do not drown short ones. *Soft lenses* fit a PPCA Gaussian per framing lens, form Bayes responsibilities, and choose the shared noise $\noiseStd^2$ by cross-run stability. *Document distance* treats each document as a distribution over clusters and compares documents with earth mover's distance under a cosine ground cost, then MDS and PERMANOVA. *Multiverse* takes the Cartesian product of analytic choices and reports variance shares for a consumer-supplied $\ell$.}

\slidesincremental{
* Extract --- kind-keyed phrases, checkpoints, quote support
* Cluster --- embed, frozen $k$-means, blind labels, lenses
* Weight --- document-level shares (and bootstrap)
* Soft lenses --- PPCA mixture; $\sigma^2$ by stability
* Document distance --- EMD on cluster shares; MDS / PERMANOVA
* Multiverse --- variance shares over analytic choices
}

\newslide{Two Uses of Transport}

\notes{Earth mover's distance appears twice, on different objects. Soft-lens selection measures mean EMD between *mixture weight* rows across independent LLM lens runs, under a cosine cost between lens means, and picks $\noiseStd^2$ inside an effective-support band. Document distance measures EMD between *documents* as distributions over clusters, under a cosine cost between cluster centroids --- answering whether groups differ in what they raise, without using lens names. Same Kantorovich programme; different histograms and ground costs.}

\slides{
* Soft $\sigma^2$: EMD of lens mixture weights across runs
* Document distance: EMD of cluster-share histograms
* Same OT; different objects and ground costs
}

\endif

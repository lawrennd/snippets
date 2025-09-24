\ifndef{humanAnalogueMachinesShort}
\define{humanAnalogueMachinesShort}

\editme

\subsection{Human Analogue Machine}

\notes{The machine learning systems we have built today that can reconstruct human text, or human classification of images, necessarily must have some aspects to them that are analagous to our understanding. As MacKay suggests the brain is neither a digital or an analogue computer, and the same can be said of the modern neural network systems that are being tagged as "artificial intelligence".}

\notes{I believe a better term for them is "human-analogue machines", because what we have built is not a system that can make intelligent decisions from first principles (a rational approach) but one that observes how humans have made decisions through our data and reconstructs that process. Machine learning is more empiricist than rational, but now we have an empirical approach that distils our evolved intelligence.}

\notes{HAMs are not representing states of the outside world with analogous states inside the machine, they are also not (directly) processing digital states through logic gates to draw their conclusions (although they are implemented on digital computers that do this to enable them to update).}

\notes{\figure{\includepng{\diagramsDir/ai/processor-ham}{60%}}{The human analogue machine creates a feature space which is analagous to that we use to reason, one way of doing this is to have a machine attempt to compress all human generated text in an auto-regressive manner.}{human-analogue-machine}}

\slides{\include{_ai/includes/processor-ham.md}}

\slides{* A human-analogue machine is a machine that has created a feature space that is analagous to the "feature space" our brain uses to reason.

* The latest generation of LLMs are exhibiting this charateristic, giving them ability to converse.}

\reading{@Lawrence-atomic24}{Chapter 11}

\include{_ai/includes/heider-simmel.md}

\newslide{Counterfeit People}

\notes{The perils of developing this capability include counterfeit people, a notion that the philosopher [Daniel Dennett has described in *The Atlantic*](https://www.theatlantic.com/technology/archive/2023/05/problem-counterfeit-people/674075/). This is where computers can represent themselves as human and fool people into doing things on that basis.}

\slides{* Perils of this include *counterfeit people*.
* Daniel Dennett has described the challenges these bring in [an article in The Atlantic](https://www.theatlantic.com/technology/archive/2023/05/problem-counterfeit-people/674075/).}

\newslide{Psychological Representation of the Machine}

\slides{* But if correctly done, the machine can be appropriately "psychologically represented"

* This might allow us to deal with the challenge of *intellectual debt* where we create machines we cannot explain.}

\addatomic{human-analogue machine}{343–5, 346–7, 358–9, 365–8}

\endif

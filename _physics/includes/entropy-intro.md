\ifndef{entropyIntro}
\define{entropyIntro}




\editme
\include{_physics/includes/laplace-molecule-anachronism.md}
\include{_physics/includes/daniel-bernoulli-hydrodynamica.md}
\include{_physics/includes/bernoulli-kinetic-assumptions.md}
\include{_physics/includes/entropy-billiards.md}
\include{_physics/includes/entropy-histogram.md}
\include{_physics/includes/ensemble-as-coarse-graining.md}

\newslide{}

\figure{\threeColumns{\includepng{\diagramsDir/physics/james-clerk-maxwell}{100%}{}{left}}{\includejpg{\diagramsDir/physics/boltzmann2}{100%}{}{center}}{\includejpg{\diagramsDir/physics/j-w-gibbs}{100%}{}{right}}{30%}{30%}{30%}}{James Clerk Maxwell (1831-1879), Ludwig Boltzmann (1844-1906) Josiah Willard Gibbs (1839-1903)}{maxwell-boltzmann-gibbs}

\notes{Many of the ideas of early statistical physicists were rejected by physicists who did not believe in the notion of a molecule. When Boltzmann was writing, it was still unclear whether heat was a fluid --- it has fluid-like properties because it seems to flow. The Graz paper is a foundation paper in the kinetic theory of gases. It was a radical change of perspective.

Max Planck took the work up early. Boltzmann had persistent trouble with German physicists, including Mach. Planck was a champion of his. The reason Planck talks about scientific theories proceeding one funeral at a time is that this perspective was so radical. You can see why the existing community resisted it. A lot of physics is about fields, continuous fields --- still is today --- and particle theories were obnoxious to that clean, continuous picture.

Boltzmann took his own life in 1906, two years before the molecular picture became widely accepted. Whether the controversy caused that is contested. Some biographies tie the suicide to the fight over atoms; the [Stanford Encyclopedia of Philosophy](https://plato.stanford.edu/archives/spr2006/entries/statphys-Boltzmann/) treats that causal story as a myth and points instead to depression and declining health.}

\newslide{}

\figure{\includegooglebook{Vuk5AQAAMAAJ}{PA373}}{Boltzmann's paper @Boltzmann-warmetheorie77 which introduced the relationship between entropy and probability. A translation with notes is available in @Kim-translation15.}{boltzmann-warmetheorie}


\notes{The important point about the uncertainty being represented here is that it is not genuine stochasticity, it is a lack of knowledge about the system. Maxwell, Boltzmann and Gibbs give us a description of the *macrostate* through a small set of parameters --- volume, temperature and pressure --- that are sufficient statistics for the gas, linked by an equation of state. They do not specify the microstate: which molecule is where, with which velocity. When we approximate the physical world we sit somewhere between the deterministic and purely stochastic worlds those scientists described.}

\newslide{}

\notes{One ongoing characteristic of people who study probability and uncertainty is the confidence with which they hold opinions about it. Arthur Eddington, then at the Cambridge Observatory rather than the Cavendish, expressed his support of the second law of thermodynamics (which Gibbs and Boltzmann made statistical: entropy increases *almost* always, not always) with an emphatic statement around page 74 of *The Nature of the Physical World*, in the chapters on the second law, not at the opening of the book [@Eddington:nature29].}

\figure{\columns{\includejpg{\diagramsDir/physics/arthur-stanley-eddington}{100%}{}{left}}{\includepng{\diagramsDir/physics/natureofphysical00eddi_7}{80%}{}{right}}{49%}{49%}}{Eddington's book on the Nature of the Physical World [@Eddington:nature29]}{eddington-book}

\newslide{}

\notes{The same Eddington dismissed the ideas of a young Chandrasekhar. Chandrasekhar had come from India to Cambridge; he was at Trinity, not the Cavendish. On 11 January 1935, at a public meeting of the Royal Astronomical Society, he presented the mass limit for a white dwarf. Beyond that limit the end state is a neutron star or a black hole --- he did not use those names --- not simply "a singularity". Eddington carried his ideas too far. He humiliated Chandrasekhar in public. The documented remark is that there should be a law of Nature to prevent a star behaving in such an absurd way; "abomination" is a later paraphrase. Whether Eddington's faith in the second law drove the dismissal is speculation; one account notes that he did not directly refute Chandrasekhar's mathematics. Chandrasekhar was deeply upset, later received the Nobel prize for the work, and disliked the controversy that followed him. Accounts of the meeting: [Universe Today](https://www.universetoday.com/articles/chandrasekhar-and-the-limits-of-physics-part-2-humiliation), [Southampton, The Stellar Graveyard](https://www.personal.soton.ac.uk/dij/GR-Explorer/NS/graveyard.htm), [Flamsteed Astronomy Society](https://www.flamsteed.info/post/ring-of-fire-chronicles-of-eddington-and-chandrasekhar-by-bobby-manoo).

Why would Eddington dislike the theory? All the mass of the universe ending up in black holes is not the maximum-entropy state. The maximum-entropy state is like the gas in this room: heat death. Chandrasekhar experienced the exchange as racially charged. That reading is understandable; it is not, on the evidence we have of Eddington --- who was open across the First World War to German physicists --- the best explanation. My belief is that he thought he saw the limit contradict the second law, and so he said to Chandrasekhar: that cannot happen.

That confuses mechanism with the law. Black holes evaporate: Hawking radiation. They do not stay in this state, but the evaporation takes a very long time. The second law still applies, as a slow leakage away from this concentration of mass. The better response would have been: the physics shows that this happens; I expect maximum entropy to apply in the long time; what is the mechanism through which this undoes itself?

I can believe in the second law of thermodynamics. I should not humiliate a student who comes up with a mechanism that initially seems to contradict it, because the two arguments work at different levels. Eddington would not have felt he was humiliating. He would have thought that he was teaching. There is a way of teaching, when you are a very senior physicist, that can be very damaging.}

\figure{\columns{\includepng{\diagramsDir/physics/natureofphysical00eddi_100}{80%}{}{left}}{\includepng{\diagramsDir/physics/ChandraNobel}{100%}{}{right}}{49%}{49%}}{Chandrasekhar (1910-1995) derived the white-dwarf mass limit. Eddington dismissed the result at the RAS on 11 January 1935, humiliating a young scientist who would later receive a Nobel prize for the work.}{physical-world-chandra}

\newslide{}

\figure{\includepng{\diagramsDir/physics/natureofphysical00eddi_100_cropped}{60%}}{Eddington makes his feelings about the primacy of the second law clear (around p.74 of [@Eddington:nature29], not the opening). Gibbs and Boltzmann made the law statistical: entropy increases almost always. A convenient extract is at [Today in Science History](https://todayinsci.com/E/Eddington_Arthur/EddingtonArthur-Entropy-Quotations.htm).}{deepest-humiliation-eddington-cropped}

\notes{The cropped quote is the one I paraphrase: if your theory contradicts Maxwell's equations, so much for Maxwell's equations; if it does not match experiment, well, experimentalists do bungle things at times; but if your theory contradicts the second law of thermodynamics, I have nothing but the deepest humiliation for you. The second law holds, he thinks, the supreme position amongst the laws of nature. Hawking radiation is the slow mechanism. Do not confuse teaching with humiliation.}
\endif

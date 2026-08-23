\ifndef{wellingEntropyPartition}
\define{wellingEntropyPartition}

\editme

\notes{\subsection{GAIST on Entropy and the Partition Function}}

\notes{Section 1.2.3 of [@Welling-generative26] defines Shannon entropy as expected surprisal, $\mathrm{S}[p] = -\int p\log p$, in nats. It computes the Gaussian entropy and shows that it depends only on $\sigma$, not on $\mu$. Section 1.2.4 introduces KL as relative entropy, the information lost when $q$ stands in for $p$, and records the chain-rule decomposition of KL. That is useful scaffolding for week 7; it is not Shannon's chain rule for $H$.}

\notes{Section 3.2.4 is the generating-function half of today's lecture: from $Z$ to mean energy, entropy, and free energy. Read those two sections. Do not look here for the Shannon axioms, for $S = kH$, or for channel capacity. Those are MacKay and Shannon (1948). GAIST treats entropy as a property of a distribution, not as a no-go on a code.}

\addreading{@Welling-generative26}{Sections 1.2.3--1.2.4 and 3.2.4}

\endif

\ifndef{clausiusCarnotSecondLaw}
\define{clausiusCarnotSecondLaw}

\editme

\subsection{Clausius and $\mathrm{d}Q/T$}

\notes{Heat is not conserved. Carnot's limit remains. That is the problem Clausius inherits from Joule and Thomson. If the caloric mill is gone, what still closes when a reversible engine runs a cycle? The answer is not a quantity of heat. It is heat divided by temperature. A reversible cycle produces no entropy.}

\newslide{Rudolf Clausius}

\figure{\includejpg{\diagramsDir/physics/rudolf-clausius}{40%}}{Rudolf Clausius (1822--1888). Photograph from the AIP Emilio Segrè Visual Archives, Lande Collection (Wikimedia Commons, CC0).}{rudolf-clausius}

\notes{Clausius is a mathematical physicist, first in Berlin, later Zurich, Würzburg and Bonn. In 1850, independently of Thomson's 1851 dynamical theory, he writes the two laws that keep Joule and Carnot in the same ledger [@Clausius-motive50]. The first law is Joule's equivalent made universal: heat is a form of work. The second is what remains of the mill: heat does not pass from cold to hot by itself, and no cyclic engine converts the heat of a single bath entirely into work.}

\speakernotes{Portrait, 1850, two laws. Do not start with Boltzmann. The question is still engines: if heat is not conserved, what is the leftover identity?}

\newslide{Two Laws}

\slides{Keep Joule's equivalent. Keep Carnot's limit. Drop conservation of heat.}

\slidesincremental{
* First law: heat and work are interchangeable, at Joule's rate
* Second law: heat does not flow from cold to hot without a cost
* A cycle cannot turn the heat of one bath entirely into work
}

\notes{The first law is why $\oint \mathrm{d}Q$ is not zero for an engine. Some of the heat taken from the hot bath does not arrive at the cold bath; it has become work. That is Joule, inside Carnot's cycle. The second law is why you still cannot take *all* of it. There is a remainder that must be rejected to the cold bath, and the size of that remainder, for a reversible engine, depends only on the two temperatures --- not on whether the working substance is steam, air, or anything else. That was Carnot's other claim, and it survives.}

\newslide{The Ratio that Survives}

\slides{After Joule, Carnot's mill is a ratio of heats, not a conserved fluid.}

\slidesincremental{
* Reversible engine: $Q_h/T_h = Q_c/T_c$
* $Q_h$ taken from the hot bath, $Q_c$ delivered to the cold
* Heat does not balance. Heat over temperature does
}

\notes{Thomson's 1851 scale is this statement: the absolute temperatures stand in the same ratio as the two heats. Write it the other way up and the books close. The heat that leaves the hot bath, divided by $T_h$, equals the heat that arrives at the cold bath, divided by $T_c$. The *difference* of the heats is the work. The *quotient* of each heat by its temperature is the same number. That number is the transformation. Clausius's 1854 paper calls it the equivalence-value of the transformation [@Clausius-equivalence54]. We are looking at a two-bath cycle; the same accounting will apply to a loop assembled from many small exchanges.}

\speakernotes{Put $Q_h/T_h = Q_c/T_c$ on the board. Both $Q$s positive. The gap $Q_h-Q_c$ is the work. The thing that matches is $Q/T$.}

\newslide{The Loop}

\slides{A reversible cycle is a closed path. The $Q/T$ account closes with it.}

\slides{
$$\oint \frac{\mathrm{d}Q}{T} = 0 \qquad \text{(reversible cycle)}$$
}

\slidesincremental{
* Every reversible loop integrates to zero
* So there is a state function $S$ with $\mathrm{d}S = \mathrm{d}Q_{\mathrm{rev}}/T$
}

\notes{If every reversible cycle gives zero, the integral of $\mathrm{d}Q/T$ between two states cannot depend on the reversible path you take. That is the definition of a state function. Clausius writes
$$
S - S_0 = \int \frac{\mathrm{d}Q_{\mathrm{rev}}}{T}.
$$
Heat $\mathrm{d}Q$ is not a state function: the heat you put in depends on the path, which is why $\oint \mathrm{d}Q$ is the work of the engine. Dividing by $T$ along a *reversible* path removes that path-dependence. Reversibility is the condition. It means the engine can be run backwards and the baths restored: no finite drops of temperature, no friction, no paddle wheel hidden in the mechanism.}

\speakernotes{One display, then state function. Contrast $\oint\mathrm{d}Q \neq 0$ (work) with $\oint\mathrm{d}Q/T = 0$ (no leftover transformation). Next slide is the sentence they should leave with.}

\newslide{A Reversible Cycle Produces No Entropy}

\slides{You return to the start. Nothing has been created.}

\slidesincremental{
* The working substance: $S$ is a state function, so $\Delta S = 0$ around any cycle
* The baths: the entropy that left the hot bath arrives at the cold bath
* Universe: $\Delta S = 0$. A reversible cycle produces no entropy
}

\notes{This is the mill, rewritten after Joule. The working fluid comes home. Its entropy comes home with it. The hot bath has lost $Q_h/T_h$; the cold bath has gained $Q_c/T_c$; those two are equal. No transformation has been left over. Reversible does not mean ``nothing happened.'' Work was done. It means the transformation can be undone, and when you close the loop there is no residue.}

\speakernotes{Say the title sentence twice. System versus baths versus universe, in that order, slowly. Students will try to make $S$ increase around a reversible cycle. Hold them to zero.}

\newslide{When the Cycle Is Irreversible}

\slides{The working substance still comes home. The books do not.}

\slidesincremental{
* Friction, a finite drop of temperature, a paddle in the mechanism
* More heat is dumped to the cold bath than the reversible case
* $\displaystyle\oint \mathrm{d}Q/T < 0$, and the entropy of the universe increases
}

\notes{An irreversible cycle is still a cycle: the working substance returns, so its $S$ is unchanged. What has changed is the baths. You took $Q_h$ from the hot bath and, because some of the fall was wasted, you delivered *more* than the reversible $Q_c$ to the cold bath. The integral $\oint \mathrm{d}Q/T$, with $\mathrm{d}Q$ the heat absorbed by the working substance, is then strictly negative [@Clausius-equivalence54]. Equivalently, the entropy lost by the hot bath is less than the entropy gained by the cold bath. The difference was produced. That is the second law as an accounting inequality, not as a prohibition in words.}

\newslide{The Name}

\figure{\includejpg{\diagramsDir/physics/clausius-coins-entropy}{62%}}{Clausius names entropy, 1865. English translation of the memoir: $\int \mathrm{d}Q/T = S-S_0$, from Greek τροπή, *transformation*. He forms the word to sit beside *energy*.}{clausius-coins-entropy}

\notes{In 1865 he gives the state function a name [@Clausius-entropy65]. *Verwandlungsinhalt*, the transformation content, would have done; he prefers a Greek root, τροπή, so that the word can pass unchanged between languages, and so that it sits next to *energy*. The two quantities, he says, are so nearly allied in their physical meanings that a similarity in designation appears desirable. Energy is the first-law account. Entropy is the second-law account. His summary of the two laws: the energy of the universe is constant; the entropy of the universe tends to a maximum.}

\speakernotes{Show the page. Transformation, not disorder, not uncertainty. Worksheet 1 payoff: this is what Clausius was measuring. Boltzmann's count and Shannon's $H$ come later, and they reuse a functional form, not this operational meaning.}

\newslide{Not Uncertainty}

\slides{Clausius's $S$ is an accounting identity for heat and temperature.}

\slidesincremental{
* Macroscopic: $S$ from $\mathrm{d}Q_{\mathrm{rev}}/T$; a reversible cycle produces none
* Microscopic, later: Maxwell, Boltzmann, Gibbs count the same $S$
* Information, later: Shannon, Jaynes reuse the functional form for a different job
}

\notes{Clausius did not give the Boltzmann distribution, and he did not make entropy a measure of uncertainty. He gave the macroscopic balance that any later prescription must respect. When we write $p_i \propto e^{-\beta E_i}/Z$ and later derive it from MaxEnt, read it as a statistical answer to a constraint he already framed: fixed mean energy, maximum entropy, no perpetual motion. The historical chain is engines, then the equivalent, then this integral, then statistics, then information.}

\addreading{@Clausius-motive50}{The 1850 paper: two laws, Carnot's limit without conserved heat}
\addreading{@Clausius-entropy65}{The 1865 memoir: $\mathrm{d}S = \mathrm{d}Q_{\mathrm{rev}}/T$, and the name entropy}

\endif

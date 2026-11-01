\ifndef{clausiusCarnotSecondLaw}
\define{clausiusCarnotSecondLaw}

\editme

\subsection{Clausius and $\mathrm{d}Q/T$}

\notes{Heat is not conserved. Carnot's limit remains. That is the problem Clausius inherits from Joule and Thomson. If the caloric mill is gone, what still closes when a reversible engine runs a cycle? The answer is not a quantity of heat. It is heat divided by temperature. A reversible cycle produces no entropy.}

\newslide{Rudolf Clausius}

\figure{\includejpg{\diagramsDir/physics/rudolf-clausius}{40%}}{Rudolf Clausius (1822--1888). Photograph from the AIP Emilio Segrè Visual Archives, Lande Collection (Wikimedia Commons, CC0).}{rudolf-clausius}

\notes{Clausius is a mathematical physicist, first in Berlin, later Zurich, Würzburg and Bonn. It is quite close between Kelvin and Clausius to get to the formula. In 1850, independently of Thomson's 1851 dynamical theory, he writes the two laws [@Clausius-motive50]. He holds on to Joule's equivalent between work and energy, keeps Carnot's limit, and drops the notion that heat is conserved. He is doing all this without a notion of conservation of energy, which is gobsmacking. Bernoulli too: $PV=NRT$ is later; he was doing it with momentum. The first law is Joule's equivalent made universal: heat is a form of work. The second is what remains of the mill: heat does not pass from cold to hot by itself, and no cyclic engine converts the heat of a single bath entirely into work.}

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

\notes{Thomson and Joule's 1854 scale is this statement: the absolute temperatures stand in the same ratio as the two heats. What Clausius notices is that in a reversible engine the heat energy at the hot temperature, divided by that temperature, equals the heat energy at the cold temperature, divided by that temperature, as you go around. If the cycle is reversible, that quantity is conserved: the integral of the small changes in heat, over the whole loop, is zero. That is what Clausius told us. If the cycle is irreversible, the same integral, with $\mathrm{d}Q$ the heat absorbed by the working substance, is strictly negative. It is never positive on that convention. Clausius's 1854 paper calls the quantity the equivalence-value of the transformation [@Clausius-equivalence54]; his uncompensated transformation is the negative of the integral, and is $\ge 0$.}

\speakernotes{Put $Q_h/T_h = Q_c/T_c$ on the board. Both $Q$s positive. The gap $Q_h-Q_c$ is the work. The thing that matches is $Q/T$.}

\newslide{The Loop}

\slides{A reversible cycle is a closed path. If it is reversible, the integral is zero.}

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

\notes{An irreversible cycle is still a cycle: the working substance returns, so its $S$ is unchanged. What has changed is the baths. You took $Q_h$ from the hot bath and, because some of the fall was wasted, you delivered *more* than the reversible $Q_c$ to the cold bath. The integral $\oint \mathrm{d}Q/T$, with $\mathrm{d}Q$ the heat absorbed by the working substance, is then strictly negative [@Clausius-equivalence54]. Equivalently, the entropy lost by the hot bath is less than the entropy gained by the cold bath. The difference was produced. Clausius's uncompensated transformation is the negative of this integral: it is $\ge 0$, and it is strictly positive when the cycle is irreversible.}

\newslide{The Name}

\figure{\includejpg{\diagramsDir/physics/clausius-coins-entropy}{62%}}{Clausius names entropy, 1865. English translation of the memoir: $\int \mathrm{d}Q/T = S-S_0$, from Greek τροπή, *transformation*. He forms the word to sit beside *energy*.}{clausius-coins-entropy}

\notes{In 1865 he gives the state function a name [@Clausius-entropy65]. Clausius writes that we might call $S$ the transformational content of the body, just as we term the magnitude $U$ its thermal and ergonal content, the inner energy; but that it is better to borrow terms for important magnitudes from the ancient languages, so that they may be adopted unchanged in all modern languages. He proposes to call $S$ the *entropy* of the body, from the Greek word τροπή, *transformation*. He has put an $n$ on the front. He says explicitly that he has formed the word to be as similar as possible to *energy*, because the two magnitudes are so nearly allied in their physical meanings that a certain similarity of designation appears desirable. They are not allied because of the division by $T$. There is no Boltzmann's constant here yet: this is a macroscopic property, something he can derive from measuring what was lost, or noticing it is not lost in a reversible cycle. He has no notion underneath it that this is anything to do with uncertainty. He just says: I need this piece to fit the puzzle. The assumption, coming at it afterwards, is that they were looking at energy conserved and therefore this piece is missing. It is not quite like that.}

\speakernotes{Show the page. Transformation, not disorder, not uncertainty. Worksheet 1 payoff: this is what Clausius was measuring. Boltzmann's count and Shannon's $H$ come later, and they reuse a functional form, not this operational meaning.}

\newslide{Not Uncertainty}

\slides{Clausius's $S$ is the piece that fits the puzzle: heat divided by temperature.}

\slidesincremental{
* Macroscopic: $S$ from $\mathrm{d}Q_{\mathrm{rev}}/T$; a reversible cycle produces none
* Microscopic, later: Maxwell, Boltzmann, Gibbs count the same $S$
* Information, later: Shannon, Jaynes reuse the functional form for a different job
}

\notes{Clausius did not give the Boltzmann distribution, and he did not make entropy a measure of uncertainty. He gave the macroscopic balance that any later prescription must respect. $S$ is a macroscopic measurement that is *extensive*: the entropy of a system increases as we increase the size of the system. Temperature is *intensive*: it does not. When we write $p_i \propto e^{-\beta E_i}/Z$ and later derive it from MaxEnt, read it as a statistical answer to a constraint he already framed: fixed mean energy, maximum entropy, no perpetual motion. The historical chain is engines, then the equivalent, then this integral, then statistics, then information.}

\notes{Later, Maxwell, then Boltzmann and Gibbs, come to the same sort of conclusions. This century, Shannon and Jaynes reuse the functional form for what might be said to be a different job. Shannon is always discrete. Wiener is continuous. Wiener never drops the mechanism behind the entropy: he always thinks about what drives the distribution. In Shannon you just say it is a probability. A lot of the theory does not have to specify what the probability *is*; you use that it normalises to one and is positive, and you derive a lot from that. That is mathematics. The other bit, where you have to talk about mechanism, is physics.}

\addreading{@Clausius-motive50}{The 1850 paper: two laws, Carnot's limit without conserved heat}
\addreading{@Clausius-entropy65}{The 1865 memoir: $\mathrm{d}S = \mathrm{d}Q_{\mathrm{rev}}/T$, and the name entropy}

\endif

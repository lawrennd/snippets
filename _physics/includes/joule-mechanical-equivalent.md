\ifndef{jouleMechanicalEquivalent}
\define{jouleMechanicalEquivalent}

\editme

\subsection{Joule and the Mechanical Equivalent}

\notes{James Prescott Joule (1818--1889) gives the answer to Rumford's riddle. He theorises that a measured quantity of mechanical work could *create* a measured quantity of heat. If it can then heat is not a conserved fluid. This would imply that Carnot's mill becomes a special case, not the general law. Joule is a Manchester brewer who tries this experiment with a paddle wheel [@Joule-equivalent50].}

\newslide{James Prescott Joule}

\figure{\includejpg{\diagramsDir/physics/james-prescott-joule}{40%}}{James Prescott Joule (1818--1889). Seated portrait, later in life (Wikimedia Commons, public domain).}{james-prescott-joule}

\notes{The family brewery is in Manchester where Joule has a private laboratory. From 1840 he is working to relate heat to electricity and to chemical affinity. In 1843 he argues that the heat from magneto-electricity is proportional to the work absorbed. Mayer, in 1842, has already claimed that agitating water warms it, without a measured force. Joule wants the equivalent.}

\speakernotes{Brewer, Manchester, private lab. Not Carnot's question. Do not start a Mayer priority fight; one sentence is enough. The paddle wheel is the mechanism.}

\newslide{The Paddle Wheel}

\figure{\includepng{\diagramsDir/physics/joule-apparatus-harpers}{48%}}{Joule's apparatus for the mechanical equivalent of heat. A falling weight turns a paddle in water; the work is known, the rise in temperature is measured. Engraving from *Harper's New Monthly Magazine*, August 1869 (Wikimedia Commons, public domain).}{joule-apparatus-harpers}

\notes{In Joule's apparatus weights descend and turn a paddle in a can of water. The work associated with dropping a mass through a height is $mgh$. It is coiled around a bearing; there is a water paddle in a tank. To do the experiment you try to get rid of friction in the spindle. He did not drop it once: he had to drop it multiple times to show how much work converted into heat. It is a very similar experiment to Rumford's, but he has a better thermometer (mercury or other liquid, not air, by the look of the apparatus) and he is measuring the specific heat capacity of water. Mechanical power is being *spent*, and heat appears. Finally people realise that heat energy and work can transform into one another. That is the 1840s. Not very long ago.}

\speakernotes{Mechanism: falling weights, paddle, thermometer. Maths: work against heat, a ratio. Contrast with Carnot's mill still in the students' heads.}

\newslide{A Number}

\slides{A definite amount of work makes a definite amount of heat.}

\slidesincremental{
* 1845, British Association at Cambridge: the paddle already gives an equivalent, still scattered
* 1850, *Philosophical Transactions*: $772$ foot-pounds to raise $1\,\mathrm{lb}$ of water by $1^\circ\mathrm{F}$
* Modern, on the same scale: about $778$ foot-pounds, or $4.186\,\mathrm{J}$ per calorie
}

\notes{Cambridge here is the British Association meeting of June 1845, not the Cambridge Philosophical Society --- that society is Thomson's 1848 scale. Joule exhibits the brass paddle to the Chemical Section; the published letter opens by saying so [@Joule-equivalent45]. That run gives about $890$ foot-pounds per degree per pound of water. He also uses other methods such as magneto-electricity, rarefaction of air, passing water through narrow tubes to give neighbouring figures. His mean estimate is near $817$. By 1850 the number is settled as $772.692$ foot-pounds [@Joule-equivalent50]. The scientific world, he notes, preoccupied with the hypothesis that heat is a substance, had almost unanimously denied that fluid friction could generate heat.}

\speakernotes{Cambridge 1845 is BAAS, not the Philosophical Society. Thomson's scale is the CPS paper. The number is still 890, not 772.}

\newslide{Not Carnot's Question}

\slides{Joule is converting work into heat. He is not running a mill between two baths.}

\slidesincremental{
* Carnot: maximum work from a *fall* of conserved caloric
* Joule: how much work *makes* how much heat
* Conservation of heat cannot be the general law if the paddle is right
}

\speakernotes{Mill versus paddle, one more time. Then the contradiction. Do not derive $\mathrm{d}Q/T$.}

\newslide{The Contradiction}

\slides{You cannot keep Carnot's conserved heat and Joule's equivalent as general laws.}

\slidesincremental{
* If heat is conserved, none of it becomes work
* If Joule is right, some of it does
* What can be kept: a *limit* that depends only on the two temperatures
}

\notes{You will hear people say that when they built steam engines they had no theory of thermodynamics. That is not true. They had theories of thermodynamics. They did not have *complete* theories. We may not have a complete theory of thermodynamics today. This is where we are with machine learning: we do not have good theories of what is going on in the models, and we do not even have good definitions of intelligence. People can go around saying AGI or superintelligence, and it does not mean very much. Caloric is better defined. At least caloric is a notion you can look at and say: it is not conserved. It is telling you something specific you should expect. It is falsifiable. If you do not define your terms, you cannot do falsifiability.}

\notes{Once you realise that Joule converts work to heat, you also get the sense that heat converts to work. You can convert all your work into heat. You cannot get all the heat back as work. Carnot is assuming that the work comes from the fall, as in a mill. Here the heat itself converts. You cannot keep that theory of heat engines and Joule's demonstration as general laws. Clausius in 1850, and Thomson in 1851, will keep Carnot's *limit* and drop conservation of heat. We take Clausius first: two laws, and $\mathrm{d}Q/T$. Thomson then returns: the 1851 dynamical theory first, and with Joule in 1854 a scale that has a bottom.}

\addreading{@Joule-equivalent45}{The 1845 letter: paddle wheel shown at the British Association, Cambridge; equivalent still scattered around 817 foot-pounds}
\addreading{@Joule-equivalent50}{The 1850 *Phil.\ Trans.* paper: $772$ foot-pounds; the settled equivalent}

\endif

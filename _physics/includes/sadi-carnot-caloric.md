\ifndef{sadiCarnotCaloric}
\define{sadiCarnotCaloric}

\editme

\subsection{Sadi Carnot and the Fall of Heat}

\notes{Black made heat a quantity you can measure, mix and hide. Once it is a quantity, it looks like a fluid you can account for. From our perspective, the next step comes from Sadi Carnot (1796--1832). Carnot has a practical question, he's not focussed on what heat is made of, he wants to understand the limits of a steam engine.}

\newslide{Sadi Carnot}

\figure{\includejpg{\diagramsDir/physics/sadi-carnot}{40%}}{Sadi Carnot (1796--1832), aged 17, in the uniform of the École Polytechnique. Portrait by Louis-Léopold Boilly, 1813 (Wikimedia Commons, public domain).}{sadi-carnot}

\notes{Nicolas Léonard Sadi Carnot was a military engineer, son of Lazare Carnot. Lazare who was a mathematician and the "Organizer of Victory" of the Revolutionary armies.  After Waterloo Lazare he was driven into exile, and Sadi's career in army under the Bourbon restoration stalled. The portrait is a decade before the book. By 1824 he is on reduced pay in Paris, attending lectures at the Conservatoire, and paying himself to print six hundred copies of a short essay: *Réflexions sur la puissance motrice du feu* [@Carnot-reflexions24].}

\speakernotes{Military engineer, not a natural philosopher. Son of Lazare; Polytechnique; the book is 1824. Do not yet say second law or entropy. The question is engines.}

\newslide{Why Look at Heat Engines?}

\slides{Steam is already doing the work of a nation. Nobody has a theory of it.}

\slidesincremental{
* Watt's engines are a British industrial fact; typical efficiency is a few per cent
* Engineers try higher pressure, and other working fluids than steam
* Carnot's questions: is there a *limit*? Does the choice of fluid matter?
}

\notes{After his time in Glasgow, James Watt had moved to Birmingham and together with Matthew Boulton, commercialised a more efficient steam engine. By the 1820s the steam engine was widely used in mines, mills, looms and forges. Carnot beleives that one day it will serve as a universal motor, but he notes that it doesn't have a theory of mechanics. France is watching Britain do steam better. The so-called "practical men" are improving the capabilities of the machine, but Carnot wants to know whether any of that can be unbounded, or whether there is a ceiling independent of the machine and of the substance that runs through it.}

\newslide{The Réflexions}

\figure{\includejpg{\diagramsDir/physics/carnot-reflexions-thurston}{45%}}{Title page of R.~H. Thurston's 1890 English translation of Carnot's 1824 *Réflexions sur la puissance motrice du feu*. The original was printed in Paris by Bachelier, at Carnot's expense, in six hundred copies.}{carnot-reflexions}

\notes{The 1824 original is a short book, 118 pages, almost unread in his lifetime. Thurston's translation is how most English readers met it. The argument does not depend on calculus. It depends on a picture of heat that Black had made plausible: caloric, a conserved fluid, falling from hot to cold.}

\newslide{A Heat Engine Is a Mill}

\slides{Work comes from the *fall* of caloric, not from destroying it.}

\slidesincremental{
* Water mill: quantity of water, height of the fall
* Heat engine: quantity of caloric, difference of temperature
* The caloric that leaves the boiler arrives in the condenser
}

\notes{Carnot's own comparison: the motive power of heat can be compared to that of a waterfall. A waterfall has a maximum you cannot exceed, whatever machine you put in the stream. The power depends on the quantity of water and the height of the fall. Heat, likewise, depends on the quantity of caloric and on what he calls the height of its fall --- the difference of temperature between the bodies exchanging it. In a steam engine the boiler is the upper reservoir, the condenser the lower. The caloric developed in the firebox is taken up by the steam, does something in the cylinder, and is given up to the cold water. In that picture heat is conserved because that is what a mill requires: the same working fluid in, the same working fluid out, work from the drop. He is not claiming to have weighed heat against work. He is taking Black's ledger and using it as the mechanics of an engine.}

\speakernotes{The mill is the slide. Quantity conserved, work from the height. Students will want to correct him. Hold that. Conservation of heat is the assumption that fits *his* question.}

\newslide{Not Joule's Question}

\slides{Carnot is looking at a *cycle* between two baths. He is not looking at conversion.}

\slidesincremental{
* His object is an engine: maximum work from a fall of heat
* Joule's object will be a paddle wheel: how much work makes how much heat
* Conservation of caloric is an assumption that fits the mill. It is not an answer to Joule
}

\notes{This is the distinction to keep. Carnot's focus is cyclic conversion of a temperature difference into work. He needs two reservoirs, a working substance, and a closed loop. On that loop, Black's accounting --- heat hidden in steam, recovered in the condenser --- looks like conservation. Joule, twenty years later, will ask whether mechanical work can *create* heat at a definite rate. That is a different experiment, and a different question. We do not yet know that energy is conserved. We do not yet know that heat *is* energy. Carnot's conservation of heat will turn out to be a special case, not the general law. Manuscripts found after his death show him beginning to doubt caloric. The book he published does not.}

\speakernotes{Do not introduce the mechanical equivalent here. Plant the gap: mill versus paddle wheel. Next will be Kelvin's scale from this picture, then Joule's twist.}

\newslide{A Short Life}

\slides{Carnot dies in the 1832 cholera epidemic, aged 36. The book almost vanishes with him.}

\slidesincremental{
* Six hundred copies, paid for by the author, unread
* Clapeyron recasts the argument in 1834
* Kelvin and Clausius will read it later --- and will have to keep the limit after the mill's working fluid is given up
}

\notes{In the summer of 1832 Carnot falls ill; he dies of cholera on 24 August, at Ivry, aged 36. The *Réflexions* have made no impression. Two years later Émile Clapeyron, another polytechnicien, writes the argument in the language of indicator diagrams, and the book becomes findable. Kelvin will take the mill and make a temperature scale from it. Clausius will have to keep what was right in Carnot --- there is a limit, and it depends only on the two temperatures --- once heat is no longer a conserved fluid. We are not there yet.}

\speakernotes{Stop. Do not derive $\mathrm{d}Q/T$. The next move in the thread is Kelvin's scale, still under conservation of heat, then Joule.}

\addreading{@Carnot-reflexions24}{The mill analogy: motive power of heat compared to a waterfall}

\endif

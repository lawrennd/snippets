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

\slides{Steam already drives mills, mines, and looms. Nobody has a theory of it.}

\slidesincremental{
* Watt's engines are a British industrial fact
* Engineers try higher pressure, and other fluids than steam
* Carnot: is there a *limit*? Does the choice of fluid matter?
}

\notes{After his time in Glasgow, James Watt had moved to Birmingham and together with Matthew Boulton, commercialised a more efficient steam engine. By the 1820s the steam engine was widely used in mines, mills, looms and forges. Carnot beleives that one day it will serve as a universal motor, but he notes that it doesn't have a theory of mechanics. France is watching Britain do steam better. The so-called "practical men" are improving the capabilities of the machine, but Carnot wants to know whether any of that can be unbounded, or whether there is a ceiling independent of the machine and of the substance that runs through it.}

\newslide{The Réflexions}

\figure{\includejpg{\diagramsDir/physics/carnot-reflexions-thurston}{45%}}{Title page of R.~H. Thurston's 1890 English translation of Carnot's 1824 *Réflexions sur la puissance motrice du feu*. The original was printed in Paris by Bachelier, at Carnot's expense, in six hundred copies.}{carnot-reflexions}

\notes{The 1824 original is a short book, 118 pages, almost unread in his lifetime. Thurston's translation is how most English readers met it. The argument does not depend on calculus. It depends on a picture of heat that Black had made plausible: caloric, a conserved fluid, falling from hot to cold.}

\newslide{A Heat Engine Is a Mill}

\slides{Caloric falls from hot to cold. The same caloric arrives at the bottom.}

\figure{\includepng{\diagramsDir/physics/carnot-1824-fig1}{32%}}{Carnot's own figure of the mill (1824). The cylinder $ab$ holds the working body; $cd$ is the piston. Body $A$ is the furnace, body $B$ the refrigerator --- two reservoirs of caloric at different temperatures. Caloric taken from $A$ is given up to $B$. Vectorised from the plate in *Réflexions sur la puissance motrice du feu* (Wikimedia Commons, public domain).}{carnot-1824-fig1}

\slidesincremental{
* Water mill: quantity of water, height of the fall; the same water arrives below
* Heat engine: quantity of caloric, difference of temperature; the same caloric arrives in the condenser
* Two reservoirs. Nothing is used up.
}

\notes{Carnot's own comparison: the motive power of heat can be compared to that of a waterfall. A waterfall has a maximum you cannot exceed, whatever machine you put in the stream. The power depends on the quantity of water and the height of the fall. Heat, likewise, depends on the quantity of caloric and on what he calls the height of its fall --- the difference of temperature between the bodies exchanging it. In a steam engine the boiler is the upper reservoir, the condenser the lower. Carnot's own plate is that mill: body $A$ the furnace, body $B$ the refrigerator, the cylinder the wheel. The caloric developed in the firebox is taken up by the steam, passes through the cylinder, and is given up to the cold water. The mill turns because the caloric *moves*. The same quantity that left the hot reservoir arrives at the cold one. That is Black's ledger, used as the mechanics of an engine: a conserved fluid falling between two baths.}

\speakernotes{Point at $A$ and $B$. Furnace and refrigerator. Same caloric in, same caloric out. The piston is the mill wheel, not heat being turned into something else. Do not mention Joule. Students may want to correct him. Hold that.}

\newslide{A Short Life}

\slides{Carnot dies in the 1832 cholera epidemic, aged 36. The book almost vanishes with him.}

\slidesincremental{
* Six hundred copies, paid for by the author, unread
* Clapeyron recasts the argument in 1834
}

\notes{In the summer of 1832 Carnot falls ill; he dies of cholera on 24 August, at Ivry, aged 36. The *Réflexions* have made no impression. Two years later Émile Clapeyron, another polytechnicien, writes the argument in the language of indicator diagrams, and the book becomes findable.}

\speakernotes{Stop. Do not derive $\mathrm{d}Q/T$. Next is Rumford's cannon.}

\addreading{@Carnot-reflexions24}{The mill analogy: motive power of heat compared to a waterfall}

\endif

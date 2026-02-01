\ifndef{davidMackayMemorial}
\define{davidMackayMemorial}

\editme

\subsection{In Memory of David MacKay}

\notes{This talk is for a memorial meeting for David MacKay, who made fundamental contributions to our understanding of the relationship between information theory, energy, and practical systems. David's work on information theory and inference provided elegant bridges between abstract mathematical principles and real-world applications.}

\notes{I first saw David speak about information theory at the 1997 Issac Newton Institute meeting on Machine Learning and Genaralisation. It was a suprise because I had been expecting him to speak about either Bayesian neural networks or Gaussian processes. But, of course, as you get to know David you realise it was unsurprising, because he'd been looking at the connections between information theory, machine learning and error correcting codes. He summarised his thinking in his book "Information Theory, Inference, and Learning Algorithms" [@MacKay-information03]. It demonstrated how information-theoretic thinking can illuminate everything from error-correcting codes to neural networks to sexual reproduction. This book was my introduction to information theory, and it was available long before it was published. Regular updates were made on David's website from the late 1990s. 

He later surprised me again, when I heard that he'd shifted away from this larger work and was focussing on energy. He did so because he believed that sustainable energy was the most important challenge humanity faced. He approache the subject with the same clarity of thinking and careful reasoning. Memorably underpinned by practical examples using phone chargers. "Sustainable Energy Without the Hot Air" [@MacKay-energy08] was published in 2008. In a video created as part of the 2009 Cambridge Campaign he went from phone chargers to sweeping national changes in the way we use energy.}


\slides{
**David MacKay (1967-2016)**
* Information theory and inference
* Neural networks and learning algorithms
* Sustainable energy and physical limits
* Cut through hype with careful reasoning
}

\newslide{How many Lightbulbs?}

\figure{\includeyoutube{UR8wRSp2IXs}{800}{600}}{A YouTube video featuring David's clarity of thought and the ideas behind sustainable energy from 2010.}{david-how-many-lightbulbs}


\subsection{This Talk}

\notes{The work I present today on the inaccessible game is my best attempt to follow in this tradition. It tries to build on  rigorous information-theoretic foundations for understanding the limitations of automotous information systems. The hope is to use this framework to underpin our understanding of information processing systems, what their limits are. I hope that David would have appreciated both the mathematical structure and the attempt to use it to deflate unrealistic promises about superintelligence which I see as problematic in the same way he felt conversations about phone chargers were problematic in distracting us from the real challenges of energy restructuring.}

\notes{As David told us ten years ago, he was highly inspired by John Bridle telling him (as an undergraduate student) "everything's connected". Across his workDavid taught us to ask: "What are the fundamental constraints? What do the numbers say?".}

\notes{In my best attempt to respect that spirit of inquiry, this work tries to ask: What fundamental information-theoretic constraints govern intelligent systems? Can we understand these constraints as rigorously as we understand thermodynamic constraints on engines?}

\slides{
**David's Approach:**
* Start with fundamental principles
* Build rigorous mathematical framework
* Apply to real systems
* Use numbers to test claims

*Today:* Ideas on applying this to information, energy and intelligence
}


\subsection{Playful}

\notes{David was also a playful person, he enjoyed games, often rephrasing physics questions as puzzles, but also ultimate frisbee,[^ultimate] or ultimate for short. One aspect of ultimate he seemed to particularly like was the "spirit of the game". In ultimate there is no referee, no arbitration. Self arbitration is part of the spirit of the game.

[^ultimate]: Have a look at the wonderful tributes to him on the [Cambridge Ultimate website](https://ultimate.soc.srcf.net/davidmackay). 
}

\figure{\includejpg{\slidesDiagrams/information/david-ultimate}{60%}}{David playing ultimate. Picture is taken from [one of his last blog posts](https://itila.blogspot.com/2016/04/perhaps-my-last-post-well-see.html).}{david-ultimate}

\notes{In honour of this idea, we consider a similar principle for "zero player games". Games of the type of Conway's game of life (@Gardner-life70) or Wolfram's cellular automata (@Wolfram-cellular83). The principle is a conceptual constraint inspired by Russell's paradox: it demands that the rules of our system not appeal to external adjudicators or reference points just like ultimate.}

\slides{* David was a playful person.
* Physics puzzles
* Ultimate Frisbee.
  * Ultimate "spirit of the game"
* Create a self-adjudicating zero-player information game
}

\endif

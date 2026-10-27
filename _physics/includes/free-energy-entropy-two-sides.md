\ifndef{freeEnergyEntropyTwoSides}
\define{freeEnergyEntropyTwoSides}

\editme

\subsection{Two Sides of the Same Coin}

\notes{We have just derived $F=U-TS$ from the Gibbs occupation, with inner energy $U=\expSamp{E}$. Helmholtz free energy is what remains after entropy's cut. That identity is the whole of the LO1 payload. It is also why two research programmes that sound opposed are not. Welling, Lu and Holdijk's *Generative AI and Stochastic Thermodynamics* was published this year. Its subtitle is *A Tale of Free Energies* [@Welling-generative26]. If that book had a slogan, it would be close to *free energy is all you need*. If this course had a slogan, it would be *entropy is all you need*. They are two sides of the same coin, and the coin is inner energy.}

\newslide{Welling's Book, This Course}

\slides{They named the book for $F$. We named the course for $S$. The hinge is $U$.}

\slidesincremental{
* GAIST: *A Tale of Free Energies* --- variational $F$, ELBO, work and heat
* This course: entropy as the no-go; $F$ as what remains after the cut $TS$
* Fix the inner energy $U=\expSamp{E}$, and maximising $S$ *is* minimising $F$
}

\speakernotes{Hold up the identity. Welling's textbook is the optional monograph on the reading list. Do not teach Chapter 5 today. The point is the coin: $U=F+TS$. We stay with entropy because that is the constraint. They stay with free energy because that is the objective you minimise in a generative model.}

\notes{GAIST explores the shared mathematics of generative models and nonequilibrium thermodynamics. The mathematics is broadly the same; the philosophy is not. Their Chapter 3 is the Helmholtz split we have just done. Their Chapter 5 will identify variational free energy with the ELBO: inference as heat, learning as work. We will meet that identification in week 5 as a *correspondence*, not as a collapse of Shannon, Boltzmann and Jaynes into one theory. Read GAIST by chapter, not cover to cover. Callen remains the undergraduate thermodynamics. The motivations of this course --- perpetual motion, the human bandwidth constraint --- are not in that book.}

\newslide{See also Friston}

\slides{The same split, used as a theory of brains.}

\slidesincremental{
* Friston: organisms minimise a *variational* free energy [@Friston-free10]
* That functional is $U[q]-T S[q]$ under a trial distribution $q$
* Named here. Developed later, if at all. Our no-go remains $S$
}

\speakernotes{Karl Friston, not a third thermodynamics. Students will hear ``free energy principle'' and think it is a different $F$. It is the same algebra under a recognition density. Sit down. Next is the entropy game.}

\notes{Karl Friston's free-energy principle treats the same variational free energy as an account of brains and of action: perception as inference that lowers a bound on surprise [@Friston-free10]. Under a trial distribution $q$ the functional is again $U[q]-TS[q]$, which is Helmholtz's split with the occupation replaced by $q$. That is why it belongs in this lecture, and why it does not get a derivation today. We stay with entropy. Entropy is the cut that forbids perpetual motion. Free energy is what you can still do once that cut is taken. Inner energy is what you started with. Three names, one identity.}

\addreading{@Welling-generative26}{A tale of free energies: the Helmholtz split is Ch.~3; we stay with entropy}
\addreading{@Friston-free10}{The free-energy principle: the same split, used as a theory of brains}

\endif

\ifndef{clausiusCarnotSecondLaw}
\define{clausiusCarnotSecondLaw}
\editme

\subsection{Carnot and Clausius}


\notes{Sadi Carnot (1796–1832) asked, in 1824, what limits the efficiency of a heat engine. Rudolf Clausius (1822–1888) built on Carnot and Kelvin to state the second law of thermodynamics in several equivalent forms, and in 1865 he coined the name *entropy* for the state function that tracks irreversibility. Boltzmann and Gibbs, later in the same century, gave the microscopic count behind Clausius's macroscopic $S$. Shannon and Jaynes, in the twentieth century, reuse the same functional form with different operational readings. The historical chain is: engines first, then entropy as a named quantity, then statistics, then information.}

\newslides{Before Boltzmann: Heat Engines}

\slidesincremental{
* Carnot (1824): no real engine beats a reversible cycle between two baths
* Clausius (1850s): heat cannot flow from cold to hot without work
* Clausius (1865): names *entropy* — the state's transformation content
}

\speakernotes{Carnot is the efficiency question; Clausius is the second law and the word entropy. Perpetual motion fails because it tries to evade that toll.}

\newslides{Clausius and the No-Go}

\slides{Clausius: the entropy of the universe tends to a maximum.}

\slidesincremental{
* You cannot run a cyclic engine that converts heat entirely into work
* Similar for perpetual motion — Clausius makes the prohibition explicit
* Prescription follows separately: Boltzmann weights, then Shannon/Jaynes
}

\notes{Clausius did not give the Boltzmann distribution. He gave the macroscopic balance that any prescription must respect. When we write $p_i \propto e^{-\beta E_i}/Z$ and later derive it from MaxEnt, read it as the statistical answer to a constraint Clausius already framed: fixed mean energy, maximum entropy, no perpetual motion.}

\slidesincremental{
* Macroscopic: Carnot $\to$ Clausius (second law, entropy named)
* Microscopic: Maxwell, Boltzmann, Gibbs (same $S$, counted states)
* Information: Shannon, Jaynes (same $H$, different job)
}

\endif

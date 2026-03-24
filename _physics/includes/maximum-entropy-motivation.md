\ifndef{maximumEntropyMotivation}
\define{maximumEntropyMotivation}

\editme

\subsection{Maximum Entropy Motivation}

\notes{Ed Jaynes [@Jaynes-information57], proposed a foundation for statistical mechanics based on information theory. Jaynes recast that the problem of assigning probabilities in statistical mechanics as a problem of inference with incomplete information.}

\slides{
* @Jaynes-information57: Statistical mechanics as inference with incomplete information
* Maximum entropy principle: maximise uncertainty given constraints
* Avoids unwarranted assumptions beyond available data
}

\notes{A central problem in statistical mechanics is assigning initial probabilities when our knowledge is incomplete. The canonical example is if we know only the average energy of a system, what probability distribution should we use? Jaynes argued that we should use the distribution that maximises entropy subject to the constraints of our knowledge.}

\newslide{Dice Example}

\slides{
* Dice example: Average result 4.5 instead of 3.5
* Constraints:
  * $\sum_{n=1}^6 P_n = 1$ (normalization)
  * $\sum_{n=1}^6 nP_n = 4.5$ (observed average)
}

\notes{Jaynes illustrated the approach with a simple example. If a die has been tossed many times, with an average result of 4.5 rather than the expected 3.5 for a fair die. What probability assignment $P_n$ ($n=1,2,...,6$) should we make for the next toss?}

\notes{We need to satisfy two constraints
\begin{align}
\sum_{n=1}^6 P_n &= 1 \\
\sum_{n=1}^6 n P_n &= 4.5
\end{align}
}
\notes{Many distributions could satisfy these constraints, but which one makes the fewest unwarranted assumptions? Jaynes argued that we should choose the distribution that is maximally noncommittal with respect to missing information - the one that maximises the entropy,
\begin{align}
S_I = -\sum_{i} p_i \log p_i
\end{align}
This principle leads to the exponential family of distributions, which in statistical mechanics gives us the canonical ensemble and other familiar distributions.}


\endif 

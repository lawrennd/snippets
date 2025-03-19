\ifndef{optimalQuestioning}
\define{optimalQuestioning}

\editme

\subsection{The Mathematics of Optimal Questioning}

\notes{
In the entropy game, our goal is to identify an unknown entity from a set of possibilities by asking yes/no questions. Each question partitions the probability space, and our objective is to minimize the expected number of questions needed.

If we have a discrete random variable $X$ with probability mass function $P(X)$, the optimal question should split the probability mass as evenly as possible. Mathematically, if we ask a question that partitions the space into sets $A$ and $A^c$ (the complement of $A$), the expected information gain is:

$$IG(A) = H(X) - \left[P(A)H(X|A) + P(A^c)H(X|A^c)\right]$$

The optimal question maximizes this information gain. It can be shown that this occurs when $P(A) \approx P(A^c) \approx 0.5$.

This principle underlies many algorithms in computer science and artificial intelligence, from binary search to decision trees. It also provides a foundational perspective on intelligence: intelligent systems ask questions (or make observations) that maximally reduce entropy about their environment.
}

\slides{
* Optimal question splits probability mass evenly
* Expected information gain:
  $$IG(A) = H(X) - \left[P(A)H(X|A) + P(A^c)H(X|A^c)\right]$$
* Maximum information gain when $P(A) \approx 0.5$
* Each optimal question reduces entropy by ~1 bit
* Intelligence metric: efficiency of entropy reduction
}

\newslide{Entropy Game as Intelligence}

\slides{
* Intelligence metrics:
  * Questions needed vs. theoretical minimum
  * Adaptability to changing probabilities
  * Handling partial information
  * Sequential decision optimization
* Human vs. AI questioning strategies
}

\exercise{
Consider a murder mystery with four suspects: Alice, Bob, Charlie, and Diana, with probabilities 0.4, 0.3, 0.2, and 0.1 respectively.

1. Calculate the initial entropy
2. What is the optimal first question?
3. Calculate the expected entropy after this question
4. How does this relate to intelligence in detective work?
}

\endif 
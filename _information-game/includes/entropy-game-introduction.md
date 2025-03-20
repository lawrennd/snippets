\ifndef{entropyGameIntroduction}
\define{entropyGameIntroduction}

\editme

\section{The Entropy Game}

\notes{The Entropy Game is a framework for understanding efficient uncertainty reduction. To start think of finding the optimal strategy for identifying an unknown entity by asking the minimum number of yes/no questions.}

\slides{
* Intelligence as optimal uncertainty reduction
  * 20 Questions game as intuitive example
  * Binary search exemplifies optimal strategy
* Information gain measures question quality
  * Wordle as a more complex example
}

\subsection{The 20 Questions Paradigm}

\notes{In the game of 20 Questions player one (Alice) thinks of an object, player two (Bob) must identify it by asking at most 20 yes/no questions. The optimal strategy is to divide the possibility space in half with each question. The binary search approach ensures maximum information gain with each inquiry and can access $2^20$ or abou a million different objects.}

\figure{\includediagram{\diagramsDir/information/binary-search-tree}{70%}}{The optimal strategy in the Entropy Game resembles a binary search, dividing the search space in half with each question.}{binary-search-tree}

\subsection{Entropy Reduction as Intelligence}

\notes{From an information-theoretic perspective, intelligence can be viewed as the capacity to efficiently reduce entropy - the uncertainty about the state of the world. Each observation or action an intelligent agent takes should maximize expected information gain, optimally reducing uncertainty given available resources.}

\slides{
* Entropy before question: $S(X)$
* Entropy after answer: $S(X|M)$
* Information gain: $I(X;M) = S(X) - S(X|M)$
* Intelligent systems maximize $I(X;M)$ per unit cost
}
\notes{The entropy before the question is $S(X)$. The entropy after the question is $S(X|M)$. The information gain is the difference between the two, $I(X;M) = S(X) - S(X|M)$. Intelligent systems maximize this information gain per unit cost.}

\notes{This framework helps explain why both biological and artificial intelligence systems appear to behave as if they're performing active inference - constantly generating predictions and updating models to minimize surprise and uncertainty. The entropy game reveals intelligence as a process of efficiently navigating information landscapes.}

\subsection{Thermodynamic Parallels}

\notes{The entropy game connects to thermodynamics through the concept of work. In thermodynamics, extracting work from a system requires reducing its entropy. Similarly, meaningful intelligent action requires reducing uncertainty about the environment. Both processes can be understood as converting free energy into useful work - whether physical work or informational value.}

\slides{
* Intelligence requires work to reduce uncertainty
* Thermodynamic work reduces physical entropy
* Both operate under resource constraints
* Both bound by fundamental efficiency limits
}

\notes{This perspective suggests a profound connection: intelligence might be understood as a special case of systems that efficiently extract, process, and utilize free energy from their environments, with thermodynamic principles setting fundamental constraints on what's possible.}

\endif 
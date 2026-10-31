\ifndef{informationGameGuessing}
\define{informationGameGuessing}

\editme

\subsection{The Information Game}

\notes{The information game is the following idea. One player thinks of an object drawn from a known finite list. For example, "I'm thinking of an animal". The other may ask only yes/no questions. For example "Does your animal have four legs?". If we assume that the choice is uniform across that list, and if we can ask optimal questions, what number of questions do you need to guarantee the answer? How does information theory help us with this?}

\newslide{The Information Game}

\slides{I'm thinking of an animal ...}

\slidesincremental{
* Goal: name the object
* Cost: number of questions (worst case, or on average)
* Optimal play halves the remaining possibilities each time
}

\speakernotes{Run this live if time allows: owl, fox, snake, Gruffalo. Two fair questions name one of four. Students should feel that a balanced question buys one bit. Do not yet write $-\sum p\log p$; the counting argument is enough.}

\newslide{Four Animals, Two Bits}

\slides{Owl, fox, snake, Gruffalo. Two fair yes/nos name one of four.}

\include{_information/includes/information-game-animal-tree.md}

\notes{With a list of size $N$ and equal prior probability on each item, an ideal strategy halves the search space at every step. After $k$ answers you can distinguish at most $2^k$ hypotheses, so you need
$$
k \ge \log_2 N
$$
questions in the worst case. Sometimes the game is called "twenty questions". Twenty questions would reach a million possibilities: $2^{10}=1024\approx 10^3$, so $2^{20}=2^{10}\times 2^{10}\approx 10^6$. Exactly $2^{20}=1\,048\,576$. A problem that drives an equiprobable yes/no answer delivers to you one *bit* of information. That is the most information you can gain at ech turn. This gives us another interpretation of Shannon's bit, it is the amount of information you gain if you manage to answer a balanced yes/no or true/false question.}

\newslide{Bits as Balanced Questions}

\slides{A fair yes/no answer distinguishes two equally likely cases i.e. one *bit*.}

\slidesincremental{
* $N$ equally likely objects $\Rightarrow$ need $\log_2 N$ bits
* Twenty questions covers megabit or $\approx$ million hypotheses: $2^{20}=2^{10}\times 2^{10}\approx 10^3\times 10^3$
* Unequal priors: best questions still split probability as evenly as possible
}

\notes{If the prior is not uniform, the best question is no longer a literal half-split of the *count* of remaining objects. It is a half-split of their *probability*. The average number of questions under optimal play becomes the Shannon entropy $H = -\sum_i p_i\log_2 p_i$.}

\endif

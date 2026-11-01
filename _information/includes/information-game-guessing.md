\ifndef{informationGameGuessing}
\define{informationGameGuessing}

\editme

\subsection{The Information Game}

\notes{Before writing a formula for entropy, play a game. One player thinks of an object drawn from a known finite list. The other may ask only yes/no questions. How many questions do you need in the worst case? That count is already a measure of information: it is how much uncertainty you must remove to name the object.}

\newslide{The Information Game}

\slides{One player has chosen an object from a known finite list. The other may ask only *yes/no* questions.}

\slidesincremental{
* Goal: name the object
* Cost: number of questions (worst case, or on average)
* Optimal play halves the remaining possibilities each time
}

\speakernotes{Run this live if time allows: pick a small list (sixteen animals, eight Cambridge colleges). Students should feel that a balanced question buys one bit. Do not yet write $-\sum p\log p$; the counting argument is enough.}

\notes{With a list of size $N$ and equal prior probability on each item, an ideal strategy halves the search space at every step. After $k$ answers you can distinguish at most $2^k$ hypotheses, so you need
$$
k \ge \lceil\log_2 N\rceil
$$
questions in the worst case. Twenty questions reach a million possibilities: $2^{20} = 1\,048\,576$. A *fair* yes/no answer therefore carries one *bit* of information. That is Shannon's unit before Shannon's formula: information as the number of balanced binary distinctions required to resolve uncertainty.}

\newslide{Bits as Balanced Questions}

\slides{A fair yes/no answer distinguishes two equally likely cases --- one *bit*.}

\slidesincremental{
* $N$ equally likely objects $\Rightarrow$ worst case $\lceil\log_2 N\rceil$ bits
* Twenty questions reach about a million hypotheses ($2^{20}$)
* Unequal priors: best questions still split probability as evenly as possible
}

\notes{If the prior is not uniform, the best question is no longer a literal half-split of the *count* of remaining objects. It is a half-split of their *probability*. The Shannon entropy $H = -\sum_i p_i\log_2 p_i$ is the information budget, not the question count. The optimal expected number of yes/no questions $L$ satisfies $H\le L<H+1$; equality $L=H$ holds only when every $p_i$ is a power of $1/2$. The lecture's own die is the exhibit: $H=\log_2 6\approx 2.585$ bits, but a Huffman strategy needs $8/3\approx 2.667$ questions on average. We will meet the formula next; the game already shows what the number is counting.}

\slides{The same idea, with a different instrument, comes next --- MacKay's balance.}

\endif

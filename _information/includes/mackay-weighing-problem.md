\ifndef{mackayWeighingProblem}
\define{mackayWeighingProblem}

\editme

\subsection{MacKay's Balance and Balls}

\notes{David MacKay opens the compression half of *Information Theory, Inference, and Learning Algorithms* with a weighing puzzle [@MacKay-information03, Exercise~4.1]. It is the information game with a ternary instrument instead of a binary question. We use it here only as a *counting* argument: how much uncertainty we start with, how much each use of the balance can remove, and why three weighings are enough in principle --- without exhibiting a particular sequence of measurements.}

\newslide{Twelve Balls, One Odd}

\slides{MacKay's weighing problem [@MacKay-information03, Ex.~4.1]: twelve balls; exactly one is odd; it may be heavier *or* lighter.}

\figure{\includediagram{\diagramsDir/information/mackay-balance-balls}{80%}}{A two-pan balance and twelve identical balls. Each use of the balance returns one of three readings: left heavy, balance, or right heavy.}{mackay-balance-balls}

\slidesincremental{
* Instrument: a two-pan balance
* Each use: left heavy, right heavy, or balance --- *three* outcomes
* Task: identify the odd ball *and* whether it is heavy or light
}

\speakernotes{State the puzzle. Do not walk through which balls go on which pan. The lecture point is the information budget, not the adaptive strategy tree.}

\notes{You are given twelve balls, identical in appearance. Exactly one differs in weight from the others; you do not know whether that odd ball is heavier or lighter. A two-pan balance compares two equal-sized groups and returns one of three readings: left side heavier, right side heavier, or equal. Design a strategy that finds the odd ball and the direction of the defect.}

\newslide{Information at the Start}

\slides{Before any weighing, how many hypotheses?}

\slidesincremental{
* 12 choices for which ball is odd
* $\times$ 2 directions (heavy or light)
* $= 24$ equally likely states of the world
}

\notes{Under a uniform prior over those twenty-four possibilities, the Shannon uncertainty we must remove is
$$
H_{\mathrm{start}} = \log_2 24 \approx 4.58 \text{ bits}.
$$
At the end we need a single named hypothesis: $H_{\mathrm{end}} = 0$. The *deficit* to close is therefore about $4.58$ bits. That difference --- start minus end --- is the information the experiment must supply.}

\newslide{Information from the Balance}

\slides{Each weighing has three possible readings.}

\slidesincremental{
* Ideal (equiprobable) outcomes: $\log_2 3 \approx 1.58$ bits per use
* Two weighings: at most $3^2 = 9$ leaves --- too few for $24$ hypotheses
* Three weighings: at most $3^3 = 27$ leaves --- enough, since $27 \ge 24$
}

\notes{A binary question yields at most one bit. The balance is richer: its alphabet size is three. If the three readings are equiprobable, one weighing contributes
$$
\log_2 3 \approx 1.585 \text{ bits}.
$$
After $k$ weighings the strategy tree has at most $3^k$ leaves, so it can name at most $3^k$ hypotheses. Compare budgets:
$$
\begin{align*}
3^2 &= 9 < 24,\\
3^3 &= 27 \ge 24.
\end{align*}
$$
Two weighings cannot suffice no matter how clever the groupings. Three weighings *can*: there is spare capacity of three unused leaves ($27-24=3$). In bits,
$$
3\log_2 3 \approx 4.75 > \log_2 24 \approx 4.58.
$$
The gap is small. That is why the puzzle feels tight, and why a first weighing that wastes an outcome (for example putting six against six, which can never balance if exactly one ball is odd) fails: you have thrown away ternary resolution and fallen back toward a binary split.}

\newslide{Doable in Three --- Strategy Deferred}

\slides{The counting argument shows three weighings *must* be enough in principle.}

\slidesincremental{
* We do *not* give the sequence of groupings today
* Optimal play keeps the three readings as near equiprobable as possible
* Same moral as twenty questions: ask questions that split the prior evenly
}

\speakernotes{Stop here. Invite them to try Exercise 4.1 before reading MacKay's solution figure. Optional aside: a first weighing of 1--6 vs 7--12 can never balance under the problem statement, so it yields only one bit and is already suboptimal.}

\notes{We stop at the existence argument. Constructing the adaptive tree --- which balls on which pan at each step --- is MacKay's exercise, and solving it is the best way to feel what ``informative experiment'' means. The only design principle we need today is the one already present in the information game: choose each measurement so that its outcomes are as nearly equiprobable as possible under the current posterior. That maximises expected information gain per weighing and is what makes the $3^3 \ge 24$ budget achievable in practice.}

\addreading{MacKay-information03}{Exercise 4.1 and the discussion on pp.~69--70}

\endif

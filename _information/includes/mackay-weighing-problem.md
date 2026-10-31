\ifndef{mackayWeighingProblem}
\define{mackayWeighingProblem}

\editme

\subsection{MacKay's Balance and Balls}

\notes{David MacKay opens the compression half of *Information Theory, Inference, and Learning Algorithms* with a weighing puzzle [@MacKay-information03, Exercise~4.1].}

\newslide{Twelve Balls, One Odd}

\slides{MacKay's weighing problem [@MacKay-information03, Ex.~4.1]: twelve balls; exactly one is odd; it may be heavier *or* lighter.}

\figure{\includediagram{\diagramsDir/information/mackay-balance-balls}{80%}}{A two-pan balance and twelve identical balls.}{mackay-balance-balls}

\slidesincremental{
* Instrument: a two-pan balance
* Task: identify the odd ball *and* whether it is heavy or light
}

\speakernotes{State the puzzle. Do not list the readings of the balance, and do not walk through which balls go on which pan.}

\notes{You are given twelve balls, identical in appearance. Exactly one differs in weight from the others; you do not know whether that odd ball is heavier or lighter. You are given a two-pan balance. Design a strategy that finds the odd ball and the direction of the defect.}

\newslide{How Should We Proceed?}

\slides{We have a finite list of hypotheses and a physical instrument. How should we think?}

\slidesincremental{
* How many outcomes are there?
* How much information do we get per measurement?
* How many measurements do we require?
}

\notes{How many outcomes does that give us? How much information can we get per measurement? And how many measurements do we (therefore) require?}

\newslide{Information at the Start}

\slides{*Maths.* Before any weighing, how many hypotheses?}

\slidesincremental{
* 12 choices for which ball is odd
* $\times$ 2 directions (heavy or light)
* $= 24$ equally likely states of the world
}

\notes{Under a uniform prior over those twenty-four possibilities, the Shannon uncertainty we must remove is
$$
H_{\text{start}} = \log_2 24 \approx 4.58 \text{ bits}.
$$
At the end we would like a single hypothesis: $H_{\mathrm{end}} = 0$. This means that the information  *deficit* is around $4.58$ bits. We need to design a set of experiments that will supply this information.}

\subsection{Try Two Outcomes}

\newslide{What should we do?}

\slidesincremental{
* Two readings $\Rightarrow$ at most $\log_2 2$ bits per use
* Mechanism next: what we actually put on the pans
}

\speakernotes{Say ``log two bits'' --- one bit if the two readings are equally likely. Do not yet mention a third reading. Board 6 vs 6 as the move people reach for from twenty questions.}

\notes{A two-outcome instrument, used optimally, returns at most $\log_2 2 = 1$ bit per measurement. The information budget then says
$$
2^4 = 16 < 24 \le 32 = 2^5,
$$
so five weighings would work, but four cannot. Whether we can organise the physical balance to achieve that one bit per measurement is a separate question and associated with the *mechanism*. }

\newslide{Maths: Two Readings}

\slides{*Maths.* Start from $\log_2 24$. Each use returns at most $\log_2 2$.}

\slidesmall{
$$
\log_2 24 \approx 4.58,\qquad 2^4 = 16 < 24 \le 32 = 2^5
$$
}

\slidesincremental{
* Four uses cannot name 24 hypotheses
* Five uses can, *if* each use really returns one bit
* That "if" is the mechanism ... answered separately
}

\notes{Write two columns if you can: left, the information budget; right, the pans. The left column does not know about equal group sizes, leftover balls, or borrowing a ball of known mass. Those constraints live on the right. The rest of this block is the right-hand column, scored afterwards by the left.}

\newslide{Mechanism: 6 vs 6}

\slides{*Mechanism.* Put six against six.}

\slidesincremental{
* The pans will tip --- the odd ball is on one side
* Follow the down pan, as if the odd ball were heavier
* Six balls remain under that story
}

\speakernotes{Ask what we actually learned. Under ``it is heavier'', 12 balls become 6, one bit toward which ball. We do *not* know the direction. The down pan is six maybe-heavies; the up pan is six maybe-lights. All twelve balls are still in play. Maths next.}

\notes{The move 6 vs 6 is a binary-search instinct that comes to us from the information game. If we already knew the odd ball was heavier, it would be a perfect split of twelve balls. We do not know that. A down-left reading means "one of the left six is heavy, *or* one of the right six is light'': twelve of the original twenty-four hypotheses remain. One bit toward the 24, and *no* ball has been eliminated.}

\newslide{Maths: What 6 vs 6 Bought}

\slides{*Maths.* Score the same physical act on the 24 hypotheses.}

\slidesincremental{
* 24 $\to$ 12 remaining hypotheses: exactly $\log_2 2$ bits
* Zero balls eliminated --- each ball is still possibly odd
* The bit went into a *coupling* of group and direction
}


%% INSERT EXERCISE FOR thE reSt OF THE ANSWeR HERE

\subsection{Three Readings}

\newslide{Aha: It Balances Three Ways}

\slides{The pans also sit *level*. Left heavy, right heavy, or balance.}

\slidesincremental{
* The instrument can give left down, right down, equal
* 6 vs 6 made the third reading impossible
* That was a mechanism choice that *threw away* a symbol
}


\speakernotes{Let them say the three readings. Then go straight to the new budget. Do not start the 4 vs 4 tree.}

\notes{A two-pan balance has a ternary alphabet, the level reading can also give us information. This is an instrument that can give us $\log_2 3$ bits of information per measurement. By starting with measuring 6 vs 6 we set the probability of a level answer to  zero: with exactly one odd ball among the twelve, the pans cannot balance.}

\newslide{Maths: Three Readings}

\slides{*Maths.* Each use now returns at most $\log_2 3$.}

\slidesmall{
$$
\log_2 3 \approx 1.58,\qquad 3^2 = 9 < 24 \le 27 = 3^3
$$
}

\slidesincremental{
* Two uses ($3 \times 3$) cannot name 24 hypotheses
* Three uses can, *if* each use really returns $\log_2 3$
* Same "if" as before: mechanism must realise the split
}

\notes{A binary question yields at most one bit. If the three readings are equiprobable, one weighing contributes
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
The gap is small. That is why the puzzle feels tight. It is the same comparison we already made with $\log_2 2$, with a larger per-use budget.}

\newslide{Mechanism Must Collect $\log_2 3$}

\slides{*Mechanism.* To earn $\log_2 3$, all three readings must be possible and near equal.}

%%% ADD IN ADDITIONAL EXERCISE HERE ... 4.1 of Mackay repeated.

\addreading{MacKay-information03}{Exercise 4.1 and the discussion on pp.~69--70}

\endif

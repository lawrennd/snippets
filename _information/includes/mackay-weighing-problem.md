\ifndef{mackayWeighingProblem}
\define{mackayWeighingProblem}

\editme

\subsection{MacKay's Balance and Balls}

\notes{David MacKay opens the compression half of *Information Theory, Inference, and Learning Algorithms* with a weighing puzzle [@MacKay-information03, Exercise~4.1]. State the puzzle first. Do not yet say that the instrument is ternary. The information-game habit is to ask how we should proceed --- what we must name --- and then to try the instrument as if it had two readings, like a yes/no question. Keep the *mechanism* (what we put on the pans) on a different slide from the *maths* (how many bits that use can return). Only after that sequence do we notice that the balance has a third reading.}

\newslide{Twelve Balls, One Odd}

\slides{MacKay's weighing problem [@MacKay-information03, Ex.~4.1]: twelve balls; exactly one is odd; it may be heavier *or* lighter.}

\figure{\includediagram{\diagramsDir/information/mackay-balance-balls}{80%}}{A two-pan balance and twelve identical balls.}{mackay-balance-balls}

\slidesincremental{
* Instrument: a two-pan balance
* Task: identify the odd ball *and* whether it is heavy or light
}

\speakernotes{State the puzzle. Do not list the readings of the balance, and do not walk through which balls go on which pan.}

\notes{You are given twelve balls, identical in appearance. Exactly one differs in weight from the others; you do not know whether that odd ball is heavier or lighter. A two-pan balance compares two equal-sized groups. Design a strategy that finds the odd ball and the direction of the defect.}

\newslide{How Should We Proceed?}

\slides{We have a finite list of hypotheses and a physical instrument. How should we think?}

\slidesincremental{
* What, exactly, do we need to name?
* What would count as a useful use of the balance?
* When would we know we were done?
}

\speakernotes{Leave this live. Do not say left, right, or level, and do not say three. After they have named the hypotheses, try the two-outcome story next --- as if this were the information game again.}

\notes{Resist jumping to a particular grouping. Count first: how many states of the world. Then try the instrument as a two-outcome device, because that is the game we already know. Keep what we put on the pans separate from the information budget those pans can return.}

\newslide{Information at the Start}

\slides{*Maths.* Before any weighing, how many hypotheses?}

\slidesincremental{
* 12 choices for which ball is odd
* $\times$ 2 directions (heavy or light)
* $= 24$ equally likely states of the world
}

\notes{Under a uniform prior over those twenty-four possibilities, the Shannon uncertainty we must remove is
$$
H_{\mathrm{start}} = \log_2 24 \approx 4.58 \text{ bits}.
$$
At the end we need a single named hypothesis: $H_{\mathrm{end}} = 0$. The *deficit* to close is therefore about $4.58$ bits. That difference --- start minus end --- is the information the experiment must supply. We have not yet said what the balance returns.}

\subsection{Try Two Outcomes}

\newslide{Let's Try Two Outcomes}

\slides{Treat the balance as the information game: *left heavy* or *right heavy* only.}

\slidesincremental{
* Two readings $\Rightarrow$ at most $\log_2 2$ bits per use
* Mechanism next: what we actually put on the pans
* Maths stays on its own slides --- the two accounts can disagree
}

\speakernotes{Say ``log two bits'' --- one bit if the two readings are equally likely. Do not yet mention a third reading. Board 6 vs 6 as the move people reach for from twenty questions.}

\notes{A two-outcome instrument, used optimally, returns at most $\log_2 2 = 1$ bit per measurement. The information budget then says
$$
2^4 = 16 < 24 \le 32 = 2^5,
$$
so five uses can suffice on paper and four cannot. Whether a physical balance *achieves* that one bit is a different question: it depends on what we put on the pans.}

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
* That ``if'' is mechanism, not maths
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

\notes{The move 6 vs 6 is the binary-search instinct. If we already knew the odd ball was heavier, it would be a perfect split of twelve balls. We do not know that. A down-left reading means ``one of the left six is heavy, *or* one of the right six is light'': twelve of the original twenty-four hypotheses remain. One bit toward the 24, and *no* ball has been eliminated. Mechanism and maths have already come apart: the pans moved, the pile of balls did not shrink.}

\newslide{Maths: What 6 vs 6 Bought}

\slides{*Maths.* Score the same physical act on the 24 hypotheses.}

\slidesincremental{
* 24 $\to$ 12 remaining hypotheses: exactly $\log_2 2$ bits
* Zero balls eliminated --- each ball is still possibly odd
* The bit went into a *coupling* of group and direction
}

\notes{The information gain can be perfect for the two-outcome model --- an even split of 24 --- while the mechanism fails to name a set of six suspect *balls*. What we carry forward is six maybe-heavy and six maybe-light. If we now *pretend* it was heavier and keep only the down pan, we have thrown away half of the remaining hypotheses by assumption, not by measurement.}

\newslide{Mechanism: 3 vs 3}

\slides{*Mechanism.* Keep going as a binary search of the balls: three against three.}

\slidesincremental{
* Under the heavier-side story, three balls remain
* Same move, smaller pile
* We are still not asking about light versus heavy
}

\notes{This is the sequence people sketch on the board: 6 vs 6, then 3 vs 3. It is the right mechanism for a different puzzle --- twelve balls, one *heavier*. Hold that sequence, because the next move is where the pans refuse to cooperate.}

\newslide{Mechanism: Three Left}

\slides{*Mechanism.* Three balls remain. We cannot put one and a half on a pan.}

\slidesincremental{
* 2 vs 2 needs a fourth ball
* Borrow one of *known normal* mass
* Then 1 vs 1 on whatever the 2 vs 2 leaves
}

\speakernotes{Make them say the known ball out loud. Ask: how many bits do we get from 2 vs 2 now? Do not calculate before they see that the split of three remaining balls cannot be even.}

\notes{With three suspects we have two mechanical choices. Weigh 1 vs 1 and leave one off: the left-off ball is the odd one *if the pans balance*. That reading is not in the two-outcome story we are trying to tell. Or weigh 2 vs 2 by padding with a ball already known to be normal: A,B against C plus a normal. The pans are now full, so in the heavier-only story they must tip, and we have not used a third symbol. We have changed the split.}

\newslide{Maths: The Known Ball Taxes the Bit}

\slides{*Maths.* Three remaining heavier-suspects; pans are 2 vs 1+known.}

\slidesmall{
$$
\left(\tfrac{2}{3},\tfrac{1}{3}\right)
\quad\Rightarrow\quad
H = h_2\!\left(\tfrac{2}{3}\right) \approx 0.92 < 1 \text{ bit}
$$
}

\slidesincremental{
* The even split was $\log_2 2$; the pans cannot make it
* Padding with a known ball is a mechanism patch
* Information gain falls because the *probabilities* are no longer equal
}

\notes{If A,B,C are the three remaining heavier-suspects and N is known normal, the reading A,B down leaves two hypotheses and has probability $2/3$; C,N down names C and has probability $1/3$. Binary entropy $h_2(2/3)\approx 0.92$ bits. The deficit $1-0.92$ is exactly the price of the mechanical constraint ``equal numbers on the pans, and no third reading''. We did not lose those bits because the mathematics of two outcomes changed. We lost them because the mechanism could not realise an equiprobable two-way split of three objects.}

\newslide{Mechanism: 1 vs 1}

\slides{*Mechanism.* If two suspects remain, weigh them against each other.}

\slidesincremental{
* Now the split *can* be even
* Under the heavier story, this names the ball
* We still have not asked light versus heavy
}

\notes{1 vs 1 of two remaining heavier-suspects returns the missing bit: the down pan is the odd ball, if the heavier-side story is true. The sequence of *acts* was 6 vs 6, 3 vs 3, 2 vs 2 with a known, then 1 vs 1. The sequence of *gains* was 1, 1, $0.92$, 1 --- already not four bits. And this named a ball only inside the heavier-side story.}

\newslide{Mechanism: Lighter or Heavier?}

\slides{*Mechanism.* We have a candidate ball. Can we name the direction?}

\slidesincremental{
* Weigh the candidate against a known normal
* Two outcomes name heavy versus light --- *if* it tips
* If it *balances*, our heavier-side story was wrong
}

\speakernotes{This is the crack in the two-outcome attempt. A known-normal comparison is the natural test for direction, and it keeps offering a third reading: level. The instrument was never a yes/no question. Pause, then the aha slide.}

\notes{To finish the original task we must name the direction as well as the ball. The obvious mechanism is candidate versus known normal. If the two-outcome story were true, this use would return the last bit: heavy or light. But if we followed the down pan all the way and the odd ball was actually light, the candidate may be normal --- and then the pans *balance*. The third reading has been sitting in the mechanism whenever a known ball appears. We cannot keep it out without lying about what the device does. That is the cue to abandon the two-outcome model, not to patch it again.}

\newslide{Two Accounts, One Experiment}

\slides{Keep the columns separate.}

\slidesincremental{
* *Maths:* $\log_2 24$ to close; at most $\log_2 2$ per two-outcome use
* *Mechanism:* 6 vs 6, 3 vs 3, 2 vs 2 with a known, 1 vs 1, then direction
* The known ball, and the unused ``level'' reading, are mechanism --- they change the gain
}

\notes{The moral is not that the binary budget is wrong. It is that an information budget is silent about pans. Equal group sizes, leftover balls, and borrowed normals are constraints on the *channel we actually have*. Score every weighing twice: what the device did, then how many bits that split was worth.}

\subsection{Three Readings}

\newslide{Aha: It Balances Three Ways}

\slides{The pans also sit *level*. Left heavy, right heavy, or balance.}

\slidesincremental{
* The instrument was never a yes/no question
* 6 vs 6 made the third reading impossible
* That was a mechanism choice that *threw away* a symbol
}

\speakernotes{Let them say the three readings. Then go straight to the new budget. Do not start the 4 vs 4 tree.}

\notes{A two-pan balance has a ternary alphabet. The reading ``level'' is not an annoyance to be designed out; it is a symbol that can carry information. The first move of the two-outcome story, 6 vs 6, sets the probability of that symbol to zero: with exactly one odd ball among the twelve, the pans cannot balance. We spent a mechanism choice to turn a three-outcome device into a two-outcome device, and then paid further mechanism taxes (the known ball) to keep the third symbol from coming back.}

\newslide{Maths: Three Readings}

\slides{*Maths.* Each use now returns at most $\log_2 3$.}

\slidesmall{
$$
\log_2 3 \approx 1.58,\qquad 3^2 = 9 < 24 \le 27 = 3^3
$$
}

\slidesincremental{
* Two uses cannot name 24 hypotheses
* Three uses can, *if* each use really returns $\log_2 3$
* Same ``if'' as before: mechanism must realise the split
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

\slidesincremental{
* First weighing: 4 vs 4, not 6 vs 6 --- so *level* can happen
* A known ball, or emptying a reading, is again a tax
* Optimal play keeps the three readings as near equiprobable as possible
}

\notes{The first weighing that realises the ternary budget puts four against four and leaves four off. Level then means the odd ball is in the four left off; a tip couples a group of four with a direction, as 6 vs 6 did, but now the third symbol is alive. We do not give the rest of the tree. The design principle is the one already present in the information game: choose each measurement so that its outcomes are as nearly equiprobable as possible under the current posterior. That maximises expected information gain per weighing and is what makes the $3^3 \ge 24$ budget achievable in practice. Adding a known-normal ball, or arranging a weighing that can never balance, is the same kind of mechanism tax we already computed for $h_2(2/3)$.}

\newslide{Doable in Three --- Strategy Deferred}

\slides{The counting argument shows three weighings *must* be enough in principle.}

\slidesincremental{
* We do *not* give the sequence of groupings today
* Info gained and mechanism are separate ledgers --- score both
* Same moral as twenty questions: split the prior evenly, now three ways
}

\speakernotes{Stop here. Invite them to try Exercise 4.1 before reading MacKay's solution figure. Optional aside: 1--6 vs 7--12 can never balance, so it yields only one bit and is already suboptimal *once we know there are three readings*.}

\notes{We stop at the existence argument. Constructing the adaptive tree --- which balls on which pan at each step --- is MacKay's exercise, and solving it is the best way to feel what ``informative experiment'' means. What the lecture owns is the split between ledgers: $\log_2 24$ versus $\log_2 2$ or $\log_2 3$ is the information account; 6 vs 6, 4 vs 4, and padding with a known ball are the mechanical account. The two are not the same, and the known-ball tax is the exhibit.}

\addreading{MacKay-information03}{Exercise 4.1 and the discussion on pp.~69--70}

\endif

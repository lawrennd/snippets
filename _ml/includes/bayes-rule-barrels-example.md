\ifndef{bayesRuleBarrelsExample}
\define{bayesRuleBarrelsExample}
\editme

\newslide{Bayes' Theorem Example}

\slides{* There are two barrels in front of you. Barrel One contains 20 apples and 4 oranges. Barrel Two other contains 4 apples and 8 oranges. You choose a barrel randomly and select a fruit. It is an apple. What is the probability that the barrel was Barrel One?}

\newslide{Bayes’ Rule Example: Answer I}

\slides{
* We are given: 
  $$\begin{aligned}
    P(\text{F}=\text{A}|\text{B}=1) = & 20/24 \\
    P(\text{F}=\text{A}|\text{B}=2) = & 4/12 \\
    P(\text{B}=1) = & 0.5 \\
    P(\text{B}=2) = & 0.5
  \end{aligned}$$
}

\newslide{Bayes' Rule Example: Answer II}

\slides{
* We use the sum rule to compute: 
  $$\begin{aligned}
    P(\text{F}=\text{A}) = & P(\text{F}=\text{A}|\text{B}=1)P(\text{B}=1) \\& + P(\text{F}=\text{A}|\text{B}=2)P(\text{B}=2) \\
          = & 20/24\times 0.5 + 4/12 \times 0.5 = 7/12
   \end{aligned}$$
* And Bayes' rule tells us that: 
  $$\begin{aligned}
    P(\text{B}=1|\text{F}=\text{A}) = & \frac{P(\text{F} = \text{A}|\text{B}=1)P(\text{B}=1)}{P(\text{F}=\text{A})}\\ 
         = & \frac{20/24 \times 0.5}{7/12} = 5/7
  \end{aligned}$$}

\notes{Work the numbers on the board if time allows. The same pattern applies to coins, medical tests, or any two-hypothesis discrete update.}

\endif

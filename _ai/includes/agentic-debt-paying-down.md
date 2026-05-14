\ifndef{agenticDebtPayingDown}
\define{agenticDebtPayingDown}

\editme

\subsection{Paying Down Agentic Debt}

\newslide{Making the judgment layer explicit}

\slidesincremental{
* Agentic debt accumulates silently when automation buries judgment calls rather than surfacing them.
* Paying it down means extracting tacit policies into *explicit, inspectable rules*.
* Start with the edges: approval exceptions, escalation triggers, known-safe waivers.
}

\notes{The first step to paying down agentic debt is an audit of the judgment layer itself. Before automating a workflow, map the decisions that currently require human sense-making: which patterns always escalate, which anomalies are pre-approved exceptions, which actions are irreversible and therefore need a higher evidence bar. This is not a one-off exercise — it is an ongoing practice of making implicit judgment explicit before ceding it to an agent.

In practice, this looks like: (a) recording the policies that are already being followed but never written down; (b) specifying what evidence is required before a delegated decision can proceed; (c) defining which actions are reversible and which require pre-authorisation or a confirmation checkpoint.}

\newslide{"I don't know" as a control primitive}

\slidesincremental{
* Robust agentic systems need an explicit *"I don't know"* action — not just low-confidence prose.
* "I don't know" must be operational: halt the task, escalate with evidence, or request human input.
* This is not a model weakness. It is a safety control.
}

\notes{One of the most important missing primitives in current agentic deployments is a first-class "I don't know" action. Language models can produce plausible-sounding text under uncertainty, which makes them poorly calibrated detectors of their own limits. Agentic systems inherit this problem: a model that cannot reliably declare "I am out of depth" becomes a system that proceeds confidently into situations where it should halt.

An operational "I don't know" means: the agent stops execution of this subtask, records the evidence it has and what is missing, and routes to a human or a higher-authority agent with that evidence. The human cost of unnecessary escalations can be tuned empirically over time; the cost of undetected over-confidence is typically much higher.}

\newslide{Time-bounded delegation}

\slidesincremental{
* Every delegated task should have a time budget and a termination policy.
* At timeout: complete with evidence, or emit *"I don't know"* and escalate.
* Converts *hidden* judgment debt into *managed, measurable* risk.
}

\notes{A practical technique for paying down agentic debt is to assign each delegated subtask a time budget $\tau$ and a termination policy. If the agent completes within budget, it submits its result with supporting evidence. If it does not complete in time, it must either return the best available partial answer with caveats, or emit an explicit escalation signal that routes the decision to a human.

This converts the invisible judgment debt — "we do not know what the agent will do when it runs out of useful context" — into a visible, tunable policy. Over time, teams can calibrate budgets empirically by observing where escalations cluster, what the costs of human interruption are, and what proportion of "I don't know" escalations turn out to be genuinely novel versus recoverable edge cases.

The key insight is that agentic debt is not just a design-time property. It accumulates at runtime, every time a delegated decision completes without leaving a legible evidence trail. Time-bounded delegation with explicit termination makes that trail mandatory.}

\endif

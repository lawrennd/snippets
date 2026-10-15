\ifndef{harnessesAndSmallModels}
\define{harnessesAndSmallModels}

\editme

\subsection{Harnesses and Small Models}

\newslide{Two ideas behind commercial progress}

\slidesincremental{
* The *unreasonable effectiveness of orchestration*
* The *model minimisation* principle
* Together: harnesses + small models on *cognitive toil*
}

\notes{We are seeing two phenomena emerging around how businesses are implementing their agentic systems. The first of which we might refer to as *the unreasonable effectiveness of orchestration*
[@Lawrence:orchestration26a]. Because these models emulate human behaviour they become more
useful when they collaborate and call tools. This is inherited from people who, when well convened, can collaborate well and create an output that is greater than what those individuals could have done without communicating. The models can exploit the information infrastructure they are given. 

THe second idea is *model minimisation*. This is the
engineering corollary of the Good Regulator theorem
[@Conant:goodregulator70]: keep the system small enough that the people who
own the risk can still model what they oversee. Put together, commercial
progress is not about "always use the largest model" it is more building harnesses around smaller models and enabling the delivery of routine cognitive work or *cognitive toil*.}

\newslide{The unreasonable effectiveness of orchestration}

\slidesincremental{
* Models emulate human behaviour
* Humans collaborate naturally, so the models to too
* A harness is a set of tools and instructions
* Can be specified by a worker with knowledge of job
}

\notes{A language model alone produces text and responses. A harness supplies tools,
context, verification, and termination. The orchestration comes through the harness and is where much of the value is recovered.}

\include{_ai/includes/oscar-citizen-ai-router.md}

\include{_ai/includes/local-government-ai-accelerator.md}

\notes{ai@cam’s [Local Government AI Accelerator](https://www.ai.cam.ac.uk/calls/local-government-ai-accelerator/)
is how Cambridge partners with councils on this class of work: proof-of-concept
projects with local authorities as active partners from the outset, not as
end-users of a centre-led drop. OSCAR sits in that same demand-side pattern —
role-holders close to the work, university and civic partners in support.}

\newslide{Small models on cognitive toil}

\slidesincremental{
* Cognitive toil: high-volume, low-novelty mental work that consumes attention.
* Prefer the *least* model that handles the routine class reliably.
}

\notes{We can think of *cognitive toil* as
repetitive mental labour that does not exercise deep judgment but still (currently)
consumes scarce human attention. Organisations are full of it. Model
minimisation says: use the smallest decision-relevant model that reliably
handles that routine class inside a harness with explicit escalate / abstain
paths.}

\newslide{Who introduces and monitors the harness}

\slidesincremental{
* Deploy with the people who already *manage that role*.
* They hold the live model of exceptions, escalation, and “good enough”.
* If they cannot introduce and monitor it, the Good Regulator condition fails.
}

\notes{In contrast to typical digital deployments (e.g. the Horizon software system), a harness does not need to be a centre-led
"platform drop". It is introduced and monitored by the people who have been
managing the role. This means e.g. the payroll lead, the triage nurse, the claims
supervisor, the security on-call. Each of them already hold the tacit judgment
layer: what is routine, what is anomaly, when to halt. Small models inside
a harness keep the system modellable enough that those same people can
own deployment, tune stop-conditions, and contest outputs. }


\notes{The same point, put publicly: value arrives workflow by workflow,
with the people who know the work — not as one centralised deployment.}

\include{_business/includes/ft-letter-workflow-by-workflow.md}

\newslide{Do not lose the judgment}

\slidesincremental{
* Workflow-by-workflow only works if the *judgment* stays with the role.
* Automating toil without preserving exceptions makes judgment *invisible*, not absent.
* That invisibility is how agentic debt begins.
}

\notes{The FT letter argues for local adoption. The hazard is to hear
“workflow by workflow” and then automate each workflow past the people who
hold the judgment. Harnesses succeed when role-holders keep the live model:
what is routine, what escalates, when to halt. If the harness replaces that
judgment instead of surfacing it, the firm still looks productive while
regulation fails. The process continues; the model does not. That is the
start of agentic debt — and the reason model minimisation and role-held
oversight travel together.}

\endif

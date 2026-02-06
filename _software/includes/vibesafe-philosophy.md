\ifndef{vibesafePhilosophy}
\define{vibesafePhilosophy}

\editme

\subsection{VibeSafe's Philosophy}

\slidesincremental{
* Make intent explicit **before** implementation
* Catch misunderstandings early
* Cost: editing markdown vs unwinding code
}

\notes{VibeSafe's core philosophy is simple: force intent to be explicit before implementation. When correcting a misunderstanding costs editing a markdown file instead of unwinding code changes, you want to have that conversation early.

This isn't about creating overhead, it's about creating a checkpoint where humans can catch AI misinterpretation when it's cheap to fix.}

\subsection{Human-AI Collaboration}

\slidesincremental{
* AI systems: Powerful but underspecified
* They follow instructions and interpret
* Missing: shared context and intent
}

\notes{AI coding assistants are powerful ... like the BFG 9000 ... but maybe a little too powerful. When you underspecify ... or even when you correctly specify ... they include  implicit or incorrect assumptions.

The challenge is to creating shared context and ensuring the AI understands not just what you said, but what you meant. VibeSafe provides structures for making that context explicit. This isn't just good for you and the current AI, it's good for you and the rest of the team ... and future AIs.}

\subsection{From Intent to Documentation}

\slides{
$$\text{WHY} \rightarrow \text{WHAT} \rightarrow \text{HOW} \rightarrow \text{DO} \rightarrow \text{DOCUMENT}$$
$$\text{Tenets} \rightarrow \text{Requirements} \rightarrow \text{CIPs} \rightarrow \text{Backlog} \rightarrow \text{Doc Compression}$$
}

\notes{VibeSafe structures development as a flow from principles to implementation to documentation:

- **WHY** (Tenets): Your project's guiding principles
- **WHAT** (Requirements): Desired outcomes, not methods
- **HOW** (CIPs): Design decisions and architectural choices
- **DO** (Backlog): Specific implementation tasks
- **DOCUMENT** (Compression): Distilling the development history into formal docs

Each level is explicit, reviewable, and provides a checkpoint for ensuring shared understanding.}

\endif


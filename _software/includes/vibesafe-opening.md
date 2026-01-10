\ifndef{vibesafeOpening}
\define{vibesafeOpening}

\editme

\subsection{The AI Development Paradox}

\slides{
* You've used GitHub Copilot, Cursor, Claude Code...
* AI writes code faster than ever
* But have you debugged AI-generated code at 2am?
}

\notes{You're all experienced engineers. You've been using AI coding assistants such as GitHub Copilot, Cursor, Claude Code, maybe others. And you've seen the promise: code generation that's faster than anything we've had before.

But you've probably also experienced the flip side: debugging code that an AI generated based on a misunderstanding of your intent. Maybe it was a subtle architectural assumption. Maybe it interpreted "user authentication" differently than you meant. And you discovered it late, after it was wired through multiple files.}

\subsection{The Cost Model Has Inverted}

\slides{
* *Traditional development:*
  * Writing code: Expensive (human time)
  * Documentation: "We'll do it later"
* *AI-assisted development:*
  * Generating documentation: Cheap (AI does it)
  * Debugging misimplementation: Expensive (discovery lag)
}

\notes{In traditional development, writing code was the expensive part, i.e. human engineering time. Documentation was often deferred or skipped.

With AI assistance, this inverts. The AI can generate documentation quickly. But if the AI misunderstands your intent and implements the wrong thing, you discover it late. The cost isn't in writing the code, it's in unwinding the wrong implementation after it's integrated into your system.}

\subsection{A Natural Reaction}

\slides{
* "This looks like a lot of paperwork"
* And you'd be right to think that...
* ...if we were still in the old cost model
}

\notes{When you first see VibeSafe, a natural reaction is: "This looks like a lot of paperwork." And you'd be absolutely right to think that ... if we were still in the traditional cost model where human time writing code was the bottleneck.

But we're not in that model anymore. The bottleneck has shifted.}

\endif

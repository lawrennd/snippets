\ifndef{vibesafeDiscussion}
\define{vibesafeDiscussion}

\editme

\section{Discussion}

\subsection{Questions for You}

\slides{
* Have you experienced "AI misunderstanding" bugs?
* How do you currently ensure shared intent?
* What would make this more useful?
}

\notes{I'd like to hear from you:

**Your experiences**: Have you hit cases where an AI assistant misunderstood your intent and generated plausible but wrong code? How did you discover it? What was the cost?

**Current practices**: How do you currently ensure shared understanding between team members and AI assistants? Do you have patterns that work well?

**Improvements**: Looking at VibeSafe, what would make it more useful for your team? What seems like unnecessary overhead? What's missing?}

\subsection{Open Questions}

\slides{
* Right granularity for CIPs?
* Integration with existing tools?
* How to handle legacy code?
}

\notes{Some open questions we're exploring:

**Granularity**: What's the right level of detail for a CIP? Too detailed and it's busywork. Too high-level and it doesn't catch misunderstandings.

**Tool integration**: How should VibeSafe integrate with issue trackers, CI/CD, code review? What would make it feel more natural in your workflow?

**Legacy systems**: Most of us aren't starting greenfield. How do you introduce VibeSafe practices to an existing codebase? Where do you start?

**Team adoption**: If we wanted to try this with the team, what would be the barriers? What would help?}

\subsection{Try It Yourself}

\slides{
* One-line installation
* GitHub: lawrennd/vibesafe
* Works with any AI assistant
}

\notes{If you're interested in trying VibeSafe, it's a one-line install:

```bash
bash -c "$(curl -fsSL https://raw.githubusercontent.com/lawrennd/vibesafe/main/scripts/install-minimal.sh)"
```

It's on GitHub at lawrennd/vibesafe. MIT licensed. Works with Cursor, Copilot, Claude Code, or any AI assistant that can read markdown files.

I'd love to hear how it works (or doesn't work) for your projects.}

\subsection{Questions?}

\slides{
* Let's discuss
* Your insights will help shape this
* Thank you!
}

\notes{Thank you. Let's open it up for discussion. Your experience and insights will be invaluable in understanding whether this approach has legs, what needs to change, and how it might fit into real engineering practice.}

\endif
\endif

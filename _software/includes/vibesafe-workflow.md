\ifndef{vibesafeWorkflow}
\define{vibesafeWorkflow}

\editme

\subsection{The Workflow in Practice}

\subsection{Example: Adding Authentication}

\slides{
1. Check tenets: Which principles apply?
2. Write requirement: "Users must authenticate securely"
3. Create CIP: JWT vs session-based approach
}

\notes{Let's walk through a concrete example: adding authentication to your application.

First, you check your project's tenets. Maybe you have a tenet about "Security Without Friction" that guides this decision.

Then you write a requirement: "Users must authenticate securely with support for single sign-on." This is the **what**—the outcome you need.

Next, you create a CIP to explore the **how**: JWT tokens? Session-based auth? OAuth2 integration? The CIP documents your reasoning, trade-offs, and chosen approach. You review this with your team (human or AI) before implementing.}

\subsection{AI Natural Breakpoints}

\slides{
* After CIP creation → Review design
* After acceptance → Create tasks?
* After implementation → Validate
}

\notes{VibeSafe defines natural breakpoints in the workflow where AI assistants should pause for human review:

1. After creating a CIP (status: Proposed) — let the human(s) review the design
2. After accepting a CIP — ask if we should create backlog tasks now
3. After implementation — let the human test and validate

These aren't arbitrary, they're the points where human judgment is most valuable. The AI can generate the content, but humans verify it matches intent.}

\subsection{The What's Next Script}

\slides{
* Project status at a glance
* For humans and AI
* "What should I work on?"
}

\notes{VibeSafe includes a "What's Next" script that summarizes project status:

- Current git branch and recent commits
- CIPs by status (proposed, accepted, in progress, closed)
- Backlog items by priority
- Recommended next steps

Both humans and AI assistants use this to quickly understand "Where are we? What should I work on next?"

It's useful when an AI assistant or human starts the session, it gets immediate context without reading through dozens of files.}

\subsection{Documentation Compression}

\slides{
* After CIP is closed: compress into docs
* Development history → permanent reference
* Future developers understand **what**, not just **how**
}

\notes{After implementation is complete and a CIP is closed, there's a final step: compression.

You've now got the development history, why you made certain decisions, what alternatives you considered, how you implemented it. This is valuable, but future developers (human or AI) don't need to read all of that to understand the current state.

Compression means distilling the closed CIPs into streamlined formal documentation (like Sphinx docs). The history is preserved for those who need it, but the primary docs stay clean and focused.}

\endif
\endif

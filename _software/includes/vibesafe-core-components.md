\ifndef{vibesafeCoreComponents}
\define{vibesafeCoreComponents}

\editme

\subsection{Core Components}

\subsection{Tenets: Your Project's Principles}

\slides{
* 5-7 guiding principles
* Not rigid rules—principles to balance
* Example: "User Autonomy Over Prescription"
}

\notes{Tenets are your project's guiding principles, eventually 5-7 of them, enough to cover key decisions but few enough to actually remember and apply.

They're not rigid rules. When tenets conflict, you need judgment. For example, VibeSafe has a tenet of "User Autonomy Over Prescription" (let users configure things) that can conflict with "Simplicity at All Levels" (don't overwhelm with options). The resolution: sensible defaults with configuration options.}

\subsection{Requirements: What, Not How}

\slides{
* "Users can install with one command"
* Not: "Create install-minimal.sh script"
* Outcomes, not methods
}

\notes{Requirements define **what** needs to be true, not **how** to make it true.

"Users can install VibeSafe with a single command" is a requirement, it's an outcome. "Create an install-minimal.sh script" is implementation, it's a method.

This separation is crucial because it lets the AI (or you) explore multiple approaches to achieving the requirement. Maybe a shell script is best. Maybe it's a Python package. Maybe something else. The requirement stays constant while implementations can evolve.}

\subsection{CIPs: Design Before Implementation}

\slides{
* Code/Capability Improvement Plans
* Document design rationale
* Review before implementing
}

\notes{Code/Capability Improvement Plans (CIPs) are where you document design decisions before implementing them.

Each CIP includes:
- What problem it solves (Motivation)
- How it solves it (Detailed Description)
- Implementation plan with checkpoints
- Testing strategy
- Links to requirements it addresses

The key: you review and refine the CIP before writing code. When you discover the AI misunderstood something, you edit markdown, not code.}

\subsection{Backlog: Execution Tasks}

\slides{
* Specific implementation tasks
* Created when CIP is *accepted*
* Not when it's proposed
}

\notes{The backlog contains specific implementation tasks. Critically, you create backlog tasks only when a CIP moves from "Proposed" to "Accepted."

Why wait? Because you don't want to create detailed implementation tasks for a design that might change or be rejected. This avoids wasted effort and keeps the backlog focused on approved work.}

\subsection{Everything is Markdown + YAML}

\slides{
* Standard file formats
* Works with any AI assistant
* Cursor, Copilot, Claude Code, Codex...
}

\notes{A key design decision: everything is stored as standard markdown files with YAML frontmatter. No proprietary formats. No platform lock-in.

This means VibeSafe works with Cursor, GitHub Copilot, Claude Code, Codex, or any other AI assistant that can read project files. Following VibeSafe's own tenets: user autonomy over prescription.}

\endif


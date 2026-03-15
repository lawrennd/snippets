\ifndef{separationOfConcerns}
\define{separationOfConcerns}

\editme


\subsection{Separation of Concerns}

\slidesincremental{* Decompose your complex problem/task into parts.
* Each part manageable (e.g. by a small team)
* Recompose to solve total problem}

\newslide{Addresses Complex Challenge}

\slidesincremental{* Highly successful approach to complex tasks.
* Tuned to the human bandwidth limitation.
* But the whole system still hard to understand.
}
\notes{To construct such complex systems an approach known as "separation of
concerns" has been developed. The idea is that you architect your
system, which consists of a large-scale complex task, into a set of
simpler tasks. Each of these tasks is separately implemented. This is
known as the decomposition of the task.

This is where Jonathan Zittrain's beautifully named term "intellectual
debt" rises to the fore. Separation of concerns enables the construction
of a complex system. But who is concerned with the overall system?}

\newslide{Intellectual Debt}

\slidesincremental{
* Technical debt is the inability to *maintain* your complex software
    system.
* Intellectual debt is the inability to *explain* your software
    system.
}

\notes{Technical debt is the inability to *maintain* your complex software system. Intellectual debt is the inability to explain your software system.}

\notes{It is right there in our approach to software engineering. "Separation
of concerns" means no one is concerned about the overall system itself.}

\addatomic{separation of concerns}{84-85, 103, 109, 199, 284, 371}

\endif

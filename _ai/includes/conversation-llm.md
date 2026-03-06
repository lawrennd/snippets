\ifndef{conversationLlm}
\define{conversationLlm}
\editme

\newslide{}

\notes{\subsection{LLM Conversations}}


\figure{\includediagram{\diagramsDir/ai/anne-llm-conversation}{80%}}{The
focus so far has been on reducing uncertainty to a few representative
values and sharing numbers with human beings. We forget that most
people can be confused by basic probabilities for example the
prosecutor's fallacy.}{anne-llm-conversation}

\newslide{In practice ...}

\slidesincremental{* LLMs are already being used for robot planning @Huang-inner22

* Ambiguities are reduced when the machine has had large scale access
  to human cultural understanding.}

\newslide{Inner Monologue and Chain of Thought}

\notes{As far back as 2022 researchers in robotics have suggested
inner monologues for LLMs. See for example the paper
[Inner Monologue: Embodied Reasoning through Planning](https://innermonologue.github.io/)
@Huang-inner22. That's now widespread through chain of thought
approaches.}

\figure{\includeyoutube{0sJjdxn5kcI}{600}{450}}{The Inner Monologue
paper suggests using LLMs for robotic planning
[@Huang-inner22].}{ai-for-data-analytics}

\notes{By interacting directly with machines that have an
understanding of human cultural context, these machines share the
nature of uncertainty in the same way humans do.}

\endif

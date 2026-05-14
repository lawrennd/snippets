\ifndef{judgmentLayerExplicit}
\define{judgmentLayerExplicit}

\editme

\subsection{The Judgment Layer}

\newslide{Organisations as emulsions}

\slidesincremental{
* Organisations are a stable mixture: automatable *routines* and irreducible *human context*.
* In a working emulsion the two phases are inseparable — like oil and water held in suspension.
* The *judgment layer* is the interface: what gets challenged, what gets waived, what triggers a halt.
}

\notes{Think of an organisation as an emulsion. One phase is the automatable routines — rule-based decisions, standard workflows, repeatable processes. The other phase is the irreducible human context — tacit norms, exceptions, escalation paths, and situational awareness that rarely makes it into documentation. In a healthy organisation these two phases are held in a stable mixture. The judgment layer is the interface between them: the decisions that route a situation from routine handling to human attention.

When we automate workflows with agentic AI, we are in effect trying to distil the automatable phase and hand it to a system. But the emulsion is mixed: the judgment calls are tangled up with the routine steps. Automating without first extracting and formalising those judgment calls does not eliminate them — it just makes them invisible. That invisibility is agentic debt.}

\newslide{What the judgment layer looks like}

\slidesincremental{
* Approval exceptions: "we usually accept this class of risk without escalation".
* Escalation triggers: "this pattern always goes to a human, even if the rule says approve".
* Context-dependent waivers: policy says X, but the situation means Y is safer.
}

\notes{The judgment layer is not one decision but a distributed set of micro-interventions embedded in the fabric of how work flows through an organisation. Security teams accumulate this knowledge over years: which alerts are usually noise, which anomalies are actually fine because of a known upstream cause, which vendor exceptions are pre-approved. None of it is written down. It lives in the heads of experienced operators and in the patterns of who emails whom when something looks off.

For a security context, this is especially acute. The same log pattern can be routine or catastrophic depending on context that is not in the log. The judgment layer is the part of the organisation that holds that context.}

\endif

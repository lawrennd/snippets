\ifndef{goodRegulatorModelMinimisation}
\define{goodRegulatorModelMinimisation}

\editme

\subsection{The Good Regulator Theorem}

\newslide{The Good Regulator theorem}

\slidesincremental{
* Every good regulator of a system must be a *model* of that system.
* The judgement layer is the regulator: it must still *model* what it oversees.
* If the system outruns the model, regulation fails — even if the tools still run.
}

\notes{Conant and Ashby: a regulator that successfully holds a system within bounds
must, in effect, contain a model of that system [@Conant:goodregulator70]. An
information-theoretic reading is that optimal regulation supports $H(R|S)=0$ —
the regulator's action can be a deterministic function of system state. The
practical reading for commercial leaders is sharper. If institutional judgement
is still meant to regulate automated and agentic systems, those systems must
remain modellable by the people who own the risk. Opacity is not merely an
explainability preference; it is a failure of the regulator condition.}

\newslide{Why we minimise models}

\slidesincremental{
* We minimise so that we can *maintain a model*.
* Smallest decision-relevant representation that still supports oversight.
* Prefer decomposable systems over opaque monoliths.
}

\notes{Model minimisation is the engineering corollary of the Good Regulator
theorem. It is not aesthetic minimalism and not anti-capability. Capability
that cannot be modelled by the judgement layer is capability the institution
cannot regulate. The unit of design is the judgement-preserving interface —
including an explicit abstain / escalate path.}

\newslide{Against maximisation by default}

\slidesincremental{
* “Use the largest model” is a default, not a design.
* Capability without a modellable envelope is how debt compounds.
* Ask: what is the *least* system that still earns regulated trust?
}

\notes{Across cybernetics and organisational science this is the same object:
Beer's live regulator [@Beer:brainofthefirm72; @Beer:heartofenterprise79];
Ashby's law of requisite variety [@Ashby:introduction56]; uncertainty
absorption and exception handling [@March:organizations58]; Galbraith's
information-processing view of organisation design
[@Galbraith:organizationdesign74]; and the boundary between routine cases and
escalated cases in knowledge hierarchies [@Garicano:hierarchies00]. Agentic AI
puts new stress on it because language becomes action at machine speed.}

\endif

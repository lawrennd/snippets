\ifndef{demonGroupsHotCold}
\define{demonGroupsHotCold}

\editme

\subsection{The Demon Sorts Groups}

\slides{Hot versus cold is a coarse label --- this lecture's grouping, now with a policy.}

\slidesincremental{
* Group $G$: pass / no-pass under the membrane rule (tail vs body)
* Within group: collisions try to restore a Maxwellian $\pi_G$
* Local-equilibrium assumption: mixing inside each side is fast vs crossings
}

\speakernotes{Callback to the die: the demon pays attention to $H(w)$ over coarse velocity sets and hopes the within-group term stays near equilibrium. The detailed-balance calculation above already used that hypothesis.}

\notes{Maxwell's sorting rule partitions velocity space into coarse sets --- "hot enough to cross" versus "cold enough to cross" --- and applies different gates to each set. That is exactly this lecture's grouping: a deterministic label $G=g(\mathbf{v})$ plus residual uncertainty inside each label. The membrane calculation assumed each chamber stays close to a Maxwellian at its own $T$ --- local equilibrium, timescale separation between collisions and crossings. When that fails, the true steady state is no longer a pair of perfect Maxwellians (tails deplete). Information engines and demons play on the tension between moving probability among groups ($H(w)$) and the within-group bath term $\sum w_i H(p_i)$ that thermodynamics prices.

The compartments, kinetic layers, and two-ledger closure are this course's construction, not a result in Leff and Rex. Worksheet 3 builds on them. I will not mark you wrong for disagreeing with the bookkeeping; I will mark you wrong for treating it as a textbook theorem.}

\newslide{Lumpability (Pointer)}

\slides{When do the groups themselves form a Markov process?}

\slidesincremental{
* If exit rates agree for every microstate in a group $\Rightarrow$ coarse chain is Markov (lumpable)
* Otherwise coarse-graining leaves memory --- projection operators (Zwanzig/Mori), not this course's core
* Demon membrane: approximately lumpable only while local equilibrium holds
}

\notes{Kemeny--Snell lumpability is the precise condition under which a partition of a Markov chain induces another Markov chain on the groups. When it fails, the macro description needs memory of how the system entered the group. Name the issue; do not develop projection-operator formalism here.}

\endif

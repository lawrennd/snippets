\ifndef{demonGroupsHotCold}
\define{demonGroupsHotCold}

\editme

\subsection{The Demon Sorts Groups}

\slides{Hot versus cold is a coarse label --- week 2's grouping, now with a policy.}

\slidesincremental{
* Group $G$: pass / no-pass under the membrane rule (tail vs body)
* Within group: collisions try to restore a Maxwellian $\pi_G$
* Local-equilibrium assumption: mixing inside each side is fast vs crossings
}

\speakernotes{Callback to the die *and* to the extra partitions. Maxwellians are licensed in the distant bulks, not at the gate. Hot versus cold is a second grouping, now in velocity, on top of the spatial one. The number-flux $T_L$, $T_R$ split already used local equilibrium as a hypothesis --- and the energy ledger forbade extending it to the membrane.}

\notes{Maxwell's sorting rule partitions velocity space into coarse sets --- ``hot enough to cross'' versus ``cold enough to cross'' --- and applies different gates to each set. That is week 2's grouping again, now stacked on the spatial compartments: a deterministic label $G=g(\mathbf{v})$ plus residual uncertainty inside each label. Local equilibrium --- timescale separation between collisions and crossings --- is the claim we already restricted to the *distant* bulks. Extending it through the kinetic layers is what made number balance and energy balance incompatible. When that extension fails, the true steady state is no longer a pair of perfect Maxwellians (tails deplete). Information engines and demons play on the tension between moving probability among groups ($H(w)$) and the within-group bath term $\sum w_i H(p_i)$ that thermodynamics prices.}

\newslide{Lumpability (Pointer)}

\slides{When do the groups themselves form a Markov process?}

\slidesincremental{
* If exit rates agree for every microstate in a group $\Rightarrow$ coarse chain is Markov (lumpable)
* Otherwise coarse-graining leaves memory --- projection operators (Zwanzig/Mori), not this course's core
* Demon membrane: approximately lumpable only while local equilibrium holds
}

\notes{Kemeny--Snell lumpability is the precise condition under which a partition of a Markov chain induces another Markov chain on the groups. When it fails, the macro description needs memory of how the system entered the group. Name the issue; do not develop projection-operator formalism here.}

\endif

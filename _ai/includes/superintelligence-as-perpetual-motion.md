\ifndef{superintelligenceAsPerpetualMotion}
\define{superintelligenceAsPerpetualMotion}

\editme

\subsection{Superintelligence as Perpetual Motion}

\notes{Claims about imminent superintelligence or artificial general intelligence that will recursively self-improve to unbounded capability bear a striking resemblance to promises of perpetual motion machines. Both violate fundamental physical constraints.}

\slides{
*Perpetual Motion:* Violates thermodynamics

*Superintelligence Singularity:* Violates information bounds

*Same pattern of impossible promises*
}

\subsubsection{The Thermodynamic Constraint}

\notes{Perpetual motion machines fail because they violate the second law of thermodynamics. You cannot extract unlimited work from a finite system without an external energy source. Entropy must increase, energy must be conserved, and there are fundamental limits on efficiency set by temperature.}

\notes{These aren't engineering challenges to overcome with better designs, they're fundamental constraints built into the structure of physical law.}

\slides{
**Perpetual Motion Fails:**
* 2nd law: entropy increases
* 1st law: energy conserved  
* Efficiency limited by temperature
* *Fundamental, not engineering limits*
}

\newslide{The Information-Theoretic Constraint}

\notes{Similarly, unbounded intelligence fails because it would require unbounded information processing. The inaccessible game shows that information processing has thermodynamic costs through:

1. **Landauer's principle:** Information erasure costs $k_BT\log 2$ per bit
2. **Marginal entropy conservation:** Information cannot be created from nothing
3. **Fisher information bounds:** Information channel capacity is finite
4. **GENERIC structure:** Any real process has dissipative components}

\slides{
**Superintelligence Fails:**
* Landauer: erasure costs energy
* Conservation: can't create information
* Fisher bounds: finite channel capacity
* GENERIC: dissipation unavoidable
* **Fundamental information limits**
}

\subsection{The Recursive Self-Improvement Fallacy}

\notes{The superintelligence narrative often invokes "recursive self-improvement": an AI that makes itself smarter, which makes it better at making itself smarter, leading to explosive growth. This is supposed to lead to capabilities that far exceed human intelligence.}

\notes{But this violates conservation of information. To "improve" requires:
- **Learning:** Extracting information from environment (limited by Fisher information)
- **Memory:** Storing that information (limited by physical substrate)
- **Computation:** Processing information (limited by Landauer and thermodynamics)
- **Erasure:** Clearing memory for new information (dissipates energy)}

\notes{Each step has information-theoretic costs. You cannot recursively self-improve without limit any more than you can build a perpetual motion machine by clever arrangement of gears.}

\slides{
**Recursive Self-Improvement:**

"AI makes itself smarter → makes itself better at getting smarter → runaway growth"

**But requires:**
* Learning (Fisher-limited)
* Memory (physically limited)
* Computation (Landauer-limited)
* Erasure (dissipative)
}

\subsection{Embodiment as Thermodynamic Necessity}

\notes{The inaccessible game reveals why embodiment—physical constraints—is not a limitation to be overcome but a necessary feature of any information-processing system.}

\notes{The Fisher information matrix $G(\boldsymbol{\theta})$ defines the information topography. It determines:
- How fast information can flow
- What channels are available  
- What bottlenecks exist
- How much energy is needed

This topography is shaped by the physical implementation. A biological brain has different $G$ than a silicon chip, which has different $G$ than a quantum computer. *Each physical substrate creates its own information landscape with its own constraints.*}

\slides{
**Embodiment = Information Topography:**

Physical substrate → Fisher information $G(\boldsymbol{\theta})$

$G$ determines:
* Information flow rates
* Channel capacities
* Energy requirements
}

\notes{Promises of "uploading" consciousness or achieving superintelligence by removing physical constraints misunderstand the relationship between information and physics. Information processing *is* physical. The constraints aren't bugs, they're features that make information processing possible at all.}

\subsection{Why the Hype Persists}

\notes{If the constraints are so fundamental, why do smart people keep claiming superintelligence is just around the corner? Several reasons.

1. *Confusing capability with intelligence:* Current AI systems can do impressive things, but that doesn't mean they're on a path to unbounded capability
2. *Ignoring thermodynamic costs:* Information processing seems "free" compared to mechanical work, but Landauer's principle shows it has real energy costs
3. *Mistaking scaling for fundamental progress:* Making systems bigger isn't the same as removing fundamental constraints
4. *Economic incentives:* Billions of dollars flow toward exciting promises}

\slides{
**Why the Hype?**
* Confuse capability with unbounded intelligence
* Ignore thermodynamic costs
* Mistake scaling for fundamental progress
* Economic incentives for bold claims

*Same reasons perpetual motion had investors!*
}

\notes{Just as perpetual motion machines attracted investors in the 19th and early 20th centuries, superintelligence  claims attract billions today. But the fundamental constraints haven't changed. The idea of this work is that information theory provides as firm a bound on intelligence as thermodynamics provides on engines.}
\endif

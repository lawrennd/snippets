\ifndef{submodularityMultiInformation}
\define{submodularityMultiInformation}

\editme

\subsection{Multi-Information and Submodularity}

\notes{Before studying the dynamics that emerge from our four axioms, we need one more piece of information-theoretic machinery: the multi-information and its connection to submodularity.}

\subsubsection{Multi-Information Definition}

\notes{For a joint distribution over variables $\mathbf{x} = (x_1, \ldots, x_N)$, the **multi-information** (also called total correlation) measures how much the variables are correlated:
$$
I(\mathbf{x}) = \sum_{i=1}^N h_i - H(\mathbf{x})
$$
where:
- $h_i$ = marginal entropy of variable $i$
- $H(\mathbf{x})$ = joint entropy
- $I(\mathbf{x}) \geq 0$ with equality iff variables are independent

The multi-information tells us how much "correlation structure" exists in the system. When $I = 0$, the variables are completely independent. As $I$ increases, the variables become more correlated.}

\slides{
**Multi-Information:**
$$
I(\mathbf{x}) = \sum_{i=1}^N h_i - H(\mathbf{x})
$$
* Measures total correlation
* $I = 0$ → independent variables
* $I > 0$ → correlated
* $I \geq 0$ always
}

\newslide{Connection to Conservation}

\notes{Recall our conservation axiom: $\sum_{i=1}^N h_i = C$. Combining with the multi-information definition:
$$
H(\mathbf{x}) = \sum_{i=1}^N h_i - I(\mathbf{x}) = C - I(\mathbf{x})
$$

This means if marginal entropies are conserved, then:
- Joint entropy and multi-information are related by: $H + I = C$
- As multi-information increases (more correlation), joint entropy decreases
- As multi-information decreases (less correlation), joint entropy increases
- The system trades off between joint entropy and correlation structure

This will be called the **Information Relaxation Principle** in Lecture 3.}

\slides{
**With Conservation:**
$$
\sum h_i = C \quad \Rightarrow \quad H + I = C
$$
* Joint entropy $\leftrightarrow$ Multi-information tradeoff
* More correlation → less joint entropy
* Less correlation → more joint entropy
* *Information Relaxation Principle (L3)*
}

\subsection{Submodularity}

\notes{Entropy has a special property called **submodularity** or *diminishing returns*. This means that adding information to a "small" set helps more than adding it to a "big" set.

Formally, for any sets $A \subseteq B$ and element $x$:
$$
H(A \cup \{x\}) - H(A) \geq H(B \cup \{x\}) - H(B)
$$

The marginal contribution of $x$ decreases as the set grows.}

\slides{
**Submodularity (Diminishing Returns):**
$$
H(A \cup \{x\}) - H(A) \geq H(B \cup \{x\}) - H(B)
$$
* $A \subseteq B$
* Adding to small set helps more
* Marginal benefit decreases
* Like diminishing utility in economics
}

\newslide{Intuitive Example: Machine Learning}

\notes{Consider building a classifier:

**First feature** (e.g., image brightness): Huge improvement! We go from random guessing to something useful.

**Second feature** (e.g., edge detection): Still helpful, but the improvement is smaller. We already had some information.

**Tenth feature** (e.g., another edge detector): Marginal improvement. We probably already captured similar information with existing features.

**Hundredth feature**: Barely helps at all. The existing 99 features likely capture most useful information.

This is submodularity: each additional feature provides less and less marginal benefit. The entropy increase from adding a new variable diminishes as we already have more variables.}

\slides{
**ML Example: Adding Features**
* Feature 1: Huge jump in accuracy
* Feature 2: Helpful but smaller gain
* Feature 10: Small improvement
* Feature 100: Barely helps

*Diminishing returns in action*
}

\subsection{Why Submodularity Matters}

\notes{Submodularity of entropy has important implications for understanding information systems:

1. **Diminishing returns**:  adding information to a system provides decreasing marginal benefit as the system already contains more information.

2. **Optimization properties**: Submodular functions have well-studied optimisation properties. Maximising a submodular function subject to constraints often has favourable computational and analytical properties.

3. **Correlation structure**: In systems with many variables, submodularity suggests that not all variables will correlate uniformly. Instead, we expect to see clustered correlation patterns.

The precise implications of submodularity for the dynamics of The Inaccessible Game will emerge as we develop the framework in later lectures. For now, the key insight is that entropy's diminishing returns property affects how information can organise in a conserved system.}

\slides{
**Why It Matters:**
* Diminishing returns property
* Optimization properties
* Suggests clustered correlations
* Not uniform spreading
* *Implications for dynamics (later)*
}

\newslide{Multi-Information as Submodular}

\notes{The multi-information itself is submodular in a specific sense. For partitions of variables, adding more variables to the partition increases multi-information by diminishing amounts.

Consider building up a system variable by variable:
- Adding the first variable: $I = 0$ (no correlations yet)
- Adding the second: $I$ can jump significantly
- Adding the third: $I$ increase is smaller (submodularity)
- Adding many more: $I$ grows slowly (diminishing returns)

This means systems naturally self-organize into finite-sized correlated groups rather than having every variable correlated with every other variable. This locality property is essential for emergence.}

\slides{
**Multi-Information Growth:**
* 1 variable: $I = 0$
* 2 variables: $I$ can jump
* 3+ variables: growth slows
* Many variables: slow growth

*Submodularity → locality in correlations*
}

\subsection{Summary: Information Structure}

\notes{Pulling together the pieces:

**Conservation**: $\sum h_i = C$ fixes total information capacity

**Multi-information**: $I = \sum h_i - H$ measures correlation structure

**Tradeoff**: $H + I = C$ means joint entropy and correlation structure trade off

**Submodularity**: Diminishing returns in how information organizes

Together, these properties provide the foundation for understanding information organisation in conserved systems.

In Lecture 3, we'll derive the basic dynamics (maximum entropy production subject to conservation constraint). The role of submodularity in creating clustered "regimes"—where some variables are tightly correlated and others nearly independent—will emerge in later lectures when we study perturbation analysis and resolution constraints (Lectures 6-9).}

\slides{
**Summary:**
* Conservation: $\sum h_i = C$
* Multi-info: $I = \sum h_i - H$  
* Tradeoff: $H + I = C$
* Submodularity: diminishing returns

*Next (L3):* Derive basic dynamics

*Later (L6-9):* Regime emergence
}

\endif


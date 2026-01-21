\ifndef{inaccessibleGameIntroduction}
\define{inaccessibleGameIntroduction}

\editme

\subsection{The Inaccessible Game}

\notes{We call our framework the "inaccessible game" because the system is isolated from external observation: an outside observer cannot extract or inject information, making the game's internal state inaccessible.}

\slides{
**The Inaccessible Game:**
* System isolated from observation
* External observer cannot extract information
* Internal state is inaccessible
* Zero-player game with information-theoretic rules
}

\notes{Like other zero-player games, such as Conway's Game of Life [@Gardner-life70], the system evolves according to internal rules without external interference. But unlike cellular automata where rules are chosen by design, in our game the rules emerge from an information-theoretic principle.}

\subsection{Why "Inaccessible"?}

\notes{The game is inaccessible because our fourth axiom—information isolation—ensures that an external observer learns nothing. Recall from Baez-Fritz-Leinster that information gained from observing a process $f: p \rightarrow q$ is measured by entropy change:
$$
F(f) = H(p) - H(q).
$$}

\notes{But if marginal entropies are conserved ($\sum h_i = C$), then an external observer sees:
- Before observation: $\sum h_i = C$
- After observation: $\sum h_i = C$  
- Information gained: $\Delta(\sum h_i) = 0$

The observer learns nothing! The system is informationally isolated from the outside world.}

\slides{
**Why "Inaccessible"?**

From BLF axioms: Info gained = $H(p) - H(q)$

Our axiom: $\sum h_i = C$ (constant)

$$\Delta(\sum h_i) = 0 \Rightarrow \text{observer learns nothing!}$$
}

\subsection{What Makes It a Game?}

\notes{The "game" has the following characteristics:

**Players:** None (zero-player game)

**State:** A probability distribution over variables, parametrized by natural parameters $\boldsymbol{\theta}$

**Rules:** Evolve to maximize entropy production subject to the constraint $\sum h_i = C$

**Dynamics:** Emerge from information geometry (Fisher information) and the constraint structure}

\slides{
**Game Characteristics:**
* Zero-player game
* State = probability distribution $p(\mathbf{x}|\boldsymbol{\theta})$
* Rule = maximize entropy production
* Constraint = $\sum h_i = C$
* Dynamics = emerge from information geometry
}

\notes{The game starts in a maximally correlated state (high multi-information $I$, low joint entropy $H$) and evolves toward states of higher entropy. Since $I + H = C$, this means the system breaks down correlations ($I$ decreases) as entropy increases.}

\subsection{Connection to Physical Reality}

\notes{Why should we care about this abstract game? Because its dynamics exhibit structure that connects to fundamental physics:

1. **GENERIC structure:** The dynamics decompose into reversible (conservative) and irreversible (dissipative) components
2. **Energy-entropy equivalence:** In the thermodynamic limit, our marginal entropy constraint becomes equivalent to energy conservation
3. **Landauer's principle:** Information erasure necessarily involves the dissipative part of the dynamics}

\slides{
**Physical Connections:**
* GENERIC structure emerges
* Energy ↔ Entropy equivalence
* Landauer's principle derivable
* Bridge between information and physics
}

\notes{The inaccessible game provides an information-theoretic foundation for thermodynamic principles. It suggests that physical laws might emerge from information-theoretic constraints, rather than information theory being derived from physics.}

\endif

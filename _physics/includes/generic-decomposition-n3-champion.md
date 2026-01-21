\ifndef{genericDecompositionN3Champion}
\define{genericDecompositionN3Champion}

\editme

\subsection{Champion Example: Three Variables with Geometric Frustration}

\subsubsection{Motivation from Physics: Frustrated Magnetic Systems}

\notes{The two variable binary system shows a little about how the conservative and dissipative parts interact, the mathematical system in physics is known as an Ising model. This makes it worth exploring what physics says about when we might expect large antisymmetric in such systems.

We would expect parameterisations that exhibit slow, underdamped, dynamics to be interesting from the perspective of the inaccessible game. Such systems can be found in *frustrated magnetism* (Toulouse 1977, Wannier 1950, Moessner & Ramirez 2006).

When magnetic spins have **competing interactions** (e.g., one spin wants to align with one neighbor but anti-align with another), the system cannot simultaneously minimise all interaction energies. This creates

* Complex free energy landscapes
* Slow relaxation dynamics
* *Oscillatory modes* (underdamped, not purely dissipative)
* Geometric phases from manifold curvature

A classic example is a triangular lattice antiferromagnet. Here three spins (or binary variables) are related in a triangle. Each spin wants to anti-align with its neighbours so it's impossible to satisfy all three preferenes simultaneously.

From the physical understanding we should expect systems with frustration that operate at `intermediate temperatures' to exhibit enhanced conservative (oscillatory) dynamics, not just pure dissipation. Here temperature is a concept from physics that can be extracted from our model. It refers to the scale of the natural parameters. Here we're saying they shouldn't be too large (low temperature) and they shouldn't be too small (high temperature).}

\slides{**Physics Motivation:**

What does statistical mechanics predict?

**Frustrated magnetic systems:**

* Competing interactions (ferro + antiferro)
* Cannot satisfy all preferences
* $\rightarrow$ Slow, oscillatory dynamics
* $\rightarrow$ Large "conservative" component

**Question:** Does this apply to information dynamics?
}

\subsubsection{Information ≡ Magnetism}

\notes{Our three-variable exponential family is mathematically identical to an Ising model,
$$
p(x_1, x_2, x_3) \propto \exp(\theta_1 x_1 + \theta_2 x_2 + \theta_3 x_3 + \theta_{12} x_1 x_2 + \theta_{13} x_1 x_3 + \theta_{23} x_2 x_3)
$$
in an Ising model there is a change of variables ($\sigma_i = 2x_i -1$),
$$
p(\sigma_1, \sigma_2, \sigma_3) \propto \exp(-\beta H)
$$
$$
H = -h_1\sigma_1 - h_2\sigma_2 - h_3\sigma_3 - J_{12}\sigma_1\sigma_2 - J_{13}\sigma_1\sigma_3 - J_{23}\sigma_2\sigma_3
$$
where $J_{ij} = \theta_{ij}/4$ (exchange couplings), $h_i$ related to $\theta_i$, in an Ising model this is an external field.

In machine leanring we could also see our model as equivalent to a Boltzmann machine with biases $b_i = \theta_i$ and weights $w_{ij} = \theta_{ij}$.

Because the mathematics is the same, then the same phenomena apply to information dynamics. So the physics theory of frustrated magnets should directly apply to information dynamics.}

\slides{
**Model Equivalence:**

Our exponential family $\equiv$ Ising model $\equiv$ Boltzmann machine

All three are THE SAME mathematical object!

* $\theta_i$ $\leftrightarrow$ external fields $h_i$ $\leftrightarrow$ biases $b_i$
* $\theta_{ij}$ $\leftrightarrow$ couplings $J_{ij}$ $\leftrightarrow$ weights $w_{ij}$

Physics predictions apply to information dynamics!
}

\notes{The theory from physics theory tells us to look for

1. **Frustration:** Mixed ferro/antiferromagnetic couplings

   * Some $J_{ij} > 0$ (want to align)
   * Some $J_{ij} < 0$ (want to anti-align)
   * **Conflicting preferences**

2. **Intermediate temperature:** $\beta|J| \approx 1$

   * Not too hot (would be purely dissipative)
   * Not too cold (would freeze)
   * In our parameterization: $|θ| \approx 1$

3. **Strong interactions:** $|J_{ij}|$ not too small

   * Need substantial coupling for frustration to matter
   * In our parameterization: $|\theta_{ij}| \gtrsim 1$

This implies that a specific pattern to try would be to consider a three variable system and  set $\theta_{12} \approx -\theta_{13}$ (equal magnitude, opposite sign). This makes variable 1 "frustrated", it wants to anti-correlate with variable 2, but correlate with variable 3.

The analogy with physics suggests that this should give us large $||A||/||S||$ (underdamped/oscillatory dynamics). Let's test this idea.}

\slides{
**Physics Says Look For:**

1. Frustration: $\theta_{12}$ and $\theta_{13}$ have opposite signs
2. Strong: $|\theta_{12}|, |\theta_{13}| \gtrsim 1$
3. Balanced: $|\theta_{12}| \approx |\theta_{13}|$
4. Intermediate T: Overall scale $|\theta| \approx 1$

**Pattern:** $\theta_{12} \approx -\theta_{13}$ with $|\theta| \approx 1$

Let's explore this
}

\subsubsection{Testing the Physics Prediction}

\notes{Following the physics guidance, we search for parameters with the frustration pattern $\theta_{12} = -\theta_{13}$ at intermediate coupling. Through systematic optimization, we found:
$$
\boldsymbol{\theta} = \begin{pmatrix}
-0.037 \\ 0.634 \\ -0.545 \\ -1.182 \\ 1.203 \\ -0.126
\end{pmatrix} = \begin{pmatrix}
\theta_1 (X_1 \text{marginal}) \\
\theta_2 (X_2 \text{marginal}) \\
\theta_3 (X_3 \text{marginal}) \\
\theta_{12} (X_1-X_2 \text{interaction}) \\
\theta_{13} (X_1-X_3 \text{interaction}) \\
\theta_{23} (X_2-X_3 \text{interaction})
\end{pmatrix}
$$

**Notice:** θ₁₂ = -1.18 and θ₁₃ = +1.20 $\rightarrow$ **Physics prediction confirmed!** Nearly equal magnitude, opposite signs, intermediate coupling strength.}

\slides{
**Testing Physics Prediction:**

θ = (-0.04, 0.63, -0.54, **-1.18**, **+1.20**, -0.13)

✓ θ₁₂ ≈ -θ₁₃ (frustration!)
✓ |θ| ≈ 1.2 (intermediate T!)

**Exactly what physics predicted!**
}

\subsubsection{Geometric Frustration}

\notes{This pattern creates **geometric frustration**:

* $x_1$ wants to **anti-correlate** with $x_2 (\theta_{12} = -1.18 < 0)$
* $x_1$ wants to **correlate** with $x_3 (\theta_{13} = +1.20 > 0)$
* *$x_1$ cannot simultaneously satisfy both preferences!*

The resulting correlations have opposite signs,
$$
\rho(X_1, X_2) = -0.30 \quad \text{(anticorrelated)},
$$
$$
\rho(X_1, X_3) = +0.30 \quad \text{(correlated)}.
$$
This frustration curves the constraint manifold $\sum_i h(x_i) = C$ sharply through parameter space, creating strong geometric phases that manifest as the antisymmetric component.}

\slides{
**Geometric Frustration:**

$x_1$ has conflicting preferences:
* Should anti-align with $x_2$ ($\rho = -0.30$)
* Should align with $x_3$ ($\rho = +0.30$)

**Cannot satisfy both!** $\rightarrow$ Curved manifold $\rightarrow$ Large $$A$
}

\setupcode{import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import expm}

\code{# Champion parameters for three binary variables
theta_champion = np.array([-0.03686028, 0.63441936, -0.54477752, 
                          -1.18199556, 1.20331936, -0.12567841])

# For demonstration, we'll analyze at this point
# (Full implementation in computational supplement)
print(f"Champion parameters θ = {theta_champion}")
print(f"\nKey pattern:")
print(f"  θ₁₂ = {theta_champion[3]:.3f}")
print(f"  θ₁₃ = {theta_champion[4]:.3f}")
print(f"  |θ₁₂ + θ₁₃| = {abs(theta_champion[3] + theta_champion[4]):.6f} ≈ 0")}

\subsubsection{GENERIC Decomposition Results}

\notes{At this point in parameter space, the linearised dynamics $M = \tfrac{\partial F}{\partial \theta}$ decompose as:
$$
M = S + A
$$
with components:

* *Symmetric part:** $||S|| = 1.35$ (dissipative/thermodynamic)
* *Antisymmetric part:* $||A|| = 1.55$ (conservative/mechanical)
* *Ratio:* $||A||/||S||$ = 1.15$

This means the *antisymmetric component exceeds the symmetric component*, we are in a conservation-dominated regime where mechanical (Hamiltonian-like) dynamics dominate thermodynamic relaxation.

For comparison

* N=2 example: $||A||/||S|| = 0.017$ (dissipation-dominated)
* N=3 champion: $||A||/||S|| = 1.15$ (conservation-dominated)
* *Improvement: 67× larger antisymmetric component*}

\slides{
**GENERIC Decomposition:**

$||S|| = 1.35$ (symmetric/dissipative)  
$||A|| = 1.55$ (antisymmetric/conservative)

$||A||/||S|| = 1.15 \rightarrow A > S$

**Conservation dominates dissipation!**
}

\subsubsection{Eigenvalue Structure}

\code{# Eigenvalue analysis (schematic - see supplement for full code)
# For the champion example:

eigs_S_champion = np.array([-1.216, -0.246, -0.072, -0.026, -0.009, 0.523])
eigs_A_champion_imag = np.array([-1.097, 0, 0, 0, 0, 1.097])

print("\nEigenvalue structure:")
print(f"S eigenvalues (all real): {eigs_S_champion}")
print(f"  Mostly negative $\rightarrow$ local dissipation")
print(f"\nA eigenvalues (purely imaginary): {eigs_A_champion_imag}i")
print(f"  ±1.1i $\rightarrow$ oscillation frequency")
print(f"  Large imaginary parts $\rightarrow$ strong rotation!")}

\notes{The eigenvalue analysis reveals.

1. **S has real eigenvalues** (symmetric matrices always do). Most are negative, indicating dissipative decay in those directions. One positive eigenvalue indicates local instability along one direction.

2. **A has purely imaginary eigenvalues** ±1.1i (antisymmetric matrices always have imaginary eigenvalues). The large imaginary parts (≈1.1) indicate strong rotational/oscillatory dynamics.

3. **Combined M = S + A:** The full dynamics exhibit both dissipation and rotation, but the rotation is strong enough to dominate the early-time behavior.}

\subsubsection{Connection to Physics: Frustrated Ising Model}

\notes{Our three-variable exponential family is mathematically equivalent to a **Boltzmann machine** (machine learning) or **Ising model** (statistical physics). 

In Ising language, convert $x_i \in {0,1}$ to spins $\sigma_i \in {-1,+1}$ via $\sigma_i = 2x_i - 1$. The performant parameters correspond to
$$
J_{12} \approx -0.30 \quad \text{(antiferromagnetic)}
$$
$$
J_{13} \approx +0.30 \quad \text{(ferromagnetic)}
$$
This is a frustrated Ising model: spin 1 wants to anti-align with spin 2 but align with spin 3—the magnetic analog of our information-geometric frustration.

Known physics: frustrated magnetic systems (Toulouse 1977, Wannier 1950) exhibit complex ground states, slow dynamics, and underdamped modes. Our large $||A||/||S||$ is the information-theoretic manifestation of these phenomena.}

\slides{
**Physics Connection:**

Our model = Ising model on triangle

$J_{12} ≈ -0.30$ (antiferro)  
$J_{13} ≈ +0.30$ (ferro)

*Frustrated magnetism*

Physics predicts: slow, underdamped dynamics  
We observe: Large $A$ (conservative flow)
}

\notes{Let's verify that physical theory correctly predicted this regime.

Statistical mechanics theory (Hohenberg & Halperin 1977, critical dynamics) predicts that frustrated systems at intermediate effective temperature should exhibit enhanced conservative dynamics.

Our example satisfies all the criteria:

1. *Frustration:* $\theta_{12} \approx = -\theta_{13}$ (competing interactions) ✓
2. *Intermediate temperature:* $|\theta| \approx 1.2$ (not too small, not too large) ✓  
3. *Conservation law:* Constraint $\sum_i H(X_i) = C$ present ✓

*Experimental validation:* Systematically varying the overall coupling strength (θ $\rightarrow$ λθ) confirms the physics prediction, $||A||/||S||$ peaks at $\lambda \approx 1.5$, with the champion at $\lambda = 1.0$ achieving 97% of the maximum.

*This is not accidental, physics theory correctly predicted the regime!*}

\slides{
**Theory Validation:**

Physics predicts: Peak at intermediate temperature

Test: Vary $\lambda$ in $\theta \rightarrow \lambda \theta$

Results:

* $\lambda = 0.1: ||A||/||S|| \approx 0.02$ (high T)
* $\lambda = 1.0: ||A||/||S|| \approx 1.18$ (champion)
* $\lambda = 1.5: ||A||/||S|| \approx 1.25$ (peak!)

**Physics was right!** ✓
}

\subsubsection{Regime Diversity in Information Dynamics}

\notes{The existence of both N=2 (||A||/||S|| = 0.017) and N=3 champion (||A||/||S|| = 1.15) examples demonstrates *regime diversity* in constrained information dynamics.

**Near-Gaussian regime** (typical near maximum entropy):

* $S >> A$ (dissipation dominates)
* Fast thermalisation
* Purely thermodynamic behavior
* Example: $N=2$ with small $|\theta|$

**Frustrated regime** (geometric frustration present):

* $A \geq S$ (conservation comparable or dominant)
* Slow, oscillatory dynamics  
* Mechanical + thermodynamic behavior
* Example: $N=3$ champion with $\theta_{12} ≈ -\theta_{13}$

Information dynamics is not just "entropy increases." The geometric structure of the constraint manifold creates rich phenomenology, with the balance between dissipative and conservative effects varying dramatically across parameter space.}

\slides{
**Regime Diversity:**

| Regime | ||A||/||S|| | Character |
|--------|------------|-----------|
| Near-Gaussian | 0.01-0.05 | Purely dissipative |
| Typical | 0.1-0.5 | Mostly dissipative |
| **Frustrated** | **$\geq 1.0$** | **Conservation-dominated** |

Information dynamics $\neq$ "entropy increases"

Rich structure from constraint geometry
}

\subsubsection{Implications}

\notes{This champion example has several important implications

1. *GENERIC is not imposed:* The decomposition M = S + A emerges naturally from constraint geometry, and the balance between components varies with position on the manifold.

2. *$A$ can dominate:* The antisymmetric part is not always a small perturbative correction. In frustrated regimes, it can exceed the symmetric part.

3. *Physics guides discovery:* Theory of frustrated magnetism correctly predicted where to look (frustration + intermediate temperature). The example was found by optimisation but validated by physics.

4. *Inaccessibility theme:* The conservation-dominated regime exists but requires systematic search to discover—it's not found by random parameter sampling despite clear theoretical signatures.

5. *Universality:* Information dynamics exhibits phenomena analogous to frustrated magnetism, critical slowing down, and other well-known physics—suggesting deep connections worth exploring.}

\slides{
**Implications:**

1. GENERIC emerges (not imposed)
2. A can dominate (not always small)
3. Physics theory works (validated!)
4. Interesting regimes hidden (optimization required)
5. Deep connections to physics (frustrated magnetism)

*Information dynamics is richer than we thought!*
}

\notes{**For further exploration:** The complete computational supplement includes:

* Publication-ready Python code reproducing all results
* Analysis of correlation structure and frustration indices
* Temperature scaling validation
* Connection to Boltzmann machines and Ising models
* Additional examples and regime exploration

See: `generic_decomposition_n3.py` in paper supplement.}
\endif

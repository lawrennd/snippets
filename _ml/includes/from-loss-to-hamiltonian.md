\ifndef{fromLossToHamiltonian}
\define{fromLossToHamiltonian}
\editme

\subsection{From Loss Landscapes to Hamiltonians}

\notes{The energies of the previous section --- quadratic residual, cross-entropy, Boltzmann-machine pairwise score --- are not only static formulae. Training *moves* on them. This section reconnects that movement to classical mechanics: the loss is a potential, gradient descent is walking downhill, practice is stochastic, and Hamiltonian Monte Carlo restores the missing kinetic energy.}

\newslides{Walking Down an Energy}

\slides{Gradient descent on a loss is walking downhill on an energy surface.}

\slidesincremental{
* Contours of $E(\mathbf{w})$ = elevation lines on a hill
* Steepest descent: step opposite $\nabla E$
* Same $E$ as least squares / negative log-likelihood
}

\notes{Imagine standing on a hillside in fog and wanting the bottom. You cannot see the whole landscape, but you can feel the steepest downward slope at your feet. Repeated steps opposite the gradient reach a local minimum. That is gradient descent on $E(\mathbf{w})$ --- for linear least squares, the bowl is convex and the minimum is unique.}

\setupplotcode{import numpy as np
import matplotlib.pyplot as plt
import mlai
import mlai.plot as plot}

\code{# Toy line: the error surface is the quadratic energy of the residual.
rng = np.random.default_rng(42)
x = np.linspace(0, 1, 25)
m_true, c_true = 1.4, -3.1
y = m_true * x + c_true + 0.15 * rng.standard_normal(x.shape)

m_vals = np.linspace(m_true - 3, m_true + 3, 80)
c_vals = np.linspace(c_true - 3, c_true + 3, 80)
m_grid, c_grid = np.meshgrid(m_vals, c_vals)
E_grid = np.zeros_like(m_grid)
for i in range(m_grid.shape[0]):
    for j in range(m_grid.shape[1]):
        E_grid[i, j] = ((y - m_grid[i, j] * x - c_grid[i, j]) ** 2).sum()

fig, ax = plt.subplots(figsize=(5, 5))
plot.regression_contour(fig, ax, m_vals, c_vals, E_grid)
mlai.write_figure('loss-energy-contour.svg', directory='\writeDiagramsDir/ml')}

\figure{\includediagram{\diagramsDir/ml/loss-energy-contour}{55%}}{Contours of the least-squares energy $E(m,c)=\sum_n(y_n-mx_n-c)^2$. Steepest descent walks toward the bowl.}{loss-energy-contour}

\newslides{Potential Energy}

\slides{The loss is a *potential energy* $V(\mathbf{q})$ on parameter space.}

\slidesincremental{
* Configuration $\mathbf{q}=\mathbf{w}$: where the system sits
* Force $\propto -\nabla V$: direction of steepest descent
* Common analogy: ball in a bowl; GD is the overdamped limit
}

\notes{In mechanics, potential energy $V(\mathbf{q})$ depends on position. Gravity on a landscape is the everyday example; electrostatic energy of a charge configuration is another. Gradient descent treats model parameters as a position $\mathbf{q}$ and the training objective as $V(\mathbf{q})$. The update $\mathbf{q}\leftarrow\mathbf{q}-\eta\nabla V$ is the discrete, friction-dominated limit of a particle sliding on that potential --- no inertia, only the force from $V$.}

\newslides{In Practice: Stochastic}

\slides{Large-scale training estimates $\nabla V$ from a random mini-batch --- stochastic gradient descent.}

\slidesincremental{
* Full-batch $\nabla V$: exact force, expensive
* SGD: noisy force; cheap; enables online updates
* Noise can help escape shallow traps (less relevant for convex bowls)
}

\notes{When $n$ is huge, summing the residual energy over every datum each step is prohibitive. Stochastic gradient descent replaces $\nabla V$ by an unbiased estimate from one example or a mini-batch. The walk is no longer smooth: the particle feels a jittering force. That is still dynamics on a *potential*; only the force estimate is random.}

\newslides{Where Is the Kinetic Energy?}

\slides{Potential alone is only half of classical mechanics. Where is the kinetic energy?}

\slidesincremental{
* GD / SGD: overdamped --- friction, no momentum inventory
* Momentum methods (heavy ball, Adam): heuristic inertia
* Physics: kinetic energy $K(\mathbf{p})$ lives on *momentum* $\mathbf{p}$
}

\notes{A Newtonian particle has both potential and kinetic energy. Pure gradient descent never tracks a momentum conjugate to $\mathbf{q}$; each step forgets velocity. Momentum SGD and Adam reintroduce inertia heuristically. Hamiltonian mechanics does it properly: introduce momentum $\mathbf{p}$ and a kinetic energy $K(\mathbf{p})$, usually $\frac{1}{2}\mathbf{p}^\top M^{-1}\mathbf{p}$.}

\newslides{The Hamiltonian}

\slides{
$$
H(\mathbf{q},\mathbf{p}) = K(\mathbf{p}) + V(\mathbf{q})
$$
}

\slidesincremental{
* Total energy = kinetic + potential
* Hamilton: $\dot{\mathbf{q}}=\partial H/\partial\mathbf{p}$, $\dot{\mathbf{p}}=-\partial H/\partial\mathbf{q}$
* $H$ conserved along the flow (ideal, frictionless case)
}

\notes{The Hamiltonian $H$ is the sum of kinetic and potential energies. Hamilton's equations generate a flow on the joint $(\mathbf{q},\mathbf{p})$ space that conserves $H$ when the system is isolated. For sampling, one chooses $V(\mathbf{q})=-\log p(\mathbf{q})$ (up to a constant) so that the marginal on $\mathbf{q}$ under the Boltzmann weight $e^{-H}$ recovers the target density $p(\mathbf{q})$.}

\newslides{Hamiltonian Monte Carlo}

\slides{HMC: invent momentum, simulate Hamiltonian dynamics, accept/reject.}

\slidesincremental{
* Draw $\mathbf{p}\sim\mathcal{N}(0,M)$; simulate leapfrog steps on $H$
* Propose $(\mathbf{q}',\mathbf{p}')$; Metropolis test on $H$
* Marginal samples of $\mathbf{q}$ target $p(\mathbf{q})\propto e^{-V(\mathbf{q})}$
}

\notes{Hamiltonian Monte Carlo (originally *hybrid* Monte Carlo) uses fictitious momentum variables so proposals move far in parameter space while staying near level sets of $H$. Discretisation error is corrected by a Metropolis accept/reject on the Hamiltonian. The method turns gradient information about $V$ into efficient exploration of high-dimensional densities --- exactly the setting of Bayesian neural network weights. For a modern textbook account that places HMC among MCMC kernels in the same free-energy language as this course, see Section 11.4.2 of [@Welling-generative26] (with the Hamiltonian preliminaries in Section 3.2.1).}

\figure{\includejpg{\diagramsDir/people/radford-neal}{35%}}{Radford M. Neal (University of Toronto).}{radford-neal}

\newslides{Radford Neal}

\slides{Radford Neal brought Hamiltonian Monte Carlo into Bayesian neural nets.}

\slidesincremental{
* Toronto; Bayesian learning and MCMC
* Hybrid Monte Carlo for backpropagation networks [@Neal:hmc92]
* PhD thesis: Bayesian neural nets; infinite width $\to$ GP [@Neal:bayesian94]
}

\notes{Radford Neal is a Canadian computer scientist at the University of Toronto whose work sits at the junction of Bayesian statistics and neural networks. In 1992 he showed how to train backpropagation networks with the hybrid Monte Carlo method [@Neal:hmc92] --- Hamiltonian dynamics as a proposal mechanism for posterior sampling over weights. His 1994 thesis [@Neal:bayesian94] remains a model of clarity: Bayesian neural nets in finite width, and the observation that infinite-width nets with suitable priors become Gaussian processes. HMC is the bridge from "energy as loss" to "energy as the potential in a physical sampler."}

\newslides{Hamiltonian Monte Carlo in ``mlai``}

\slides{Teachable HMC: invent momentum, leapfrog on $H$, Metropolis on $\Delta H$.}

\slidesincremental{
* Target: $V(\mathbf{q})=-\log p(\mathbf{q}\mid\mathcal{D})$ (loss as potential)
* ``HamiltonianMonteCarlo`` in ``mlai``; trace $H$ and accept rate
* Contrast: SGD point estimate vs HMC posterior samples
}

\notes{The reusable component lives in ``mlai.hmc`` (CIP-0008): diagonal-mass kinetic energy, leapfrog proposals, and a Metropolis correction on $\Delta H$. Below we first overlay leapfrog paths on a 2D quadratic potential (standard normal / least-squares bowl), then contrast an SGD point estimate with HMC samples for a small logistic regression --- the same energy language as the lecture.}

\code{# 2D quadratic potential: V(q)=0.5||q||^2  (standard normal target).
# Leapfrog trajectories on the same contour language as regression_contour.
from mlai import HamiltonianMonteCarlo

potential = lambda q: 0.5 * np.dot(q, q)
grad_potential = lambda q: np.asarray(q, dtype=float)

hmc = HamiltonianMonteCarlo(
    potential=potential,
    grad_potential=grad_potential,
    step_size=0.15,
    n_steps=10,
)
result, trajectories = hmc.sample(
    q0=np.zeros(2), n_samples=40, random_state=0, return_trajectory=True
)

q1 = np.linspace(-3, 3, 80)
q2 = np.linspace(-3, 3, 80)
Q1, Q2 = np.meshgrid(q1, q2)
V_grid = 0.5 * (Q1 ** 2 + Q2 ** 2)

fig, ax = plt.subplots(figsize=(5, 5))
plot.hmc_contour_trajectories(
    ax, q1, q2, V_grid,
    trajectories=trajectories[:12],
    samples=result.samples,
    fontsize=16,
)
ax.set_title(f'HMC leapfrog paths (accept rate {result.accept_rate:.2f})')
mlai.write_figure('hmc-quadratic-trajectories.svg', directory='\writeDiagramsDir/ml')}

\figure{\includediagram{\diagramsDir/ml/hmc-quadratic-trajectories}{55%}}{Leapfrog trajectories and samples from teachable HMC on $V(\mathbf{q})=\tfrac12\|\mathbf{q}\|^2$. Accept/reject keeps the chain on the Boltzmann target $e^{-V}$.}{hmc-quadratic-trajectories}

\code{# SGD point estimate vs HMC samples for logistic regression.
# Potential V(w) = -log p(w|D) with a flat prior (negative log-likelihood).
from mlai import LR, Basis, linear, HamiltonianMonteCarlo

rng = np.random.default_rng(0)
X = rng.normal(size=(60, 1))
y = (1.5 * X[:, 0] + 0.25 * rng.normal(size=60) > 0).astype(float).reshape(-1, 1)
model = LR(X, y, Basis(linear, number=2))

def potential(q):
    model.parameters = q
    return -float(model.log_likelihood())

def grad_potential(q):
    model.parameters = q
    return np.asarray(model.gradients, dtype=float)

# Point estimate by steepest descent on V
q_sgd = np.zeros(2)
for _ in range(250):
    q_sgd = q_sgd - 0.05 * grad_potential(q_sgd)

hmc = HamiltonianMonteCarlo(
    potential=potential, grad_potential=grad_potential,
    step_size=0.04, n_steps=10,
)
hmc_result = hmc.sample(q0=q_sgd, n_samples=300, random_state=1)

fig, axes = plt.subplots(3, 1, figsize=(6, 5), sharex=True)
plot.hmc_traces(axes, hmc_result, param_indices=[0, 1], fontsize=12)
axes[0].set_title(
    f'Logistic HMC traces (accept {hmc_result.accept_rate:.2f}); '
    f'SGD point = ({q_sgd[0]:.2f}, {q_sgd[1]:.2f})'
)
mlai.write_figure('hmc-logistic-traces.svg', directory='\writeDiagramsDir/ml')
print('SGD:', q_sgd, 'HMC mean:', hmc_result.samples.mean(axis=0))}

\figure{\includediagram{\diagramsDir/ml/hmc-logistic-traces}{70%}}{Hamiltonian and weight traces for logistic regression. $V(\mathbf{w})=-\log p(\mathbf{w}\mid\mathcal{D})$; SGD gives one downhill point, HMC a cloud of posterior samples.}{hmc-logistic-traces}

\speakernotes{Name kinetic energy and Neal; show the trajectory figure if builds are available. Emphasise V = -log posterior, not a new loss species.}

\addreading{@Neal:hmc92}{Hybrid Monte Carlo for backpropagation networks}
\addreading{@Neal:bayesian94}{Bayesian Learning for Neural Networks (thesis)}
\addreading{@Welling-generative26}{Section 11.4.2 (Hamiltonian Monte Carlo); cf. Section 3.2.1}

\endif

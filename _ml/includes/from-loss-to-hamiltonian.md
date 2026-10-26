\ifndef{fromLossToHamiltonian}
\define{fromLossToHamiltonian}
\editme

\subsection{From Loss Landscapes to Hamiltonians}

\notes{Seeing standard energies from machine learning as simply the logarithm of the probability leads to a form of static energy. It's only the "potential energy" of a system. The aim is to find the minimum potential energy, and that is what we call learning. So what of "kinetic energy".}

\notes{We can think of the movement of the system as being the *learning dynamics*. The training is the movement of the parameters towards the minimum. That movement could have mass, and therefore momentum and kinetic energy.}

\notes{Sometimes this analogy is proposed, like in momentum variables for stochastic gradient descent, but the analogy seems loose. One place where it's tight is *Hamiltonian Monte-Carlo*. }

\newslide{Walking Down an Energy}

\slides{Gradient descent: 'walking downhill'}

\slidesincremental{
* Contours of $\objectiveFunction(\weightVector)$ = elevation lines on a hill
* Steepest descent: step opposite $\nabla \objectiveFunction$
* Same $\objectiveFunction$ as least squares / negative log-likelihood
}

\notes{Imagine a mass on a hill. It is sensitive to the pull of gravity as transmitted to it through the local slope. This is the potential energy, $\objectiveFunction(\weightVector)$, acting as a force. The force is taken by the gradient of the potential energy which gives the slope, $\nabla \objectiveFunction(\weightVector)$.}

\notes{In gradient descent we take repeated steps opposite the gradient to reach a local minimum. We consider a little example below where the loss surface, the energy, is taken from a small regression problem where the true line has a gradient of $m=1.4$ and an offset of $c=-3.1$. We sample some data from that line by adding noise with a standard deviation of $0.15$. Then we show the energy landscape for this system.}

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

\figure{\includediagram{\diagramsDir/ml/loss-energy-contour}{55%}}{Contours of the least-squares energy $\objectiveFunction(m,c)=\sum_n(y_n-mx_n-c)^2$. Steepest descent walks toward the bowl.}{loss-energy-contour}

\notes{In physics the parameters would be the position, $q$, instead of the weights, $w$. And typically (for a Hamiltonian) we denote the potential energy in physics by $V(\cdot)$, so instead of $\objectiveFunction(\weightVector)$ we have $V(\mathbf{q})$.}

\newslide{Potential Energy}

\slides{The loss is a *potential energy* $V(\mathbf{q})$ on parameter space.}

\slidesincremental{
* Configuration $\mathbf{q}=\weightVector$: where the system sits
* Force $\propto -\nabla V$: direction of steepest descent
* Common analogy: ball in a bowl; GD is the overdamped limit
}

\notes{So in mechanics, potential energy $V(\mathbf{q})$ depends on position, $q$. Gravity on a landscape is the everyday example mentioned above. But there are other forms of potential energy, for example the electrostatic energy of a charge configuration. Or the displacement of a spring. Gradient descent treats model parameters as a position $\mathbf{q}$ and the training objective as $V(\mathbf{q})$. The update $\mathbf{q}\leftarrow\mathbf{q}-\eta\nabla V$ is a discrete, \emph{friction}-dominated limit of a particle sliding on a potential. There is no inertia, there is only force from $V(\cdot)$.}

\newslide{In Practice: Stochastic}

\notes{Modern neural network models train when the number of data points is very large. This makes computing the exact gradients very computationally expensive. The energy is typically decomposed as a sum over data points,
$$
\objectiveFunction(\weightVector, \mathbf{X}) = \sum_i \objectiveFunction(\weightVector, \mathbf{x}_i)
$$
where the full data $\mathbf{X} = \{ \mathbf{x}_i\}_{i=1}^\numData$.}

\slides{SGD estimates $\nabla V$ from a random mini-batch}

\slidesincremental{
* Full-batch $\nabla V$: exact force, expensive
* SGD: noisy force; cheap; enables online updates
* Noise can help escape shallow traps (less relevant for convex bowls)
}

\notes{So when $\numData$ is huge, the sum becomes prophibitive. Stochastic gradient descent replaces $\nabla V$ by an unbiased estimate from one example or a mini-batch. The walk is no longer smooth: the particle feels a jittering force. That is still dynamics on a *potential*; only the force estimate is random.}

\notes{The closely related stochastic gradient with Langevin dynamics (SGLD, @Welling-langevin11) makes this connection very explicit. There the descent is taken to be a descent in a high friction regime which is subject to *thermal noise*. Thermal noise is the response of the descending particle to being bumped by particles of a surrounding fluid, like in Brownian motion. So SGLD is like Brownian motion in a potential well.}

\newslide{Where Is the Kinetic Energy?}

\slides{Where is the kinetic energy?}

\slidesincremental{
* GD / SGD: overdamped---friction, no momentum inventory
* Momentum methods (heavy ball, Adam): heuristic inertia
* Physics: kinetic energy $T(\mathbf{p})$ lives on *momentum* $\mathbf{p}$
}

\notes{A classical particle has both potential and kinetic energy. Pure gradient descent never tracks a momentum conjugate to $\mathbf{q}$; each step forgets velocity. Momentum SGD and Adam reintroduce inertia heuristically. Hamiltonian mechanics does it properly: introduce momentum $\mathbf{p}$ and a kinetic energy $T(\mathbf{p})$, usually $\frac{1}{2}\mathbf{p}^\top M^{-1}\mathbf{p}$.}

\newslide{The Hamiltonian}

\slides{
$$
H(\mathbf{q},\mathbf{p}) = T(\mathbf{p}) + V(\mathbf{q})
$$
}

\slidesincremental{
* Total energy = kinetic + potential
* Hamilton: $\dot{\mathbf{q}}=\partial H/\partial\mathbf{p}$, $\dot{\mathbf{p}}=-\partial H/\partial\mathbf{q}$
* $H$ conserved along the flow (ideal, frictionless case)
}

\notes{The Hamiltonian $H$ is the sum of kinetic and potential energies. Hamilton's equations are a mainstay of mechanics. They generate a flow on the joint $(\mathbf{q},\mathbf{p})$ space that conserves $H$ when the system is isolated. For sampling, one chooses $V(\mathbf{q})=-\log p(\mathbf{q})$ (up to a constant) so that the marginal on $\mathbf{q}$ under the Boltzmann weight $e^{-H}$ recovers the target density $p(\mathbf{q})$.}

\addreading{@Welling-generative26}{Section 3.2.1}

\newslide{Hamiltonian Monte Carlo}

\slides{HMC: invent momentum, simulate Hamiltonian dynamics, accept/reject.}

\slidesincremental{
* Draw $\mathbf{p}\sim\mathcal{N}(0,M)$; integrate Hamilton's equations for a short fictitious time
* Propose the *endpoint* $(\mathbf{q}',\mathbf{p}')$; Metropolis test on $H$
* Marginal samples of $\mathbf{q}$ target $p(\mathbf{q})\propto e^{-V(\mathbf{q})}$
}

\notes{Hamiltonian Monte Carlo (originally *hybrid* Monte Carlo) uses fictitious momentum variables so proposals move far in parameter space while staying near level sets of $H$. The continuous flow cannot be integrated in closed form for a general $V$, so we discretise. Discretisation error is corrected by a Metropolis accept/reject on the Hamiltonian. The method turns gradient information about $V$ into efficient exploration of high-dimensional densities. The method was originally developed for Bayesian sampling of neural network weights.}

\notes{In these systems time is introduced as a "fictitious variable" representing the evolution of the algorithm and the momentum variables are known as "auxiliary variables". The idea is to show that as time increases the system converges to the stationary distribution associated with the energy function, $\objectiveFunction(\weightVector)$.}

\newslide{Why Stay on a Contour of $H$?}

\slides{Moving along a contour of $H$ costs nothing.}

\slidesincremental{
* Target on $(\mathbf{q},\mathbf{p})$: $\pi\propto e^{-H(\mathbf{q},\mathbf{p})}$
* Along a contour $H$ is constant, so $\pi$ is constant
* Metropolis accepts with $\min(1,e^{-\Delta H})$: $\Delta H\approx 0$ means accept
}

\notes{We want samples from $p(\mathbf{q})\propto e^{-V(\mathbf{q})}$. Hamiltonian Monte Carlo
works on an enlarged space, adding a momentum $\mathbf{p}$ so that the joint density is
$\pi(\mathbf{q},\mathbf{p})\propto e^{-H(\mathbf{q},\mathbf{p})}=e^{-V(\mathbf{q})}e^{-T(\mathbf{p})}$.
The $\mathbf{q}$ marginal is the target we care about, and $\mathbf{p}$ is a nuisance variable we discard.

Now ask what makes a good proposal. A Metropolis step accepts with probability
$\min(1,e^{-\Delta H})$ (given the map is reversible and volume preserving, which is the
next section's business). A proposal is cheap to accept when it lands where $\pi$ is about
as large as where it started, which means $\Delta H\approx 0$. Along a contour of $H$ the
joint density $\pi$ does not change at all, so a move that stays on the contour is one the
target is indifferent to.

Compare random-walk Metropolis. A big step in a random direction usually goes uphill in
$V$, the density drops, and the step is rejected. So the step size has to stay small, and
the walk diffuses. A contour of $H$ is different: it can be long, and you can travel all
the way round it at no cost in acceptance.}

\newslide{Contours Are Not Contours of $V$}

\slides{Staying on a level of $H$ is not staying at a level of $V$.}

\slidesincremental{
* $H=V(\mathbf{q})+T(\mathbf{p})$: kinetic energy converts to potential and back
* Up the side of the bowl, $\mathbf{p}$ shrinks; back down, it grows
* Fresh $\mathbf{p}\sim\mathcal{N}(0,M)$ jumps to a new level of $H$
}

\notes{It would be a mistake to read this as keeping $\mathbf{q}$ at constant $V$. A particle
on a level set of $H$ rolls up the side of the well, slowing as it goes, and rolls back
down. Kinetic energy $T$ and potential energy $V$ trade off while their sum stays fixed. So
$\mathbf{q}$ travels a long way and visits many values of $V$, and that is exactly the
exploration we want.

What the flow cannot do is change the level of $H$. That job goes to the momentum refresh.
Drawing $\mathbf{p}\sim\mathcal{N}(0,M)$ afresh is an exact Gibbs update of
$\pi(\mathbf{p}\mid\mathbf{q})$, and it changes $T$, hence $H$, while leaving $\mathbf{q}$ alone.
Each iteration therefore has two parts: a random hop between levels, and a deterministic,
free-of-charge trip around the level we landed on. Together they cover the joint space.}

\code{import numpy as np
import matplotlib.pyplot as plt
import mlai
import mlai.plot as plot

fig, ax = plt.subplots(figsize=(5, 5))
plot.hmc_level_refresh(ax, hamiltonians=(0.5, 1.0, 2.0), fontsize=16)
mlai.write_figure('hmc-level-refresh.svg', directory='\writeDiagramsDir/ml')}

\figure{\includediagram{\diagramsDir/ml/hmc-level-refresh}{55%}}{Unit harmonic oscillator, $H=(q^2+p^2)/2$. Circles are levels of $H$. The solid arc rides one level (Hamiltonian flow). The dashed jump at fixed $q$ is a momentum refresh onto a new level.}{hmc-level-refresh}

\speakernotes{Solid = free trip around a contour. Dashed = Gibbs update of $p$, which changes $H$ and leaves $q$ alone.}

\newslide{Why Not Just Descend?}

\slides{Descent crosses contours of $V$. Sampling must not.}

\slidesincremental{
* Descent goes toward the mode: great for a point estimate, wrong for a distribution
* Each descent step changes $V$ a lot, so $\pi$ changes a lot, so it gets rejected
* High dimensions: typical samples sit away from the mode
}

\notes{This ties back to the energy story. When $V$ was a loss, crossing its contours was the
whole point: that is how we reach the bottom of the bowl. When $e^{-V}$ is a distribution
the bottom is just the single most probable point, and in high dimensions most of the
probability mass lies in a shell around it rather than at it. Samples have to be spread over
that shell, so a move that keeps dropping to lower $V$ is working against us. The Hamiltonian flow
gives us a way to travel without changing the density, which is the one thing descent
cannot do.

The shell is not a metaphor. For $q\sim\mathcal{N}(0,I_d)$ we have $\|q\|^2\sim\chi^2_d$, with mean $d$ and variance $2d$. The relative width of that law is $\sqrt{2/d}$, so as $d$ grows the mass concentrates near $\|q\|^2=d$, a spherical shell of radius $\sqrt{d}$, not at the mode $q=0$. Descent toward the mode is walking *out* of the typical set.}

\code{import numpy as np
import matplotlib.pyplot as plt
import mlai
import mlai.plot as plot

fig, ax = plt.subplots(figsize=(6, 4))
plot.chi2_concentration(ax, dims=(2, 10, 50), fontsize=16)
mlai.write_figure('chi2-concentration.svg', directory='\writeDiagramsDir/ml')}

\figure{\includediagram{\diagramsDir/ml/chi2-concentration}{60%}}{Density of $\|q\|^2/d$ for $q\sim\mathcal{N}(0,I_d)$. Mean is $1$ for every $d$; the mass tightens around that value. Typical samples sit in a shell, not at the mode.}{chi2-concentration}

\speakernotes{Point at $d=50$: almost all the mass is near $\|q\|^2=d$. The mode of the Gaussian is still the origin. Descent heads for a point that is not where samples live.}

\newslide{Why Leapfrog?}

\slides{We now know we want to follow a contour of $H$. The computer cannot follow a curve, it takes steps.}

\slidesincremental{
* A descent-shaped step walks off the level: $H$ grows, and Metropolis fights the drift
* The discrete map must be reversible and volume-preserving, or the accept/reject is no longer a small correction
}

\notes{The computer cannot follow a contour as a curve. It takes steps. We already know why those steps have to stay near a level of $H$: that move is free, and Metropolis accepts it. The remaining question is which discrete map keeps us there.

A careless step has the same shape as gradient descent: evaluate the field, move. That was the right move when $V$ was a loss. Here it walks off the contour, $H$ grows, and Metropolis is asked to undo a structural failure.}

\speakernotes{The contour argument is done. This slide is the discrete-step problem. Then Euler leaving the circle, then leapfrog.}

\newslide{Euler Leaves the Orbit}

\slides{Forward Euler on a quadratic well: each step is a shear, the circle inflates.}

\slidesincremental{
* $q\leftarrow q+\varepsilon p$, $p\leftarrow p-\varepsilon q$
* $H$ grows at every step
* Metropolis on $\Delta H$ then rejects almost everything
}

\notes{Forward Euler is the descent-shaped integrator: evaluate the field, take a step. On the harmonic well $V(q)=q^2/2$ the true motion in $(q,p)$ is a circle. Euler does
$$
q\leftarrow q+\varepsilon p,\qquad p\leftarrow p-\varepsilon q
$$
using the *old* $q$ in the momentum update. Each step is a shear. The radius grows. $H$ at the end is larger than $H$ at the start. Run Metropolis on that $\Delta H$ and you are fighting a systematic pump of energy.

The continuous flow was reversible and volume-preserving: a small cloud of possible $(q,p)$ --- an ensemble of microstates --- kept its area as it rode around the circle (Liouville). Euler inflates the cloud and cannot be run backwards by the same rule. The Metropolis correction that was supposed to mop up a small discretisation error is then asked to undo a structural failure, and it cannot.}

\newslide{Leapfrog Stays Near It}

\slides{Leapfrog: half-step $\mathbf{p}$, full-step $\mathbf{q}$, half-step $\mathbf{p}$.}

\slidesincremental{
* Reversible: flip $\mathbf{p}$, replay, flip $\mathbf{p}$
* Each substep has $\det J=1$ --- a cloud of states keeps its area
* $H$ wobbles without a secular drift, so accept rates stay high
}

\notes{Leapfrog (velocity Verlet) splits the momentum update around the position update: a half-step of $\mathbf{p}$, a full-step of $\mathbf{q}$, a half-step of $\mathbf{p}$. Reverse the tape by flipping the sign of $\mathbf{p}$, taking the same steps, flipping $\mathbf{p}$ again. Each substep is a shear whose Jacobian is triangular with ones on the diagonal, so a blob of possible $(\mathbf{q},\mathbf{p})$ keeps its area. $H$ still wobbles --- the map is not the true flow --- but the wobble does not accumulate a drift. Metropolis then sees a small $\Delta H$ and the accept rate stays usable.

That is the reason for leapfrog. Not that it is a more accurate ODE solver in the usual sense. A high-order Runge--Kutta can track the circle more closely and still fail reversibility or volume, and then the Metropolis correction is no longer a small mopping-up. The discretisation has to respect the geometry that made the continuous flow a valid proposal in the first place.}

\speakernotes{Do not derive the symplectic form. The figure is the argument: Euler walks off the circle, leapfrog stays. Name reversible + volume-preserving; stop.}

\code{import numpy as np
import matplotlib.pyplot as plt
import mlai

# Harmonic oscillator H = (q^2 + p^2)/2. Exact motion is the unit circle
# from (1, 0). Euler inflates it; leapfrog stays nearby.
eps = 0.3
n_steps = 40
q0, p0 = 1.0, 0.0

def euler_path(q, p, eps, n):
    qs, ps = [q], [p]
    for _ in range(n):
        q_new = q + eps * p
        p_new = p - eps * q
        q, p = q_new, p_new
        qs.append(q)
        ps.append(p)
    return np.array(qs), np.array(ps)

def leapfrog_path(q, p, eps, n):
    qs, ps = [q], [p]
    for _ in range(n):
        p = p - 0.5 * eps * q
        q = q + eps * p
        p = p - 0.5 * eps * q
        qs.append(q)
        ps.append(p)
    return np.array(qs), np.array(ps)

q_eu, p_eu = euler_path(q0, p0, eps, n_steps)
q_lf, p_lf = leapfrog_path(q0, p0, eps, n_steps)
theta = np.linspace(0, 2 * np.pi, 200)

fig, ax = plt.subplots(figsize=(5, 5))
ax.set_aspect('equal')
ax.plot(np.cos(theta), np.sin(theta), 'k--', linewidth=1, label='exact $H$')
ax.plot(q_eu, p_eu, 'C1-o', markersize=3, linewidth=1, label='Euler')
ax.plot(q_lf, p_lf, 'C0-o', markersize=3, linewidth=1, label='leapfrog')
ax.plot([q0], [p0], 'ko', markersize=5)
ax.set_xlabel('$q$')
ax.set_ylabel('$p$')
ax.set_xlim(-2.2, 2.2)
ax.set_ylim(-2.2, 2.2)
ax.legend(frameon=False, loc='upper right')
mlai.write_figure('leapfrog-vs-euler.svg', directory='\writeDiagramsDir/ml')}

\figure{\includediagram{\diagramsDir/ml/leapfrog-vs-euler}{55%}}{Harmonic oscillator $H=(q^2+p^2)/2$, forty steps of size $0.3$ from $(1,0)$. The exact motion is the dashed circle. Euler inflates $H$; leapfrog stays near the level set.}{leapfrog-vs-euler}

\newslide{The Algorithm: Hop, Ride, Correct}

\slides{Each iteration: hop to a new level, ride around it, correct.}

\slidesincremental{
1. **Hop:** draw $\mathbf{p}\sim\mathcal{N}(0,M)$ (changes $H$, not $\mathbf{q}$)
2. **Ride:** $L$ leapfrog steps from $(\mathbf{q},\mathbf{p})$ to $(\mathbf{q}',\mathbf{p}')$
3. **Correct:** accept with probability $\min(1,e^{-\Delta H})$, else stay at $\mathbf{q}$
}

\notes{Each move alone fails. The momentum refresh moves between levels of $H$
but leaves $\mathbf{q}$ where it was. The leapfrog ride moves $\mathbf{q}$ a long way but
stays on one level, so alone it could never visit the others. Both leave
$e^{-H}$ invariant, and alternating them covers the joint space: a random hop
between levels, then a nearly free trip around the level we landed on.

The Metropolis step is the safety net. Leapfrog does not follow the level exactly,
so $\Delta H$ is small but not zero, and the accept/reject removes the bias that
would otherwise leave us sampling the wrong density.

Two knobs. The step size $\varepsilon$ sets how well leapfrog stays on the level,
and so the accept rate. The number of steps $L$ sets how far round the level we
travel. Too few and the chain is a random walk. Too many and the orbit curves
back toward where it started, which wastes computation.}

\code{# One HMC iteration. V, grad_V: potential and its gradient.
# Leapfrog matches mlai.hmc.leapfrog with unit mass.
def hmc_step(q, V, grad_V, eps, L, rng):
    p = rng.standard_normal(q.shape)           # 1. hop: new level of H
    H0 = V(q) + 0.5 * p @ p

    q_new, p_new = q.copy(), p.copy()          # 2. ride: leapfrog
    p_new -= 0.5 * eps * grad_V(q_new)
    for _ in range(L - 1):
        q_new += eps * p_new
        p_new -= eps * grad_V(q_new)
    q_new += eps * p_new
    p_new -= 0.5 * eps * grad_V(q_new)
    p_new = -p_new                             # flip: makes the map reversible

    H1 = V(q_new) + 0.5 * p_new @ p_new        # 3. correct: Metropolis on dH
    if np.log(rng.uniform()) < H0 - H1:
        return q_new, True
    return q, False}

\speakernotes{Say it as three verbs: hop, ride, correct. Then point at the trajectory
figure: the curves are step 2, the markers are what survives step 3.}

\code{import numpy as np
import matplotlib.pyplot as plt
import mlai
import mlai.plot as plot

fig, ax = plt.subplots(figsize=(5, 5))
plot.hmc_hop_ride(ax, hamiltonians=(0.5, 1.0, 2.0), step_size=0.25, n_steps=12, fontsize=16)
mlai.write_figure('hmc-hop-ride.svg', directory='\writeDiagramsDir/ml')}

\figure{\includediagram{\diagramsDir/ml/hmc-hop-ride}{55%}}{Hop, ride, correct on $H=(q^2+p^2)/2$. Dashed verticals: momentum refresh (hop). Marked polylines: leapfrog (ride). Large markers: accepted endpoints (correct).}{hmc-hop-ride}

\newslide{Trajectories Propose; Endpoints Sample}

\slides{Curves are step 2; markers are what survives step 3.}

\slidesincremental{
* The leapfrog path builds one proposal --- waypoints are discarded
* Only the accepted endpoint enters the chain
* Next iteration hops again: fresh $\mathbf{p}$, new level of $H$
}

\notes{With the algorithm in place this is a reading of the figure, not a new warning. Hamiltonian dynamics explore a level set of $H$ to construct a proposal (the ride). The sample from $p(\mathbf{q})\propto e^{-V(\mathbf{q})}$ is the position $\mathbf{q}'$ if Metropolis accepts (the correct). Reject, and the chain stays at $\mathbf{q}$. Either way the curve is scaffolding for one move, not a cloud of draws. The next iteration hops: a fresh $\mathbf{p}$ lands on a new level, and we ride again.}

\speakernotes{Point at the quadratic figure: curves = step 2; markers = step 3. The three circles were the same loop in $(q,p)$.}

\addreading{@Welling-generative26}{Section 11.4.2}

\newslide{Radford Neal}

\figure{\includejpg{\diagramsDir/people/radford-neal}{35%}}{Radford M. Neal (University of Toronto).}{radford-neal}

\newslide{Radford Neal}

\slides{Radford Neal brought Hamiltonian Monte Carlo into Bayesian neural nets.}

\slidesincremental{
* Toronto; Bayesian learning and MCMC
* Hybrid Monte Carlo for backpropagation networks [@Neal:hmc92]
* PhD thesis: Bayesian neural nets; infinite width $\to$ GP [@Neal:bayesian94]
}

\notes{Radford Neal is a Canadian computer scientist at the University of Toronto who (along with David MacKay) introduced ideas form Bayesian statistics into machine learning and neural networks. He introduced the hybrid Monte Varlo method for training neural networks with backpropagation [@Neal:hmc92]. The Hamiltonian dynamics act as a proposal mechanism for posterior sampling over weights. His 1994 thesis [@Neal:bayesian94] is still worth reading today. Alongside the benefits of the HMC approach he showed how infinite-width nets with suitable priors become Gaussian processes. Over time the term Hamiltonian was preferred to hybrid, and this allows us to really see the connection between "energy as loss" and "energy as the potential in a physical sampler." Meaning that our sampling algorithm is being built by an analogy to a well-understood physical system.}

\addreading{@Neal:hmc92}{Hybrid Monte Carlo for backpropagation networks}
\addreading{@Neal:bayesian94}{Bayesian Learning for Neural Networks (thesis)}


\subsection{Hamiltonian Monte Carlo Example}

\slidesincremental{
* Target: $V(\mathbf{q})=-\log p(\mathbf{q}\mid\mathcal{D})$ (loss as potential)
* ``HamiltonianMonteCarlo`` in ``mlai``; trace $H$ and accept rate
* Contrast: SGD point estimate vs HMC posterior samples
}

\notes{The reusable component lives in ``mlai.hmc``. It has diagonal-mass kinetic energy, leapfrog *proposals*, and a Metropolis correction on $\Delta H$ --- hop, ride, correct, as above. Below we first overlay leapfrog paths on a 2D quadratic potential (standard normal / least-squares bowl) --- curves are the ride, markers are what the correct kept --- then contrast an SGD point estimate with HMC samples for a small logistic regression --- the same energy language as the lecture.}

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

\newslide{}

\figure{\includediagram{\diagramsDir/ml/hmc-quadratic-trajectories}{55%}}{Leapfrog *trajectories* (curves) are proposals, not samples. Markers are accepted endpoints only. Target $V(\mathbf{q})=\tfrac12\|\mathbf{q}\|^2$; Metropolis on $\Delta H$ keeps the chain on $e^{-V}$.}{hmc-quadratic-trajectories}

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

\newslide{}

\figure{\includediagram{\diagramsDir/ml/hmc-logistic-traces}{70%}}{Hamiltonian and weight traces for logistic regression. $V(\weightVector)=-\log p(\weightVector\mid\mathcal{D})$; SGD gives one downhill point, HMC a cloud of posterior samples.}{hmc-logistic-traces}

\speakernotes{Name kinetic energy and Neal. Hop, ride, correct is the loop. Euler leaves the circle, leapfrog stays. Trajectory figure: curves = ride; markers = correct. $V=-\log$ posterior, not a new loss species.}


\endif

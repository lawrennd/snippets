\ifndef{spontaneousOrganization}
\define{spontaneousOrganization}

\editme

\subsection{Spontaneous Organization Through Entropy Maximization}

\notes{For the system to 'spontaneously organise' we need to understand how  how mutual information evolves under our dynamics.

We're maximizing entropy in the natural parameter space $\boldsymbol{\theta}$, not directly in probability space. This distinction is crucial - while maximizing entropy in probability space would lead to independence between variables, maximizing entropy in natural parameter space can simultaneously increase both joint entropy and mutual information.}

\slides{
* Can entropy maximization lead to information organization
* Requires: mutual information increases despite overall entropy growth
* Would provides theoretical foundation for emergence of structure
}

\newslide{Formal Analysis of Spontaneous Organization}

\notes{
Joint distribution over variables $Z = (X, M)$, where $M$ represents memory variables in an information reservoir (at a saddle point in the dynamics) and $X$ represents observable variables. The system evolves by maximizing entropy $S$ in the natural parameter space $\boldsymbol{\theta}$,
$$
\frac{\text{d}\boldsymbol{\theta}}{\text{d}t} = \eta \nabla_{\boldsymbol{\theta}}S[p(z,t)].
$$
To understand spontaneous organization, we need to examine how mutual information $I(X;M)$ evolves under these dynamics. We can decompose the joint entropy,
$$
S[p(z,t)] = S(X) + S(M) - I(X;M).
$$
Taking the derivative across turns,
$$
\frac{\text{d}S}{\text{d}t} = \frac{\text{d}S(X)}{\text{d}t} + \frac{\text{d}S(M)}{\text{d}t} - \frac{\text{d}I(X;M)}{\text{d}t}.
$$
}

\slides{
* Joint entropy decomposition: $S[p(z,t)] = S(X) + S(M) - I(X;M)$
* Turns derivative: $\frac{\text{d}S}{\text{d}t} = \frac{\text{d}S(X)}{\text{d}t} + \frac{\text{d}S(M)}{\text{d}t} - \frac{\text{d}I(X;M)}{\text{d}t}$
* Spontaneous organization when: $\frac{\text{d}I(X;M)}{\text{d}t} > 0$
}

\notes{
We know $\frac{\text{d}S}{\text{d}t} > 0$ (entropy is being maximized), and because $M$ are at saddle points we know that $\frac{\text{d}S(M)}{\text{d}t} \approx 0$. Therefore we can rearrange to find,
$$
\frac{\text{d}I(X;M)}{\text{d}t} \approx \frac{\text{d}S(X)}{\text{d}t}  - \frac{\text{d}S}{\text{d}t}.
$$
Spontaneous organization emerges when $\frac{\text{d}I(X;M)}{\text{d}t} > 0$, which occurs when
$$
\frac{\text{d}S(X)}{\text{d}t} > \frac{\text{d}S}{\text{d}t}.
$$
}

\subsection{Fisher Information and Multiple Timescales in Spontaneous Organization}

\notes{
We introduce the Fisher information and the effect of multiple timescales to analyze when the gradient condition $\frac{\text{d}S(X)}{\text{d}t} > \frac{\text{d}S}{\text{d}t}$ holds.}

\notes{The Fisher information matrix $G(\boldsymbol{\theta})$ provides a natural metric on the statistical manifold of probability distributions. For our joint distribution $p(z|\boldsymbol{\theta})$, the Fisher information is defined as
$$
G_{ij}(\boldsymbol{\theta}) = \mathbb{E}\left[\frac{\partial \log p(z|\boldsymbol{\theta})}{\partial \theta_i}\frac{\partial \log p(z|\boldsymbol{\theta})}{\partial \theta_j}\right].
$$}

\notes{ When we partition our variables into fast variables $X$ and slow variables $M$ (representing the information reservoir), we are suggesting a a timescale separation in the natural parameter dynamics,
$$
\frac{\text{d}\boldsymbol{\theta}_X}{\text{d}t} = \eta_X \nabla_{\boldsymbol{\theta}_X}S[p(z,t)],
$$
$$
\frac{\text{d}\boldsymbol{\theta}_M}{\text{d}t} =  \eta_M \nabla_{\boldsymbol{\theta}_M}S[p(z,t)],
$$
where $\left|\nabla_{\boldsymbol{\theta}_X}S[p(z,t)]\right| \gg \left|\nabla_{\boldsymbol{\theta}_M}S[p(z,t)]\right|$ indicates that $X$ evolves much faster than $M$.
}

\newslide{Multiple Timescales and Mutual Information Growth}

\notes{
This timescale separation reflects an asymmetry that would drive spontaneous organization. The entropy dynamics can be expressed in terms of the Fisher information matrix and the natural parameter velocities,
$$
\frac{\text{d}S}{\text{d}t} = \nabla_{\boldsymbol{\theta}}S \cdot \frac{\text{d}\boldsymbol{\theta}}{\text{d}t} = \nabla_{\boldsymbol{\theta}_X}S \cdot \frac{\text{d}\boldsymbol{\theta}_X}{\text{d}t} + \nabla_{\boldsymbol{\theta}_M}S \cdot \frac{\text{d}\boldsymbol{\theta}_M}{\text{d}t}.
$$

Substituting our gradient ascent dynamics with different learning rates:
$$
\frac{\text{d}S}{\text{d}t} = \nabla_{\boldsymbol{\theta}_X}S \cdot (\eta_X \nabla_{\boldsymbol{\theta}_X}S) + \nabla_{\boldsymbol{\theta}_M}S \cdot (\eta_M \nabla_{\boldsymbol{\theta}_M}S) = \eta_X \|\nabla_{\boldsymbol{\theta}_X}S\|^2 + \eta_M \|\nabla_{\boldsymbol{\theta}_M}S\|^2.
$$

Similarly, the marginal entropy of $X$ evolves according to,
$$
\frac{\text{d}S(X)}{\text{d}t} = \nabla_{\boldsymbol{\theta}_X}S(X) \cdot \frac{\text{d}\boldsymbol{\theta}_X}{\text{d}t} = \nabla_{\boldsymbol{\theta}_X}S(X) \cdot (\eta_X \nabla_{\boldsymbol{\theta}_X}S) = \eta_X \nabla_{\boldsymbol{\theta}_X}S(X) \cdot \nabla_{\boldsymbol{\theta}_X}S.
$$

Note that this is not generally equal to $\eta_X \|\nabla_{\boldsymbol{\theta}_X}S(X)\|^2$ unless $\nabla_{\boldsymbol{\theta}_X}S = \nabla_{\boldsymbol{\theta}_X}S(X)$, which is not typically the case when variables are correlated.

The gradient condition for spontaneous organization, $\frac{\text{d}I(X;M)}{\text{d}t} > 0$, can be rewritten using our earlier relation 
$$
\frac{\text{d}I(X;M)}{\text{d}t} \approx \frac{\text{d}S(X)}{\text{d}t} - \frac{\text{d}S}{\text{d}t},
$$ 
giving
$$
\eta_X \nabla_{\boldsymbol{\theta}_X}S(X) \cdot \nabla_{\boldsymbol{\theta}_X}S > \eta_X \|\nabla_{\boldsymbol{\theta}_X}S\|^2 + \eta_M \|\nabla_{\boldsymbol{\theta}_M}S\|^2.
$$

Since $\eta_M \|\nabla_{\boldsymbol{\theta}_M}S\|^2 > 0$ (except exactly at saddle points), this inequality requires:
$$
\nabla_{\boldsymbol{\theta}_X}S(X) \cdot \nabla_{\boldsymbol{\theta}_X}S > \|\nabla_{\boldsymbol{\theta}_X}S\|^2.
$$

This is a stronger condition than simply requiring the gradients to be aligned. By the Cauchy-Schwarz inequality, we know that $\nabla_{\boldsymbol{\theta}_X}S(X) \cdot \nabla_{\boldsymbol{\theta}_X}S \leq \|\nabla_{\boldsymbol{\theta}_X}S(X)\| \cdot \|\nabla_{\boldsymbol{\theta}_X}S\|$. Therefore, the condition can only be satisfied when $\|\nabla_{\boldsymbol{\theta}_X}S(X)\| > \|\nabla_{\boldsymbol{\theta}_X}S\|$ and the gradients are sufficiently aligned.
}

\slides{
* Fisher information: $G_{ij}(\boldsymbol{\theta}) = \mathbb{E}\left[\frac{\partial \log p(z|\boldsymbol{\theta})}{\partial \theta_i}\frac{\partial \log p(z|\boldsymbol{\theta})}{\partial \theta_j}\right]$
* Multiple timescales: $\eta_X \gg \eta_M$
* Spontaneous organization requires: $\|\nabla_{\boldsymbol{\theta}_X}S(X)\|^2 > \|\nabla_{\boldsymbol{\theta}_X}S\|^2$
}

\newslide{Condition for Information Structure Emergence}

\notes{This inequality suggests that spontaneous organization occurs when the gradient of marginal entropy $S(X)$ with respect to $\boldsymbol{\theta}_X$ has a larger magnitude than the gradient of joint entropy $S$ with respect to the same parameters.}

\notes{This condition can be satisfied when $X$ variables are strongly coupled to $M$ variables in a specific way. We express the mutual information gradient
$$
\nabla_{\boldsymbol{\theta}_X}I(X;M) = \nabla_{\boldsymbol{\theta}_X}S(X) + \nabla_{\boldsymbol{\theta}_X}S(M) - \nabla_{\boldsymbol{\theta}_X}S.
$$}

\notes{Since $M$ evolves slowly, we can approximate $\nabla_{\boldsymbol{\theta}_X}S(M) \approx 0$, yielding
$$
\nabla_{\boldsymbol{\theta}_X}I(X;M) \approx \nabla_{\boldsymbol{\theta}_X}S(X) - \nabla_{\boldsymbol{\theta}_X}S.
$$}

\notes{Our condition for spontaneous organization can be rewritten as
$$
\|\nabla_{\boldsymbol{\theta}_X}S(X)\|^2 > \|\nabla_{\boldsymbol{\theta}_X}S\|^2.
$$}

\notes{We can expand this condition using the relationship between these gradients. Since $\nabla_{\boldsymbol{\theta}_X}I(X;M) \approx \nabla_{\boldsymbol{\theta}_X}S(X) - \nabla_{\boldsymbol{\theta}_X}S$, we can write
$$
\|\nabla_{\boldsymbol{\theta}_X}S(X)\|^2 = \|\nabla_{\boldsymbol{\theta}_X}S + \nabla_{\boldsymbol{\theta}_X}I(X;M)\|^2.
$$

Expanding this squared norm we have
$$
\|\nabla_{\boldsymbol{\theta}_X}S(X)\|^2 = \|\nabla_{\boldsymbol{\theta}_X}S\|^2 + \|\nabla_{\boldsymbol{\theta}_X}I(X;M)\|^2 + 2\nabla_{\boldsymbol{\theta}_X}S \cdot \nabla_{\boldsymbol{\theta}_X}I(X;M).
$$

For our condition $\|\nabla_{\boldsymbol{\theta}_X}S(X)\|^2 > \|\nabla_{\boldsymbol{\theta}_X}S\|^2$ to be satisfied, we need
$$
\|\nabla_{\boldsymbol{\theta}_X}I(X;M)\|^2 + 2\nabla_{\boldsymbol{\theta}_X}S \cdot \nabla_{\boldsymbol{\theta}_X}I(X;M) > 0
$$

To analyze when this condition holds, we must examine the Fisher information geometry near saddle points. At a saddle point of the entropy landscape, the Hessian matrix of the entropy has both positive and negative eigenvalues. The Fisher information matrix $G(\boldsymbol{\theta})$ provides the natural metric on this statistical manifold.

Near a saddle point, the Fisher information matrix exhibits a characteristic eigenvalue spectrum with a separation between large and small eigenvalues. The eigenvectors corresponding to small eigenvalues define the slow manifold (associated with memory variables $M$), while those with large eigenvalues correspond to fast-evolving directions (associated with observable variables $X$).

The gradient of joint entropy can be decomposed into components along these eigendirections. Due to the timescale separation, the gradient components along fast directions quickly equilibrate, while components along slow directions persist. This creates a scenario where:

1. The gradient flow predominantly occurs along fast directions, with slow directions acting as constraints
2. The system explores configurations that maximize entropy subject to these constraints

Under these conditions, the dot product $\nabla_{\boldsymbol{\theta}_X}S \cdot \nabla_{\boldsymbol{\theta}_X}I(X;M)$ can become positive when the entropy gradient aligns with directions that increase mutual information. This alignment is not guaranteed but becomes increasingly probable as the system explores the entropy landscape near saddle points.

This  analysis  identifies the conditions under which spontaneous organisation becomes possible within the framework of entropy maximization in natural parameter space. The key insight is that the geometry of the Fisher information near saddle points creates regions where entropy maximization and mutual information may occur simultaneously.
}

\slides{
* Mutual information gradient: $\nabla_{\boldsymbol{\theta}_X}I(X;M) \approx \nabla_{\boldsymbol{\theta}_X}S(X) - \nabla_{\boldsymbol{\theta}_X}S$
* Organization emerges when entropy gradients diverge in direction
* Fast variables $X$ explore state space while slow variables $M$ capture persistent patterns
}

\newslide{Adiabatic Elimination and Effective Dynamics}

\notes{
This timescale separation enables an adiabatic elimination process where fast variables $X$ reach a quasi-equilibrium for each slow configuration of $M$. This creates effective dynamics where $M$ adapts to encode statistical regularities in the behavior of $X$.

Mathematically, we can express this using the Hessian matrices,
$$
\mathbf{H}_X = \frac{\partial^2 S}{\partial \boldsymbol{\theta}_X \partial \boldsymbol{\theta}_X},
$$
$$
\mathbf{H}_{XM} = \frac{\partial^2 S}{\partial \boldsymbol{\theta}_X \partial \boldsymbol{\theta}_M}.
$$

The condition for spontaneous organization becomes
$$
\frac{\text{d}I(X;M)}{\text{d}t} \approx \eta_X \text{tr}(\mathbf{H}_{S(X)}) - \eta_X \text{tr}(\mathbf{H}_S) - \eta_M \text{tr}(\mathbf{H}_{XM}) = -\eta_M \text{tr}(\mathbf{H}_{XM}).
$$

This approximation is valid when the system has reached a quasi-equilibrium state for the fast variables $X$, where $\nabla_{\boldsymbol{\theta}_X}S \approx \nabla_{\boldsymbol{\theta}_X}S(X)$. In this regime, the first two terms approximately cancel out, leaving the cross-correlation term dominant. Here, $\mathbf{H}_{S(X)}$ is the Hessian of the marginal entropy $S(X)$ with respect to $\boldsymbol{\theta}_X$, $\mathbf{H}_S$ is the Hessian of the joint entropy, and $\mathbf{H}_{XM}$ is the cross-correlation Hessian measuring how changes in $\boldsymbol{\theta}_X$ affect gradients with respect to $\boldsymbol{\theta}_M$.

Thus, mutual information increases when $\text{tr}(\mathbf{H}_{XM}) < 0$, which occurs when the cross-correlation Hessian between $X$ and $M$ has predominantly negative eigenvalues. This represents configurations where joint entropy increases more efficiently by strengthening correlations rather than breaking them.

This provides a precise mathematical characterization of when spontaneous organization emerges from entropy maximization in natural parameter space under multiple timescales.
}

\slides{
* Adiabatic elimination: fast variables reach quasi-equilibrium for each slow configuration
* Condition: $\frac{\text{d}I(X;M)}{\text{d}t} \approx -\eta_M \text{tr}(\mathbf{H}_{XM})$
* Organization occurs when $\text{tr}(\mathbf{H}_{XM}) < 0$
* System develops correlations that maximize entropy efficiently
}


\setupcode{import numpy as np
from scipy.stats import multivariate_normal
import matplotlib.pyplot as plt
import mlai.plot as plot
import matplotlib.gridspec as gridspec}

\helpercode{class SpontaneousOrganizationDemo:
    def __init__(self, learning_rate=0.1):
        """
        Initialize a system with fast (X) and slow (M) variables to demonstrate
        spontaneous organization through entropy maximization.
        
        Parameters:
        -----------
        learning_rate: float
            Base learning rate for gradient ascent
        """
        # Define timescale separation (η_X >> η_M)
        self.eta_X = learning_rate
        self.eta_M = learning_rate * 0.01  # M evolves 100x slower than X
        
        # Initialize natural parameters for joint distribution
        # θ_X controls X variables, θ_M controls M variables
        self.theta_X = np.array([-2.0, 0.5])  # Initial parameters for X
        self.theta_M = np.array([1.0, -1.0])  # Initial parameters for M
        
        # Coupling parameter between X and M
        self.theta_XM = np.array([0.3, 0.3])  # Initial coupling
        
        # Grid for visualization
        self.x_grid = np.linspace(-3, 3, 50)
        self.m_grid = np.linspace(-3, 3, 50)
        self.X, self.M = np.meshgrid(self.x_grid, self.m_grid)
        
        # History tracking
        self.history = {
            'joint_entropy': [],
            'marginal_entropy_X': [],
            'marginal_entropy_M': [],
            'mutual_information': [],
            'theta_X': [],
            'theta_M': [],
            'theta_XM': []
        }
        
        # Store initial state
        self._update_history()
    
    def joint_distribution(self):
        """Compute the joint distribution p(X,M)"""
        # Create a grid of points
        pos = np.dstack((self.X, self.M))
        
        # Construct precision matrix from natural parameters
        precision = np.array([
            [self.theta_X[1], self.theta_XM[0]],
            [self.theta_XM[1], self.theta_M[1]]
        ])
        
        # Ensure precision matrix is positive definite
        min_eig = np.min(np.linalg.eigvals(precision))
        if min_eig <= 0:
            # Add small positive value to diagonal if not positive definite
            precision += np.eye(2) * (abs(min_eig) + 0.01)
        
        # Mean vector
        mean = np.linalg.solve(precision, np.array([self.theta_X[0], self.theta_M[0]]))
        
        # Compute covariance matrix
        cov = np.linalg.inv(precision)
        
        # Compute joint distribution
        p_joint = multivariate_normal.pdf(pos, mean=mean, cov=cov)
        
        # Normalize (for numerical stability)
        p_joint /= np.sum(p_joint)
        
        return p_joint, mean, cov
    
    def marginal_distributions(self, p_joint):
        """Compute marginal distributions p(X) and p(M)"""
        p_X = np.sum(p_joint, axis=0)
        p_X /= np.sum(p_X)
        
        p_M = np.sum(p_joint, axis=1)
        p_M /= np.sum(p_M)
        
        return p_X, p_M
    
    def compute_entropies(self, p_joint):
        """Compute joint entropy, marginal entropies, and mutual information"""
        # Get marginals
        p_X, p_M = self.marginal_distributions(p_joint)
        
        # Compute entropies (avoiding log(0))
        eps = 1e-10
        S_joint = -np.sum(p_joint * np.log(p_joint + eps))
        S_X = -np.sum(p_X * np.log(p_X + eps))
        S_M = -np.sum(p_M * np.log(p_M + eps))
        
        # Mutual information
        I_XM = S_X + S_M - S_joint
        
        return S_joint, S_X, S_M, I_XM
    
    def entropy_gradients(self):
        """Compute gradients of entropy with respect to natural parameters"""
        # Get current joint distribution
        p_joint, mean, cov = self.joint_distribution()
        
        # Small perturbation for numerical gradient
        epsilon = 1e-5
        
        # Compute base entropy
        S_joint, S_X, S_M, I_XM = self.compute_entropies(p_joint)
        
        # Gradient for theta_X
        grad_theta_X = np.zeros_like(self.theta_X)
        for i in range(len(self.theta_X)):
            # Perturb parameter
            self.theta_X[i] += epsilon
            p_perturbed, _, _ = self.joint_distribution()
            S_perturbed, _, _, _ = self.compute_entropies(p_perturbed)
            self.theta_X[i] -= epsilon  # Restore
            
            # Compute gradient
            grad_theta_X[i] = (S_perturbed - S_joint) / epsilon
        
        # Gradient for theta_M
        grad_theta_M = np.zeros_like(self.theta_M)
        for i in range(len(self.theta_M)):
            # Perturb parameter
            self.theta_M[i] += epsilon
            p_perturbed, _, _ = self.joint_distribution()
            S_perturbed, _, _, _ = self.compute_entropies(p_perturbed)
            self.theta_M[i] -= epsilon  # Restore
            
            # Compute gradient
            grad_theta_M[i] = (S_perturbed - S_joint) / epsilon
        
        # Gradient for theta_XM
        grad_theta_XM = np.zeros_like(self.theta_XM)
        for i in range(len(self.theta_XM)):
            # Perturb parameter
            self.theta_XM[i] += epsilon
            p_perturbed, _, _ = self.joint_distribution()
            S_perturbed, _, _, _ = self.compute_entropies(p_perturbed)
            self.theta_XM[i] -= epsilon  # Restore
            
            # Compute gradient
            grad_theta_XM[i] = (S_perturbed - S_joint) / epsilon
        
        return grad_theta_X, grad_theta_M, grad_theta_XM
    
    def gradient_ascent_step(self):
        """Perform one step of gradient ascent with different timescales"""
        # Compute gradients
        grad_theta_X, grad_theta_M, grad_theta_XM = self.entropy_gradients()
        
        # Update parameters with different learning rates
        self.theta_X += self.eta_X * grad_theta_X
        self.theta_M += self.eta_M * grad_theta_M  # Slow variables
        
        # Coupling parameters evolve at an intermediate rate
        eta_XM = np.sqrt(self.eta_X * self.eta_M)
        self.theta_XM += eta_XM * grad_theta_XM
        
        # Update history
        self._update_history()
        
        # Return current entropies and mutual information
        p_joint, _, _ = self.joint_distribution()
        return self.compute_entropies(p_joint)
    
    def _update_history(self):
        """Update history of parameters and information measures"""
        p_joint, _, _ = self.joint_distribution()
        S_joint, S_X, S_M, I_XM = self.compute_entropies(p_joint)
        
        self.history['joint_entropy'].append(S_joint)
        self.history['marginal_entropy_X'].append(S_X)
        self.history['marginal_entropy_M'].append(S_M)
        self.history['mutual_information'].append(I_XM)
        self.history['theta_X'].append(self.theta_X.copy())
        self.history['theta_M'].append(self.theta_M.copy())
        self.history['theta_XM'].append(self.theta_XM.copy())
    
    def run_simulation(self, steps=100):
        """Run gradient ascent for specified number of steps"""
        results = []
        for i in range(steps):
            S_joint, S_X, S_M, I_XM = self.gradient_ascent_step()
            results.append((S_joint, S_X, S_M, I_XM))
            
            if i % 10 == 0:
                print(f"Step {i}: Joint Entropy = {S_joint:.4f}, MI = {I_XM:.4f}")
        
        return results
    
    def visualize_results(self):
        """Visualize the evolution of entropy and mutual information"""
        steps = range(len(self.history['joint_entropy']))
        
        # Create figure with subplots
        fig = plt.figure(figsize=plot.big_wide_figsize)
        gs = gridspec.GridSpec(2, 2, height_ratios=[1, 1])
        
        # Plot entropies
        ax1 = plt.subplot(gs[0, 0])
        ax1.plot(steps, self.history['joint_entropy'], 'b-', label='Joint Entropy S(X,M)')
        ax1.plot(steps, self.history['marginal_entropy_X'], 'g--', label='Marginal Entropy S(X)')
        ax1.plot(steps, self.history['marginal_entropy_M'], 'r--', label='Marginal Entropy S(M)')
        ax1.set_xlabel('Gradient Ascent Step')
        ax1.set_ylabel('Entropy')
        ax1.set_title('Evolution of Entropy')
        ax1.legend()
        ax1.grid(True)
        
        # Plot mutual information
        ax2 = plt.subplot(gs[0, 1])
        ax2.plot(steps, self.history['mutual_information'], 'k-', linewidth=2)
        ax2.set_xlabel('Gradient Ascent Step')
        ax2.set_ylabel('Mutual Information I(X;M)')
        ax2.set_title('Evolution of Mutual Information')
        ax2.grid(True)
        
        # Plot joint distribution at the beginning and end
        p_initial, mean_initial, cov_initial = self.joint_distribution()
        
        # Restore parameters to initial state for visualization
        self.theta_X = self.history['theta_X'][0].copy()
        self.theta_M = self.history['theta_M'][0].copy()
        self.theta_XM = self.history['theta_XM'][0].copy()
        p_initial, mean_initial, cov_initial = self.joint_distribution()
        
        # Restore parameters to final state
        self.theta_X = self.history['theta_X'][-1].copy()
        self.theta_M = self.history['theta_M'][-1].copy()
        self.theta_XM = self.history['theta_XM'][-1].copy()
        p_final, mean_final, cov_final = self.joint_distribution()
        
        # Plot initial distribution
        ax3 = plt.subplot(gs[1, 0])
        c3 = ax3.contourf(self.X, self.M, p_initial, cmap='viridis')
        ax3.set_xlabel('X (Fast Variable)')
        ax3.set_ylabel('M (Slow Variable)')
        ax3.set_title('Initial Joint Distribution p(X,M)')
        plt.colorbar(c3, ax=ax3)
        
        # Plot final distribution
        ax4 = plt.subplot(gs[1, 1])
        c4 = ax4.contourf(self.X, self.M, p_final, cmap='viridis')
        ax4.set_xlabel('X (Fast Variable)')
        ax4.set_ylabel('M (Slow Variable)')
        ax4.set_title('Final Joint Distribution p(X,M)')
        plt.colorbar(c4, ax=ax4)
        
        plt.tight_layout()
        return fig
}

\code{
# Run the demonstration
np.random.seed(42)  # For reproducibility
demo = SpontaneousOrganizationDemo(learning_rate=0.05)
results = demo.run_simulation(steps=150)
}

\setupplotcode{import matplotlib.pyplot as plt
import mlai.plot as plot
import mlai
import matplotlib.gridspec as gridspec
}
\plotcode{fig = demo.visualize_results()

# Add a text box explaining the key findings
plt.figtext(0.5, 0.01, 
            "Spontaneous Organisation: Despite maximizing joint entropy, mutual information I(X;M) increases.\n"
            "This occurs because the fast variables X evolve quickly while slow variables M act as an information reservoir.\n"
            "The timescale separation (η_X >> η_M) creates conditions where correlations strengthen during entropy maximization.",
            ha="center", fontsize=12, bbox={"facecolor":"lightgray", "alpha":0.5, "pad":5})


mlai.write_figure(filename='spontaneous-organisation.svg', 
                  directory='\writeDiagramsDir/information-game')}

\newslide{Spontaneous Organisation}

\figure{\includediagram{\diagramsDir/information-game/spontaneous-organisation}{70%}}{Spontaneous organisation.}{spontaneous-organisation}

\endif

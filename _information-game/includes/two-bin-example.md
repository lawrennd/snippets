\ifndef{twoBinExample}
\define{twoBinExample}

\editme

\include{_information-game/includes/jaynes-world-histogram.md}

\subsection{Two-Bin Histogram Example}

\notes{The simplest possible example of Jaynes' World is a two-bin histogram with probabilities $p$ and $1-p$. This minimal system allows us to visualize the entire entropy landscape.}

\slides{
* Simplest example: Two-bin system
* States represented by probability $p$ (with $1-p$ in second bin)
}
\newslide{Entropy}
\slides{
* Entropy
  $$
  S(p) = -p\log p - (1-p)\log(1-p)
  $$
* Maximum entropy at $p = 0.5$
* Minimal entropy at $p = 0$ or $p = 1$
}

\notes{
The natural parameter is the log odds, $\theta = \log\frac{p}{1-p}$, and the update given by the entropy gradient is
$$
\Delta \theta_{\text{steepest}} = \eta \frac{\text{d}S}{\text{d}\theta} = \eta p(1-p)(\log(1-p) - \log p).
$$
The Fisher information is
$$
G(\theta) = p(1-p)
$$
This creates a dynamic where as $p$ approaches either 0 or 1 (minimal entropy states), the Fisher information approaches zero, creating a critical slowing" effect. This critical slowing is what leads to the formation of *information resevoirs*. Note also that in the *natural gradient* the updated is given by multiplying the gradient by the inverse Fisher information, which would lead to a more efficient update of the form, 
$$
\Delta \theta_{\text{natural}} =  \eta(\log(1-p) - \log p),
$$
however, it is this efficiency that we want our game to avoid, because it is the inefficient behaviour in the reagion of saddle points that leads to critical slowing and the emergence of information resevoirs.
}

\setupcode{import numpy as np}

\code{# Python code for gradients
p_values = np.linspace(0.000001, 0.999999, 10000)
theta_values = np.log(p_values/(1-p_values))
entropy = -p_values * np.log(p_values) - (1-p_values) * np.log(1-p_values)
fisher_info = p_values * (1-p_values)
gradient = fisher_info * (np.log(1-p_values) - np.log(p_values))
}

\newslide{Natural Gradients vs Steepest Ascent}
\slides{$$
\Delta \theta_{\text{steepest}} = \eta \frac{\text{d}S}{\text{d}\theta} = \eta p(1-p)(\log(1-p) - \log p).
$$
$$
G(\theta) = p(1-p)
$$
$$
\Delta \theta_{\text{natural}} =  \eta(\log(1-p) - \log p)
$$
}
\setupplotcode{import matplotlib.pyplot as plt
import mlai.plot as plot
import mlai}

\plotcode{fig, (ax1, ax2) = plt.subplots(1, 2, figsize=plot.big_wide_figsize)

ax1.plot(theta_values, entropy)
ax1.set_xlabel('$\\theta$')
ax1.set_ylabel('Entropy $S(p)$')
ax1.set_title('Entropy Landscape')

ax2.plot(theta_values, gradient)
ax2.set_xlabel('$\\theta$')
ax2.set_ylabel('$\\nabla_\\theta S(p)$')
ax2.set_title('Entropy Gradient vs. Position')

mlai.write_figure(filename='two-bin-histogram-entropy-gradients.svg', 
				  directory = '\writeDiagramsDir/information-game')}

\newslide{}

\figure{\includediagram{\diagramsDir/information-game/two-bin-histogram-entropy-gradients}{95%}}{Entropy gradients of the two bin histogram agains position.}{two-bin-histogram-entropy-gradients}

\notes{This example reveals the entropy extrema at $p = 0$, $p = 0.5$, and $p = 1$. At minimal entropy ($p \approx 0$ or $p \approx 1$), the gradient approaches zero, creating natural information reservoirs. The dynamics slow dramatically near these points - these are the areas of critical slowing that create information reservoirs.
} 

\subsection{Gradient Ascent in Natural Parameter Space}

\notes{We can visualize the entropy maximization process by performing gradient ascent in the natural parameter space $\theta$. Starting from a low-entropy state, we follow the gradient of entropy with respect to $\theta$ to reach the maximum entropy state.}

\setupcode{import numpy as np}

\helpercode{# Helper functions for two-bin histogram
def theta_to_p(theta):
    """Convert natural parameter theta to probability p"""
    return 1.0 / (1.0 + np.exp(-theta))

def p_to_theta(p):
    """Convert probability p to natural parameter theta"""
    # Add small epsilon to avoid numerical issues
    p = np.clip(p, 1e-10, 1-1e-10)
    return np.log(p/(1-p))

def entropy(theta):
    """Compute entropy for given theta"""
    p = theta_to_p(theta)
    # Safe entropy calculation
    return -p * np.log2(p) - (1-p) * np.log2(1-p)

def entropy_gradient(theta):
    """Compute gradient of entropy with respect to theta"""
    p = theta_to_p(theta)
    return p * (1-p) * (np.log2(1-p) - np.log2(p))

def plot_histogram(ax, theta, max_height=None):
    """Plot two-bin histogram for given theta"""
    p = theta_to_p(theta)
    heights = np.array([p, 1-p])
    
    if max_height is None:
        max_height = 1.25
    
    # Compute entropy
    S = entropy(theta)
    
    # Create the histogram
    bins = [1, 2, 3]  # Bin edges
    if ax is None:
        fig, ax = plt.subplots(figsize=(6, 4))
    ax.hist(bins[:-1], bins=bins, weights=heights, align='left', rwidth=0.8, edgecolor='black')
    
    # Customize the plot
    ax.set_xlabel("Bin")
    ax.set_ylabel("Probability")
    ax.set_title(f"Two-Bin Histogram (Entropy {S:.3f})")
    ax.set_xticks(bins[:-1])
    ax.set_ylim(0, max_height)
}

\code{# Parameters for gradient ascent
theta_initial = -9.0  # Start with low entropy 
learning_rate = 1
num_steps = 1500

# Initialize
theta_current = theta_initial
theta_history = [theta_current]
p_history = [theta_to_p(theta_current)]
entropy_history = [entropy(theta_current)]

# Perform gradient ascent in theta space
for step in range(num_steps):
    # Compute gradient
    grad = entropy_gradient(theta_current)
    
    # Update theta
    theta_current = theta_current + learning_rate * grad
    
    # Store history
    theta_history.append(theta_current)
    p_history.append(theta_to_p(theta_current))
    entropy_history.append(entropy(theta_current))
    if step % 100 == 0:
    print(f"Step {step+1}: θ = {theta_current:.4f}, p = {p_history[-1]:.4f}, Entropy = {entropy_history[-1]:.4f}")
}

\setupplotcode{import matplotlib.pyplot as plt
import mlai.plot as plot
import mlai}

\plotcode{# Create a figure showing the evolution
fig, axes = plt.subplots(2, 3, figsize=(15, 8))
fig.tight_layout(pad=3.0)

# Select steps to display
steps_to_show = [0, 300, 600, 900, 1200, 1500]

# Plot histograms for selected steps
for i, step in enumerate(steps_to_show):
    row, col = i // 3, i % 3
    plot_histogram(axes[row, col], theta_history[step])
    axes[row, col].set_title(f"Step {step}: θ = {theta_history[step]:.2f}, p = {p_history[step]:.3f}")

mlai.write_figure(filename='two-bin-histogram-evolution.svg', 
                  directory = '\writeDiagramsDir/information-game')

# Plot entropy evolution
plt.figure(figsize=(10, 6))
plt.plot(range(num_steps+1), entropy_history, 'o-')
plt.xlabel('Gradient Ascent Step')
plt.ylabel('Entropy')
plt.title('Entropy Evolution During Gradient Ascent')
plt.grid(True)
mlai.write_figure(filename='two-bin-entropy-evolution.svg', 
                  directory = '\writeDiagramsDir/information-game')

# Plot trajectory in theta space
plt.figure(figsize=(10, 6))
theta_range = np.linspace(-5, 5, 1000)
entropy_curve = [entropy(t) for t in theta_range]
plt.plot(theta_range, entropy_curve, 'b-', label='Entropy Landscape')
plt.plot(theta_history, entropy_history, 'ro-', label='Gradient Ascent Path')
plt.xlabel('Natural Parameter θ')
plt.ylabel('Entropy')
plt.title('Gradient Ascent Trajectory in Natural Parameter Space')
plt.axvline(x=0, color='k', linestyle='--', alpha=0.3)
plt.legend()
plt.grid(True)
mlai.write_figure(filename='two-bin-trajectory.svg', 
                  directory = '\writeDiagramsDir/information-game')}

\newslide{Gradient Ascent Evolution}

\figure{\includediagram{\diagramsDir/information-game/two-bin-histogram-evolution}{95%}}{Evolution of the two-bin histogram during gradient ascent in natural parameter space.}{two-bin-histogram-evolution}

\newslide{Entropy Evolution}

\figure{\includediagram{\diagramsDir/information-game/two-bin-entropy-evolution}{80%}}{Entropy evolution during gradient ascent for the two-bin histogram.}{two-bin-entropy-evolution}

\newslide{Trajectory in Natural Parameter Space}

\figure{\includediagram{\diagramsDir/information-game/two-bin-trajectory}{80%}}{Gradient ascent trajectory in the natural parameter space for the two-bin histogram.}{two-bin-trajectory}

\notes{The gradient ascent visualization shows how the system evolves in the natural parameter space $\theta$. Starting from a negative $\theta$ (corresponding to a low-entropy state with $p << 0.5$), the system follows the gradient of entropy with respect to $\theta$ until it reaches $\theta = 0$ (corresponding to $p = 0.5$), which is the maximum entropy state.

Note that the maximum entropy occurs at $\theta = 0$, which corresponds to $p = 0.5$. The gradient of entropy with respect to $\theta$ is zero at this point, making it a stable equilibrium for the gradient ascent process.}

\endif

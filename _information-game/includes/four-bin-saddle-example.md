\ifndef{fourBinSaddleExample}
\define{fourBinSaddleExample}

\editme

\subsection{Four-Bin Saddle Point Example}

\notes{To illustrate saddle points and information reservoirs, we need at least a 4-bin system. This creates a 3-dimensional parameter space where we can observe genuine saddle points.}

\slides{* Four-bin system creates 3D parameter space
* Saddle points appear where:
  * Gradient is zero
  * Some directions increase entropy
  * Other directions decrease entropy
* Information reservoirs form in critically slowed directions
}

\notes{Consider a 4-bin system parameterized by natural parameters $\theta_1$, $\theta_2$, and $\theta_3$ (with one constraint). A saddle point occurs where the gradient $\nabla_\theta S = 0$, but the Hessian has mixed eigenvalues - some positive, some negative.}

\notes{At these points, the Fisher information matrix $G(\theta)$ eigendecomposition reveals.

* Fast modes: large positive eigenvalues → rapid evolution
* Slow modes: small positive eigenvalues → gradual evolution 
* Critical modes: near-zero eigenvalues → information reservoirs

The eigenvectors of $G(\theta)$ at the saddle point determine which parameter combinations form information reservoirs.
}

\setupcode{import numpy as np}

\helpercode{# Exponential family entropy functions for 4-bin system
def exponential_family_entropy(theta):
    """
    Compute entropy of a 4-bin exponential family distribution
    parameterized by natural parameters theta
    """
    # Compute the log-partition function (normalization constant)
    log_Z = np.log(np.sum(np.exp(theta)))
    
    # Compute probabilities
    p = np.exp(theta - log_Z)
    
    # Compute entropy: -sum(p_i * log(p_i))
    entropy = -np.sum(p * np.log(p), where=p>0)
    
    return entropy

def entropy_gradient(theta):
    """
    Compute the gradient of the entropy with respect to theta
    """
    # Compute the log-partition function (normalization constant)
    log_Z = np.log(np.sum(np.exp(theta)))
    
    # Compute probabilities
    p = np.exp(theta - log_Z)
    
    # Gradient is theta times the second derivative of log partition function
    return -p*theta + p*(np.dot(p, theta))

# Add a gradient check function
def check_gradient(theta, epsilon=1e-6):
    """
    Check the analytical gradient against numerical gradient
    """
    # Compute analytical gradient
    analytical_grad = entropy_gradient(theta)
    
    # Compute numerical gradient
    numerical_grad = np.zeros_like(theta)
    for i in range(len(theta)):
        theta_plus = theta.copy()
        theta_plus[i] += epsilon
        entropy_plus = exponential_family_entropy(theta_plus)
        
        theta_minus = theta.copy()
        theta_minus[i] -= epsilon
        entropy_minus = exponential_family_entropy(theta_minus)
        
        numerical_grad[i] = (entropy_plus - entropy_minus) / (2 * epsilon)
    
    # Compare
    print("Analytical gradient:", analytical_grad)
    print("Numerical gradient:", numerical_grad)
    print("Difference:", np.abs(analytical_grad - numerical_grad))
    
    return analytical_grad, numerical_grad

# Project gradient to respect constraints (sum of theta is constant)
def project_gradient(theta, grad):
    """
    Project gradient to ensure sum constraint is respected
    """
    # Project to space where sum of components is zero
    return grad - np.mean(grad)

# Perform gradient ascent on entropy
def gradient_ascent_four_bin(theta_init, steps=100, learning_rate=1):
    """
    Perform gradient ascent on entropy for 4-bin system
    """
    theta = theta_init.copy()
    theta_history = [theta.copy()]
    entropy_history = [exponential_family_entropy(theta)]
    
    for _ in range(steps):
        # Compute gradient
        grad = entropy_gradient(theta)
        proj_grad = project_gradient(theta, grad)
        
        # Update parameters
        theta += learning_rate * proj_grad
        
        # Store history
        theta_history.append(theta.copy())
        entropy_history.append(exponential_family_entropy(theta))
    
    return np.array(theta_history), np.array(entropy_history)
}

\code{# Test the gradient calculation
test_theta = np.array([0.5, -0.3, 0.1, -0.3])
test_theta = test_theta - np.mean(test_theta)  # Ensure constraint is satisfied
print("Testing gradient calculation:")
analytical_grad, numerical_grad = check_gradient(test_theta)

# Verify if we're ascending or descending
entropy_before = exponential_family_entropy(test_theta)
step_size = 0.01
test_theta_after = test_theta + step_size * analytical_grad
entropy_after = exponential_family_entropy(test_theta_after)
print(f"Entropy before step: {entropy_before}")
print(f"Entropy after step: {entropy_after}")
print(f"Change in entropy: {entropy_after - entropy_before}")
if entropy_after > entropy_before:
    print("We are ascending the entropy gradient")
else:
    print("We are descending the entropy gradient")}

\code{# Initialize with asymmetric distribution (away from saddle point)
theta_init = np.array([1.0, -0.5, -0.2, -0.3])
theta_init = theta_init - np.mean(theta_init)  # Ensure constraint is satisfied

# Run gradient ascent
theta_history, entropy_history = gradient_ascent_four_bin(theta_init, steps=100, learning_rate=1.0)

# Create a grid for visualization
x = np.linspace(-2, 2, 100)
y = np.linspace(-2, 2, 100)
X, Y = np.meshgrid(x, y)

# Compute entropy at each grid point (with constraint on theta3 and theta4)
Z = np.zeros_like(X)
for i in range(X.shape[0]):
    for j in range(X.shape[1]):
        # Create full theta vector with constraint that sum is zero
        theta1, theta2 = X[i,j], Y[i,j]
        theta3 = -0.5 * (theta1 + theta2)
        theta4 = -0.5 * (theta1 + theta2)
        theta = np.array([theta1, theta2, theta3, theta4])
        Z[i,j] = exponential_family_entropy(theta)

# Compute gradient field
dX = np.zeros_like(X)
dY = np.zeros_like(Y)
for i in range(X.shape[0]):
    for j in range(X.shape[1]):
        # Create full theta vector with constraint
        theta1, theta2 = X[i,j], Y[i,j]
        theta3 = -0.5 * (theta1 + theta2)
        theta4 = -0.5 * (theta1 + theta2)
        theta = np.array([theta1, theta2, theta3, theta4])
        
        # Get full gradient and project
        grad = entropy_gradient(theta)
        proj_grad = project_gradient(theta, grad)
        
        # Store first two components
        dX[i,j] = proj_grad[0]
        dY[i,j] = proj_grad[1]

# Normalize gradient vectors for better visualization
norm = np.sqrt(dX**2 + dY**2)
# Avoid division by zero
norm = np.where(norm < 1e-10, 1e-10, norm)
dX_norm = dX / norm
dY_norm = dY / norm

# A few gradient vectors for visualization
stride = 10}

\setupplotcode{import matplotlib.pyplot as plt
import mlai.plot as plot
import mlai}

\plotcode{fig = plt.figure(figsize=plot.big_wide_figsize)

# Create contour lines only (no filled contours)
contours = plt.contour(X, Y, Z, levels=15, colors='black', linewidths=0.8)
plt.clabel(contours, inline=True, fontsize=8, fmt='%.2f')

# Add gradient vectors (normalized for direction, but scaled by magnitude for visibility)
plt.quiver(X[::stride, ::stride], Y[::stride, ::stride], 
           dX_norm[::stride, ::stride], dY_norm[::stride, ::stride], 
           color='r', scale=30, width=0.003, scale_units='width')

# Plot the gradient ascent trajectory
plt.plot(theta_history[:, 0], theta_history[:, 1], 'b-', linewidth=2, 
         label='Gradient Ascent Path')
plt.scatter(theta_history[0, 0], theta_history[0, 1], color='green', s=100, 
           marker='o', label='Start')
plt.scatter(theta_history[-1, 0], theta_history[-1, 1], color='purple', s=100, 
           marker='*', label='End')

# Add labels and title
plt.xlabel('$\\theta_1$')
plt.ylabel('$\\theta_2$')
plt.title('Entropy Contours with Gradient Field')

# Mark the saddle point (approximately at origin for this system)
plt.scatter([0], [0], color='yellow', s=100, marker='*', 
            edgecolor='black', zorder=10, label='Saddle Point')
plt.legend()

mlai.write_figure(filename='simplified-saddle-point-example.svg', 
                  directory = './information-game')

# Plot entropy evolution during gradient ascent
plt.figure(figsize=plot.big_figsize)
plt.plot(entropy_history)
plt.xlabel('Gradient Ascent Step')
plt.ylabel('Entropy')
plt.title('Entropy Evolution During Gradient Ascent')
plt.grid(True)
mlai.write_figure(filename='four-bin-entropy-evolution.svg', 
                  directory = './information-game')}

\newslide{Saddle Point Example}

\figure{\includediagram{\diagramsDir/information-game/simplified-saddle-point-example}{70%}}{Visualisation of a saddle point projected down to two dimensions.}{simplified-saddle-point-example}

\newslide{Entropy Evolution}

\figure{\includediagram{\diagramsDir/information-game/four-bin-entropy-evolution}{70%}}{Entropy evolution during gradient ascent on the four-bin system.}{four-bin-entropy-evolution}

\notes{The animation of system evolution would show initial rapid movement along high-eigenvalue directions, progressive slowing in directions with low eigenvalues and formation of information reservoirs in the critically slowed directions. Parameter-capacity uncertainty emerges naturally at the saddle point.
} 



\endif

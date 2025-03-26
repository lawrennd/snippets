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

\code{# Exponential family entropy with saddle point
def exponential_family_entropy(theta1, theta2, theta3=None):
    """
    Compute entropy of a 4-bin exponential family distribution
    parameterized by natural parameters theta1, theta2, theta3
    (with the constraint that probabilities sum to 1)
    """
    # If theta3 is not provided, we'll use a function of theta1 and theta2
    if theta3 is None:
        theta3 = -0.5 * (theta1 + theta2)
    
    # Compute the log-partition function (normalization constant)
    theta4 = -(theta1 + theta2 + theta3)  # Constraint
    log_Z = np.log(np.exp(theta1) + np.exp(theta2) + np.exp(theta3) + np.exp(theta4))
    
    # Compute probabilities
    p1 = np.exp(theta1 - log_Z)
    p2 = np.exp(theta2 - log_Z)
    p3 = np.exp(theta3 - log_Z)
    p4 = np.exp(theta4 - log_Z)
    
    # Compute entropy: -sum(p_i * log(p_i))
    entropy = -np.sum(
        np.array([p1, p2, p3, p4]) * 
        np.log(np.array([p1, p2, p3, p4])), 
        axis=0, where=np.array([p1, p2, p3, p4])>0
    )
    
    return entropy

def entropy_gradient(theta1, theta2, theta3=None):
    """
    Compute the gradient of the entropy with respect to theta1 and theta2
    """
    # If theta3 is not provided, we'll use a function of theta1 and theta2
    if theta3 is None:
        theta3 = -0.5 * (theta1 + theta2)
    
    # Compute the log-partition function
    theta4 = -(theta1 + theta2 + theta3)  # Constraint
    log_Z = np.log(np.exp(theta1) + np.exp(theta2) + np.exp(theta3) + np.exp(theta4))
    
    # Compute probabilities
    p1 = np.exp(theta1 - log_Z)
    p2 = np.exp(theta2 - log_Z)
    p3 = np.exp(theta3 - log_Z)
    p4 = np.exp(theta4 - log_Z)
    
    # For the gradient, we need to account for the constraint on theta3
    # When theta3 = -0.5(theta1 + theta2), we have:
    # theta4 = -(theta1 + theta2 + theta3) = -(theta1 + theta2 - 0.5(theta1 + theta2)) = -0.5(theta1 + theta2)
    
    # Gradient components with chain rule applied
    # For theta1: ∂S/∂theta1 + ∂S/∂theta3 * ∂theta3/∂theta1 + ∂S/∂theta4 * ∂theta4/∂theta1
    grad_theta1 = (p1 * (np.log(p1) + 1)) - 0.5 * (p3 * (np.log(p3) + 1)) - 0.5 * (p4 * (np.log(p4) + 1))
    
    # For theta2: ∂S/∂theta2 + ∂S/∂theta3 * ∂theta3/∂theta2 + ∂S/∂theta4 * ∂theta4/∂theta2
    grad_theta2 = (p2 * (np.log(p2) + 1)) - 0.5 * (p3 * (np.log(p3) + 1)) - 0.5 * (p4 * (np.log(p4) + 1))
    
    return grad_theta1, grad_theta2

# Create a grid of points
x = np.linspace(-2, 2, 100)
y = np.linspace(-2, 2, 100)
X, Y = np.meshgrid(x, y)

# Compute entropy and its gradient at each point
Z = exponential_family_entropy(X, Y)
dX, dY = entropy_gradient(X, Y)

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
# Note: We're using the negative of the gradient to point in direction of increasing entropy
plt.quiver(X[::stride, ::stride], Y[::stride, ::stride], 
           -dX_norm[::stride, ::stride], -dY_norm[::stride, ::stride], 
           color='r', scale=30, width=0.003, scale_units='width')

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
}


\newslide{Saddle Point Example}

\figure{\includediagram{\diagramsDir/information-game/simplified-saddle-point-example}{70%}}{Visualisation of a saddle point projected down to two dimensions.}{simplified-saddle-point-example}

\notes{The animation of system evolution would show initial rapid movement along high-eigenvalue directions, progressive slowing in directions with low eigenvalues and formation of information reservoirs in the critically slowed directions. Parameter-capacity uncertainty emerges naturally at the saddle point.
} 

\endif

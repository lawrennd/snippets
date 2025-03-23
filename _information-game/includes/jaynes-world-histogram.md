\ifndef{jaynesWorldHistogram}
\define{jaynesWorldHistogram}

\editme

\subsection{Histogram Game}

\setupcode{import numpy as np}

\setupplotcode{import matplotlib.pyplot as plt}

\helpercode{def plot_histogram(p, max_height=None):
    heights = p
    if max_height is None:
        max_height = 1.25*heights.max()
    S = - (p*np.log2(p)).sum()

    # Define bin edges
    bins = [1, 2, 3, 4, 5]  # Bin edges

    # Create the histogram
    plt.figure(figsize=(6, 4))  # Adjust figure size for slides
    plt.hist(bins[:-1], bins=bins, weights=heights, align='left', rwidth=0.8, edgecolor='black') # Use weights for probabilities


    # Customize the plot for better slide presentation
    plt.xlabel("Bin")
    plt.ylabel("Probability")
    plt.title(f"Four Bin Histogram (Entropy {S:.3f})")
    plt.xticks(bins[:-1]) # Show correct x ticks
    plt.ylim(0,max_height) # Set y limit for visual appeal
    plt.tight_layout() # Improve layout


    # Display the plot
    plt.show()
}


\plotcode{# Define probabilities
p = np.zeros(4)
p[0] = 4/13
p[1] = 3/13
p[2] = 3.7/13
p[3] = 1 - p.sum()

plot_histogram(p)}

\setupcode{import matplotlib.pyplot as plt
import numpy as np

# Define the entropy function
def entropy(lambdas):
    ells = 1/lambdas
    p = ells**2/(ells**2).sum()
    return np.log2(np.sum(ells**2))-np.sum(p * np.log2(ells**2))

# Define the gradient of the entropy function
def entropy_gradient(lambdas):
    ells = 1/lambdas
    denominator = np.sum(ells**2)
    ell_entropy = -2/(ells**2)*np.log2(ells)
    p = ells**2/denominator
    const = (p**2*ell_entropy).sum()
    gradient = -ells*ells*2*ells*(p*ell_entropy - const)
    return gradient

# Numerical gradient check
def numerical_gradient(func, lambdas, h=1e-6):
    numerical_grad = np.zeros_like(lambdas)
    for i in range(len(lambdas)):
        temp_lambda_plus = lambdas.copy()
        temp_lambda_plus[i] += h
        temp_lambda_minus = lambdas.copy()
        temp_lambda_minus[i] -= h
        numerical_grad[i] = (func(temp_lambda_plus) - func(temp_lambda_minus)) / (2 * h)
    return numerical_grad

# Initial parameters (lambda)
initial_lambdas = np.array([0.01, 100, 100, 100])
#initial_lambdas = np.array([1.01, 0.99, 1.2, 3.1])
# Gradient check
numerical_grad = numerical_gradient(entropy, initial_lambdas)
analytical_grad = entropy_gradient(initial_lambdas)
print("Numerical Gradient:", numerical_grad)
print("Analytical Gradient:", analytical_grad)
print("Gradient Difference:", np.linalg.norm(numerical_grad - analytical_grad))  # Check if close to zero


# Steepest ascent
lambdas = initial_lambdas.copy()
ells = 1/lambdas
plot_histogram(ells**2/(ells**2).sum(), 1)

learning_rate = 1
iterations = 15000
entropy_values = []
lambdas_history = []

for _ in range(iterations):
    grad = entropy_gradient(lambdas)
    lambdas += learning_rate * grad # update lambda for steepest ascent
    entropy_values.append(entropy(lambdas))
    lambdas_history.append(lambdas)

ells = 1/lambdas
plot_histogram(ells**2/(ells**2).sum(), 1)


# Plot entropy vs. iteration
plt.plot(range(iterations), entropy_values)
plt.xlabel("Iterations")
plt.ylabel("Entropy")
plt.title("Entropy vs. Iterations (Steepest Ascent)")
plt.show()
}

\endif

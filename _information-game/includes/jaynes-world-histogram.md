\ifndef{jaynesWorldHistogram}
\define{jaynesWorldHistogram}

\editme

\subsection{Histogram Game}

\notes{To illustrate the concept of the Jaynes' world entropy game we'll run a simple example using a four bin histogram. The entropy of a four bin histogram can be computed as,
$$
S(p) = - \sum_{i=1}^4 p_i \log_2 p_i.
$$
}

\include{_software/includes/mlai-software.md}

\setupcode{import numpy as np}


\notes{Some helper code to plot the histogram and compute its entropy.}

\setupplotcode{import matplotlib.pyplot as plt
import mlai.plot as plot}

\helpercode{def plot_histogram(ax, p, max_height=None):
    heights = p
    if max_height is None:
        max_height = 1.25*heights.max()
    S = - (p*np.log2(p)).sum()

    # Define bin edges
    bins = [1, 2, 3, 4, 5]  # Bin edges

    # Create the histogram
    if ax is None:
        fig, ax = plt.subplots(figsize=(6, 4))  # Adjust figure size 
    ax.hist(bins[:-1], bins=bins, weights=heights, align='left', rwidth=0.8, edgecolor='black') # Use weights for probabilities


    # Customize the plot for better slide presentation
    ax.set_xlabel("Bin")
    ax.set_ylabel("Probability")
    ax.set_title(f"Four Bin Histogram (Entropy {S:.3f})")
    ax.set_xticks(bins[:-1]) # Show correct x ticks
    ax.set_ylim(0,max_height) # Set y limit for visual appeal
    ax.tight_layout() # Improve layout

}


\code{
# Define probabilities
p = np.zeros(4)
p[0] = 4/13
p[1] = 3/13
p[2] = 3.7/13
p[3] = 1 - p.sum()}

\setupplotcode{import matplotlib.pyplot as plt
import mlai.plot as plot
import mlai.write_figure}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
plot_histogram(ax, p)
mlai.write_figure(filename='four-bin-histogram.svg', 
				  directory = '\writeDiagramsDir/information-game')
}

\setupcode{import numpy as np}

\helpercode{# Define the entropy function
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
}

\setupcode{import numpy as np}

\code{# Initial parameters (lambda)
initial_lambdas = np.array([100, 0.01, 0.01, 0.01])

# Gradient check
numerical_grad = numerical_gradient(entropy, initial_lambdas)
analytical_grad = entropy_gradient(initial_lambdas)
print("Numerical Gradient:", numerical_grad)
print("Analytical Gradient:", analytical_grad)
print("Gradient Difference:", np.linalg.norm(numerical_grad - analytical_grad))  # Check if close to zero}

\setupcode{import numpy as np}

\code{# Steepest ascent algorithm
lambdas = initial_lambdas.copy()

learning_rate = 1
iterations = 15000
entropy_values = []
lambdas_history = []

for _ in range(iterations):
    grad = entropy_gradient(lambdas)
    lambdas += learning_rate * grad # update lambda for steepest ascent
    entropy_values.append(entropy(lambdas))
    lambdas_history.append(lambdas)
}

\setupplotcode{import matplotlib.pyplot as plt
import mlai.plot as plot
import mlai.write_figure}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
plot_at = [0, 100, 1000, 10000, iterations-1]
for i in plot_at:
    plot_histogram(ax, lambdas_history[i]**2/(lambdas_history[i]**2).sum(), 1)
    # write the figure, padding the iteration number with zeros to 5 digits
    mlai.write_figure(filename=f'four-bin-histogram-iteration-{i:05d}.svg', 
					  directory = '\writeDiagramsDir/information-game')
}

\displaycode{nu.display_plots('two_point_sample{sample:0>3}.svg', 
                            '\writeDiagramsDir/gp', 
							sample=IntSlider(13, 13, 17, 1))}
							
\notes{\figure{\includediagram{\diagramsDir/gp/two_point_sample013}{80%}}{Sample from the joint Gaussian model, points indexed by 1 and 8 highlighted.}{two-point-sample-13}}

\subsubsection{Prediction of $\mappingFunction_{8}$ from $\mappingFunction_{1}$}

\slides{
\define{width}{80%}
\startanimation{four-bin-histogram}{13}{17}
\newframe{\includediagram{\diagramsDir/gp/two_point_sample013}{\width}}{two_point_sample3}
\newframe{\includediagram{\diagramsDir/gp/two_point_sample014}{\width}}{two_point_sample3}
\newframe{\includediagram{\diagramsDir/gp/two_point_sample015}{\width}}{two_point_sample3}
\newframe{\includediagram{\diagramsDir/gp/two_point_sample016}{\width}}{two_point_sample3}
\newframe{\includediagram{\diagramsDir/gp/two_point_sample017}{\width}}{two_point_sample3}
\endanimation
}
\notes{\figure{\includediagram{\diagramsDir/gp/two_point_sample017}{80%}}{The joint Gaussian over $\mappingFunction_1$ and $\mappingFunction_8$ along with the conditional distribution of $\mappingFunction_8$ given $\mappingFunction_1$}{two-point-sample-one-eight}}


\plotcode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
ax.plot(range(iterations), entropy_values)
ax.set_xlabel("Iterations")
ax.set_ylabel("Entropy")
ax.set_title("Entropy vs. Iterations (Steepest Ascent)")
mlai.write_figure(filename='four-bin-histogram-entropy-vs-iterations.svg', 
				  directory = '\writeDiagramsDir/information-game')
}

\figure{\includediagram{\diagramsDir/information-game/four-bin-histogram-entropy-vs-iterations.svg}{70%}}{Four bin histogram entropy game. The plot shows the increasing entropy against the number of iterations.}{four-bin-histogram-entropy-vs-iterations}

\endif

\ifndef{fourBinExample}
\define{fourBinExample}

\editme

\include{_information-game/includes/jaynes-world-histogram.md}

\subsection{Four Bin Histogram Entropy Game}

\notes{To do this we represent the histogram parameters as a vector of length 4, $\mappingVector{\lambda} = [\lambda_1, \lambda_2, \lambda_3, \lambda_4]$ and define the histogram probabilities to be $p_i = \lambda_i^2 / \sum_{j=1}^4 \lambda_j^2$.}

\setupcode{import numpy as np}

\helpercode{# Define the entropy function 
def entropy(lambdas):
    p = lambdas**2/(lambdas**2).sum()
    
    # Safe entropy calculation
    nonzero_p = p[p > 0]
    nonzero_lambdas = lambdas[p > 0]
    return np.log2(np.sum(lambdas**2))-np.sum(nonzero_p * np.log2(nonzero_lambdas**2))

# Define the gradient of the entropy function
def entropy_gradient(lambdas):
    denominator = np.sum(lambdas**2)
    p = lambdas**2/denominator
    
    # Safe log calculation
    log_terms = np.zeros_like(lambdas)
    nonzero_idx = lambdas != 0
    log_terms[nonzero_idx] = np.log2(np.abs(lambdas[nonzero_idx]))
    
    p_times_lambda_entropy = -2*log_terms/denominator
    const = (p*p_times_lambda_entropy).sum()
    gradient = 2*lambdas*(p_times_lambda_entropy - const)
    return gradient

# Numerical gradient check
def numerical_gradient(func, lambdas, h=1e-5):
    numerical_grad = np.zeros_like(lambdas)
    for i in range(len(lambdas)):
        temp_lambda_plus = lambdas.copy()
        temp_lambda_plus[i] += h
        temp_lambda_minus = lambdas.copy()
        temp_lambda_minus[i] -= h
        numerical_grad[i] = (func(temp_lambda_plus) - func(temp_lambda_minus)) / (2 * h)
    return numerical_grad
}

\notes{We can then ascend the gradeint of the entropy function, starting at a parameter setting where the mass is placed in the first bin, we take $\lambda_2 = \lambda_3 = \lambda_4 = 0.01$ and $\lambda_1 = 100$.}

\notes{First to check our code we compare our numerical and analytic gradients.}
\setupcode{import numpy as np}

\code{# Initial parameters (lambda)
initial_lambdas = np.array([100, 0.01, 0.01, 0.01])

# Gradient check
numerical_grad = numerical_gradient(entropy, initial_lambdas)
analytical_grad = entropy_gradient(initial_lambdas)
print("Numerical Gradient:", numerical_grad)
print("Analytical Gradient:", analytical_grad)
print("Gradient Difference:", np.linalg.norm(numerical_grad - analytical_grad))  # Check if close to zero}

\notes{Now we can run the steepest ascent algorithm.}

\define{\gradientAscentTurns}{15000}
\setupcode{import numpy as np}

\code{# Steepest ascent algorithm
lambdas = initial_lambdas.copy()

learning_rate = 1
turns = \gradientAscentTurns
entropy_values = []
lambdas_history = []

for _ in range(turns):
    grad = entropy_gradient(lambdas)
    lambdas += learning_rate * grad # update lambda for steepest ascent
    entropy_values.append(entropy(lambdas))
    lambdas_history.append(lambdas.copy())
}

\notes{We can plot the histogram at a set of chosen turn numbers to see the progress of the algorithm.}

\setupplotcode{import matplotlib.pyplot as plt
import mlai.plot as plot
import mlai}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
plot_at = [0, 100, 1000, 2500, 5000, 7500, 10000, 12500, turns-1]
for i, iter in enumerate(plot_at):
    plot_histogram(ax, lambdas_history[i]**2/(lambdas_history[i]**2).sum(), 1)
    # write the figure,
    mlai.write_figure(filename=f'four-bin-histogram-turn-{i:02d}.svg', 
					  directory = '\writeDiagramsDir/information-game')
}

\setupdisplaycode{import notutils as nu
from ipywidgets import IntSlider}
\displaycode{nu.display_plots('two_point_sample{sample:0>3}.svg', 
                            '\writeDiagramsDir/information-game', 
							sample=IntSlider(5, 5, 5, 1))}
							

\subsubsection{}

\slides{
\define{width}{80%}
\startanimation{four-bin-histogram}{0}{9}
\newframe{\includediagram{\diagramsDir/information-game/four-bin-histogram-turn-00}{\width}}{four-bin-histogram}
\newframe{\includediagram{\diagramsDir/information-game/four-bin-histogram-turn-01}{\width}}{four-bin-histogram}
\newframe{\includediagram{\diagramsDir/information-game/four-bin-histogram-turn-02}{\width}}{four-bin-histogram}
\newframe{\includediagram{\diagramsDir/information-game/four-bin-histogram-turn-03}{\width}}{four-bin-histogram}
\newframe{\includediagram{\diagramsDir/information-game/four-bin-histogram-turn-04}{\width}}{four-bin-histogram}
\newframe{\includediagram{\diagramsDir/information-game/four-bin-histogram-turn-05}{\width}}{four-bin-histogram}
\newframe{\includediagram{\diagramsDir/information-game/four-bin-histogram-turn-06}{\width}}{four-bin-histogram}
\newframe{\includediagram{\diagramsDir/information-game/four-bin-histogram-turn-07}{\width}}{four-bin-histogram}
\newframe{\includediagram{\diagramsDir/information-game/four-bin-histogram-turn-08}{\width}}{four-bin-histogram}
\endanimation
}
\notes{\figure{\includediagram{\diagramsDir/information-game/four-bin-histogram-turn-00}{20%}\includediagram{\diagramsDir/information-game/four-bin-histogram-turn-02}{20%}\includediagram{\diagramsDir/information-game/four-bin-histogram-turn-04}{20%}\includediagram{\diagramsDir/information-game/four-bin-histogram-turn-06}{20%}\includediagram{\diagramsDir/information-game/four-bin-histogram-turn-08}{20%}}{Intermediate stages of the histogram entropy game. After 0, 1000, 5000, 10000 and \gradientAscentTurns iterations.}{four-bin-histogram-turns}}

\notes{And we can also plot the changing entropy as a function of the number of game turns.}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
ax.plot(range(turns), entropy_values)
ax.set_xlabel("turns")
ax.set_ylabel("entropy")
ax.set_title("Entropy vs. turns (Steepest Ascent)")
mlai.write_figure(filename='four-bin-histogram-entropy-vs-turns.svg', 
				  directory = '\writeDiagramsDir/information-game')
}
\newslide{Four Bin Histogram Entropy Game}
\figure{\includediagram{\diagramsDir/information-game/four-bin-histogram-entropy-vs-turns}{70%}}{Four bin histogram entropy game. The plot shows the increasing entropy against the number of turns across \gradientAscentTurns iterations of gradient ascent.}{four-bin-histogram-entropy-vs-turns}

\notes{Note that the entropy starts at a saddle point, increaseases rapidly, and the levels off towards the maximum entropy, with the gradient decreasing slowly in the manner of Zeno's paradox.}

\endif
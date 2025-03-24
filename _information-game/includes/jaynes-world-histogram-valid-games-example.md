\ifndef{jaynesWorldHistogramValidGamesExample}
\define{jaynesWorldHistogramValidGamesExample}

\editme

\include{_information-game/includes/jaynes-world-histogram.md}
\subsection{Jaynes World Histogram Valid Games Example}

\notes{If we try to play the histogram game by setting $\lambda_1 = 1.0$ and $\lambda_2 = 0.5, \lambda_3 = 1.5, \lambda_4 = 0.4$ we obtain a starting configuration of the form,}

\setupcode{import numpy as np}

\code{lambdas = np.array([1.0, 0.5, 1.5, 0.4])
p = lambdas**2/lambdas**2.sum()
print(p)}

\setupplotcode{import matplotlib.pyplot as plt
import mlai.plot as plot}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
plot_histogram(ax, p)
mlai.write_figure(filename='jaynes-world-histogram-valid-games-example-1.svg', 
				  directory = '\writeDiagramsDir/information-game')
}

\figure{\includediagram{\diagramsDir/information-game/jaynes-world-histogram-valid-games-example-1}{\width}}{Jaynes world histogram valid games example 1.}{jaynes-world-histogram-valid-games-example-1}

\notes{If we now descend the entropy gradient in the steepest direction we obtain the following configuration.}

\setupcode{import numpy as np}

\code{
turns = 15000
lambdas = initial_lambdas.copy()

learning_rate = 1
entropy_values = []
lambdas_history = []

for _ in range(turns):
    grad = entropy_gradient(lambdas)
    lambdas -= learning_rate * grad # update lambda for steepest descent
    entropy_values.append(entropy(lambdas))
    lambdas_history.append(lambdas)
}

\setupplotcode{import matplotlib.pyplot as plt
import mlai.plot as plot}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
plot_histogram(ax, lambdas_history[-1]**2/(lambdas_history[-1]**2).sum())
mlai.write_figure(filename='jaynes-world-histogram-valid-games-origin.svg', 
				  directory = '\writeDiagramsDir/information-game')
}

\figure{\includediagram{\diagramsDir/information-game/jaynes-world-histogram-valid-games-origin}{\width}}{Jaynes world histogram valid games example 2.}{jaynes-world-histogram-valid-games-origin}

\notes{We can now check whether we can return to the original configuration through steepest ascent.}

\setupcode{import numpy as np}

\code{
lambdas = lambdas_history[-1].copy()

learning_rate = 1

for _ in range(turns):
    grad = entropy_gradient(lambdas)
    lambdas += learning_rate * grad # update lambda for steepest ascent
    entropy_values.append(entropy(lambdas))
    lambdas_history.append(lambdas)
}

\setupplotcode{import matplotlib.pyplot as plt
import mlai.plot as plot}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
plot_histogram(ax, lambdas_history[-1]**2/(lambdas_history[-1]**2).sum())
mlai.write_figure(filename='jaynes-world-histogram-valid-games-end.svg', 
				  directory = '\writeDiagramsDir/information-game')
}

\figure{\includediagram{\diagramsDir/information-game/jaynes-world-histogram-valid-games-end}{\width}}{Jaynes world histogram valid games example 3.}{jaynes-world-histogram-valid-games-end}

\notes{And if we view the path from the start to the end by visualising the sequence of histograms we see that we don't return to the original configuration.}

\setupplotcode{import matplotlib.pyplot as plt
import mlai.plot as plot}

\plotcode{# Plot 10 equally spaced histograms from the descent/ascent.
# Plot them in a 2x5 grid
fig, ax = plt.subplots(2, 5, figsize=plot.big_wide_figsize)
for i in range(0, len(lambdas_history), len(lambdas_history)//10):
    plot_histogram(ax[i//5, i%5], lambdas_history[i]**2/(lambdas_history[i]**2).sum())
mlai.write_figure(filename='jaynes-world-histogram-valid-games-path.svg', 
				  directory = '\writeDiagramsDir/information-game')
}

\figure{\includediagram{\diagramsDir/information-game/jaynes-world-histogram-valid-games-path}{\width}}{Jaynes world histogram valid games path.}{jaynes-world-histogram-valid-games-path}

\endif
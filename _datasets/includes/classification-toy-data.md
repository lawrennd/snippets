\ifndef{classificationToyData}
\define{classificationToyData}

\editme

\subsection{Toy Data}

\notes{We'll consider a toy data set and a decision boundary that separates red crosses from green circles.}
\slides{
- Red crosses (+ve) and green circles (-ve).}

\setupcode{import numpy as np}

\code{np.random.seed(seed=1000001)
x_plus = np.random.normal(loc=1.3, size=(30, 2))
x_minus = np.random.normal(loc=-1.3, size=(30, 2))}


\setupplotcode{import mlai
import mlai.plot as plot
import matplotlib.pyplot as plt}

\plotcode{# plot data
fig, ax = plt.subplots(figsize=plot.big_figsize)
ax.plot(x_plus[:, 0], x_plus[:, 1], 'rx')
ax.plot(x_minus[:, 0], x_minus[:, 1], 'go')

plt.tight_layout()
mlai.write_figure("artificial-classification-example.svg", directory="\writeDiagramsDir/ml")}

\figure{\includediagram{\diagramsDir/ml/artificial-classification-example}{80%}}{Red crosses and green circles are sampled from two separate Gaussian distributions with 30 examples of each.}{artificial-classification-examples}

\endif

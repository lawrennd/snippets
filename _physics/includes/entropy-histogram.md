\ifndef{entropyHistogram}
\define{entropyHistogram}

\editme

\newslide{}

\setupcode{import numpy as np}

\code{p = np.random.randn(10000, 1)
xlim = [-4, 4]
x = np.linspace(xlim[0], xlim[1], 200)
y = 1/np.sqrt(2*np.pi)*np.exp(-0.5*x*x)}

\setupplotcode{import matplotlib.pyplot as plt
import mlai.plot as plot
import mlai}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
ax.plot(x, y, 'r', linewidth=3)
ax.hist(p, 100, density=True)
ax.set_xlim(xlim)

mlai.write_figure('gaussian-histogram.svg', directory='\writeDiagramsDir/ml')}

\notes{Another important figure for Cambridge was the first to derive the probability distribution that results from small balls banging together in this manner. In doing so, James Clerk Maxwell founded the field of statistical physics.}

\figure{\includediagram{\diagramsDir/ml/gaussian-histogram}{80%}}{James Clerk Maxwell 1831-1879 Derived distribution of velocities of particles in an ideal gas (elastic fluid).}{gaussian-histogram}

\endif

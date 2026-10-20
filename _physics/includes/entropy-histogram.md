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

\figure{\includediagram{\diagramsDir/ml/gaussian-histogram}{80%}}{Maxwell (1831--1879): each *Cartesian velocity component* of an ideal-gas particle is Gaussian. Speed $v=|\mathbf{v}|$ is not --- it picks up a $v^2$ Jacobian.}{gaussian-histogram}

\newslides{Gaussian Components, Not Speed}

\slides{The histogram above is one component $v_x$. The Maxwell *speed* distribution is different.}

\slidesincremental{
* Component $v_x$: Gaussian (what we plotted)
* Speed $v=|\mathbf{v}|$: $f(v)\propto v^2 e^{-mv^2/2kT}$
* Week 3: how that change of variables shifts continuous entropy
}

\speakernotes{Forward pointer only. Do not derive the Jacobian entropy shift today --- that is week 3 (differential entropy and KL). Week 5 returns with MaxEnt against a reference measure.}

\notes{Both facts are Maxwell--Boltzmann physics. Confusing them is easy because textbooks say ``Maxwell--Boltzmann distribution'' for either object. The geometric factor $v^2$ is a change of variables. Continuous entropy is not invariant under that map; relative entropy is. We return to the calculation when differential entropy and KL are on the board.}

\endif

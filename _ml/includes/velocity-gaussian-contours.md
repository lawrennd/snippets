\ifndef{velocityGaussianContours}
\define{velocityGaussianContours}
\editme

\setuphelpercode{import mlai.plot as plot
import mlai
import numpy as np
import os}

\helpercode{def plot_correlated_gaussian(mu_x = 0, 
                             var_x = 1, mu_y = 0, var_y = 1, 
						     xlabel = "$v_x$", ylabel = "$v_y$", correlation = 0.5, ax=None, diagrams="\writeDiagramsDir/ml"):

    sd_x = np.sqrt(var_x)
    sd_y = np.sqrt(var_y)
    tau = 2*np.pi

    x = np.linspace(mu_x-3*sd_x, mu_x+3*sd_x, 100)[:, np.newaxis]
    y = np.linspace(mu_y-3*sd_y, mu_y+3*sd_y, 100)[:, np.newaxis]

    p_x = 1/np.sqrt(tau*var_x)*np.exp(-1/(2*var_x)*(x - mu_x)**2)
    p_y = 1/np.sqrt(tau*var_y)*np.exp(-1/(2*var_y)*(y - mu_y)**2)

    covMat = np.asarray([[1, correlation], [correlation, 1]])
    fact = np.asarray([[sd_x, 0], [0, sd_y]])
    covMat = np.dot(np.dot(fact,covMat), fact)
    v, R = np.linalg.eig(covMat)
	if ax is None:
	    fig, ax = plt.subplots(1, 1, figsize=plot.big_figsize)

    ax.plot(mu_x, mu_y, 'x', color=[1., 0., 1.], markersize=5, linewidth=3)
    theta = np.linspace(0, tau, 100)
    xel = np.sin(theta)*np.sqrt(v[0])
    yel = np.cos(theta)*np.sqrt(v[1])
    vals = np.dot(R,np.vstack([xel, yel]))
    ax.plot(vals[0, :]+mu_x, vals[1, :]+mu_y, '-', color=[1., 0., 1.], linewidth=3)
    ax.set_xlim([np.min(x), np.max(x)])
    ax.set_ylim([np.min(y), np.max(y)])
    ax.set_xticks([mu_x-3*sd_x, mu_x, mu_x+3*sd_x])
    ax.set_yticks([mu_y-3*sd_y, mu_y, mu_y+3*sd_y])
    ax.set_xlabel(xlabel, fontsize=20)
    ax.set_ylabel(ylabel, fontsize=20)
}
\newslide{Independent Gaussians}

\setupplotcode{import matplotlib.pyplot as plt
import mlai}

\plotcode{fig, ax = plt.subplots(1, 1, figsize=plot.big_figsize)
plot_correlated_gaussian(correlation=0.0, ax=ax)

mlai.write_figure(figure=fig, filename=f'independent-gaussians.svg', directory="\writeDiagramsDir/ml", transparent=True)}

\figure{\includediagram{\diagramsDir/ml/independent-gaussians}{60%}}{Two independent Gaussians for the $x$ and $y$ velocity of a ball.}{independent-gaussians}

\newslide{Correlated Gaussians}

\plotcode{fig, ax = plt.subplots(1, 1, figsize=plot.big_figsize)
plot_correlated_gaussian(correlation=0.995, ax=ax)

mlai.write_figure(figure=fig, filename=f'correlated-gaussians.svg', directory="\writeDiagramsDir/ml", transparent=True)
}

\figure{\includediagram{\diagramsDir/ml/correlated-gaussians}{60%}}{A correlated Gaussian for the $x$ and $y$ velocity of a ball. If all balls were correlated in this way, this would imply that the whole box is moving towards the upper right or bottom left.}{correlated-gaussians}

\newslide{Anticorrelated Gaussians}

\plotcode{fig, ax = plt.subplots(1, 1, figsize=plot.big_figsize)
plot_correlated_gaussian(correlation=-0.995, ax=ax)

mlai.write_figure(figure=fig, filename=f'anti-correlated-gaussians.svg', directory="\writeDiagramsDir/ml", transparent=True)
}

\figure{\includediagram{\diagramsDir/ml/anti-correlated-gaussians}{60%}}{An anti-correlated Gaussian for the $x$ and $y$ velocity of a ball. If all balls were anti-correlated in this way, this would imply that the whole box is moving towards the upper left or bottom right.}{anti-correlated-gaussians}



\endif

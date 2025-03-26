\ifndef{twoBinExample}
\define{twoBinExample}

\editme

\subsection{Two-Bin Histogram Example}

\notes{The simplest possible example of Jaynes' World is a two-bin histogram with probabilities $p$ and $1-p$. This minimal system allows us to visualize the entire entropy landscape.}

\slides{
* Simplest example: Two-bin system
* States represented by probability $p$ (with $1-p$ in second bin)
* Entropy: $S(p) = -p\log p - (1-p)\log(1-p)$
* Maximum entropy at $p = 0.5$
* Minimal entropy at $p = 0$ or $p = 1$
}

\notes{
The natural parameter is the log odds, $\theta = \log\frac{p}{1-p}$, and the update given by the entropy gradient is
$$
\Delta \theta_{\text{steepest}} = \eta \frac{\text{d}S}{\text{d}\theta} = \eta p(1-p)(\log(1-p) - \log p).
$$
The Fisher information is
$$
G(\theta) = p(1-p)
$$
This creates a dynamic where as $p$ approaches either 0 or 1 (minimal entropy states), the Fisher information approaches zero, creating a critical slowing" effect. This critical slowing is what leads to the formation of *information resevoirs*. Note also that in the *natural gradient* the updated is given by multiplying the gradient by the inverse Fisher information, which would lead to a more efficient update of the form, 
$$
\Delta \theta_{\text{natural}} =  \eta(\log(1-p) - \log p),
$$
however, it is precisely this efficiency that we want our game to avoid, because it is the inefficient behaviour in the reagion of saddle points that leads to critical slowing and the emergence of information resevoirs.
}

\setupcode{import numpy as np}

\code{# Python code for gradients
p_values = np.linspace(0.000001, 0.999999, 10000)
theta_values = np.log(p_values/(1-p_values))
entropy = -p_values * np.log(p_values) - (1-p_values) * np.log(1-p_values)
fisher_info = p_values * (1-p_values)
gradient = fisher_info * (np.log(1-p_values) - np.log(p_values))
}

\newslide{Natural Gradients vs Steepest Ascent}
\slides{$$
\Delta \theta_{\text{steepest}} = \eta \frac{\text{d}S}{\text{d}\theta} = \eta p(1-p)(\log(1-p) - \log p).
$$
$$
G(\theta) = p(1-p)
$$
$$
\Delta \theta_{\text{natural}} =  \eta(\log(1-p) - \log p),
$$
}
\setupplotcode{import matplotlib.pyplot as plt
import mlai.plot as plot
import mlai}

\plotcode{fig, (ax1, ax2) = plt.subplots(1, 2, figsize=plot.big_wide_figsize)

ax1.plot(theta_values, entropy)
ax1.set_xlabel('$\\theta$')
ax1.set_ylabel('Entropy $S(p)$')
ax1.set_title('Entropy Landscape')

ax2.plot(theta_values, gradient)
ax2.set_xlabel('$\\theta$')
ax2.set_ylabel('$\\nabla_\\theta S(p)$')
ax2.set_title('Entropy Gradient vs. Position')

mlai.write_figure(filename='two-bin-histogram-entropy-gradients.svg', 
				  directory = '\writeDiagramsDir/information-game')}

\newslide{}

\figure{\includediagram{\diagramsDir/information-game/two-bin-histogram-entropy-gradients}{95%}}{Entropy gradients of the two bin histogram agains position.}{two-bin-histogram-entropy-gradients}

\notes{This simple example reveals the entropy extrema at $p = 0$, $p = 0.5$, and $p = 1$. At minimal entropy ($p \approx 0$ or $p \approx 1$), the gradient approaches zero, creating natural information reservoirs. The dynamics slow dramatically near these points - these are the areas of critical slowing that create information reservoirs.
} 

\endif

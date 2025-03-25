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
The natural parameter is $\theta = \log\frac{p}{1-p}$, and the entropy gradient is:
$$\frac{dS}{d\theta} = p(1-p)(\log(1-p) - \log p)$$

The Fisher information is:
$$G(\theta) = p(1-p)$$

This creates a fascinating dynamic: as $p$ approaches either 0 or 1 (minimal entropy states), the Fisher information approaches zero, creating a "critical slowing" effect exactly where information reservoirs would form.
}

\code{
# Python visualization code
import numpy as np
import matplotlib.pyplot as plt

p_values = np.linspace(0.001, 0.999, 1000)
entropy = -p_values * np.log(p_values) - (1-p_values) * np.log(1-p_values)
fisher_info = p_values * (1-p_values)
gradient = fisher_info * (np.log(1-p_values) - np.log(p_values))

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
ax1.plot(p_values, entropy)
ax1.set_xlabel('p')
ax1.set_ylabel('Entropy S(p)')
ax1.set_title('Entropy Landscape')

ax2.plot(p_values, gradient)
ax2.set_xlabel('p')
ax2.set_ylabel('Entropy Gradient')
ax2.set_title('Entropy Gradient vs. Position')
}

\notes{This simple example reveals several key principles:
1. Entropy extrema occur at $p = 0$, $p = 0.5$, and $p = 1$
2. At minimal entropy ($p \approx 0$ or $p \approx 1$), the gradient approaches zero, creating natural information reservoirs
3. The dynamics slow dramatically near these points - critical slowing creates memory
} 

\endif

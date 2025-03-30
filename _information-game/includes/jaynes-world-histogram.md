\ifndef{jaynesWorldHistogram}
\define{jaynesWorldHistogram}

\editme

\subsection{Histogram Game}

\notes{To illustrate the concept of the Jaynes' world entropy game we'll run a simple example using a four bin histogram. The entropy of a four bin histogram can be computed as,
$$
S(p) = - \sum_{i=1}^4 p_i \log_2 p_i.
$$
}


\setupcode{import numpy as np}

\notes{First we write some helper code to plot the histogram and compute its entropy.}

\setupplotcode{import matplotlib.pyplot as plt
import mlai.plot as plot}

\helpercode{def plot_histogram(ax, p, max_height=None):
    heights = p
    if max_height is None:
        max_height = 1.25*heights.max()
    
    # Safe entropy calculation that handles zeros
    nonzero_p = p[p > 0]  # Filter out zeros
    S = - (nonzero_p*np.log2(nonzero_p)).sum()

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
}

\notes{We can compute the entropy of any given histogram.}
\code{
# Define probabilities
p = np.zeros(4)
p[0] = 4/13
p[1] = 3/13
p[2] = 3.7/13
p[3] = 1 - p.sum()

# Safe entropy calculation
nonzero_p = p[p > 0]  # Filter out zeros
entropy = - (nonzero_p*np.log2(nonzero_p)).sum()
print(f"The entropy of the histogram is {entropy:.3f}.")
}

\setupplotcode{import matplotlib.pyplot as plt
import mlai.plot as plot
import mlai}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
fig.tight_layout()
plot_histogram(ax, p)
ax.set_title(f"Four Bin Histogram (Entropy {entropy:.3f})")
mlai.write_figure(filename='four-bin-histogram.svg', 
				  directory = '\writeDiagramsDir/information-game')
}

\figure{\includediagram{\diagramsDir/information-game/four-bin-histogram}{70%}}{The entropy of a four bin histogram.}{four-bin-histogram-entropy}

\notes{We can play the entropy game by starting with a histogram with all the probability mass in the first bin and then ascending the gradient of the entropy function.}


\endif

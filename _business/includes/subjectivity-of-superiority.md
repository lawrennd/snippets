\ifndef{subjectivityOfSuperiority}
\define{subjectivityOfSuperiority}

\editme

\subsection{Subjectivity of Superiority}

\notes{There's a concept known as the phenomenon of illusory superiority, where individuals all think they are better than average at a given task/role.}

\notes{But because many tasks/roles are not uniquely defined, imagining that you can rank these roles is flawed. If there is a ranking, it's subjective according to how different people perceive the role. And under individuals different perception of the role, we *can* all be better than average, because we each have a different idea of what the ideal looks like.}

\setupcode{import numpy as np
import matplotlib.pyplot as plt}

\helpercode{def create_spider_plot(categories, scores, title, ax, max_value=10, min_value=0):
    """
    Create a spider plot for a given set of categories and scores.

    Parameters:
    - categories (list): The criteria labels for the spider plot.
    - scores (list): The scores for each criterion.
    - title (str): Title of the spider plot.
    - ax (matplotlib.axes._subplots.AxesSubplot): The subplot axis.
    - max_value (int): Maximum value for the radial scale.
    - min_value (int): Minimum value for the radial scale.
    """
    # Number of variables
    num_vars = len(categories)

    # Compute angles for the radar chart
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    angles += angles[:1]

    # Append the first score to close the plot
    scores += scores[:1]

    # Set up the spider plot
    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)
    
    # Draw one per variable + lines
    ax.plot(angles, scores, linewidth=2)
    ax.fill(angles, scores, alpha=0.25)

    # Labels for each category
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories, fontsize=10)

    # Radial scale
    ax.set_ylim(min_value, max_value)
    ax.set_yticks(range(min_value, max_value + 1, 2))  # Tick marks every 2 units
    ax.set_yticklabels([])

    # Add title
    ax.set_title(title, fontsize=12, fontweight="bold")

def generate_spider_plots(data, categories, max_value=10, min_value=0):
    """
    Generate a series of spider plots for different datasets.

    Parameters:
    - data (dict): A dictionary where keys are titles and values are score lists.
    - categories (list): The criteria labels for the spider plots.
    - max_value (int): Maximum value for the radial scale.
    - min_value (int): Minimum value for the radial scale.
    """
    num_plots = len(data)
    cols = 2
    rows = (num_plots + 1) // 2

    fig, axs = plt.subplots(rows, cols, subplot_kw={'polar': True}, figsize=(10, 5 * rows))
    axs = axs.flatten()

    for idx, (title, scores) in enumerate(data.items()):
        create_spider_plot(categories, scores, title, axs[idx], max_value, min_value)

    # Hide any unused subplots
    for ax in axs[len(data):]:
        ax.axis('off')

    plt.tight_layout()
    plt.show()
}

\code{# Example for academics
def plot_academics():
    categories = [
        "Mentorship", "Research Quality", "Teaching Inspiration", "Teaching Dedication",
        "Public Understanding", "Technical Depth", "Collaboration", "Professionalism"
    ]

    academic_profiles = {
        "Innovative Researcher": [6, 9, 4, 5, 7, 8, 8, 6],
        "Dedicated Teacher": [3, 4, 9, 9, 5, 4, 3, 5],
        "Public Communicator": [4, 4, 8, 4, 9, 5, 5, 4],
        "Well-Rounded Academic": [5, 6, 7, 7, 7, 6, 5, 5]
    }

    generate_spider_plots(academic_profiles, categories)
}

\code{# Example for drivers
def plot_drivers():
    categories = [
        "Reaction Time", "Vehicle Control", "Awareness", "Adherence to Rules",
        "Risk Assessment", "Passenger Comfort", "Defensive Driving", "Error Recovery"
    ]

    driver_profiles = {
        "Aggressive Driver": [8, 9, 8, 4, 4, 3, 4, 8],
        "Defensive Driver": [4, 3, 6, 8, 9, 9, 8, 6],
        "Inexperienced Driver": [4, 3, 5, 8, 4, 4, 4, 4],
        "Balanced Driver": [6, 7, 6, 7, 7, 4, 5, 6]
    }

    generate_spider_plots(driver_profiles, categories)
}

\setupplotcode{import mlai}

\plotcode{# Call both plots for demonstration
plot_academics()
mlai.write_figure("academic_capability_plots.svg", directory="\writeDiagramsDir/business")
plot_drivers()
mlai.write_figure("driver_capability_plots.svg", directory="\writeDiagramsDir/business")}

\figure{\includediagram{\diagramsDir/business/academic_capability_plots}{50%}}{There is no first principles definition of what it means to be a good academic.}{academic-capability-plots}

\endif

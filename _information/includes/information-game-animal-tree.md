\ifndef{informationGameAnimalTree}
\define{informationGameAnimalTree}

\editme

\setupplotcode{import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import mlai.plot as plot
import mlai}

\plotcode{def draw_yesno_tree(ax, node, x, y, dx, dy):
    """Draw a yes/no question tree. Leaves are named objects; internal nodes are questions.
    Each child dict may set leaf=True. Left is no, right is yes.
    """
    is_leaf = bool(node.get('leaf', False))
    label = node['label']
    width = max(0.16, 0.012 * len(label) + 0.08)
    height = 0.09
    facecolor = '#F4E2C9' if is_leaf else '#D6EAF8'
    box = FancyBboxPatch((x - width / 2, y - height / 2), width, height,
                         boxstyle='round,pad=0.012,rounding_size=0.02',
                         facecolor=facecolor, edgecolor='black', linewidth=1.2)
    ax.add_patch(box)
    ax.text(x, y, label, ha='center', va='center', fontsize=11)
    if is_leaf:
        return
    y_child = y - dy
    for key, x_child, name, ha, dx_text in (
            ('no', x - dx, 'no', 'right', -0.02),
            ('yes', x + dx, 'yes', 'left', 0.02)):
        child = node.get(key)
        if child is None:
            continue
        ax.plot([x, x_child], [y - height / 2, y_child + height / 2],
                color='black', lw=1.2, zorder=0)
        ax.text((x + x_child) / 2 + dx_text,
                (y + y_child) / 2,
                name, ha=ha, va='bottom', fontsize=9, color='#1B4F72')
        draw_yesno_tree(ax, child, x_child, y_child, dx / 2, dy)

animal_tree = {
    'label': 'Four legs?',
    'no': {
        'label': 'Wings?',
        'no': {'label': 'Snake', 'leaf': True},
        'yes': {'label': 'Owl', 'leaf': True},
    },
    'yes': {
        'label': 'Storybook?',
        'no': {'label': 'Fox', 'leaf': True},
        'yes': {'label': 'Gruffalo', 'leaf': True},
    },
}

fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
draw_yesno_tree(ax, animal_tree, x=0.5, y=0.88, dx=0.22, dy=0.36)
ax.set_xlim(0.0, 1.0)
ax.set_ylim(0.02, 1.0)
ax.axis('off')
mlai.write_figure('information-game-animal-tree.svg',
                  directory='\writeDiagramsDir/information')}

\figure{\includediagram{\diagramsDir/information/information-game-animal-tree}{70%}}{A balanced yes/no tree for four animals. Each question halves the remaining list, so two answers name one of $2^2=4$ hypotheses.}{information-game-animal-tree}

\endif

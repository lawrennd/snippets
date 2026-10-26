\ifndef{lifeGliderLoaferConway}
\define{lifeGliderLoaferConway}

\include{_simulation/includes/automata-base.md}
\include{_simulation/includes/life-implementation.md}
\include{_simulation/includes/automata-diagrams.md}

\editme

\subsection{Spaceships, oscillators and static patterns}

\notes{The game leads to patterns emerging, some of these patterns are static, but some oscillate in place, with varying periods. Others oscillate, but when they complete their cycle they've translated to a new location, in other words they move. In Life the former are known as [oscillators](https://conwaylife.com/wiki/Oscillator) and the latter as [spaceships](https://conwaylife.com/wiki/Spaceship).}

\helpercode{class LifePattern:
    """Class to represent and validate classic Life patterns"""
    def __init__(self, 
                 name: str,
                 pattern: List[Tuple[int, int]],
                 period: int,
                 translation: Tuple[int, int] = None,
                 discovery_year: int = None,
                 discoverer: str = None):
        """
        Args:
            name: Name of the pattern
            pattern: List of (x,y) coordinates for live cells
            period: Number of steps before pattern repeats
            translation: (dx,dy) movement after one period
            discovery_year: Year pattern was discovered
            discoverer: Name of discoverer
        """
        self.name = name
        self.pattern = pattern
        self.period = period
        self.translation = translation or (0, 0)
        self.discovery_year = discovery_year
        self.discoverer = discoverer
    
    def to_grid(self, size: int = 20) -> Grid:
        """Convert pattern to Grid instance"""
        grid = Grid(size, size)
        min_x = min(x for x, _ in self.pattern)
        min_y = min(y for _, y in self.pattern)
        
        # Center the pattern
        offset_x = size//2 - (max(x for x, _ in self.pattern) + min_x)//2
        offset_y = size//2 - (max(y for _, y in self.pattern) + min_y)//2
        
        for x, y in self.pattern:
            grid[x + offset_x, y + offset_y] = 1
        return grid}



\subsection{Pattern Analysis}

\notes{Before looking at specific examples, let's understand how these patterns behave. Life patterns can be classified by their periodic behavior and movement:
- *Static patterns* remain unchanged from one generation to the next
- *Oscillators* return to their initial state after a fixed number of generations (their period)
- *Spaceships* combine oscillation with translation, moving across the grid while cycling through their states

Each pattern can be characterized by:
- Its period (how many steps before it repeats)
- Its translation (how far it moves each period)
- Its velocity (translation per period)}



\helpercode{def rle_to_cells(rle: str) -> List[Tuple[int, int]]:
    """Decode a LifeWiki RLE pattern into live-cell (x, y) coordinates."""
    cells: List[Tuple[int, int]] = []
    x = y = 0
    count = 0
    for char in rle.strip():
        if char.isdigit():
            count = count * 10 + int(char)
            continue
        n = count if count else 1
        count = 0
        if char == 'o':
            cells.extend((x + i, y) for i in range(n))
            x += n
        elif char == 'b':
            x += n
        elif char == '$':
            y += n
            x = 0
        elif char == '!':
            break
    return cells}

\helpercode{# Classic patterns from LifeWiki RLE (https://conwaylife.com)
GLIDER = LifePattern(
    name="Glider",
    pattern=rle_to_cells("bob$2bo$3o!"),
    period=4,
    translation=(1, 1),
    discovery_year=1969,
    discoverer="Richard K. Guy"
)

LOAFER = LifePattern(
    name="Loafer",
    pattern=rle_to_cells("b2o2bob2o$o2bo2b2o$bobo$2bo$8bo$6b3o$5bo$6bo$7b2o!"),
    period=7,
    translation=(-1, 0),
    discovery_year=2013,
    discoverer="Josh Ball"
)

GOSPER_GLIDER_GUN = LifePattern(
    name="Gosper Glider Gun",
    pattern=rle_to_cells(
        "24bo$22bobo$12b2o6b2o12b2o$11bo3bo4b2o12b2o$"
        "2o8bo5bo3b2o$2o8bo3bob2o4bobo$10bo5bo7bo$11bo3bo$12b2o!"
    ),
    period=30,
    discovery_year=1970,
    discoverer="Bill Gosper"
)}

\setupcode{import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation}

\helpercode{def create_pattern_animation(pattern: LifePattern, 
                              steps: int = 20, 
                              size: int = 30,
                              interval: int = 200):
    """Create animation of a Life pattern evolution
    
    Args:
        pattern: LifePattern to animate
        steps: Number of steps to evolve
        size: Grid size
        interval: Animation interval in milliseconds
    """
    # Fixed boundaries keep spaceships from wrapping around the grid.
    history = run_life(
        size, size,
        steps=steps,
        initial_state=pattern.to_grid(size).grid,
        boundary='fixed',
    )

    fig, ax = plt.subplots(figsize=(5, 5))
    fig.set_facecolor('white')
    im = plot_automata_grid(history[0], ax)
    title = ax.set_title(f"{pattern.name} - Step 0")

    def animate(frame):
        im.set_data(history[frame].grid)
        title.set_text(f"{pattern.name} - Step {frame}")
        return im, title

    anim = FuncAnimation(
        fig, animate, frames=len(history),
        interval=interval, blit=False
    )

    filename = pattern.name.lower().replace(" ", "-") + '.gif'
    mlai.write_animation(
        anim, filename,
        directory='\writeDiagramsDir/simulation',
        writer='pillow',
        dpi=80,
    )
    plt.close(fig)}

\
\notes{John Horton Conway, as the creator of the game of life, could be seen somehow as the god of this small universe. He created the rules. The rules are so simple that in many senses he, and we, are all-knowing in this space. But despite our knowledge, this world can still 'surprise' us. From the simple rules, emergent patterns of behaviour arise.}

\newslide{Glider}

\plotcode{# Generate Glider animation
create_pattern_animation(GLIDER, steps=20)}

\figure{\columns{\aligncenter{*Glider (1969)*}\aligncenter{\includegif{\diagramsDir/simulation/glider}{80%}{}{left}}}{\includejpg{\diagramsDir/maths/John-Conway}{80%}{}{right}}{45%}{45%}}{*Left* A Glider pattern discovered 1969 by Richard K. Guy. *Right*. John Horton Conway, creator of *Life* (1937-2020). The glider is an oscillator that moves diagonally after creation.}{glider-loafer-conway}

\notes{The glider was 'discovered' in 1969 by Richard K. Guy. What do we mean by discovered in this context? Well, as soon as the game of life is defined, objects such as the glider do somehow exist, but the many configurations of the game mean that it takes some time for us to see one and know it exists. This means, that despite being the creator, Conway, and despite the rules of the game being simple, and despite the rules being deterministic, we are not 'omniscient' in any simplistic sense. It requires computation to 'discover' what can exist in this universe once it's been defined.} 

\newslide{Gosper Glider Gun}

\plotcode{# Generate Gosper Glider Gun animation
create_pattern_animation(GOSPER_GLIDER_GUN, steps=50, size=50)}

\figure{\includegif{\diagramsDir/simulation/gosper-glider-gun}{80%}}{The Gosper glider gun is a configuration that creates gliders. A new glider is released after every 30 turns.}{gosper-glider-gun}

\notes{These patterns had to be discovered, in the same way that a scientist might discover a disease, or an explorer a new land. For example, the Gosper glider gun was [discovered by Bill Gosper in 1970](https://conwaylife.com/wiki/Bill_Gosper). It is a pattern that creates a new glider every 30 turns of the game.}

\newslide{Loafer}

\plotcode{# Generate Loafer animation
create_pattern_animation(LOAFER, steps=28)}

\figure{\columns{\aligncenter{*Loafer (2013)*}\aligncenter{\includegif{\diagramsDir/simulation/loafer}{80%}{}{left}}}{\includejpg{\diagramsDir/maths/John-Conway}{80%}{}{right}}{45%}{45%}}{*Left* A Loafer pattern discovered by Josh Ball in 2013. *Right*. John Horton Conway, creator of *Life* (1937-2020).}{the-loafer-spaceship}

\notes{Despite widespread interest in Life, some of its patterns were only very recently discovered like the Loafer, discovered in 2013 by Josh Ball. So, despite the game having existed for over forty years, and the rules of the game being simple, there are emergent behaviors that are unknown.}

\endif

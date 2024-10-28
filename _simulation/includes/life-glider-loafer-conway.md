\ifndef{lifeGliderLoaferConway}
\define{lifeGliderLoaferConway}

\include{_simulation/includes/automata-base.md}
\include{_simulation/includes/life-implementation.md}

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



\helpercode{# Define classic patterns
GLIDER = LifePattern(
    name="Glider",
    pattern=[(0,1), (1,2), (2,0), (2,1), (2,2)],
    period=4,
    translation=(1,1),
    discovery_year=1969,
    discoverer="Richard K. Guy"
)

LOAFER = LifePattern(
    name="Loafer",
    pattern=[(0,2), (1,0), (1,2), (2,1), (2,2), (3,2), (4,2)],
    period=7,
    translation=(1,0),
    discovery_year=2013,
    discoverer="Josh Ball"
)

GOSPER_GLIDER_GUN = LifePattern(
    name="Gosper Glider Gun",
    pattern=[(0,2), (0,3), (1,2), (1,3), (8,3), (8,4), (9,2), (9,4), 
             (10,2), (10,3), (16,4), (16,5), (16,6), (17,4), (18,5),
             (22,1), (22,2), (23,0), (23,2), (24,0), (24,1), (24,2),
             (25,0), (25,1), (34,3), (34,4), (35,3), (35,4)],
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
    # Initialize with pattern
    history = run_life(
        size, size,
        steps=steps,
        initial_state=pattern.to_grid(size).grid
    )
    
    # Create figure and axis
    fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
    fig.set_facecolor('white')
    
    # Plot initial state
    plot_life_grid(history[0], ax)
    
    def animate(frame):
        ax.clear()
        plot_life_grid(history[frame], ax)
        ax.set_title(f"{pattern.name} - Step {frame}")
        return ax,
    
    anim = FuncAnimation(
        fig, animate, frames=len(history),
        interval=interval, blit=True
    )
    
    # Save animation
    filename = pattern.name.lower().replace(" ", "-")
    anim.save(mlai.filename_join(f'{filename}.gif',
                                '\writeDiagramsDir/simulation'),
              writer='pillow')}

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

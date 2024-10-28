\ifndef{lifeGliderLoaferConway}
\define{lifeGliderLoaferConway}

\editme

\subsection{Spaceships, oscillators and static patterns}

\setuphelpercode{import numpy as np
from typing import List, Tuple, Dict}

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
        
    def to_grid(self, size: int = 20) -> np.ndarray:
        """Convert pattern to grid representation"""
        grid = np.zeros((size, size), dtype=int)
        min_x = min(x for x, _ in self.pattern)
        min_y = min(y for _, y in self.pattern)
        
        # Center the pattern
        offset_x = size//2 - (max(x for x, _ in self.pattern) + min_x)//2
        offset_y = size//2 - (max(y for _, y in self.pattern) + min_y)//2
        
        for x, y in self.pattern:
            grid[y + offset_y, x + offset_x] = 1
        return grid
    
    def to_svg(self, cell_size: int = 30) -> str:
        """Generate SVG of the pattern"""
        grid = self.to_grid()
        size = len(grid)
        
        svg = f'''<svg xmlns="http://www.w3.org/2000/svg"
                     viewBox="-1.5 -1.5 {size*cell_size + 3} {size*cell_size + 3}"
                     width="{size*cell_size + 3}"
                     height="{size*cell_size + 3}">
        <style>
            .cell {{ fill: black; }}
            .grid {{ stroke: #c0c0c0; stroke-width: 3; }}
        </style>
        <rect width="100%" height="100%" fill="white"/>
        '''
        
        # Draw grid
        for i in range(size + 1):
            svg += f'<line class="grid" x1="{i*cell_size}" y1="0" x2="{i*cell_size}" y2="{size*cell_size}"/>'
            svg += f'<line class="grid" x1="0" y1="{i*cell_size}" x2="{size*cell_size}" y2="{i*cell_size}"/>'
            
        # Draw cells
        for y in range(size):
            for x in range(size):
                if grid[y, x]:
                    svg += f'<rect class="cell" x="{x*cell_size}" y="{y*cell_size}" width="{cell_size}" height="{cell_size}"/>'
        
        svg += '</svg>'
        return svg}

\helpercode{def create_svg_animation(pattern: LifePattern, 
                          steps: int = 20, 
                          cell_size: int = 30, 
                          fps: int = 4) -> str:
    """Create an animated SVG of a Life pattern evolution
    
    Args:
        pattern: LifePattern instance to animate
        steps: Number of evolution steps
        cell_size: Size of each cell in pixels
        fps: Frames per second
    
    Returns:
        SVG string with SMIL animation
    """
    grid = pattern.to_grid()
    size = len(grid)
    duration = steps / fps
    
    # Start SVG with animation container
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg"
                  viewBox="-1.5 -1.5 {size*cell_size + 3} {size*cell_size + 3}"
                  width="{size*cell_size + 3}"
                  height="{size*cell_size + 3}">
        <style>
            .cell {{ fill: black; }}
            .grid {{ stroke: #c0c0c0; stroke-width: 3; }}
        </style>
        <defs>
    '''
    
    # Create all frames as symbols
    frames = []
    current_grid = grid.copy()
    for frame in range(steps):
        symbol_id = f"frame{frame}"
        frames.append(symbol_id)
        
        svg += f'<symbol id="{symbol_id}">'
        # Draw cells for this frame
        for y in range(size):
            for x in range(size):
                if current_grid[y, x]:
                    svg += f'<rect class="cell" x="{x*cell_size}" y="{y*cell_size}" '
                    svg += f'width="{cell_size}" height="{cell_size}"/>'
        svg += '</symbol>'
        
        # Evolve grid for next frame
        current_grid = evolve_life(current_grid)
    
    svg += '</defs>'
    
    # Draw static grid lines
    for i in range(size + 1):
        svg += f'<line class="grid" x1="{i*cell_size}" y1="0" x2="{i*cell_size}" y2="{size*cell_size}"/>'
        svg += f'<line class="grid" x1="0" y1="{i*cell_size}" x2="{size*cell_size}" y2="{i*cell_size}"/>'
    
    # Create use element that will be animated
    svg += '<use id="animation" href="#frame0"/>'
    
    # Add SMIL animation
    svg += f'''<animate 
        xlink:href="#animation"
        attributeName="href"
        values="{';'.join('#' + f for f in frames)}"
        dur="{duration}s"
        repeatCount="indefinite"/>
    </svg>'''
    
    return svg}

\helpercode{def create_animated_pattern_analysis(pattern: LifePattern) -> str:
    """Generate HTML with pattern analysis and animation
    
    Creates a side-by-side view of:
    1. Pattern information
    2. Evolution animation
    3. Grid position tracking
    """
    return f'''<div class="pattern-analysis">
        <div class="info">
            <h3>{pattern.name}</h3>
            <ul>
                <li>Discovered: {pattern.discovery_year} by {pattern.discoverer}</li>
                <li>Period: {pattern.period} steps</li>
                <li>Translation: ({pattern.translation[0]}, {pattern.translation[1]})</li>
            </ul>
        </div>
        <div class="animation">
            {create_svg_animation(pattern)}
        </div>
    </div>
    '''}

\setupcode{from matplotlib import animation
import matplotlib.pyplot as plt
from typing import List}

\helpercode{def generate_pattern_animations(pattern: LifePattern, 
                                steps: int = 20,
                                formats: List[str] = ['svg', 'gif']):
    """Generate pattern animations in multiple formats
    
    Args:
        pattern: LifePattern to animate
        steps: Number of evolution steps
        formats: List of formats to generate ('svg' and/or 'gif')
    """
    base_filename = pattern.name.lower().replace(" ", "-")
    
    if 'svg' in formats:
        # Generate SVG animation
        animation_svg = create_svg_animation(pattern, steps=steps, fps=4)
        svg_filename = mlai.filename_join(f"{base_filename}.svg", 
                                        "\writeDiagramsDir/simulation/")
        with open(svg_filename, 'w') as f:
            f.write(animation_svg)
            
    if 'gif' in formats:
        # Create matplotlib animation
        fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
        grid = pattern.to_grid()
        img = ax.imshow(grid, interpolation='nearest')
        plt.close()
        
        def animate(frame):
            nonlocal grid
            grid = evolve_life(grid)
            img.set_array(grid)
            return [img]
            
        anim = animation.FuncAnimation(fig, animate, 
                                     frames=steps,
                                     interval=200,
                                     blit=True)
        
        gif_filename = mlai.filename_join(f"{base_filename}.gif",
                                        "\writeDiagramsDir/simulation/")
        anim.save(gif_filename)}

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

\notes{The game leads to patterns emerging, some of these patterns are static, but some oscillate in place, with varying periods. Others oscillate, but when they complete their cycle they've translated to a new location, in other words they move. In Life the former are known as [oscillators](https://conwaylife.com/wiki/Oscillator) and the latter as [spaceships](https://conwaylife.com/wiki/Spaceship).}

\subsection{Pattern Analysis}

\notes{Before looking at specific examples, let's understand how these patterns behave. Life patterns can be classified by their periodic behavior and movement:
- *Static patterns* remain unchanged from one generation to the next
- *Oscillators* return to their initial state after a fixed number of generations (their period)
- *Spaceships* combine oscillation with translation, moving across the grid while cycling through their states

Each pattern can be characterized by:
- Its period (how many steps before it repeats)
- Its translation (how far it moves each period)
- Its velocity (translation per period)}

\plotcode{# Generate animations for each pattern
for pattern in [GLIDER, LOAFER, GOSPER_GLIDER_GUN]:
    generate_pattern_animations(pattern, steps=30)}

\notes{\subsection{Loafers and Gliders}}

\notes{John Horton Conway, as the creator of the game of life, could be seen somehow as the god of this small universe. He created the rules. The rules are so simple that in many senses he, and we, are all-knowing in this space. But despite our knowledge, this world can still 'surprise' us. From the simple rules, emergent patterns of behaviour arise. These include static patterns that don't change from one turn to the next. They also include, oscillators, that pulse between different forms across different periods of time. A particular form of oscillator is known as a 'spaceship', this is one that moves across the board as the game evolves. One of the simplest and earliest spaceships to be discovered is known as the glider.}

\newslide{Glider}

\figure{\columns{\aligncenter{*Glider (1969)*}\aligncenter{\includegif{\diagramsDir/simulation/glider}{80%}{}{left}}}{\includejpg{\diagramsDir/maths/John-Conway}{80%}{}{right}}{45%}{45%}}{*Left* A Glider pattern discovered 1969 by Richard K. Guy. *Right*. John Horton Conway, creator of *Life* (1937-2020). The glider is an oscillator that moves diagonally after creation. From the simple rules of Life it's not obvious that such an object does exist, until you do the necessary computation.}{glider-loafer-conway}

\notes{The glider was 'discovered' in 1969 by Richard K. Guy. What do we mean by discovered in this context? Well, as soon as the game of life is defined, objects such as the glider do somehow exist, but the many configurations of the game mean that it takes some time for us to see one and know it exists. This means, that despite being the creator, Conway, and despite the rules of the game being simple, and despite the rules being deterministic, we are not 'omniscient' in any simplistic sense. It requires computation to 'discover' what can exist in this universe once it's been defined.} 

\newslide{}

\figure{\includegif{\diagramsDir/simulation/gosper-glider-gun}{80%}}{The Gosper glider gun is a configuration that creates gliders. A new glider is released after every 30 turns.}{gosper-glider-gun}

\notes{These patterns had to be discovered, in the same way that a scientist might discover a disease, or an explorer a new land. For example, the Gosper glider gun was [discovered by Bill Gosper in 1970](https://conwaylife.com/wiki/Bill_Gosper). It is a pattern that creates a new glider every 30 turns of the game.}

\newslide{Loafer}

\notes{Despite widespread interest in Life, some of its patterns were only very recently discovered like the Loafer, discovered in 2013 by Josh Ball. So, despite the game having existed for over forty years, and the rules of the game being simple, there are emergent behaviors that are unknown.}

\newslide{}

\figure{\columns{\aligncenter{*Loafer (2013)*}\aligncenter{\includegif{\diagramsDir/simulation/loafer}{80%}{}{left}}}{\includejpg{\diagramsDir/maths/John-Conway}{80%}{}{right}}{45%}{45%}}{*Left* A Loafer pattern discovered by Josh Ball in 2013. *Right*. John Horton Conway, creator of *Life* (1937-2020).}{the-loafer-spaceship}

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

\displaycode{# Generate both static and animated versions of patterns
for pattern in [GLIDER, LOAFER, GOSPER_GLIDER_GUN]:
    # Generate static SVG
    svg = pattern.to_svg()
    filename = mlai.filename_join(f"{pattern.name.lower()}-pattern.svg", 
                                "\writeDiagramsDir/simulation/")
    with open(filename, 'w') as f:
        f.write(svg)
        
    # Generate animations
    generate_pattern_animations(pattern, steps=30, formats=['svg', 'gif'])}

\notes{The game leads to patterns emerging, some of these patterns are static, but some oscillate in place, with varying periods. Others oscillate, but when they complete their cycle they've translated to a new location, in other words they move. In Life the former are known as [oscillators](https://conwaylife.com/wiki/Oscillator) and the latter as [spaceships](https://conwaylife.com/wiki/Spaceship).}

subsection{Pattern Analysis}

\notes{Before looking at specific examples, let's understand how these patterns behave. Life patterns can be classified by their periodic behavior and movement:
- *Static patterns* remain unchanged from one generation to the next
- *Oscillators* return to their initial state after a fixed number of generations (their period)
- *Spaceships* combine oscillation with translation, moving across the grid while cycling through their states

Each pattern can be characterized by:
- Its period (how many steps before it repeats)
- Its translation (how far it moves each period)
- Its velocity (translation per period)}

\displaycode{# Show analysis of Glider pattern
print(create_animated_pattern_analysis(GLIDER))}


\notes{\subsection{Loafers and Gliders}}

\notes{John Horton Conway, as the creator of the game of life, could be seen somehow as the god of this small universe. He created the rules. The rules are so simple that in many senses he, and we, are all-knowing in this space. But despite our knowledge, this world can still 'surprise' us. From the simple rules, emergent patterns of behaviour arise. These include static patterns that don't change from one turn to the next. They also include, oscillators, that pulse between different forms across different periods of time. A particular form of oscillator is known as a 'spaceship', this is one that moves across the board as the game evolves. One of the simplest and earliest spaceships to be discovered is known as the glider.}

\newslide{Pattern Analysis}

\notes{We can verify these patterns computationally. For example, the Glider has a period of 4 steps before repeating, but translates diagonally by one cell in each direction. The Loafer has a period of 7 steps and moves horizontally by one cell each period.}

\newslide{Glider}

\figure{\columns{\aligncenter{*Glider (1969)*}\aligncenter{\includegif{\diagramsDir/simulation/Glider}{80%}{}{left}}}{\includejpg{\diagramsDir/maths/John-Conway}{80%}{}{right}}{45%}{45%}}{*Left* A Glider pattern discovered 1969 by Richard K. Guy. *Right*. John Horton Conway, creator of *Life* (1937-2020). The glider is an oscillator that moves diagonally after creation. From the simple rules of Life it's not obvious that such an object does exist, until you do the necessary computation.}{glider-loafer-conway}

\notes{The glider was 'discovered' in 1969 by Richard K. Guy. What do we mean by discovered in this context? Well, as soon as the game of life is defined, objects such as the glider do somehow exist, but the many configurations of the game mean that it takes some time for us to see one and know it exists. This means, that despite being the creator, Conway, and despite the rules of the game being simple, and despite the rules being deterministic, we are not 'omniscient' in any simplistic sense. It requires computation to 'discover' what can exist in this universe once it's been defined.} 


\newslide{}
\notes{}

\figure{\includegif{\diagramsDir/simulation/Gosperglidergun}{80%}}{The Gosper glider gun is a configuration that creates gliders. A new glider is released after every 30 turns.}{gosper-glider-gun}

\notes{These patterns had to be discovered, in the same way that a scientist might discover a disease, or an explorer a new land. For example, the Gosper glider gun was [discovered by Bill Gosper in 1970](https://conwaylife.com/wiki/Bill_Gosper). It is a pattern that creates a new glider every 30 turns of the game.}


\newslide{Loafer}

\notes{Despite widespread interest in Life, some of its patterns were only very recently discovered like the Loafer, discovered in 2013 by Josh Ball. So, despite the game having existed for over forty years, and the rules of the game being simple, there are emergent behaviors that are unknown.}

\newslide{}

\figure{\columns{\aligncenter{*Loafer (2013)*}\aligncenter{\includegif{\diagramsDir/simulation/Loafer}{80%}{}{left}}}{\includejpg{\diagramsDir/maths/John-Conway}{80%}{}{right}}{45%}{45%}}{*Left* A Loafer pattern discovered by Josh Ball in 2013. *Right*. John Horton Conway, creator of *Life* (1937-2020).}{the-loafer-spaceship}

\endif

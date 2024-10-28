\ifndef{automataDiagrams}
\define{automataDiagrams}

\editme

\setuphelpercode{import numpy as np
from typing import List, Tuple, Dict, Optional}

\helpercode{def generate_life_rule_diagram(rule_type: str) -> str:
    """Generate SVG visualization of Game of Life rules matching original diagrams
    
    Args:
        rule_type: One of 'loneliness-before', 'loneliness-after',
                  'overcrowding-before', 'overcrowding-after',
                  'birth-before', 'birth-after'
    """
    # Rule configurations - (x,y) coordinates of filled cells
    configs = {
        'loneliness-before': [(0,0), (2,0), (1,1)],  # 2 neighbors
        'loneliness-after': [(0,0), (2,0)],  # Cell dies
        'overcrowding-before': [(0,0), (2,0), (2,1), (2,2), (1,1)],  # 4 neighbors
        'overcrowding-after': [(0,0), (2,0), (2,1), (2,2)],  # Cell dies
        'birth-before': [(0,0), (2,0), (2,2)],  # 3 neighbors
        'birth-after': [(0,0), (2,0), (2,2), (1,1)]  # New cell born
    }
    
    cell_size = 30
    
    # SVG setup with original viewBox and background
    svg = f'''<svg
    xmlns="http://www.w3.org/2000/svg"
    viewBox="-20 -20 130 130"
    width="130"
    height="130">
<rect width="130" height="130" x="-20" y="-20" fill="#fff"/>
'''
    
    # Draw filled cells
    for x, y in configs[rule_type]:
        svg += f'<rect width="{cell_size}" height="{cell_size}" '
        svg += f'x="{x*cell_size}" y="{y*cell_size}" fill="#000"/>\n'
    
    # Draw vertical grid lines
    for i in range(4):
        x = i * cell_size
        svg += f'<line x1="{x}" y1="-20" x2="{x}" y2="110" '
        svg += f'stroke="#c0c0c0" stroke-width="3"/>\n'
    
    # Draw horizontal grid lines
    for i in range(4):
        y = i * cell_size
        svg += f'<line x1="-20" y1="{y}" x2="110" y2="{y}" '
        svg += f'stroke="#c0c0c0" stroke-width="3"/>\n'
    
    # Draw red highlight box around center cell
    fill = "none" if "after" in rule_type else "#000"
    svg += f'<rect width="{cell_size}" height="{cell_size}" '
    svg += f'x="{cell_size}" y="{cell_size}" stroke="red" '
    svg += f'stroke-width="3" fill="{fill}"/>\n'
    
    svg += '</svg>'
    return svg}

\helpercode{def get_neighborhood_state(left: int, center: int, right: int) -> int:
    """Convert three cells into their neighborhood state index (0-7)
    
    Args:
        left: State of left cell (0 or 1)
        center: State of center cell (0 or 1)
        right: State of right cell (0 or 1)
        
    Returns:
        Integer from 0-7 representing the neighborhood state
    """
    return (left << 2) | (center << 1) | right}


\helpercode{def generate_wolfram_rule_markdown_table(rule_number: int) -> str:
    """Generate a Markdown table explaining a cellular automaton rule
    
    Args:
        rule_number: Integer from 0-255 specifying the rule
        
    Returns:
        Markdown formatted table explaining the rule
    """
    rule_binary = format(rule_number, '08b')
    
    # Create table header
    table = "| Pattern | Result | Binary Position | Rule Bit |\n"
    table += "|---------|---------|----------------|----------|\n"
    
    # Create patterns
    neighborhoods = [
        (1,1,1), (1,1,0), (1,0,1), (1,0,0),
        (0,1,1), (0,1,0), (0,0,1), (0,0,0)
    ]
    
    # Add each row
    for i, pattern in enumerate(neighborhoods):
        pattern_str = ''.join(['■' if x == 1 else '□' for x in pattern])
        result = '■' if rule_binary[i] == '1' else '□'
        table += f"| {pattern_str} | {result} | {7-i} | {rule_binary[i]} |\n"
    
    return table}

\helpercode{def generate_wolfram_rule_diagram(rule_number: int) -> str:
    """Generate SVG visualization explaining a Wolfram rule
    
    Args:
        rule_number: Rule number (0-255) to visualize
    """
    cell_size = 30
    pattern_width = 3 * cell_size
    pattern_height = cell_size
    total_width = 8 * (pattern_width + cell_size)
    total_height = 3 * pattern_height
    
    rule_binary = format(rule_number, '08b')
    neighborhoods = [
        (1,1,1), (1,1,0), (1,0,1), (1,0,0),
        (0,1,1), (0,1,0), (0,0,1), (0,0,0)
    ]
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" 
              viewBox="0 0 {total_width} {total_height}">
    <style>
        .label {{ font: bold {cell_size//2}px sans-serif; }}
    </style>
    '''
    
    # Draw each neighborhood and result
    for i, neighborhood in enumerate(neighborhoods):
        x_offset = i * (pattern_width + cell_size)
        
        # Draw input pattern
        for j, cell in enumerate(neighborhood):
            x = x_offset + j * cell_size
            fill = "black" if cell else "white"
            svg += f'<rect x="{x}" y="0" width="{cell_size}" height="{cell_size}" '
            svg += f'fill="{fill}" stroke="gray"/>'
        
        # Draw arrow
        svg += f'''<line x1="{x_offset + pattern_width//2}" 
                       y1="{pattern_height + 5}" 
                       x2="{x_offset + pattern_width//2}" 
                       y2="{2*pattern_height - 5}" 
                       stroke="black" 
                       marker-end="url(#arrowhead)"/>'''
        
        # Draw result
        result = int(rule_binary[i])
        x = x_offset + cell_size
        y = 2 * pattern_height
        fill = "black" if result else "white"
        svg += f'<rect x="{x}" y="{y}" width="{cell_size}" height="{cell_size}" '
        svg += f'fill="{fill}" stroke="gray"/>'
        
        # Add binary value label
        svg += f'<text x="{x_offset + pattern_width//2}" '
        svg += f'y="{total_height + cell_size//2}" '
        svg += f'text-anchor="middle" class="label">{rule_binary[i]}</text>'
    
    # Add arrowhead definition
    svg += '''
    <defs>
        <marker id="arrowhead" markerWidth="10" markerHeight="7" 
                refX="9" refY="3.5" orient="auto">
            <polygon points="0 0, 10 3.5, 0 7" fill="black"/>
        </marker>
    </defs>
    '''
    
    svg += '</svg>'
    return svg}

\notes{These diagram generation functions maintain consistent styling while providing
specialized visualizations for:

1. Wolfram rule definitions and their outcomes
2. Game of Life rules and their effects

They work with the base Grid class but provide custom layouts specific to teaching
and explaining the rules of each system.}

\endif

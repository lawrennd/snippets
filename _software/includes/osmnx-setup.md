\ifndef{osmnxSetup}
\define{osmnxSetup}

\editme

\subsection{OSMnx Setup}

\notes{We start by installing some Python packages. We'll use OSMnx, a Python package that makes it easy to download, model, analyze, and visualize street networks and other spatial data from OpenStreetMap.}

\setupcode{%%capture
%pip install osmnx}

\setupcode{import osmnx as ox
import matplotlib.pyplot as plt
import warnings
import math
warnings.filterwarnings("ignore", category=FutureWarning, module='osmnx')}

\notes{OSMnx provides a powerful interface to OpenStreetMap data, allowing us to programmatically access geographic information that would otherwise require manual browsing of the OpenStreetMap website.}

\notes{https://www.openstreetmap.org/search?query=nyeri}

\endif



\ifndef{osmCodeReuseFynesse}
\define{osmCodeReuseFynesse}

\editme

\subsection{Code Reuse with Fynesse}

\notes{We will be reusing some of the functions we created in the first practical. This demonstrates one of the key principles of data science: building reusable code libraries that can be applied across multiple projects.

\setupcode{%%capture
%pip install osmnx}

\codeassignment{Install your Fyness library, and run code to show its available.}{!git clone https://github.com/YOUR_USERNAME/fynesse_YOUR_PROJECT.git
import os, subprocess, importlib, sys
sys.path.append("/content/fynesse_YOUR_PROJECT")
import fynesse}

\code{# Example: Plot a city map using your reusable function
# fynesse.access.plot_city_map('Nyeri, Kenya', -0.4371, 36.9580, 2)}

\endif

\endif

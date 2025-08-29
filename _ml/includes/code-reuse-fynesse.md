\ifndef{codeReuseFynesse}
\define{codeReuseFynesse}

\editme

\subsection{Code Reuse with Fynesse}

\notes{We will be reusing some of the functions we created in the first practical. This demonstrates one of the key principles of data science: building reusable code libraries that can be applied across multiple projects.

The Fynesse library you created in Practical 1 implemented the Access-Assess-Address framework with geospatial functionality. Now we'll use it as a foundation for more advanced analysis.}

\setupcode{%%capture
%pip install osmnx
!git clone https://github.com/YOUR_USERNAME/fynesse_YOUR_PROJECT.git
import os, subprocess, importlib, sys
sys.path.append("/content/fynesse_YOUR_PROJECT")
import fynesse}

\notes{Test that your library works by using one of the functions you created:}

\code{# Example: Plot a city map using your reusable function
# fynesse.access.plot_city_map('Nyeri, Kenya', -0.4371, 36.9580, 2)}

\notes{This approach to code reuse is fundamental to efficient data science workflows. By packaging commonly used functionality into libraries, we can focus on the novel aspects of each analysis rather than reimplementing basic operations.}

\endif

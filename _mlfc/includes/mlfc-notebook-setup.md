\ifndef{mlfcNotebookSetup}
\define{mlfcNotebookSetup}

\editme

\subsection{ML Foundations Course Notebook Setup}

\notes{We install some bespoke codes for creating and saving plots as well as loading data sets.}

\setupcode{%%capture
%pip install notutils
%pip install pods
%pip install mlai}

\setupcode{import notutils
import pods
import mlai
import mlai.plot as plot}

\include{_notebooks/includes/plot-setup.md}

\endif

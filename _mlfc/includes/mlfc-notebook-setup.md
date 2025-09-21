\ifndef{mlfcNotebookSetup}
\define{mlfcNotebookSetup}

\editme

\subsection{ML Foundations Course Notebook Setup}

\notes{We install some bespoke codes for creating and saving plots as well as loading data sets.}

\setupcode{%%capture
%pip install notutils
%pip install git+https://github.com/lawrennd/ods.git
%pip install git+https://github.com/lawrennd/mlai.git}

\define{podsSoftware}
\define{notutilsSoftware}
\define{mlaiSoftware}

\setupcode{import notutils
import pods
import mlai
import mlai.plot as plot}

\include{_notebooks/includes/plot-setup.md}

\endif

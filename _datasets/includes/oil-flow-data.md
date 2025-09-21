\ifndef{oilFlowData}
\define{oilFlowData}

\editme

\comment{\subsection{Oil Data}

\begin{frame}
  \frametitle{Oil Data}
  \begin{columns}
    \column{0.4\textwidth}
    \begin{itemize}
    \item Simulated measurements from an oil pipeline {\footnotesize \citep{Bishop:oil93}}.
    \item Pipleline contains oil, water and gas.
    \item Three phases of flow in pipeline---homogeneous, stratified and annular.
    \item <2->Gamma densitometry sensors arranged in a configuration around
      pipeline.
    \end{itemize}

    \column{0.3\textwidth}

    \begin{center}
      % 
      \begin{minipage}[b][0.8\textheight][t]{0.5\columnwidth}%
        % 
        \begin{minipage}[t][0.3\textheight]{1\columnwidth}%
          \begin{center}
            Homogeneous
          \end{center}%
        \end{minipage}\\
        % 
        \begin{minipage}[t][0.3\textheight]{1\columnwidth}%
          \begin{center}
            Stratified
          \end{center}%
        \end{minipage}\\
        % 
        \begin{minipage}[t][0.3\textheight]{1\columnwidth}%
          \begin{center}
            Annular
          \end{center}%
        \end{minipage}%
      \end{minipage}
      \end{center}
  \column{0.2\textwidth}
  \begin{center}
    \includegraphics<1>[height=0.8\textheight]{../../../dimred/tex/diagrams/oilData}
    \includegraphics<2>[height=0.8\textheight]{../../../dimred/tex/diagrams/oilDataSensors}
  \end{center}
  \end{columns}
\end{frame}

\begin{frame}[fragile]
  \frametitle{Oil Data}
  \begin{itemize}
  \item 12 simulated measurements of oil flow in a pipe.
  \item Nature of flow is dependent on relative proportion of oil, water and
    gas.
  \end{itemize}
}
\subsection{Oil Flow Data}

\notes{This data set is from a physics-based simulation of oil flow in a pipeline. The data was generated as part of a project to determine the fraction of oil, water and gas in North Sea oil pipes [@Bishop:gtm96].}

\setupcode{import pods}

\code{data = pods.datasets.oil()}

\notes{The data consists of 1000 12-dimensional observations of simulated oil flow in a pipeline. Each observation is labelled according to the multi-phase flow configuration (homogeneous, annular or laminar).}

\code{# Convert data["Y"] from [1, -1, -1] in each row to rows of 0 or 1 or 2
Y = data["Y"]
# Find rows with 1 in first column (class 0)
class0 = (Y[:, 0] == 1).astype(int) * 0
# Find rows with 1 in second column (class 1) 
class1 = (Y[:, 1] == 1).astype(int) * 1
# Find rows with 1 in third column (class 2)
class2 = (Y[:, 2] == 1).astype(int) * 2
# Combine into single array of class labels 0,1,2
labels = class0 + class1 + class2}

\notes{The data is returned as a dictionary containing training and test inputs ('X', 'Xtst'), training and test labels ('Y', 'Ytst'), and the names of the features.}


\setupplotcode{import matplotlib.pyplot as plt
import mlai.plot as plot
import mlai
import numpy as np}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
# Plot first two dimensions of the data
classes = np.unique(labels)
colors = ['r', 'g', 'b']
for i, cls in enumerate(classes):
    idx = data['Y'] == cls
    ax.plot(data['X'][idx, 0], data['X'][idx, 1], colors[i] + '.', 
            markersize=10, label=f'Class {cls}')
ax.set_xlabel('1st dimension')
ax.set_ylabel('2nd dimension')
ax.legend()

mlai.write_figure('oil-flow-data.svg', directory='\writeDiagramsDir/datasets')}

\figure{\includediagram{\diagramsDir/datasets/oil-flow-data}{80%}}{Visualization of the first two dimensions of the oil flow data from @Bishop-oil93}{oil-flow-data}

\notes{As normal we include the citation information for the data.}

\code{print(data['citation'])}

\notes{And extra information about the data is included, as standard, under the keys `info` and `details`.}

\code{print(data['details'])}

\code{X = data['X']
Y = data['Y']}
\endif

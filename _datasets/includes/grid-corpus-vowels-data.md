\ifndef{gridCorpusVowelsData}
\define{gridCorpusVowelsData}

\editme

\comment{

    \item Grid corpus data modeled for synthesis by Jon Barker.
    \item 33 context dependent vowel phones from 34 (mixed male/female) subjects.
    \item Means and variances of synthesis HMM for subjects {\scriptsize \citep{Shichiri:eigenvoices02}}.
    \end{itemize}
    \column{0.45\textwidth}

    \begin{center}
      % 
      \begin{minipage}[b][0.8\textheight][t]{0.5\columnwidth}%
        % 
        \begin{minipage}[c][0.3\textheight]{1\columnwidth}%
          \begin{center}
            34 Subjects'
          \end{center}%
        \end{minipage}\\
        % 
        \begin{minipage}[c][0.3\textheight]{1\columnwidth}%
          \begin{center}
            Vowel
          \end{center}%
        \end{minipage}\\
        % 
        \begin{minipage}[c][0.3\textheight]{1\columnwidth}%
          \begin{center}
            Phones 
          \end{center}
        \end{minipage}
      \end{minipage}\movie[loop]{%
        \begin{minipage}[b][0.8\textheight][t]{0.5\columnwidth}%
          % 
          \begin{minipage}[t][0.3\textheight]{1\columnwidth}%
            \begin{center}
              \includegraphics[height=0.2\textheight]{../../../dimred/tex/diagrams/gridCorpusNl}
            \end{center}%
          \end{minipage}\\
          % 
          \begin{minipage}[t][0.3\textheight]{1\columnwidth}%
            \begin{center}
              \includegraphics[height=0.2\textheight]{../../../dimred/tex/diagrams/gridCorpusMc}
            \end{center}%
          \end{minipage}\\
          % 
          \begin{minipage}[t][0.3\textheight]{1\columnwidth}%
            \begin{center}
              \includegraphics[height=0.2\textheight]{../../../dimred/tex/diagrams/gridCorpusJb}
            \end{center}%
          \end{minipage}%
        \end{minipage}}{/home/neil/aaron/urtasun_cvpr06_tracking.avi}
    \end{center}
    
  \end{columns}
  
\end{frame}

\begin{frame}[fragile]
  \frametitle{Grid Corpus Vowels}
  \begin{itemize}
    \item Grid Corpus: \url{http://www.dcs.shef.ac.uk/spandh/gridcorpus/}.
    \item For each context dependent phone: 5 state HMM, one Gaussian component
      per state. 25 MFCC channels, with deltas and accelerations. 
%$5 \times
 %     25 \times 3=375$ means per phone and 375 variances. 750 features
%      per phone, $750\times 33=24,750$ features per individual.
  \end{itemize}
  \begin{center}
    % 
  \begin{figure}
}
\subsection{Grid Corpus Vowels Data}

\notes{This data set collection is from an classic early microarray paper on the yeast cell cycle [@Spellman:yeastcellcy98].}


\setupcode{import pods}

\code{data = pods.datasets.grid_corpous_vowels()}

\notes{}


\code{data['Y'].describe()}

\notes{}

\code{print(data['Y'].columns)}

\notes{}


\code{print(data['Y'].index)}


\setupplotcode{import matplotlib.pyplot as plt
import mlai.plot as plot
import mlai}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
ax.plot()
ax.set_xlabel()
ax.set_ylabel()

mlai.write_figure('grid-corpos-vowels-data.svg', directory='\writeDiagramsDir/datasets')}

\figure{\includediagram{\diagramsDir/datasets/grid-corpus-vowels-data}{80%}}{}{grid-corpus-vowels-data}

\notes{As normal we include the citation information for the data.}


\code{print(data['citation'])}

\notes{And extra information about the data is included, as standard, under the keys `info` and `details`.}


\code{print(data['info'])
print()
print(data['details'])}

\endif

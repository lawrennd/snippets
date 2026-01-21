\ifndef{osuRun1Data}
\define{osuRun1Data}

\editme

\comments{\subsection{Stick Man Data}

\begin{frame}
  \frametitle{Stick Man Data}
  \begin{columns}
    \column{0.55\textwidth}
    \begin{itemize}
    \item $\numData=55$ frames of motion capture.
    \item $xyz$ locations of 34 points on the body.
    \item $\dataDim=102$ dimensional data.
    \item ``Run 1'' available from \url{http://accad.osu.edu/research/mocap/mocap_data.htm}.
    \end{itemize}

    \column{0.45\textwidth}

    \begin{center}
      % 
      \begin{minipage}[b][0.8\textheight][t]{0.5\columnwidth}%
        % 
        \begin{minipage}[c][0.3\textheight]{1\columnwidth}%
          \begin{center}
            Changing
          \end{center}%
        \end{minipage}\\
        % 
        \begin{minipage}[c][0.3\textheight]{1\columnwidth}%
          \begin{center}
            Angle
            \end{center}%
        \end{minipage}\\
        % 
        \begin{minipage}[c][0.3\textheight]{1\columnwidth}%
          \begin{center}
            of Run
            \end{center}%
        \end{minipage}%
      \end{minipage}\movie[loop]{%
        \begin{minipage}[b][0.8\textheight][t]{0.5\columnwidth}%
          % 
          \begin{minipage}[t][0.3\textheight]{1\columnwidth}%
            \begin{center}
              \includegraphics[height=0.2\textheight]{../../../fgplvm/tex/diagrams/demStick3Angle1}
            \end{center}%
          \end{minipage}\\
          % 
          \begin{minipage}[t][0.3\textheight]{1\columnwidth}%
            \begin{center}
              \includegraphics[height=0.2\textheight]{../../../fgplvm/tex/diagrams/demStick3Angle2}
            \end{center}%
          \end{minipage}\\
          % 
          \begin{minipage}[t][0.3\textheight]{1\columnwidth}%
            \begin{center}
              \includegraphics[height=0.2\textheight]{../../../fgplvm/tex/diagrams/demStick3Angle3}
            \end{center}%
          \end{minipage}%
        \end{minipage}}{/home/neil/aaron/urtasun_cvpr06_tracking.avi}
    \end{center}
    
  \end{columns}

\end{frame}
}
\subsection{OSU Motion Capture Data: Run 1}

\notes{Motion capture data the Open Motion Data Project by The Ohio State University Advanced Computing Center for the Arts and Design. Historically the data website was found here <http://accad.osu.edu/research/mocap/mocap_data.htm>, although it is now missing. The centre website is here: <https://accad.osu.edu>.}

\setupcode{import pods}

\notes{You can download different data from the site, here we download the 'run1' motion.}

\code{data = pods.datasets.osu_run1()}

\notes{The data dictionary contains the keys 'Y' and 'connect', which represent the data and connections that can be used to create the skeleton.}

\code{data['Y'].shape}

\notes{The data has often been used in talks demonstrating GP-LVM models and comparing variants such as back constrained and temporal models.}

\code{print(data['citation'])}

\notes{And extra information about the data is included, as standard, under the keys under `details`.}


\code{print(data['details'])}
\endif

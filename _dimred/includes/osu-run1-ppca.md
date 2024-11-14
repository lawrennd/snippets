\ifndef{osuRun1Ppca}
\define{osuRun1Ppca}

\editme

\subsection{Examples: Motion Capture Data}

\include{_datasets/includes/osu-run1-data.md}

\notes{Once the data is loaded in we can examine the first two principal components as follows,}

\code{q = 2
U, ell, sigma2 = ppca(Y, q)
mu_x, C_x = posterior(Y, U, ell, sigma2)}

\setupplotcode{import matplotlib.pyplot as plt
import mlai}
\plotcode{plt.plot(mu_x[:, 0], mu_x[:, 1], 'rx-')
mlai.write_figure("dem_osu_run1.svg", directory="\writeDiagramsDir/dimred/")
}

\figure{\includediagram{\diagramsDir/dimred/dem_osu_run1}{70%}}{First two principal components of motion capture data of an individual running.}{dem-osu-run1}

\notes{Here because the data is a time course, we have connected points that are
neighbouring in time. This highlights the form of the run, which involves 3
paces. This projects in our low dimensional space to 3 loops. We can examin how
much residual variance there is in the system by looking at `sigma2`.}

\code{print(sigma2)}

\endif

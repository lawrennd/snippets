\ifndef{oilFlowSklearnPca}
\define{oilFlowSklearnPca}

\editme

\subsection{Scikit-learn implementation PCA}

\notes{We've implemented PCA as part of supporting the learning process, but in practice we can use the `scikit-learn` implementation. Let's try it on the oil flow data.}

\include{_datasets/includes/oil-flow-data.md}


\installcode{scikit-learn}

\setupcode{from sklearn.decomposition import PCA}
\code{pca = PCA(n_components=2)
pca.fit(X)
X_pca = pca.transform(X)}

\setupplotcode{from matplotlib import pyplot as plt
import mlai
from mlai import plot}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_figsize)
# Three labels stored in Y
labels = ["homogeneous", "annular", "stratified"]
for i in range(3):
    ax.scatter(X_pca[y==i, 0], X_pca[y==i, 1], label=f'Label {i}')
ax.set_xlabel('First principal component')
ax.set_ylabel('Second principal component')
ax.legend()

plot.write_figure("oil-flow-pca-sklearn", directory='\writeDiagramsDir/dimred')}

\figure{\includegraphics[width=0.5\textwidth]{\diagramsDir/dimred/oil-flow-pca_sklearn.svg}}{PCA of the oil flow data.}{oil-flow-pca-sklearn}

\endif
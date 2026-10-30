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
class_names = ["homogeneous", "annular", "stratified"]
for i, name in enumerate(class_names):
    ax.scatter(X_pca[labels==i, 0], X_pca[labels==i, 1], label=name)
ax.set_xlabel('First principal component')
ax.set_ylabel('Second principal component')

mlai.write_figure("oil-flow-pca-sklearn.svg", directory='\writeDiagramsDir/dimred')}

\figure{\includediagram{\diagramsDir/dimred/oil-flow-pca_sklearn}{60%}}{PCA of the oil flow data. The flow is homogeneous, annular and stratified.}{oil-flow-pca-sklearn}

\endif

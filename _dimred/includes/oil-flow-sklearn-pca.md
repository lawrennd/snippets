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

\code{# Find rows with 1 in first column (class 0)
class0 = (Y[:, 0] == 1).astype(int) * 0
# Find rows with 1 in second column (class 1) 
class1 = (Y[:, 1] == 1).astype(int) * 1
# Find rows with 1 in third column (class 2)
class2 = (Y[:, 2] == 1).astype(int) * 2
# Combine into single array of class labels 0,1,2
lbls = class0 + class1 + class2}
\setupplotcode{from matplotlib import pyplot as plt
import mlai
from mlai import plot}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_figsize)
# Three labels stored in Y
labels = ["homogeneous", "annular", "stratified"]
for i in range(3):
    ax.scatter(X_pca[lbls==i, 0], X_pca[lbls==i, 1], label=f'{labels[i]}')
ax.set_xlabel('First principal component')
ax.set_ylabel('Second principal component')
ax.legend()

mlai.write_figure("oil-flow-pca-sklearn.svg", directory='\writeDiagramsDir/dimred')}

\figure{\includediagram{\diagramsDir/dimred/oil-flow-pca_sklearn}{60%}}{PCA of the oil flow data.}{oil-flow-pca-sklearn}

\endif

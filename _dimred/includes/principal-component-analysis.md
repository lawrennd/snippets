\ifndef{principalComponentAnalysis}
\define{principalComponentAnalysis}

\editme

\subsection{Principal Component Analysis}

\notes{Principal Component Analysis (PCA) is one of the most fundamental and widely used dimensionality reduction techniques. While commonly credited to @Pearson-lines01, who was interested in finding "lines and planes of closest fit to systems of points in space", the method as we will review it today was introduced and *named* by Hotelling (@Hotelling:analysis33). The approach is often used as a way of looking for correlations, but Hotelling's motivation was a principled alternative to Spearman's factor analysis [@Spearman-general04].

Often PCA is introduced as a method for finding directions of maximum variance in high-dimensional data, and this is the interpretation that is due to @Pearson-lines01, but philosophically these approaches arre different even though they turn out to be identical mathematically. In a very real sense "many models lead to the PCA algorithm". But these equivalences are only true when a *linear* interpretation is sought. Nonlinear extensions of these ideas (maximum variance directions, eigenvalue problems, latent variable models) all lead to *different* algorithms. However, since the linear algorithm has so many interpretations it is a wise place to begin analysis.}

\slides{
* PCA (@Hotelling:analysis33) is a linear embedding
* Today its presented as:
  * Rotate to find 'directions' in data with maximal variance
  * How do we find these directions?
}

\notes{The mathematical foundation of PCA relies on analyzing the sample covariance matrix of the data. For a dataset with $\numData$ points, this matrix is given by:}

$$
\mathbf{S}=\frac{1}{\numData}\sum_{i=1}^\numData \left(\dataVector_{i, :}-\meanVector\right)\left(\dataVector_{i, :} - \meanVector\right)^\top
$$

\newslide{Principal Component Analysis}

\slides{
* Find directions in the data, $\latentVector = \mathbf{U}\dataVector$, for which variance is maximized.
}

\notes{The modern interpretation focuses on finding a set of orthogonal directions (principal components) along which the data varies the most, but Hotelling's original formulation was derived from the  idea of latent variables. The optimization problem we solve today, which maximizes the variance along each direction while maintaining orthogonality constraints, arises as the solution of the original latent variable formulation [@Tipping-probpca99].}

\newslide{Lagrangian}
\slides{
* Solution is found via constrained optimisation (which uses [Lagrange multipliers](https://en.wikipedia.org/wiki/Lagrange_multiplier)):
  $$
  L\left(\mathbf{u}_{1},\lambda_{1}\right)=\mathbf{u}_{1}^{\top}\mathbf{S}\mathbf{u}_{1}+\lambda_{1}\left(1-\mathbf{u}_{1}^{\top}\mathbf{u}_{1}\right)
  $$

* Gradient with respect to $\mathbf{u}_{1}$
  $$\frac{\text{d}L\left(\mathbf{u}_{1},\lambda_{1}\right)}{\text{d}\mathbf{u}_{1}}=2\mathbf{S}\mathbf{u}_{1}-2\lambda_{1}\mathbf{u}_{1}$$
  rearrange to form
  $$\mathbf{S}\mathbf{u}_{1}=\lambda_{1}\mathbf{u}_{1}.$$
  Which is known as an [*eigenvalue problem*](https://en.wikipedia.org/wiki/Eigenvalues_and_eigenvectors).
* Further directions that are *orthogonal* to the first can also be shown to be eigenvectors of the covariance.
}

\setupcode{import numpy as np}

\code{# Generate correlated 2D Gaussian samples
num_points = 200
mean = np.array([0, 0])
cov = np.array([[2.0, 1.8], 
                [1.8, 2.0]])
X = np.random.multivariate_normal(mean, cov, num_points)}

\setupplotcode{import matplotlib.pyplot as plt
import mlai.plot as plot}

\helpercode{def pca_plot(ax, X):
    # Compute eigenvalues and eigenvectors of covariance matrix
    eigvals, eigvecs = np.linalg.eigh(np.cov(X.T))
    
    # Plot data points
    ax.scatter(X[:, 0], X[:, 1], alpha=0.5)
    ax.set_xlabel('$x_1$')
    ax.set_ylabel('$x_2$')
    ax.axis('equal')

    mlai.write_figure("pca-directions-000.svg", directory='\writeDiagramsDir/dimred')

    # Plot covariance ellipse
    # Get eigenvalues and eigenvectors of covariance matrix
    eigenvals, eigenvecs = np.linalg.eigh(cov)
    
    # Calculate angle of rotation from largest eigenvector
    angle = np.arctan2(eigenvecs[1,1], eigenvecs[0,1])
    
    # Calculate width and height of ellipse from eigenvalues
    width = 2 * np.sqrt(eigenvals[1])  # 2 std deviations
    height = 2 * np.sqrt(eigenvals[0])
    
    # Create and add ellipse patch
    ellipse = plt.matplotlib.patches.Ellipse(mean, width, height,
                                           angle=angle * 180/np.pi,
                                           facecolor='none',
                                           edgecolor='r',
                                           linestyle='--')
    ax.add_patch(ellipse)
    mlai.write_figure("pca-directions-001.svg", directory='\writeDiagramsDir/dimred')
    
    # Plot principal components
    counter = 1
    for i in [0, 1]:
        counter += 1
        ax.arrow(mean[0], mean[1], 
                eigvecs[0, i]*np.sqrt(eigvals[i]), 
                eigvecs[1, i]*np.sqrt(eigvals[i]),
                head_width=0.1, head_length=0.1, fc='k', ec='k')
        mlai.write_figure(f"pca-directions-{counter:03d}.svg", directory='\writeDiagramsDir/dimred')}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_figsize)
pca_plot(ax, X)}


\setupdisplaycode{import notutils as nu}
\displaycode{nu.display_plots("pca-directions-{counter:0>3}.svg", directory="\writeDiagramsDir/dimred", counter=(0, 3))}

\newslide{PCA directions}

\slides{
  \define{\width}{60%}
  \define{animationName}{pca-directions}
  \startanimation{\animationName}{0}{3}
  \newframe{\includediagram{\diagramsDir/dimred/pca-directions-000}{\width}}{\animationName}
  \newframe{\includediagram{\diagramsDir/dimred/pca-directions-001}{\width}}{\animationName}
  \newframe{\includediagram{\diagramsDir/dimred/pca-directions-002}{\width}}{\animationName}
  \newframe{\includediagram{\diagramsDir/dimred/pca-directions-003}{\width}}{\animationName}
  \endanimation

  *Maximum variance directions are eigenvectors of the covariance matrix*
}

\notes{\figure{\includediagram{\diagramsDir/dimred/pca-directions-003}{\width}}{Illustration of PCA on 2D correlated Gaussian data. The arrows show the principal components (eigenvectors scaled by square root of eigenvalues). The ellipse represents the covariance structure.}{pca-directions-003}}
\endif

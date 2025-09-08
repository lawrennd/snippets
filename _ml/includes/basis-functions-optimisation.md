\ifndef{basisFunctionsOptimisation}
\define{basisFunctionsOptimisation}

\editme


\newslide{Expand the Brackets}
\notes{To minimize this objective, we first expand the brackets as follows,}
\begin{aligned}
  \errorFunction(\mappingVector,\dataStd^2) = &\frac{\numData}{2}\log \dataStd^2 + \frac{1}{2\dataStd^2}\sum_{i=1}^{\numData}\dataScalar_i^{2} \\ & -\frac{1}{\dataStd^2}\sum_{i=1}^{\numData}\dataScalar_i\mappingVector^{\top}\basisVector_i\\ &+\frac{1}{2\dataStd^2}\sum_{i=1}^{\numData}\mappingVector^{\top}\basisVector_i\basisVector_i^{\top}\mappingVector+\text{const}.
\end{aligned}

\newslide{Expand the Brackets}
\notes{Now we pull out the vectors, $\mappingVector$, to highlight that what we have is a multivariate quadratic form in $\mappingVector$.}
\begin{aligned} \errorFunction(\mappingVector, \dataStd^2) = & \frac{\numData}{2}\log \dataStd^2 + \frac{1}{2\dataStd^2}\sum_{i=1}^{\numData}\dataScalar_i^{2} \\ & -\frac{1}{\dataStd^2} \mappingVector^\top\sum_{i=1}^{\numData}\basisVector_i \dataScalar_i\\ & +\frac{1}{2\dataStd^2}\mappingVector^{\top}\left[\sum_{i=1}^{\numData}\basisVector_i\basisVector_i^{\top}\right]\mappingVector+\text{const}.\end{aligned}

\subsection{Design Matrices}

\notes{We like to make use of *design* matrices for our data. Design matrices involve placing the data points into rows of the matrix and data features into the columns of the matrix. By convention, we are referincing a vector with a bold lower case letter, and a matrix with a bold upper case letter. The design matrix is therefore given by}\slides{* Design matrix notation}
  $$
  \basisMatrix = \begin{bmatrix} \mathbf{1} & \inputVector & \inputVector^2\end{bmatrix}
  $$
  so that
  $$
  \basisMatrix \in \Re^{\numData \times \dataDim}.
  $$
  
\subsubsection{Multivariate Derivatives Reminder}

\notes{To find the minimum of the objective function, we need to make use of multivariate calculus. The two results we need from multivariate calculus have the following form.}
\slides{* We will need some multivariate calculus.}
  $$\frac{\text{d}\mathbf{a}^{\top}\mappingVector}{\text{d}\mappingVector}=\mathbf{a}$$
  and
  $$\frac{\text{d}\mappingVector^{\top}\mathbf{A}\mappingVector}{\text{d}\mappingVector}=\left(\mathbf{A}+\mathbf{A}^{\top}\right)\mappingVector$$
  or if $\mathbf{A}$ is symmetric (*i.e.* $\mathbf{A}=\mathbf{A}^{\top}$)
  $$\frac{\text{d}\mappingVector^{\top}\mathbf{A}\mappingVector}{\text{d}\mappingVector}=2\mathbf{A}\mappingVector.$$

\subsection{Differentiate}

\notes{Differentiating with respect to the vector $\mappingVector$ we obtain}\slides{Differentiate wrt $\mappingVector$}
$$\frac{\text{d} E\left(\mappingVector,\dataStd^2 \right)}{\text{d}\mappingVector}=-\frac{1}{\dataStd^2} \sum_{i=1}^{\numData}\basisVector_i\dataScalar_i+\frac{1}{\dataStd^2} \left[\sum_{i=1}^{\numData}\basisVector_i\basisVector_i^{\top}\right]\mappingVector$$
Leading to
$$\mappingVector^{*}=\left[\sum_{i=1}^{\numData}\basisVector_i\basisVector_i^{\top}\right]^{-1}\sum_{i=1}^{\numData}\basisVector_i\dataScalar_i,$$

\newslide{Matrix Notation}

\notes{Rewriting this result in matrix notation we obtain:}
$$
\sum_{i=1}^{\numData}\basisVector_i\basisVector_i^\top = \basisMatrix^\top \basisMatrix$$
$$\sum _{i=1}^{\numData}\basisVector_i\dataScalar_i = \basisMatrix^\top \dataVector
$$

\newslide{Update Equations}
\notes{Setting the derivative to zero we obtain update equations for the parameter vector and the noise variance.}
\slides{* Update for $\mappingVector^{*}$}
  $$
  \mappingVector^{*} = \left(\basisMatrix^\top \basisMatrix\right)^{-1} \basisMatrix^\top \dataVector
  $$
\slides{* The equation for $\left.\dataStd^2\right.^{*}$ may also be found}
  $$
  \left.\dataStd^2\right.^{*}=\frac{\sum_{i=1}^{\numData}\left(\dataScalar_i-\left.\mappingVector^{*}\right.^{\top}\basisVector_i\right)^{2}}{\numData}.
  $$

\newslide{Avoid Direct Inverse}
\notes{In practice we should avoid solving these equations through direct use of the inverse. Instead we solve for $\mappingVector$ in the following linear system.}
\slides{* E.g. Solve for $\mappingVector$}
  $$
  \left(\basisMatrix^\top \basisMatrix\right)\mappingVector = \basisMatrix^\top \dataVector
$$
\notes{Compare this system with *solve for* $\mathbf{x}$ in} 
$$
\mathbf{A}\mathbf{x} = \mathbf{b}.
$$
\notes{For example see the `numpy.linalg.solve` or `torch.linalg.solve`.}
\slides{* See `np.linalg.solve`
* In practice use $\mathbf{Q}\mathbf{R}$ decomposition (see lab class notes).}
\notes{But the correct and more stable approach is to make use of the QR decomposition.}

\ifndef{qrDecompositionRegression}
\include{_ml/includes/qr-decomposition-regression.md}
\else
\notes{Don't forget, the multivariate solution should be computed using QR decomposition.}
\endif

\endif

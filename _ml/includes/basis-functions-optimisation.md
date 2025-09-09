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

\notes{To find the minimum of the objective function, we need to make use of multivariate calculus. The two results we need from multivariate calculus have the following form.
  $$\frac{\text{d}\mathbf{a}^{\top}\mappingVector}{\text{d}\mappingVector}=\mathbf{a}$$
  and
  $$\frac{\text{d}\mappingVector^{\top}\mathbf{A}\mappingVector}{\text{d}\mappingVector}=\left(\mathbf{A}+\mathbf{A}^{\top}\right)\mappingVector$$
  or if $\mathbf{A}$ is symmetric (*i.e.* $\mathbf{A}=\mathbf{A}^{\top}$)
  $$\frac{\text{d}\mappingVector^{\top}\mathbf{A}\mappingVector}{\text{d}\mappingVector}=2\mathbf{A}\mappingVector.$$}

\slides{
  $$\frac{\text{d}\mathbf{a}^{\top}\mappingVector}{\text{d}\mappingVector}=\mathbf{a}$$
  $$\frac{\text{d}\mappingVector^{\top}\mathbf{A}\mappingVector}{\text{d}\mappingVector}=\left(\mathbf{A}+\mathbf{A}^{\top}\right)\mappingVector$$
\centerdiv{or}
  $$\frac{\text{d}\mappingVector^{\top}\mathbf{A}\mappingVector}{\text{d}\mappingVector}=2\mathbf{A}\mappingVector$$
  \centerdiv{for symmetric $\mathbf{A}$.}}

\subsection{Differentiate}

\notes{Differentiating with respect to the vector $\mappingVector$ we obtain
$$\frac{\text{d} E\left(\mappingVector,\dataStd^2 \right)}{\text{d}\mappingVector}=-\frac{1}{\dataStd^2} \sum_{i=1}^{\numData}\basisVector_i\dataScalar_i+\frac{1}{\dataStd^2} \left[\sum_{i=1}^{\numData}\basisVector_i\basisVector_i^{\top}\right]\mappingVector$$
Leading to
$$\left[\sum_{i=1}^{\numData}\basisVector_i\basisVector_i^{\top}\right]\mappingVector^{*}=\sum_{i=1}^{\numData}\basisVector_i\dataScalar_i.$$}

\slides{Differentiate wrt $\mappingVector$
\begin{aligned}
\frac{\text{d} E\left(\mappingVector,\dataStd^2 \right)}{\text{d}\mappingVector}= & -\frac{1}{\dataStd^2} \sum_{i=1}^{\numData}\basisVector_i\dataScalar_i \\ & +\frac{1}{\dataStd^2} \left[\sum_{i=1}^{\numData}\basisVector_i\basisVector_i^{\top}\right]\mappingVector
\end{aligned}}

\newslide{Find Stationar Point}
\slides{* Set to zero leading to
$$\left[\sum_{i=1}^{\numData}\basisVector_i\basisVector_i^{\top}\right]\mappingVector^{*}=\sum_{i=1}^{\numData}\basisVector_i\dataScalar_i.$$}

\newslide{Matrix Notation}

\notes{Rewriting this result in matrix notation we obtain:}
$$
\sum_{i=1}^{\numData}\basisVector_i\basisVector_i^\top = \basisMatrix^\top \basisMatrix$$
$$\sum _{i=1}^{\numData}\basisVector_i\dataScalar_i = \basisMatrix^\top \dataVector
$$

\newslide{Update Equations}
\notes{Setting the derivative to zero we obtain update equations for the parameter vector and the noise variance. First to find $\mappingVector^{*}$ we solve
  $$
  \left(\basisMatrix^\top \basisMatrix\right)  \mappingVector^{*} = \basisMatrix^\top \dataVector
  $$
and the update for $\left.\dataStd^2\right.^*$ is
  $$
  \left.\dataStd^2\right.^{*}=\frac{\sum_{i=1}^{\numData}\left(\dataScalar_i-\left.\mappingVector^{*}\right.^{\top}\basisVector_i\right)^{2}}{\numData}.
  $$}

\slides{* To find $\mappingVector^{*}$ solve
  $$
  \left(\basisMatrix^\top \basisMatrix\right)  \mappingVector^{*} = \basisMatrix^\top \dataVector
  $$
* The equation for $\left.\dataStd^2\right.^{*}$ may also be found
$$
  \left.\dataStd^2\right.^{*}=\frac{\sum_{i=1}^{\numData}\left(\dataScalar_i-\left.\mappingVector^{*}\right.^{\top}\basisVector_i\right)^{2}}{\numData}$$
  }
  
  
\newslide{Avoid Direct Inverse}
\notes{Wee should avoid solving these equations through direct use of the inverse. Instead we solve for $\mappingVector$ in the following linear system.}
\slides{* E.g. Solve for $\mappingVector$}
  $$
  \left(\basisMatrix^\top \basisMatrix\right)\mappingVector = \basisMatrix^\top \dataVector
$$
\notes{Compare this system with *solve for* $\mathbf{x}$ in} 
$$
\mathbf{A}\mathbf{x} = \mathbf{b}.
$$
\notes{For example see the `numpy.linalg.solve` or `torch.linalg.solve`.}
\newslide{Solving}

\slides{* See `np.linalg.solve`
* In practice use $\mathbf{Q}\mathbf{R}$ decomposition (see lab class notes).}
\notes{But the correct and more stable approach is to make use of the QR decomposition.}

\ifndef{qrDecompositionRegression}

\notes{We can now set up the system to solve with QR decomposition.}

\setupcode{import pandas as pd
import mlai}
\code{poly_args = {'num_basis':4, # four basis: 1, x, x^2, x^3
             'data_limits':xlim}
\designVariable = pd.DataFrame(data = mlai.polynomial(x, **poly_args), 
                   columns = [f'$x^{n}$' for n in range(poly_args['num_basis'])])}

\include{_ml/includes/qr-decomposition-regression.md}
\else
\notes{Don't forget, the multivariate solution should be computed using QR decomposition.}
\endif

\endif

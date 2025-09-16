\ifndef{twoDGaussianMaths}
\define{twoDGaussianMaths}
\editme

\subsection{Independent Gaussians}

$$
p(w, h) = p(w)p(h)
$$

\newslide{Independent Gaussians}

\notes{$$
p(w, h) = \frac{1}{\sqrt{2\pi \dataStd_1^2}\sqrt{2\pi\dataStd_2^2}} \exp\left(-\frac{1}{2}\left(\frac{(w-\meanScalar_1)^2}{\dataStd_1^2} + \frac{(h-\meanScalar_2)^2}{\dataStd_2^2}\right)\right)
$$}
\slides{\begin{aligned}
p(w, h) = \frac{1}{\sqrt{2\pi \dataStd_1^2}\sqrt{2\pi\dataStd_2^2}} \exp\left(-&\frac{1}{2}\left(\frac{(w-\meanScalar_1)^2}{\dataStd_1^2} \right. \\ \left. +& \frac{(h-\meanScalar_2)^2}{\dataStd_2^2}\right)\right)
\end{aligned}}


\newslide{Independent Gaussians}

\slidesmall{
$$
p(w, h) = \frac{1}{\sqrt{2\pi\dataStd_1^22\pi\dataStd_2^2}} \exp\left(-\frac{1}{2}\left(\begin{bmatrix}w \\ h\end{bmatrix} - \begin{bmatrix}\meanScalar_1 \\ \meanScalar_2\end{bmatrix}\right)^\top\begin{bmatrix}\dataStd_1^2& 0\\0&\dataStd_2^2\end{bmatrix}^{-1}\left(\begin{bmatrix}w \\ h\end{bmatrix} - \begin{bmatrix}\meanScalar_1 \\ \meanScalar_2\end{bmatrix}\right)\right)
$$
}

\newslide{Independent Gaussians}

$$
p(\dataVector) = \frac{1}{\det{2\pi \mathbf{D}}^{\frac{1}{2}}} \exp\left(-\frac{1}{2}(\dataVector - \meanVector)^\top\mathbf{D}^{-1}(\dataVector - \meanVector)\right)
$$

\subsection{Correlated Gaussian}

\notes{Form correlated from original by rotating the data space using matrix
$\rotationMatrix$.}

\slidesmall{$$
p(\dataVector) = \frac{1}{\det{2\pi\mathbf{D}}^{\frac{1}{2}}} \exp\left(-\frac{1}{2}(\dataVector - \meanVector)^\top\mathbf{D}^{-1}(\dataVector - \meanVector)\right)
$$}

\newslide{Correlated Gaussian}

\slidesmall{$$
p(\dataVector) = \frac{1}{\det{2\pi\mathbf{D}}^{\frac{1}{2}}} \exp\left(-\frac{1}{2}(\rotationMatrix^\top\dataVector - \rotationMatrix^\top\meanVector)^\top\mathbf{D}^{-1}(\rotationMatrix^\top\dataVector - \rotationMatrix^\top\meanVector)\right)
$$}

\newslide{Correlated Gaussian}

\slidesmall{$$
p(\dataVector) = \frac{1}{\det{2\pi\mathbf{D}}^{\frac{1}{2}}} \exp\left(-\frac{1}{2}(\dataVector - \meanVector)^\top\rotationMatrix\mathbf{D}^{-1}\rotationMatrix^\top(\dataVector - \meanVector)\right)
$$}
\notes{this gives an inverse covariance matrix:}
$$
\covarianceMatrix^{-1} = \rotationMatrix \mathbf{D}^{-1} \rotationMatrix^\top
$$

\newslide{Correlated Gaussian}

\slidesmall{$$
p(\dataVector) = \frac{1}{\det{2\pi\covarianceMatrix}^{\frac{1}{2}}} \exp\left(-\frac{1}{2}(\dataVector - \meanVector)^\top\covarianceMatrix^{-1} (\dataVector - \meanVector)\right)
$$}
$$
\covarianceMatrix = \rotationMatrix \mathbf{D} \rotationMatrix^\top
$$
\endif

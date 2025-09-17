\ifndef{gpOptimize}
\define{gpOptimize}
\editme

\subsection{Learning Covariance Parameters}

Can we determine covariance parameters from the data?

\newslide{}

$$
\gaussianDist{\dataVector}{\mathbf{0}}{\kernelMatrix}=\frac{1}{(2\pi)^\frac{\numData}{2}{\det{\kernelMatrix}^{\frac{1}{2}}}}{\exp\left(-\frac{\dataVector^{\top}\kernelMatrix^{-1}\dataVector}{2}\right)}
$$

\newslide{}

$$
\begin{aligned}
    \gaussianDist{\dataVector}{\mathbf{0}}{\kernelMatrix}=\frac{1}{(2\pi)^\frac{\numData}{2}\color{\blueColor}{\det{\kernelMatrix}^{\frac{1}{2}}}}\color{\redColor}{\exp\left(-\frac{\dataVector^{\top}\kernelMatrix^{-1}\dataVector}{2}\right)}
\end{aligned}
$$ 

\newslide{}

$$
\begin{aligned}
    \log \gaussianDist{\dataVector}{\mathbf{0}}{\kernelMatrix}=&\color{\blueColor}{-\frac{1}{2}\log\det{\kernelMatrix}}\color{\redColor}{-\frac{\dataVector^{\top}\kernelMatrix^{-1}\dataVector}{2}} \\ &-\frac{\numData}{2}\log2\pi
\end{aligned}
$$ 

$$
\errorFunction(\parameterVector) = \color{\blueColor}{\frac{1}{2}\log\det{\kernelMatrix}} + \color{\redColor}{\frac{\dataVector^{\top}\kernelMatrix^{-1}\dataVector}{2}}
$$


\include{_gp/includes/gp-optimize-capacity.md}
\include{_gp/includes/gp-optimize-data-fit.md}
\include{_gp/includes/gp-optimize-data-fit-capacity.md}


\endif

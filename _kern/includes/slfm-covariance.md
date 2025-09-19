\ifndef{slfmCovariance}
\define{slfmCovariance}

\editme

\subsection{Semi Parametric Latent Factor Covariance}

\define{formula}{\kernelScalar(i, j, \inputVector, \inputVector^\prime) = w_i w_j \kernelScalar(\inputVector, \inputVector^\prime)}

\loadcode{slfm_cov}{mlai}

\setupcode{import mlai.plot as plot
import mlai
import numpy as np}

\plotcode{kernel = mlai.Kernel(function=slfm_cov, subkernel=mlai.eq_cov, W=np.asarray([[1],[5]]))

plot.multi_output_covariance_func(kernel, num_outputs=2, shortname='slfm', diagrams='\writeDiagramsDir/kern/')}


\includecovariane{slfm}{\formula}{Semi-parametric latent factor model covariance function.}

\endif

\ifndef{lmcCovariance}
\define{lmcCovariance}
\editme

\subsection{Linear Model of Coregionalization Covariance}

\define{\formula}{\kernelScalar(i, j, \inputVector, \inputVector^\prime) = b_{i,j} \kernelScalar(\inputVector, \inputVector^\prime)}

\loadcode{lmc_cov}{mlai}

\setupplotcode{import mlai.plot as plot
import mlai
import numpy as np}

\plotcode{kernel = mlai.Kernel(function=lmc_cov, 
                     subkernel_list=[mlai.eq_cov, mlai.mlp_cov],
                     B_list=[np.asarray([[1, 0.5],[0.5, 1.5]]), 
                            np.asarray([[0.8, 0.3],[0.3, 0.8]])])

plot.multi_output_covariance_func(kernel, num_outputs=2, shortname='lmc', diagrams='\writeDiagramsDir/kern/')}

\includecovariance{lmc}{\formula}{Linear model of coregionalization covariance function.}


\endif

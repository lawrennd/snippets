\ifndef{icmCovariance}
\define{icmCovariance}
\editme

\subsection{Intrinsic Coregionalization Model Covariance}

\define{formula}{\kernelScalar(i, j, \inputVector, \inputVector^\prime) = b_{i,j} \kernelScalar(\inputVector, \inputVector^\prime)}

\loadcode{icm_cov}{mlai}

\setupplotcode{import mlai.plot as plot
import mlai
import numpy as np}

\plotcode{kernel = mlai.Kernel(function=icm_cov,
                     name='Intrinsic Coregionalisation Model',
                     shortname='icm',					 
                     formula='\formula',
					 subkernel=mlai.eq_cov,
					 B = np.asarray([[1, 0.5],[0.5, 1.5]]))

plot.multi_output_covariance_func(kernel, num_outputs=2, shortname='icm', diagrams='\writeDiagramsDir/kern/')}

\includecovariance{icm}{\formula}{Intrinsic coregionalization model covariance function.}

\endif

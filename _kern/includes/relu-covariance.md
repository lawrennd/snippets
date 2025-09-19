\ifndef{reluCovariance}
\define{reluCovariance}

\editme

\subsection{RELU Covariance}

\loadcode{relu_cov}{mlai}

\define{formula}{\kernelScalar(\inputVector, \inputVector^\prime) = 
\frac{\|\inputVector\| \|\inputVector^\prime\|}{2\pi} \left(\pi - \arccos\left(\frac{\inputVector^\top \inputVector^\prime + b}{\|\inputVector\| \|\inputVector^\prime\|}\right)\right)}


\setupplotcode{import mlai.plot as plot
import mlai
import numpy as np}

\plotcode{kernel = mlai.Kernel(function=mlai.relu_cov,
                     name='RELU',
                     shortname='relu',					 
                     formula='\kernelScalar(\inputVector, \inputVector^\prime) = \frac{\|\inputVector\| \|\inputVector^\prime\|}{2\pi} \left(\pi - \arccos\left(\frac{\inputVector^\top \inputVector^\prime + b}{\|\inputVector\| \|\inputVector^\prime\|}\right)\right)',
					 w=5, b=0.5)
					 
plot.covariance_func(kernel, diagrams='\writeDiagramsDir/kern/')}

\includecovariance{relu}{\formula}{Rectified linear unit covariance function.}


\endif

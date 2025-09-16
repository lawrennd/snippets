\ifndef{olympicMarathonPolynomialSample}
\define{olympicMarathonPolynomialSample}

\editme

\subsection{Olympic Marathon Polynomial Sample}

\setupcode{import numpy as np
import pods}

\code{data = pods.datasets.olympic_marathon_men()
x = data['X']
y = data['Y']

offset = y.mean()
scale = np.sqrt(y.var())
yhat = (y - offset)/scale
xlim = (1876,2044)

num_data = x.shape[0]}

\notes{Now let's build the basis matrices. We define the polynomial basis as follows.}

\loadcode{polynomial}{mlai}

\setupcode{import mlai}

\code{degree=4
alpha = 4
sigma2 = 0.1
num_pred_data = 100 # how many points to use for plotting predictions
x_pred = np.linspace(xlim[0], xlim[1], num_pred_data)[:, None] # input locations for predictions
data_limits=xlim
basis = mlai.Basis(mlai.polynomial, number=degree+1, data_limits=data_limits)
Phi_pred = basis.Phi(x_pred)
Phi = basis.Phi(x)
}

\subsection{Sampling from the Prior}

\notes{Now we will sample from the prior to produce a vector $\mappingVector$ and use it to plot a function which is representative of our belief *before* we fit the data. To do this we are going to use the properties of the Gaussian density and a sample from a *standard normal* using the function `np.random.normal`.}

\notes{Let's use this way of constructing samples from a Gaussian to check what functions look like *a priori*. The process will be as follows. First, we sample a random vector $K$ dimensional from `np.random.normal`. Then we scale it by $\sqrt{\alpha}$ to obtain a prior sample of $\mappingVector$.}

\code{K = degree + 1
z_vec = np.random.normal(size=K)
w_sample = z_vec*np.sqrt(alpha)
print(w_sample)}

\notes{Now we can combine our sample from the prior with the basis functions to create a function,}

\setupcode{import numpy as np}
\code{f_sample = np.dot(Phi_pred,w_sample)}

\setupplotcode{import matplotlib.pyplot as plt
import mlai.plot}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
_ = ax.plot(x_pred.flatten(), f_sample.flatten(), 'r-', linewidth=3)}

\notes{Note that we have carefully scaled our data using `xlim` to ensure that the polynomials don't go too large. These samples should be well behaved.}

\notes{Now we need to recompute the basis functions from above,}


\subsection{Mean Output}

\slides{* Each sample $\mappingVector_s$ has a prediction $\mappingFunctionVector_s$}
\notes{The prediction function can now be computed. In matrix form, the predictions can be computed as}
$$
\mappingFunctionVector_s = \basisMatrix \mappingVector_s.
$$ 
\notes{This involves a matrix multiplication between a fixed matrix $\basisMatrix$ and a vector  drawn from a distribution $p(\mappingVector)$. Because $\mappingVector_s$ is drawn from a distribution, this imples that $\mappingFunctionVector_s$ should also be drawn from a distribution. 
}

\setupcode{import numpy as np}

\code{f_sample = np.dot(Phi_pred, w_sample)}

\setupplotcode{import matplotlib.pyplot as plt
import mlai.plot}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
_ = ax.plot(x_pred.flatten(), f_sample.flatten(), 'r-', linewidth=3)}

\notes{Now let's loop through some samples and plot various functions as samples from this system,}

\plotcode{num_samples = 10
K = degree+1
fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
for i in range(num_samples):
    z_vec = np.random.normal(size=K)
    w_sample = z_vec*np.sqrt(alpha)
    f_sample = np.dot(Phi_pred,w_sample)
    _ = ax.plot(x_pred.flatten(), f_sample.flatten(), linewidth=2)
	
mlai.write_figure(filename='polynomial-prior-samples.svg', directory='\writeDiagramsDir/ml')}

\figure{\includediagram{\diagramsDir/ml/polynomial-prior-samples}{80%}}{Samples of $\basisMatrix \mappingVector$ with $\mappingVector$ taken from the prior.}{polynomial-prior-samples}

\endif

\ifndef{erichFriedmanPackingGp}
\define{erichFriedmanPackingGp}

\installcode{mlai}
\include{_datasets/includes/erich-friedman-packing-data.md}

\editme

\subsection{Gaussian Process Fit}

\notes{Our first objective will be to perform a Gaussian process fit to the data, we'll do this using the [`mlai`](https://github.com/lawrennd/mlai) software.}

\setupcode{from mlai import Kernel, eq_cov, GP, SCG}
\code{kernel = Kernel(eq_cov)
m_full = GP(x, y, sigma2=1.0, kernel=kernel)
_ = SCG().optimize(m_full) # Optimize parameters of covariance function}

\notes{The first commands set up the model with an exponentiated quadratic covariance, then `SCG().optimize(m_full)`
optimizes the parameters of the covariance function and the noise level of the model using scaled conjugate gradients. Once the fit is complete, we'll try creating some test points, and computing the output of the GP model in terms of the mean and standard deviation of the posterior functions. We plot the mean function and the standard deviation at 400 locations. We can obtain the predictions using
`y_mean, y_var = m_full.predict(xt)`
}

\code{xt = np.linspace(0,100,400)[:,np.newaxis]
yt_mean, yt_var = m_full.predict(xt)
yt_sd=np.sqrt(yt_var)}

\notes{Now we plot the results using the helper function in `mlai.plot`.}

\setupdisplaycode{import matplotlib.pyplot as plt
import mlai.plot as plot
import mlai}

\displaycode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
plot.model_output(m_full, ax=ax,  xlabel="n", ylabel="s", fontsize=20, portion=0.2)
ax.set_xlim(xlim)
ax.set_ylim(ylim)
mlai.write_figure(figure=fig,
                  filename="erich-friedman-packing-gp.svg", 
                  directory = "\writeDiagramsDir/gp",
                  transparent=True)}

\newslide{Erich Friedman Packing Data GP}

\figure{\includediagram{\diagramsDir/gp/erich-friedman-packing-gp}{80%}}{Gaussian process fit to the Erich Friedman Packing data.}{erich-friedman-packing-gp}



\endif

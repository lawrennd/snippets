\ifndef{stepFunctionGp}
\define{stepFunctionGp}
\editme

\include{_ml/includes/step-function-data.md}

\subsection{Step Function Data GP}

\notes{We can fit a Gaussian process to the step function data using ```mlai``` as follows.}

\setupcode{from mlai import Kernel, eq_cov, GP, SCG}
\code{kernel = Kernel(eq_cov)
m_full = GP(x, yhat, sigma2=1.0, kernel=kernel)
_ = SCG().optimize(m_full) # Optimize parameters of covariance function}

\notes{Where ```GP``` with an exponentiated quadratic kernel gives us a standard GP regression model.}

\notes{The model is optimized using ```SCG().optimize(m_full)``` which runs scaled conjugate gradients on the shared parameter surface (noise and kernel lengthscale/variance).}

\displaycode{fig, ax=plt.subplots(figsize=plot.big_wide_figsize)
plot.model_output(m_full, scale=scale, offset=offset, ax=ax, fontsize=20, portion=0.5)
ax.set_ylim(ylim)
ax.set_xlim(xlim)

mlai.write_figure(figure=fig,filename='\writeDiagramsDir/gp/step-function-gp.svg', 
            transparent=True, frameon=True)}
			

\figure{\includediagram{\diagramsDir/gp/step-function-gp}{80%}}{Gaussian process fit to the step function data. Note the large error bars and the over-smoothing of the discontinuity. Error bars are shown at two standard deviations.}{step-function-gp}


\notes{The resulting fit to the step function data shows some challenges. In particular, the over smoothing at the discontinuity. If we know how many discontinuities there are, we can parameterize them in the step function. But by doing this, we form a semi-parametric model. The parameters indicate how many discontinuities are, and where they are. They can be optimized as part of the model fit. But if new, unforeseen, discontinuities arise when the model is being deployed in practice, these won't be accounted for in the predictions.}

\endif

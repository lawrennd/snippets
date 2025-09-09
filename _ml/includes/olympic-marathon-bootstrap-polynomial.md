\ifndef{olympicMarathonBootstrapPolynomial}
\define{olympicMarathonBootstrapPolynomial}

\include{_ml/includes/olympic-marathon-polynomial.md}

\editme

\subsection{Bootstrap and Olympic Marathon Data}

\notes{First we define a function to bootstrap resample our dataset.}

\setupcode{import numpy as np}

\code{def bootstrap(X, y):
    "Return a bootstrap sample from a data set."
    n = X.shape[0]
    ind = np.random.choice(n, n, replace=True) # Sample randomly with replacement.
    return X[ind, :], y[ind, :]}


\code{num_bootstraps = 10}

\code{def bootstrap_fit(Phi, y, size):
    W = np.zeros((Phi.shape[1], size))
    for i in range(size):
	    Phi_hat, y_hat = bootstrap(Phi, y)
    	W[:, i:i+1] = basis_fit(Phi_hat, y_hat)
	return W}

\subsection{Linear Fit}

\slides{$$\mappingFunction(x, \mappingVector) = \mappingScalar_0 + \mappingScalar_1 \inputScalar$$}

\code{poly_args = {'num_basis':2, # two basis functions (1 and x)
             'data_limits':xlim}
Phi = mlai.polynomial(x, **poly_args)
W_hat = bootstrap_fit(Phi, y, num_bootstraps)}

\notes{Now we make some predictions for the fit.}

\code{x_pred = np.linspace(xlim[0], xlim[1], 400)[:, np.newaxis]
Phi_pred = mlai.polynomial(x_pred, **poly_args)
f_pred = Phi_pred@W_hat}

\setupplotcode{import matplotlib.pyplot as plt
import mlai.plot as plot
import mlai}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
_ = ax.plot(x, y, 'r.',markersize=10)
ax.set_xlabel('year', fontsize=20)
ax.set_ylabel('pace min/km', fontsize=20)
ax.set_xlim(xlim)
ax.set_ylim(ylim)

_ = ax.plot(x_pred, f_pred, 'b-', linewidth=2)

mlai.write_figure(filename='olympic-marathon-bootstrap-polynomial-2.svg', 
				  directory='\writeDiagramsDir/ml')}

\figure{\includediagram{\diagramsDir/ml/olympic-marathon-bootstrap-polynomial-2}{80%}}{Fit of a 1 degree polynomial (a linear model) to the olympic marathon data.}{olympic-marathon-bootstrap-polynomial-2}


\subsection{Cubic Fit}

\slides{$$\mappingFunction(x, \mappingVector) = \mappingScalar_0 + \mappingScalar_1 \inputScalar + \mappingScalar_2 \inputScalar^2 + \mappingScalar_{3} \inputScalar^3$$}

\code{poly_args = {'num_basis':4, # four basis: 1, x, x^2, x^3
             'data_limits':xlim}
Phi = mlai.polynomial(x, **poly_args)
W_hat = bootstrap_fit(Phi, y, num_bootstraps)}


\code{Phi_pred = mlai.polynomial(x_pred, **poly_args)
f_pred = Phi_pred@W_hat}

\setupplotcode{import matplotlib.pyplot as plt
import mlai.plot as plot
import mlai}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
_ = ax.plot(x, y, 'r.',markersize=10)
ax.set_xlabel('year', fontsize=20)
ax.set_ylabel('pace min/km', fontsize=20)
ax.set_xlim(xlim)
ax.set_ylim(ylim)

_ = ax.plot(x_pred, f_pred, 'b-', linewidth=2)

mlai.write_figure(filename='olympic-marathon-bootstrap-polynomial-4.svg', 
				  directory='\writeDiagramsDir/ml')}

\figure{\includediagram{\diagramsDir/ml/olympic-marathon-bootstrap-polynomial-4}{80%}}{Fit of a 3 degree polynomial (a cubic model) to the olympic marathon data.}{olympic-marathon-bootstrap-polynomial-4}

\subsection{9th Degree Polynomial Fit}

\slides{$$\mappingFunction(x, \mappingVector) = \mappingScalar_0 + \mappingScalar_1 \inputScalar + \mappingScalar_2 \inputScalar^2 + \dots + \mappingScalar_{9} \inputScalar^{9}$$}

\notes{Now we'll try a 9th degree polynomial fit to the data.}

\code{poly_args = {'num_basis':10, # basis up to x^9
             'data_limits':xlim}
Phi = mlai.polynomial(x, **poly_args)
W_hat = bootstrap_fit(Phi, y, num_bootstraps)}


\code{Phi_pred = mlai.polynomial(x_pred, **poly_args)
f_pred = Phi_pred@W_hat}

\setupplotcode{import matplotlib.pyplot as plt
import mlai.plot as plot
import mlai}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
_ = ax.plot(x, y, 'r.',markersize=10)
ax.set_xlabel('year', fontsize=20)
ax.set_ylabel('pace min/km', fontsize=20)
ax.set_xlim(xlim)
ax.set_ylim(ylim)

_ = ax.plot(x_pred, f_pred, 'b-', linewidth=2)

mlai.write_figure(filename='olympic-marathon-bootstrap-polynomial-10.svg', 
				  directory='\writeDiagramsDir/ml')}

\figure{\includediagram{\diagramsDir/ml/olympic-marathon-bootstrap-polynomial-10}{80%}}{Fit of a 9 degree polynomial to the olympic marathon data.}{olympic-marathon-bootstrap-polynomial-10}


\subsection{16th Degree Polynomial Fit}

\slides{$$\mappingFunction(x, \mappingVector) = \mappingScalar_0 + \mappingScalar_1 \inputScalar + \mappingScalar_2 \inputScalar^2 + \dots + \mappingScalar_{16} \inputScalar^{16}$$}

\notes{Now we'll try a 16th degree polynomial fit to the data.}

\code{poly_args = {'num_basis':17, # basis up to x^16
             'data_limits':xlim}
Phi = mlai.polynomial(x, **poly_args)
W_hat = bootstrap_fit(Phi, y, num_bootstraps)}


\code{Phi_pred = mlai.polynomial(x_pred, **poly_args)
f_pred = Phi_pred@W_hat}

\setupplotcode{import matplotlib.pyplot as plt
import mlai.plot as plot
import mlai}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
_ = ax.plot(x, y, 'r.',markersize=10)
ax.set_xlabel('year', fontsize=20)
ax.set_ylabel('pace min/km', fontsize=20)
ax.set_xlim(xlim)
ax.set_ylim(ylim)

_ = ax.plot(x_pred, f_pred, 'b-', linewidth=2)

mlai.write_figure(filename='olympic-marathon-bootstrap-polynomial-17.svg', 
				  directory='\writeDiagramsDir/ml')}

\figure{\includediagram{\diagramsDir/ml/olympic-marathon-bootstrap-polynomial-17}{80%}}{Fit of a 16 degree polynomial to the olympic marathon data.}{olympic-marathon-bootstrap-polynomial-17}


\subsection{Bootstrap Confidence Intervals}

\notes{We can also use the bootstrap to create confidence intervals for our predictions, showing the uncertainty in our model.}

\code{def plot_polynomial_bootstrap_confidence(x, y, x_pred, degree=3, num_bootstraps=50):
    """Plot bootstrap confidence intervals for polynomial fit.
    
    :param x: training inputs
    :param y: training outputs
    :param x_pred: prediction points
    :param degree: polynomial degree
    :param num_bootstraps: number of bootstrap samples
    """
    poly_args = {'num_basis': degree + 1, 'data_limits': xlim}
    Phi = mlai.polynomial(x, **poly_args)
    W_hat = bootstrap_fit(Phi, y, num_bootstraps)
    
    Phi_pred = mlai.polynomial(x_pred, **poly_args)
    f_pred_bootstrap = Phi_pred @ W_hat  # Shape: (n_pred_points, n_bootstrap_samples)
    
    # Transpose to get shape (n_bootstrap_samples, n_pred_points)
    f_pred_bootstrap = f_pred_bootstrap.T
    
    # Compute confidence intervals
    f_mean = np.mean(f_pred_bootstrap, axis=0)  # Mean across bootstrap samples
    f_std = np.std(f_pred_bootstrap, axis=0)    # Std across bootstrap samples
    
    # Ensure all arrays have the right shape
    if f_mean.ndim > 1:
        f_mean = f_mean.flatten()
    if f_std.ndim > 1:
        f_std = f_std.flatten()
    
    f_lower = f_mean - 1.96 * f_std  # 95% confidence interval
    f_upper = f_mean + 1.96 * f_std
    
    return f_mean, f_lower, f_upper, f_pred_bootstrap}

\code{f_mean, f_lower, f_upper, f_pred_bootstrap = plot_polynomial_bootstrap_confidence(x, y, x_pred, degree=3)}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)

# Plot training data
ax.plot(x, y, 'r.', markersize=10, label='Training Data')

# Plot mean prediction
ax.plot(x_pred.flatten(), f_mean, 'b-', linewidth=2, label='Mean Prediction')

# Plot confidence interval
ax.fill_between(x_pred.flatten(), f_lower, f_upper, 
                alpha=0.3, color='blue', label='95% Confidence Interval')

# Plot some individual bootstrap fits
for i in range(0, num_bootstraps, 5):  # Show every 5th bootstrap fit
    ax.plot(x_pred.flatten(), f_pred_bootstrap[i, :].flatten(), 'g-', alpha=0.1, linewidth=1)

ax.set_xlabel('year', fontsize=20)
ax.set_ylabel('pace min/km', fontsize=20)
ax.set_xlim(xlim)
ax.set_ylim(ylim)
ax.legend(fontsize=16)
ax.set_title('Bootstrap Confidence Intervals for Cubic Polynomial', fontsize=20)

mlai.write_figure(filename='olympic-marathon-bootstrap-confidence.svg', 
                  directory='\writeDiagramsDir/ml')}

\figure{\includediagram{\diagramsDir/ml/olympic-marathon-bootstrap-confidence}{80%}}{Bootstrap confidence intervals for a cubic polynomial fit to Olympic marathon data. The shaded region shows the 95% confidence interval, and individual bootstrap fits are shown in light green.}{olympic-marathon-bootstrap-confidence}

\notes{The confidence intervals show the uncertainty in our predictions. The width of the confidence interval reflects the variance of the model - wider intervals indicate higher variance. This visualization helps us understand not just the point predictions but also the reliability of those predictions.}

\notes{The bootstrap method provides a powerful way to estimate bias and variance without needing to know the true underlying function. By resampling from our training data, we can approximate how our model would perform on different samples from the same distribution, giving us insights into the bias-variance tradeoff.}

\notes{This analysis is particularly valuable for model selection - we can choose the polynomial degree that minimizes the total error (bias + variance) rather than just the training error.}


                            
\endif

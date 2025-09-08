\ifndef{olympicMarathonBiasVariancePlots}
\define{olympicMarathonBiasVariancePlots}

\include{_ml/includes/olympic-marathon-bootstrap-polynomial.md}

\editme

\subsection{Bias-Variance Analysis for Olympic Marathon Data}

\notes{We can use the bootstrap to characterise the bias and variance for different polynomials on the olympic data. The bootstrap allows us to estimate how much the model predictions vary when trained on different samples from the same underlying distribution.}

\notes{For each polynomial degree, we'll compute the bias and variance by comparing the bootstrap predictions to the true underlying function (which we approximate using a high-degree polynomial fit to all the data).}

\setupcode{import numpy as np
import matplotlib.pyplot as plt
import mlai.plot as plot
import mlai}

\code{def compute_bias_variance(x_pred, f_pred_bootstrap, f_true):
    """Compute bias and variance from bootstrap predictions.
    
    :param x_pred: prediction points
    :param f_pred_bootstrap: bootstrap predictions (n_bootstrap, n_points)
    :param f_true: true function values
    """
    # Mean prediction across bootstrap samples
    f_mean = np.mean(f_pred_bootstrap, axis=0)
    
    # Bias: difference between mean prediction and true function
    bias = np.mean((f_mean - f_true)**2)
    
    # Variance: average variance of predictions around the mean
    variance = np.mean(np.var(f_pred_bootstrap, axis=0))
    
    return bias, variance, f_mean}

\code{def analyze_polynomial_bias_variance(x, y, x_pred, max_degree=16, num_bootstraps=50):
    """Analyze bias-variance tradeoff for polynomial models.
    
    :param x: training inputs
    :param y: training outputs  
    :param x_pred: prediction points
    :param max_degree: maximum polynomial degree to test
    :param num_bootstraps: number of bootstrap samples
    """
    degrees = range(1, max_degree + 1)
    biases = []
    variances = []
    total_errors = []
    
    # Use a high-degree polynomial as approximation to true function
    poly_args_true = {'num_basis': max_degree + 5, 'data_limits': xlim}
    Phi_true = polynomial(x, **poly_args_true)
    w_true = basis_fit(Phi_true, y)
    Phi_pred_true = polynomial(x_pred, **poly_args_true)
    f_true = Phi_pred_true @ w_true
    
    for degree in degrees:
        # Bootstrap predictions for this degree
        poly_args = {'num_basis': degree + 1, 'data_limits': xlim}
        Phi = polynomial(x, **poly_args)
        W_hat = bootstrap_fit(Phi, y, num_bootstraps)
        
        # Predictions on test points
        Phi_pred = polynomial(x_pred, **poly_args)
        f_pred_bootstrap = Phi_pred @ W_hat
        
        # Compute bias and variance
        bias, variance, f_mean = compute_bias_variance(x_pred, f_pred_bootstrap, f_true)
        
        biases.append(bias)
        variances.append(variance)
        total_errors.append(bias + variance)
        
    return degrees, biases, variances, total_errors}

\code{degrees, biases, variances, total_errors = analyze_polynomial_bias_variance(x, y, x_pred)}

\setupplotcode{import matplotlib.pyplot as plt
import mlai.plot as plot
import mlai}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)

ax.plot(degrees, biases, 'b-', linewidth=2, label='Bias$^2$')
ax.plot(degrees, variances, 'r-', linewidth=2, label='Variance')
ax.plot(degrees, total_errors, 'g-', linewidth=2, label='Total Error')

ax.set_xlabel('Polynomial Degree', fontsize=20)
ax.set_ylabel('Error', fontsize=20)
ax.set_title('Bias-Variance Tradeoff for Olympic Marathon Data', fontsize=20)
ax.legend(fontsize=16)
ax.grid(True, alpha=0.3)

# Mark the optimal point
optimal_idx = np.argmin(total_errors)
ax.axvline(x=degrees[optimal_idx], color='k', linestyle='--', alpha=0.7)
ax.text(degrees[optimal_idx] + 0.5, max(total_errors) * 0.8, 
        f'Optimal: degree {degrees[optimal_idx]}', fontsize=14)

mlai.write_figure(filename='olympic-marathon-bias-variance-plots.svg', 
                  directory='\writeDiagramsDir/ml')}

\figure{\includediagram{\diagramsDir/ml/olympic-marathon-bias-variance-plots}{80%}}{Bias-variance tradeoff for polynomial models on Olympic marathon data. The bias decreases with model complexity while variance increases. The optimal model balances these two sources of error.}{olympic-marathon-bias-variance-plots}

\notes{The plot shows the classic bias-variance tradeoff. As we increase the polynomial degree:

1. **Bias decreases**: Higher degree polynomials can capture more complex patterns in the data
2. **Variance increases**: Higher degree polynomials are more sensitive to variations in the training data
3. **Total error**: The sum of bias and variance shows a U-shaped curve with an optimal point

The optimal polynomial degree (around 3-4 in this case) minimizes the total generalization error by balancing bias and variance.}

\notes{This analysis demonstrates the "Goldilocks principle" in machine learning - we want a model that's not too simple (high bias) and not too complex (high variance), but just right for the amount of data we have.}

\subsection{Bootstrap Confidence Intervals}

\notes{We can also use the bootstrap to create confidence intervals for our predictions, showing the uncertainty in our model.}

\code{def plot_bootstrap_confidence(x, y, x_pred, degree=3, num_bootstraps=50):
    """Plot bootstrap confidence intervals for polynomial fit.
    
    :param x: training inputs
    :param y: training outputs
    :param x_pred: prediction points
    :param degree: polynomial degree
    :param num_bootstraps: number of bootstrap samples
    """
    poly_args = {'num_basis': degree + 1, 'data_limits': xlim}
    Phi = polynomial(x, **poly_args)
    W_hat = bootstrap_fit(Phi, y, num_bootstraps)
    
    Phi_pred = polynomial(x_pred, **poly_args)
    f_pred_bootstrap = Phi_pred @ W_hat
    
    # Compute confidence intervals
    f_mean = np.mean(f_pred_bootstrap, axis=0)
    f_std = np.std(f_pred_bootstrap, axis=0)
    f_lower = f_mean - 1.96 * f_std  # 95% confidence interval
    f_upper = f_mean + 1.96 * f_std
    
    return f_mean, f_lower, f_upper, f_pred_bootstrap}

\code{f_mean, f_lower, f_upper, f_pred_bootstrap = plot_bootstrap_confidence(x, y, x_pred, degree=3)}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)

# Plot training data
ax.plot(x, y, 'r.', markersize=10, label='Training Data')

# Plot mean prediction
ax.plot(x_pred, f_mean, 'b-', linewidth=2, label='Mean Prediction')

# Plot confidence interval
ax.fill_between(x_pred.flatten(), f_lower.flatten(), f_upper.flatten(), 
                alpha=0.3, color='blue', label='95% Confidence Interval')

# Plot some individual bootstrap fits
for i in range(0, num_bootstraps, 5):  # Show every 5th bootstrap fit
    ax.plot(x_pred, f_pred_bootstrap[i, :], 'g-', alpha=0.1, linewidth=1)

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

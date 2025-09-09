\ifndef{olympicMarathonBiasVariancePlots}
\define{olympicMarathonBiasVariancePlots}

\editme

\subsection{Bias-Variance Analysis for Olympic Marathon Data}

\notes{We can use the bootstrap to characterise the bias and variance for different polynomials on the olympic data. The bootstrap allows us to estimate how much the model predictions vary when trained on different samples from the same underlying distribution.}

\notes{For each polynomial degree, we compute the bias and variance by comparing the bootstrap predictions at the training inputs against the observed targets. Concretely, we average the bootstrap predictions per training input and measure squared error to the observed $y$ (bias$^2$), and we average the bootstrap prediction variance across training inputs (variance). This non-OOB bootstrap estimate exhibits the expected pattern: high bias for low-degree polynomials and higher variance for high-degree polynomials.}

\setupcode{import numpy as np
import matplotlib.pyplot as plt
import mlai.plot as plot
import mlai}

\code{def compute_bias_variance(x_pred, f_pred_bootstrap, f_full_dataset):
    """Compute bias and variance from bootstrap predictions.
    
    :param x_pred: prediction points
    :param f_pred_bootstrap: bootstrap predictions (n_bootstrap, n_points)
    :param f_full_dataset: prediction from full dataset
    """
    # Mean prediction across bootstrap samples
    f_mean = np.mean(f_pred_bootstrap, axis=0)
    
    # Ensure f_mean has the right shape (flatten if needed)
    if f_mean.ndim > 1:
        f_mean = f_mean.flatten()
    if f_full_dataset.ndim > 1:
        f_full_dataset = f_full_dataset.flatten()
    
    # Bias: difference between mean bootstrap prediction and full dataset prediction
    bias = np.mean((f_mean - f_full_dataset)**2)
    
    # Variance: average variance of bootstrap predictions around their mean
    variance = np.mean(np.var(f_pred_bootstrap, axis=0))
    
    return bias, variance, f_mean}

\code{def analyze_polynomial_bias_variance(x, y, x_pred, max_degree=6, num_bootstraps=50):
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
    
    for degree in degrees:
        # Bootstrap predictions for this degree
        poly_args = {'num_basis': degree + 1, 'data_limits': xlim}
        Phi = mlai.polynomial(x, **poly_args)
        W_hat = bootstrap_fit(Phi, y, num_bootstraps)

        # Predictions at training inputs for each bootstrap model
        # Phi: (n_train, n_basis), W_hat: (n_basis, B) -> (n_train, B)
        F_train = (Phi @ W_hat).T  # (B, n_train)

        # Per-point bootstrap mean and variance of predictions
        mu = F_train.mean(axis=0)            # (n_train,)
        var_point = F_train.var(axis=0)      # (n_train,)

        # Bias^2 and Variance using observed targets as reference
        bias = np.mean((mu - y.flatten())**2)
        variance = np.mean(var_point)

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

ylim = [0, 1]
ax.set_ylim(ylim)
ax.set_xlabel('Polynomial Degree', fontsize=20)
ax.set_ylabel('Error', fontsize=20)
ax.set_title('Bias-Variance Tradeoff for Olympic Marathon Data', fontsize=20)
ax.legend(fontsize=16)
ax.grid(True, alpha=0.3)

# Mark the optimal point
optimal_idx = np.argmin(total_errors)
ax.axvline(x=degrees[optimal_idx], color='k', linestyle='--', alpha=0.7)
ax.text(degrees[optimal_idx] + 0.5, ylim[1] * 0.8, 
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


\endif

\ifndef{poissonRegression}
\define{poissonRegression}

\include{_ml/includes/poisson-distribution.md}

\editme

\subsection{Poisson Regression}

\slides{
* In a Poisson regression make rate a function of space/time.
  $$\log \lambda(\inputVector, t) = \mappingVector_x^\top
\basisVector_\inputScalar(\inputVector) + \mappingVector_t^\top \basisVector_t(t)$$
* This is known as a *log linear* or *log additive* model. 
* The link function is a logarithm.
* We can rewrite such a function as 
  $$\log \lambda(\inputVector, t) = \mappingFunction_x(\inputVector) + \mappingFunction_t(t)$$
}

\notes{Poisson regression is a type of generalized linear model (GLM) used when modeling count data. It assumes the response variable follows a Poisson distribution and uses a logarithmic link function to relate the mean of the response to the linear predictor.

In this model, we make the rate parameter λ a function of covariates (like space or time). The logarithm of the rate is modeled as a linear combination of the input features:

$$\log \lambda(\inputVector, t) = \mappingVector_x^\top \basisVector_\inputScalar(\inputVector) + \mappingVector_t^\top \basisVector_t(t)$$

where:
- $\mappingVector_x$ and $\mappingVector_t$ are parameter vectors
- $\basisVector_\inputScalar(\inputVector)$ and $\basisVector_t(t)$ are basis functions for space and time respectively

This formulation is known as a log-linear or log-additive model because we're adding terms in the log space. The logarithm serves as our link function, connecting the linear predictor to the response variable's mean.}

\newslide{Multiplicative Model}

\slides{
* Be careful though ... a log additive model is really multiplicative.
  $$\log \lambda(\inputVector, t) = \mappingFunction_x(\inputVector) + \mappingFunction_t(t)$$
* Becomes $$\lambda(\inputVector, t) = \exp(\mappingFunction_x(\inputVector) + \mappingFunction_t(t))$$
* Which is equivalent to  $$\lambda(\inputVector, t) = \exp(\mappingFunction_x(\inputVector))\exp(\mappingFunction_t(t))$$
* Link functions can be deceptive in this way.
}

\notes{An important characteristic of this model that practitioners should be aware of is that while we add terms in the log space, the model becomes multiplicative when we transform back to the original space. This happens because:

1. We start with the log-additive form: $\log \lambda(\inputVector, t) = \mappingFunction_x(\inputVector) + \mappingFunction_t(t)$

2. When we exponentiate both sides to get back to λ, the addition in log space becomes multiplication:
   $$\lambda(\inputVector, t) = \exp(\mappingFunction_x(\inputVector) + \mappingFunction_t(t)) = \exp(\mappingFunction_x(\inputVector))\exp(\mappingFunction_t(t))$$

This multiplicative nature has important implications for interpretation. For example, if we increase one input variable, it has a multiplicative effect on the rate, not an additive one. This can lead to rapid growth in the predicted counts as input values increase.}





\newslide{Synthetic Example}

\notes{Let's look at another example using synthetic data to demonstrate Poisson regression without relying on external APIs.}

\setupcode{import numpy as np
import statsmodels.api as sm}

\code{# Generate some example count data
np.random.seed(42)
n_samples = 100
x1 = np.random.uniform(0, 10, n_samples)
x2 = np.random.uniform(0, 5, n_samples)
X = np.column_stack((x1, x2))

# True relationship: y ~ Poisson(exp(1 + 0.3*x1 - 0.2*x2))
lambda_true = np.exp(1 + 0.3*x1 - 0.2*x2)
y = np.random.poisson(lambda_true)

# Fit Poisson regression
model_synthetic = sm.GLM(y, sm.add_constant(X), family=sm.families.Poisson())
result_synthetic = model_synthetic.fit()}

\notes{The `statsmodels` library in Python provides a convenient way to fit Poisson regression models. The `sm.GLM` function is used to fit generalized linear models, and we specify the Poisson family to indicate that we're modeling count data. The `sm.add_constant(x)` function adds a column of ones to the design matrix to account for the intercept term.}


\notes{In this synthetic example, we generate count data that follows a Poisson distribution where the rate parameter $\lambda$ depends on two predictor variables. This demonstrates how Poisson regression can model count data with multiple predictors.}

\plotcode{fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Plot actual vs predicted counts
y_pred = result_synthetic.predict(sm.add_constant(X))
ax1.scatter(y, y_pred, alpha=0.5)
ax1.plot([0, max(y)], [0, max(y)], 'r--')
ax1.set_xlabel('Actual Counts')
ax1.set_ylabel('Predicted Counts')
ax1.set_title('Actual vs Predicted')

# Plot residuals
residuals = y - y_pred
ax2.scatter(y_pred, residuals, alpha=0.5)
ax2.axhline(y=0, color='r', linestyle='--')
ax2.set_xlabel('Predicted Counts')
ax2.set_ylabel('Residuals')
ax2.set_title('Residual Plot')

plt.tight_layout()
plt.show()
mlai.write_figure("poisson-regression-diagnostics.svg", directory="\writeDiagramsDir/ml/")}

\newslide{Poisson Regression Diagnostics}

\figure{\includediagram{\diagramsDir/ml/poisson-regression-diagnostics.svg}{80%}}{Diagnostic plots for the Poisson regression model showing actual vs predicted counts and residual analysis.}{poisson-regression-diagnostics}

\endif

\ifndef{logisticRegressionFit}
\define{logisticRegressionFit}

\editme

\subsection{Model Fit Statistics}

\slides{
* Model fit statistics help assess classification performance:
  * Pseudo R-squared measures (McFadden, Cox-Snell, Nagelkerke)
  * Log-likelihood ratio test for model significance
  * AIC/BIC help compare models
}

\newslide{Parameter Estimates}
\slides{
* Parameter estimates tell us about log-odds relationships:
  * Coefficients show change in log-odds per unit change
  * Standard errors show coefficient uncertainty 
  * P-values test significance of each predictor
  * Confidence intervals provide range estimates
}

\newslide{Model Diagnostics}
\slides{
* Classification-specific diagnostics:
  * Deviance residuals for outlier detection
  * Leverage and influence measures
  * Goodness-of-fit tests (Hosmer-Lemeshow)
}

\newslide{Prediction and Classification}
\slides{
* Model predictions and classification:
  * Predicted probabilities from fitted model
  * Classification using probability threshold (typically 0.5)
  * Confusion matrix and classification metrics
}

\notes{The statsmodels summary for logistic regression provides several diagnostic measures that help us evaluate our classification model's performance and identify potential areas for improvement.

**Model Fit Statistics:**
The logistic regression model doesn't have a traditional R-squared since we're dealing with binary outcomes rather than continuous responses. Instead, we use pseudo R-squared measures:

- **McFadden's R-squared**: Compares the log-likelihood of our model to a null model with only an intercept. Values between 0.2-0.4 indicate excellent fit.
- **Log-Likelihood Ratio (LLR) test**: Tests whether our model is significantly better than the null model. A low p-value indicates our predictors significantly improve the model.
- **AIC/BIC**: Help compare different model specifications. Lower values indicate better models when comparing alternatives.

**Parameter Interpretation:**
The coefficients in logistic regression represent changes in log-odds:
- A positive coefficient means the feature increases the odds of the positive class
- A negative coefficient means the feature decreases the odds of the positive class  
- The magnitude indicates the strength of the effect
- To get odds ratios, we exponentiate the coefficients: $\exp(\beta_j)$

For example, if a coefficient is 0.693, then $\exp(0.693) = 2.0$, meaning a one-unit increase in that feature doubles the odds of the positive outcome.

**Diagnostic Considerations:**
Unlike linear regression, logistic regression has different diagnostic concerns:

1. **Multicollinearity**: Check condition numbers and correlation matrices, just like in linear regression
2. **Outliers and Influential Points**: Use deviance residuals and leverage measures to identify problematic observations
3. **Model Adequacy**: Hosmer-Lemeshow test checks if predicted probabilities match observed frequencies
4. **Separation**: Perfect or quasi-perfect separation can cause convergence issues and inflated standard errors

**Classification Performance:**
Beyond the statistical diagnostics, we should evaluate practical classification performance:
- **Confusion Matrix**: Shows true vs predicted classifications
- **Accuracy**: Overall percentage of correct predictions  
- **Precision/Recall**: Important when classes are imbalanced
- **ROC/AUC**: Measures discrimination ability across different thresholds}


\endif

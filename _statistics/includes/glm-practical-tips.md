\ifndef{glmPracticalTips}
\define{glmPracticalTips}

\editme
\subsection{Practical Tips}

\notes{\notes{In practice feature engineering is critical to the success of a GLM. Build modular data processing pipelines that allow you to easily test different feature sets. For example, if modeling house prices, you might want to test combinations of raw features (square footage, bedrooms), derived features (price per square foot), and interaction terms (bedrooms $\times$ bathrooms). Consider non-linear transformations of continuous variables. For instance, taking the log of price data often helps normalise distributions. Be thoughtful about encoding categorical variables. One-hot encoding isn't always optimal, for high-cardinality categories, consider target encoding or feature hashing. Scale features appropriately: standardization or min-max scaling depending on your model assumptions. Document your feature creation process thoroughly, including the rationale for each transformation. Jupyter notebooks can be a good place to do this.}

\slides{
* Feature engineering is critical
* Build modular pipelines to test features
* Consider interactions between variables
* Document your process carefully
}

\notes{Model validation requires careful consideration. Cross-validation should match your real-world use case. For time series data, use time-based splits rather than random splits. Bootstrap sampling can help with understanding parameter uncertainty. For example, bootstrapping can show if a coefficient's sign might flip under different samples. Hold-out test sets should be truly independent. In a customer churn model, this might mean testing on future customers rather than a random subset. Watch for data leakage, especially with time-dependent features. E.g. if predicting customer churn, using future purchase data would create leakage.}

\newslide{Model Validation}

\slides{
* Use cross-validation wisely
* Bootstrap for uncertainty
* Keep hold-out test sets
* Beware of temporal leakage
}

\newslide{Diagnostic Checks}

Diagnostic checks are essential for building confidence about the model reliability. Create residual plots against fitted values and each predictor. Look for systematic patterns, a U-shaped residual plot suggests missing quadratic terms. For logistic regression, plot predicted probabilities against actual outcomes in bins to check calibration. Calculate influence measures like Cook's distance to identify outliers. In a house price model, a mansion might have outsized influence on coefficients. Check [variance inflation factors](https://en.wikipedia.org/wiki/Variance_inflation_factor) (VIF) for multicollinearity. High VIF (>5-10) suggests problematic correlation between predictors.

\slides{
* Plot residuals systematically
* Check for non-linear patterns
* Identify influential points
* Test feature relationships
}

\newslide{Visualisation}

\notes{Visualisation remains crucial throughout. Before modeling, create scatter plots, box plots, and histograms to understand your data distribution and relationships. Use pairs plots to identify correlations and potential interactions between features. Create residual diagnostic plots including Q-Q plots for normality checking. When communicating results, focus on interpretable visualizations. For instance, partial dependence plots can show how predictions change with a single feature.}

\slides{
* Always plot raw data first
* Create diagnostic visualisations
* Check model assumptions
* Communicate results clearly
}

\notes{Other practical considerations include starting simple and add complexity incrementally. A basic linear model often provides a good baseline. Keep track of model performance metrics across iterations to ensure changes actually improve results. Consider the computational cost of feature engineering: some transformations might not be feasible in production. Think about how features will be available in production. If a feature requires complex processing or external data, it might not be practical. For categorical variables with many levels, consider grouping rare categories. When dealing with missing data, document your imputation strategy and test its impact on model performance. When using the Access, Assess, Address approach remember that documentation of the missing values is part of Assess. Imputation can only occur in Address.}

\endif

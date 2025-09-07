\ifndef{logistRegressionStatsmodelsShort}
\define{logistRegressionStatsmodelsShort}


\editme

\subsection{Using `statsmodels`}

\notes{The statsmodels package provides a more convenient way to fit logistic regression models with additional statistical analysis capabilities.}

\setupcode{import statsmodels.api as sm}

\code{# Add constant term to X_train and X_test for intercept
X_train_sm = sm.add_constant(X_train)
X_test_sm = sm.add_constant(X_test)

# Fit logistic regression
model = sm.Logit(y_train, X_train_sm)
results = model.fit()

# Print summary of model results
print(results.summary())

# Make predictions on test set
y_pred = results.predict(X_test_sm)
print("\nTest set accuracy:", np.mean((y_pred > 0.5) == y_test))}

\notes{The statsmodels implementation provides additional statistical metrics like p-values, confidence intervals, and various diagnostic tests that can help evaluate the model's fit and assumptions.}

\endif

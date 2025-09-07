\ifndef{logisticRegressionStatsmodels}
\define{logisticRegressionStatsmodels}

\editme


\subsection{Logistic Regression with `statsmodels`}

\notes{In logistic regression, we model the relationship between a binary response variable $\dataScalar_i \in \{0,1\}$ and input variables $\inputVector_i$ using the logistic function. Unlike linear regression, we cannot directly model the probability using a linear function since probabilities must lie between 0 and 1.

The logistic regression model uses the sigmoid function to map any real-valued input to the range [0,1]:

$$p(\dataScalar_i = 1|\inputVector_i) = \sigma(\mappingVector^\top\inputVector_i) = \frac{1}{1 + \exp(-\mappingVector^\top\inputVector_i)}$$

where $\sigma(\cdot)$ is the sigmoid function and $\mappingVector^\top\inputVector_i = \sum_{j=1}^D \weightScalar_j\inputScalar_{i,j}$ is the linear predictor.

The key components are:
- $\dataScalar_i \in \{0,1\}$ is the binary target/response variable
- $\inputVector_i$ contains the input features/explanatory variables  
- $\mappingVector$ contains the parameters/coefficients we learn
- $\sigma(\cdot)$ is the sigmoid activation function that maps $(-\infty, \infty) \to (0, 1)$

The model assumes that given the features $\inputVector_i$, the response $\dataScalar_i$ follows a Bernoulli distribution:

$$\dataScalar_i|\inputVector_i \sim \text{Bernoulli}(\sigma(\mappingVector^\top\inputVector_i))$$

This gives us the likelihood:

$$p(\dataScalar_i|\inputVector_i) = \sigma(\mappingVector^\top\inputVector_i)^{\dataScalar_i} \left(1 - \sigma(\mappingVector^\top\inputVector_i)\right)^{1-\dataScalar_i}$$

The log-odds (logit) transformation provides a linear relationship:

$$\log\left(\frac{p(\dataScalar_i = 1|\inputVector_i)}{1 - p(\dataScalar_i = 1|\inputVector_i)}\right) = \mappingVector^\top\inputVector_i$$

This means the coefficients $\mappingVector$ represent the change in log-odds for a unit change in the corresponding feature.}

\newslide{Logistic Regression Model}

\slides{* Logistic regression models binary response $\dataScalar_i \in \{0,1\}$ vs inputs $\inputVector_i$:
  $$p(\dataScalar_i = 1|\inputVector_i) = \sigma(\mappingVector^\top\inputVector_i)$$
  where $\sigma(z) = \frac{1}{1 + \exp(-z)}$ is the sigmoid function
  
* Bernoulli distribution:
  $$\dataScalar_i|\inputVector_i \sim \text{Bernoulli}(\sigma(\mappingVector^\top\inputVector_i))$$
}

\newslide{Log-Odds and Linear Predictor}

\slides{* Log-odds (logit) transformation:
  $$\text{logit}(p) = \log\left(\frac{p}{1-p}\right) = \mappingVector^\top\inputVector_i$$
  
* Coefficients represent change in log-odds:
  $$\Delta \text{logit}(p) = \weightScalar_j \Delta \inputScalar_j$$
}

\setupcode{import statsmodels.api as sm
import numpy as np
import pandas as pd
from sklearn.datasets import make_classification}

\code{# Demo of logistic regression using python statsmodels.
# Create a synthetic binary classification dataset
X, y = make_classification(n_samples=200, n_features=2, n_redundant=0, 
                         n_informative=2, n_clusters_per_class=1, 
                         random_state=42)

# Convert to DataFrame for easier handling
df = pd.DataFrame(X, columns=['feature1', 'feature2'])
df['target'] = y

# Split into train and test sets
indices = np.random.permutation(df.shape[0])
num_train = int(np.ceil(df.shape[0]/2))
train_indices = indices[:num_train]
test_indices = indices[num_train:]

X_train = df[['feature1', 'feature2']].iloc[train_indices]
y_train = df['target'].iloc[train_indices]
X_test = df[['feature1', 'feature2']].iloc[test_indices]
y_test = df['target'].iloc[test_indices]

# Add constant term to design matrix
X_train_sm = sm.add_constant(X_train)
X_test_sm = sm.add_constant(X_test)

# Fit logistic regression model
model = sm.Logit(y_train, X_train_sm)
results = model.fit()
results.summary()
}

\newslide{Model Fit Statistics}
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



\setupplotcode{import matplotlib.pyplot as plt
import mlai
from mlai import plot}

\code{# Make predictions on test set
y_pred_proba = results.predict(X_test_sm)
y_pred = (y_pred_proba > 0.5).astype(int)

# Calculate classification metrics
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)

print(f"Test Accuracy: {accuracy:.3f}")
print(f"Confusion Matrix:\n{conf_matrix}")
print(f"\nClassification Report:\n{classification_report(y_test, y_pred)}")
}

\plotcode{# Create visualization of the logistic regression results
fig, axes = plt.subplots(1, 2, figsize=(15, 6))

# Plot 1: Data points colored by true class
ax1 = axes[0]
scatter = ax1.scatter(X_train['feature1'], X_train['feature2'], 
                     c=y_train, cmap='RdYlBu', alpha=0.7, s=50)
ax1.set_xlabel('Feature 1')
ax1.set_ylabel('Feature 2')
ax1.set_title('Training Data (True Classes)')
plt.colorbar(scatter, ax=ax1)

# Plot 2: Decision boundary and predicted probabilities
ax2 = axes[1]

# Create a mesh to plot the decision boundary
h = 0.1
x_min, x_max = X_train['feature1'].min() - 1, X_train['feature1'].max() + 1
y_min, y_max = X_train['feature2'].min() - 1, X_train['feature2'].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                     np.arange(y_min, y_max, h))

# Predict probabilities on the mesh
mesh_points = np.c_[xx.ravel(), yy.ravel()]
mesh_points_sm = sm.add_constant(mesh_points)
Z = results.predict(mesh_points_sm)
Z = Z.reshape(xx.shape)

# Plot decision boundary and probability contours
contour = ax2.contourf(xx, yy, Z, levels=50, alpha=0.6, cmap='RdYlBu')
ax2.contour(xx, yy, Z, levels=[0.5], colors='black', linewidths=2, linestyles='--')

# Plot training points
ax2.scatter(X_train['feature1'], X_train['feature2'], 
           c=y_train, cmap='RdYlBu', edgecolors='black', s=50)
ax2.set_xlabel('Feature 1')
ax2.set_ylabel('Feature 2')
ax2.set_title('Decision Boundary and Probability Contours')
plt.colorbar(contour, ax=ax2)

plt.tight_layout()
plt.show()
mlai.write_figure("logistic-regression-classification-statsmodels.svg", directory="\writeDiagramsDir/ml")}

\notes{Looking at our classification results, we can evaluate several aspects of model performance:

**Decision Boundary Analysis:**
The visualization shows how our logistic regression model creates a linear decision boundary in the feature space. The dashed black line represents the 0.5 probability threshold where the model switches between predicting class 0 and class 1. The colored contours show the predicted probability landscape - areas closer to red have higher probability of being class 1, while areas closer to blue have higher probability of being class 0.

**Model Performance:**
From the classification metrics, we can assess:
- **Accuracy**: Overall percentage of correct predictions on the test set
- **Confusion Matrix**: Shows the breakdown of true positives, false positives, true negatives, and false negatives
- **Precision and Recall**: Important when we care about specific types of errors (e.g., medical diagnosis)

**Potential Issues to Monitor:**
1. **Feature Scaling**: If features have very different scales, consider standardization
2. **Linear Separability**: Our model assumes a linear decision boundary - if classes aren't linearly separable, consider polynomial features or non-linear methods
3. **Class Imbalance**: If one class dominates, consider resampling techniques or adjusting the decision threshold
4. **Overfitting**: Monitor performance on validation data, especially with many features}

\newslide{Logistic Regression Classification}

\figure{\includediagram{\diagramsDir/ml/logistic-regression-classification-statsmodels}{80%}}{Logistic regression classification results showing training data and decision boundary with probability contours using `statsmodels`.}{logistic-regression-classification-statsmodels}

\notes{The classification visualization reveals several important aspects of our logistic regression model:

**Linear Decision Boundary:**
The model creates a straight-line decision boundary (shown as the dashed line at 0.5 probability). This linear separator works well when classes are roughly linearly separable, but may struggle with more complex class distributions.

**Probability Gradients:**
The colored contours show how predicted probabilities change smoothly across the feature space. Points far from the decision boundary have probabilities close to 0 or 1 (high confidence), while points near the boundary have probabilities around 0.5 (uncertain predictions).

**Model Extensions:**
For more complex classification problems, we can enhance the basic logistic regression model:
- **Polynomial Features**: Add $x_1^2$, $x_2^2$, $x_1 x_2$ terms for non-linear decision boundaries
- **Feature Interactions**: Include products of features to capture synergistic effects
- **Regularization**: Add L1 (Lasso) or L2 (Ridge) penalties to prevent overfitting
- **Feature Engineering**: Transform or combine features to better capture relationships

To incorporate multiple features and transformations into our model, we need a systematic way to organize this information through the design matrix.}

\newslide{Classification Performance}

\slides{
* Key classification insights:
  * Linear decision boundary separates classes
  * Smooth probability transitions
  * High confidence far from boundary
}

\newslide{Model Limitations}

\slides{
* Linear classifier limitations:
  * Assumes linear separability
  * May underfit complex relationships
  * Single decision threshold
}

\newslide{Model Improvements}

\slides{
* Model improvements possible with:
  * Polynomial features for non-linear boundaries
  * Feature interactions
  * Regularization techniques
  * Threshold optimization
}

\subsubsection{Design Matrix for Logistic Regression}

\slides{
* The design matrix $\designMatrix$ stores our features
* Each row represents one data point
* Each column represents one feature
* For $n$ data points and $p$ features:
  $$\designMatrix = \begin{bmatrix} 
  1 & x_{11} & x_{12} & \cdots & x_{1p} \\
  1 & x_{21} & x_{22} & \cdots & x_{2p} \\
  \vdots & \vdots & \vdots & \ddots & \vdots \\
  1 & x_{n1} & x_{n2} & \cdots & x_{np}
  \end{bmatrix}$$
* First column of 1s provides intercept term
}

\notes{The design matrix in logistic regression works similarly to linear regression but with some important differences. Each row represents an observation, and columns represent features. However, the interpretation of the model changes:

For logistic regression:
$$\text{logit}(p_i) = \log\left(\frac{p_i}{1-p_i}\right) = \designMatrix_i \mappingVector$$

where $\designMatrix_i$ is the $i$-th row of the design matrix and $p_i = p(\dataScalar_i = 1|\inputVector_i)$.

**Feature Engineering for Classification:**
We can enhance the design matrix with additional transformed features:

- **Polynomial Features**: $x_1^2$, $x_2^2$ for capturing non-linear relationships
- **Interaction Terms**: $x_1 \times x_2$ for capturing feature synergies  
- **Categorical Encodings**: One-hot encoding for categorical variables
- **Standardized Features**: Z-score normalization for better numerical stability

The choice of features in the design matrix directly affects the model's ability to capture complex decision boundaries while maintaining interpretability.}


\setupcode{import statsmodels.api as sm
import numpy as np
import pandas as pd
from sklearn.datasets import make_classification
from sklearn.preprocessing import PolynomialFeatures}

\code{# Demo of polynomial logistic regression using python statsmodels.
# Create a more complex non-linear classification dataset
X, y = make_classification(n_samples=300, n_features=2, n_redundant=0, 
                         n_informative=2, n_clusters_per_class=2, 
                         random_state=42)

# Convert to DataFrame for easier handling
df = pd.DataFrame(X, columns=['feature1', 'feature2'])
df['target'] = y

# Split into train and test sets
indices = np.random.permutation(df.shape[0])
num_train = int(np.ceil(df.shape[0]*0.7))
train_indices = indices[:num_train]
test_indices = indices[num_train:]

X_train = df[['feature1', 'feature2']].iloc[train_indices]
y_train = df['target'].iloc[train_indices]
X_test = df[['feature1', 'feature2']].iloc[test_indices]
y_test = df['target'].iloc[test_indices]

# Create polynomial features up to degree 2
poly_features = PolynomialFeatures(degree=2, include_bias=False)
X_train_poly = poly_features.fit_transform(X_train)
X_test_poly = poly_features.transform(X_test)

# Convert back to DataFrame to see feature names
feature_names = poly_features.get_feature_names_out(['feature1', 'feature2'])
X_train_poly_df = pd.DataFrame(X_train_poly, columns=feature_names)
X_test_poly_df = pd.DataFrame(X_test_poly, columns=feature_names)

# Add constant term to design matrix
X_train_poly_sm = sm.add_constant(X_train_poly_df)
X_test_poly_sm = sm.add_constant(X_test_poly_df)

print("Polynomial features:", feature_names)
print("Design matrix shape:", X_train_poly_sm.shape)

# Fit polynomial logistic regression model
model_poly = sm.Logit(y_train.values, X_train_poly_sm)
results_poly = model_poly.fit()
results_poly.summary()}


\setupplotcode{import matplotlib.pyplot as plt
import mlai
from mlai import plot}

\code{# Compare linear vs polynomial logistic regression performance
from sklearn.metrics import accuracy_score

# Predictions from polynomial model
y_pred_poly_proba = results_poly.predict(X_test_poly_sm)
y_pred_poly = (y_pred_poly_proba > 0.5).astype(int)

# Predictions from simple linear model (for comparison)
X_test_linear_sm = sm.add_constant(X_test)
model_linear = sm.Logit(y_train.values, sm.add_constant(X_train))
results_linear = model_linear.fit(disp=0)
y_pred_linear_proba = results_linear.predict(X_test_linear_sm)
y_pred_linear = (y_pred_linear_proba > 0.5).astype(int)

print(f"Linear Logistic Regression Test Accuracy: {accuracy_score(y_test, y_pred_linear):.3f}")
print(f"Polynomial Logistic Regression Test Accuracy: {accuracy_score(y_test, y_pred_poly):.3f}")
}

\plotcode{# Create comparison visualization
fig, axes = plt.subplots(1, 2, figsize=(15, 6))

# Create a mesh for decision boundary plotting
h = 0.1
x_min, x_max = X_train['feature1'].min() - 1, X_train['feature1'].max() + 1
y_min, y_max = X_train['feature2'].min() - 1, X_train['feature2'].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                     np.arange(y_min, y_max, h))

# Plot 1: Linear logistic regression
ax1 = axes[0]
mesh_points = np.c_[xx.ravel(), yy.ravel()]
mesh_points_sm = sm.add_constant(mesh_points)
Z_linear = results_linear.predict(mesh_points_sm)
Z_linear = Z_linear.reshape(xx.shape)

contour1 = ax1.contourf(xx, yy, Z_linear, levels=50, alpha=0.6, cmap='RdYlBu')
ax1.contour(xx, yy, Z_linear, levels=[0.5], colors='black', linewidths=2)
ax1.scatter(X_train['feature1'], X_train['feature2'], 
           c=y_train, cmap='RdYlBu', edgecolors='black', s=50)
ax1.set_xlabel('Feature 1')
ax1.set_ylabel('Feature 2')
ax1.set_title('Linear Logistic Regression')

# Plot 2: Polynomial logistic regression
ax2 = axes[1]
mesh_points_poly = poly_features.transform(mesh_points)
mesh_points_poly_sm = sm.add_constant(mesh_points_poly)
Z_poly = results_poly.predict(mesh_points_poly_sm)
Z_poly = Z_poly.reshape(xx.shape)

contour2 = ax2.contourf(xx, yy, Z_poly, levels=50, alpha=0.6, cmap='RdYlBu')
ax2.contour(xx, yy, Z_poly, levels=[0.5], colors='black', linewidths=2)
ax2.scatter(X_train['feature1'], X_train['feature2'], 
           c=y_train, cmap='RdYlBu', edgecolors='black', s=50)
ax2.set_xlabel('Feature 1')
ax2.set_ylabel('Feature 2')
ax2.set_title('Polynomial Logistic Regression')

plt.tight_layout()
plt.show()
mlai.write_figure("polynomial-logistic-regression-comparison-statsmodels.svg", directory="\writeDiagramsDir/ml")}

\newslide{Linear vs Polynomial Logistic Regression}

\figure{\includediagram{\diagramsDir/ml/polynomial-logistic-regression-comparison-statsmodels}{80%}}{Comparison between linear and polynomial logistic regression decision boundaries using `statsmodels`.}{polynomial-logistic-regression-comparison-statsmodels}

\notes{The comparison between linear and polynomial logistic regression reveals important insights about model flexibility and performance:

**Linear vs Non-linear Decision Boundaries:**
- The linear model (left) creates a straight decision boundary, which may be too restrictive for complex class distributions
- The polynomial model (right) can create curved decision boundaries that better separate non-linearly separable classes
- The polynomial features ($x_1^2$, $x_2^2$, $x_1 x_2$) allow the model to capture quadratic relationships

**Model Performance Trade-offs:**
The polynomial model typically shows:
1. **Improved Training Accuracy**: Better fit to training data due to increased flexibility
2. **Risk of Overfitting**: More parameters may lead to poor generalization
3. **Interpretability Loss**: Coefficients for polynomial terms are harder to interpret
4. **Computational Complexity**: More features require more computation

**Feature Engineering Considerations:**
When adding polynomial features, consider:
- **Feature Scaling**: Polynomial features can have very different scales (e.g., $x$ vs $x^2$)
- **Multicollinearity**: Polynomial features are often highly correlated
- **Regularization**: L1/L2 penalties become more important with many features
- **Cross-validation**: Essential for selecting optimal polynomial degree

The statsmodels summary shows how each polynomial term contributes to the model, with p-values indicating which transformations are statistically significant for improving classification performance.}

\endif

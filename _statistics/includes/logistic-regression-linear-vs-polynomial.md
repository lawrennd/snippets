\ifndef{logisticRegressionEvaluation}
\define{logisticRegressionEvaluation}

\editme


\subsubsection{Linear vs Polynomial Logistic Regression}

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

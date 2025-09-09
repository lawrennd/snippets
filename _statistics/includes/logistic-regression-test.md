\ifndef{logisticRegressionTest}
\define{logisticRegressionTest}

\editme

\subsection{Predictions of the Model}

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

\setupplotcode{import matplotlib.pyplot as plt
import mlai
from mlai import plot}


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
mlai.write_figure("logistic-regression-classification-statsmodels.svg", directory="\writeDiagramsDir/statistics")}

\figure{\includediagram{\diagramsDir/statistics/logistic-regression-classification-statsmodels}{80%}}{Plot of the logistic regression fit made by `statsmodels`.}{logistic-regression-classification-statsmodels}

\endif

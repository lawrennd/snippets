\ifndef{logisticRegressionTrain}
\define{logisticRegressionTrain}

\editme

\subsection{Fitting the Model}

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

\endif

\ifndef{logisticRegressionGradientDescent}
\define{logisticRegressionGradientDescent}

\editme

\subsection{Batch Gradient Descent}

\notes{We will need to define some initial random values for our vector and then minimize the objective by descending the gradient.}

\code{# Separate train and test
indices = np.random.permutation(X.shape[0])
num_train = int(np.ceil(X.shape[0]/2))
train_indices = indices[:num_train]
test_indices = indices[num_train:]
X_train = X.iloc[train_indices]
y_train = y.iloc[train_indices]==True
X_test = X.iloc[test_indices]
y_test = y.iloc[test_indices]==True}


\setupcode{import numpy as np}
\code{# gradient descent algorithm
w_vals = np.random.normal(size=(X.shape[1]+1, 1), scale = 0.001)
# Convert weights to a pandas DataFrame with column names
if typeof(X_train) is pd.DataFrame:
	w = pd.DataFrame(data=w_vals, 
	                 index=['Eins'] + list(X_train.columns), 
					 columns=['weight'])

eta = 1e-9
iters = 10000
for i in range(iters):
    g, Phi = predict(w, X_train, mlai.linear)
    w -= eta*gradient(g, Phi, y_train) + 0.001*w
    if not i % 100:
        print("Iter", i, "Objective", objective(g, y_train))}

\endif

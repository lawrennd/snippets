\ifndef{nigeriaNmisDataLogistic}
\define{nigeriaNmisDataLogistic}

\include{_datasets/includes/nigeria-nmis-data-classification.md}

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

\notes{Let's look at the weights and how they relate to the inputs.}

\setupcode{import matplotlib.pyplot as plt}
\code{# Plot a histogram of the weights
plt.figure(figsize=(10, 6))
if typeof(w) is pd.DataFrame:
    plt.bar(w.index, w['weight'])
else:
    plt.bar(w)
plt.xticks(rotation=90)
plt.xlabel('Features')
plt.ylabel('Weight Value')
plt.title('Histogram of Model Weights')
plt.tight_layout()
mlai.write_figure('nmis-logistic-regression-weights.svg', directory='\writeDiagramsDir/ml')}

\writeassignment{What does the magnitude of the weight vectors tell you about the different parameters and their influence on outcome? Are the weights of roughly the same size, if not, how might you fix this?}{10}

\code{g_test, Phi_test = predict(w, X_test, linear)
np.sum(g_test[y_test]>0.5)}

\subsection{Stochastic Gradient Descent}

\codeassignment{Now construct a stochastic gradient descent algorithm and run it on the data. Is it faster or slower than batch gradient descent? What can you do to improve convergence speed?}{}{20}

\endif

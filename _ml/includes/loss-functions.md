\ifndef{lossFunctions}
\define{lossFunctions}

\editme

\subsection{Loss Functions}

\setupcode{from mlai.loss import LossFunction}

\loadcode{MeanSquaredError}{mlai.loss}
\loadcode{MeanAbsoluteError}{mlai.loss}
\loadcode{BinaryCrossEntropyLoss}{mlai.loss}

\setupcode{import numpy as np}

\code{y_pred = np.array([[0.8], [0.3], [0.9], [0.1]])
y_true = np.array([[1.0], [0.0], [1.0], [0.0]])

losses = {
    'MSE': MeanSquaredError(),
    'MAE': MeanAbsoluteError(),
    'BCE': BinaryCrossEntropyLoss()
}

print("Loss Function Demonstration:")
print(f"Predictions: {y_pred.flatten()}")
print(f"True values: {y_true.flatten()}")
print()

for name, loss in losses.items():
    loss_value = loss.forward(y_pred, y_true)
    gradient = loss.gradient(y_pred, y_true)
    print(f"{name:3}: Loss = {loss_value:.4f}, Gradient = {gradient.flatten()}")
}


\subsection{Test loss function gradients}

\notes{Testing loss function gradients with finite differences.}
\loadcode{finite_difference_jacobian}{mlai.utils}
\loadcode{verify_gradient_implementation}{mlai.utils}


\code{# Test data
y_pred = np.array([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]])
y_true = np.array([[1.1, 2.1], [2.9, 4.1], [5.1, 5.9]])

results = {}}

\code{# Test Mean Squared Error
mse_loss = MeanSquaredError()
def mse_func(pred):
	return mse_loss.forward(pred.reshape(y_pred.shape), y_true)

numerical_grad = finite_difference_jacobian(mse_func, y_pred.flatten()).flatten()
analytical_grad = mse_loss.gradient(y_pred, y_true).flatten()
results['MSE'] = verify_gradient_implementation(analytical_grad, numerical_grad)
print(f"Mean Squared Error: {'PASS' if results['MSE'] else 'FAIL'}")}
    
\code{# Test Mean Absolute Error
mae_loss = MeanAbsoluteError()
def mae_func(pred):
	return mae_loss.forward(pred.reshape(y_pred.shape), y_true)

numerical_grad = finite_difference_jacobian(mae_func, y_pred.flatten()).flatten()
analytical_grad = mae_loss.gradient(y_pred, y_true).flatten()
results['MAE'] = verify_gradient_implementation(analytical_grad, numerical_grad)
print(f"Mean Absolute Error: {'PASS' if results['MAE'] else 'FAIL'}")}

\loadcode{HuberLoss}{mlai.loss}

\code{# Test Huber Loss
huber_loss = HuberLoss(delta=1.0)
def huber_func(pred):
	return huber_loss.forward(pred.reshape(y_pred.shape), y_true)

numerical_grad = finite_difference_jacobian(huber_func, y_pred.flatten()).flatten()
analytical_grad = huber_loss.gradient(y_pred, y_true).flatten()
results['Huber'] = verify_gradient_implementation(analytical_grad, numerical_grad)
print(f"Huber Loss: {'PASS' if results['Huber'] else 'FAIL'}")}
    
\code{# Test Binary Cross Entropy
bce_loss = BinaryCrossEntropyLoss()
y_pred_bce = np.array([[0.8], [0.3], [0.9]])
y_true_bce = np.array([[1.0], [0.0], [1.0]])

def bce_func(pred):
	return bce_loss.forward(pred.reshape(-1, 1), y_true_bce)

numerical_grad = finite_difference_jacobian(bce_func, y_pred_bce.flatten()).flatten()
analytical_grad = bce_loss.gradient(y_pred_bce, y_true_bce).flatten()
results['BCE'] = verify_gradient_implementation(analytical_grad, numerical_grad)
print(f"Binary Cross Entropy: {'PASS' if results['BCE'] else 'FAIL'}")}

\loadcode{CrossEntropyLoss}{mlai.loss}

\code{# Test Cross Entropy
ce_loss = CrossEntropyLoss()
y_pred_ce = np.array([[0.1, 0.9], [0.8, 0.2], [0.3, 0.7]])
y_true_ce = np.array([[0, 1], [1, 0], [0, 1]])

def ce_func(pred):
	return ce_loss.forward(pred.reshape(-1, 2), y_true_ce)

numerical_grad = finite_difference_jacobian(ce_func, y_pred_ce.flatten()).flatten()
analytical_grad = ce_loss.gradient(y_pred_ce, y_true_ce).flatten()
results['CE'] = verify_gradient_implementation(analytical_grad, numerical_grad)
print(f"Cross Entropy: {'PASS' if results['CE'] else 'FAIL'}")}


\endif

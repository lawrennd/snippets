\ifndef{logisticRegressionPerceptron}
\define{logisticRegressionPerceptron}

\editme


\subsection{Logistic Regression vs Perceptron}


\notes{We already looked at the Perceptron, where the prediction function was given by 
$$
\mappingFunction(\mappingVector, \inputVector_i) = \text{sign}(\designVector_i^\top \mappingVector) 
$$
and the sign of the output gave us the class, where we had a positive and negative class.}

\notes{In logistic regression, the prediction function gives us the probability of positive class, 
$$
\mappingFunction(\mappingVector, \inputVector) = \pi_i = \transformationFunction(\designVector_i^\top \mappingVector)
$$
so the two are closely related. We can think of the sigmoid as providing a "soft decision" whereas the sign provides a hard decision.}

\notes{Let's make a more detailed study by considering a *stochastic gradient descent* algorithm for the logistic regression of the negative log likelihood. We'll compare that update to the Perceptron update.}

\notes{We can think of the Perceptron update as randomly sampling a data point, $i$, checking its prediction. If the predicted class doesn't match the true class, $y_i$, then we update the weights by subtracting $\designVector_i$ if the prediction is positive, and adding $\designVector_i$ if the prediction is negative. Using $\dataScalar_i\in\{0,1\}$ to match logistic regression, a compact update is}
$$
 \mappingVector_\text{new} \leftarrow \mappingVector_\text{old} - \eta(\heaviside(\designVector_i^\top \mappingVector) (1-\dataScalar_i) \designVector_i - (1-\heaviside(\designVector_i^\top \mappingVector)) \dataScalar_i \designVector_i
$$

The gradient of the negative log-likelihood of logistic regression is
$$
\frac{\text{d}\errorFunction(\mappingVector)}{\text{d}\mappingVector} = -\sum_{i=1}^\numData
\dataScalar_i\left(1-\transformationFunction\left(\mappingVector^\top \designVector_i\right)\right)
\designVector_i +  \sum_{i=1}^\numData
(1-\dataScalar_i)\left(\transformationFunction\left(\mappingVector^\top \designVector_i\right)\right)
\designVector_i.
$$
so the gradient with respect to one point is 
$$
\frac{\text{d}\errorFunction_i(\mappingVector)}{\text{d}\mappingVector}=\dataScalar_i\left(1-\transformationFunction\left(\mappingVector^\top \designVector_i\right)\right)
\designVector_i + (1-\dataScalar_i)\left(\transformationFunction\left(\mappingVector^\top \designVector_i\right)\right)
\designVector_i.
$$
and the stochastic gradient update for logistic regression (with mini-batch size set to 1) is
$$
\mappingVector_\text{new} \leftarrow \mappingVector_\text{old} - \eta ((1-\dataScalar_i)\left(\transformationFunction\left(\mappingVector^\top \designVector_i\right)\right) - \dataScalar_i\left(1-\transformationFunction\left(\mappingVector^\top \designVector_i\right)\right)
\designVector_i)
$$
The difference between the two is that for the perceptron we are using the Heaviside function, $\heaviside(\cdot)$, whereas for logistic regression we're using the sigmoid, $\transformationFunction(\cdot)$, which is like a soft version of the Heaviside function.

\setupplotcode{import matplotlib.pyplot as plt
import mlai
import mlai.plot}

\plotcode{fig, ax = plt.subplots(figsize=plot.two_figsize)
f = np.linspace(-8, 8, 100)
h = 1/(1+np.exp(-f))
H = np.zeros(100)
H[51:] = 1.0
ax.plot(f, h, 'r-', lw=3)
ax.plot(f, H, 'b-', lw=3)

ax.set_title('Sigmoid vs Heaviside Function', fontsize=20)
ax.set_xlabel('$f_i$', fontsize=20)
ax.set_ylabel('$h_i$', fontsize=20)
mlai.write_figure('sigmoid-heaviside.svg', directory='\writeDiagrams/ml', transparent=True)
}

\notes{When $\pi(\inputVector_i)=\transformationFunction(>0.5$ we classify as the positive class, when $\piJust like the peceptron, the vector $\mappingVector$ gives the 

\endif

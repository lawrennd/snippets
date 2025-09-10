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

\notes{Because $\pi(\designVector_i)=\transformationFunction(\designVector_i)$, when $\transformationFunction(\designVector_i)>0.5$ we classify as the positive class, otherwise we classify as the negative class. So the decision boundary is just like the peceptron. The vector $\mappingVector$ gives the normal vector for the decision boundary.}

\notes{In two dimensions, in the linear basis, the prediction function is 
$$
\transformationFunction\left(w_1 \inputScalar_{i, 1} + w_2 \inputScalar_{i, 2} + b\right)
$$
and the equation of a plane is 
$$
w_1 \inputScalar_{i, 1} + w_2 \inputScalar_{i, 2} + b = 0
$$ 
or
$$
w_1 \inputScalar_{i, 1} + w_2 \inputScalar_{i, 2} = -b.
$$ 
}

\notes{We can mirror the way we implemented the Perceptron by selecting a point, $i$, at random and setting the logistic regression weights to that point, $\mappingVector = \designVector_i$, if it is in the positive class, and setting to $\mappingVector = -\designVector_i$ if it is in the negatvie class. That guarantees that the selected point will be correctly classified.}

\code{def init_logistic_regression(phi_plus, phi_minus, seed=1000001):
    """
    Initialise the perceptron algorithm with random weights and bias.
    
    The perceptron is a simple binary classifier that learns a linear decision boundary.
    This function initialises the weight vector w and bias b by randomly selecting
    a point from either the positive or negative class and setting the normal vector
    accordingly.
    
    Mathematical formulation:
    The perceptron decision function is f(x) = w^T φ, where:
    - w is the weight vector (normal to the decision boundary)
    - φ is the design matrix vector
    
    :param phi_plus: Positive class data points, shape (n_plus, n_features)
    :type phi_plus: numpy.ndarray
    :param phi_minus: Negative class data points, shape (n_minus, n_features)
    :type phi_minus: numpy.ndarray
    :param seed: Random seed for reproducible initialisation
    :type seed: int, optional
    :returns: Initial weight vector, shape (n_features,)
    :rtype: numpy.ndarray
    :returns: Initial bias term
    :rtype: float
    :returns: The randomly selected point used for initialisation
    :rtype: numpy.ndarray
    
    Examples:
        >>> phi_plus = np.array([[1, 1, 2], [1, 2, 3], [1, 3, 4]])
        >>> phi_minus = np.array([[1, 0, 0], [1, 1, 0], [1, 0, 1]])
        >>> w, phi_select = init_logistic_regression(phi_plus, phi_minus)
        >>> print(f"Weight vector: {w}")
    """
    np.random.seed(seed=seed)
    # flip a coin (i.e. generate a random number and check if it is greater than 0.5)
    plus_portion = phi_plus.shape[0]/(phi_plus.shape[0] + phi_minus.shape[0])
    choose_plus = np.random.rand(1)<plus_portion
    if choose_plus:
        # generate a random point from the positives
        index = np.random.randint(0, phi_plus.shape[0])
        phi_select = phi_plus[index, :]
        w = phi_plus[index, :].astype(float)  # set the normal vector to plus that point
    else:
        # generate a random point from the negatives
        index = np.random.randint(0, phi_minus.shape[0])
        phi_select = phi_minus[index, :]
        w = -phi_minus[index, :].astype(float)  # set the normal vector to minus that point.
    return w, phi_select}
	
\plotcode{def init_logistic_regression_plot(f, ax, phi_plus, phi_minus, w, fontsize=18):
    """
    Initialize a plot for showing the logistic decision boundary.

    :param f: Matplotlib figure object.
    :param ax: Array of matplotlib axes (should have 2 axes).
    :param phi_plus: Positive class design points (numpy array).
    :param phi_minus: Negative class design  points (numpy array).
    :param w: Weight vector for the logistic regression.
    :param fontsize: Font size for labels and titles (default: 18).
    :returns: Dictionary containing plot handles for updating.
    """
    h = {}

    ax[0].set_aspect('equal')
    # Plot the data again
    ax[0].plot(phi_plus[:, 1], phi_plus[:, 2], 'rx')
    ax[0].plot(phi_minus[:, 1], phi_minus[:, 2], 'go')
    plot_limits = {}
    plot_limits['x'] = np.asarray(ax[0].get_xlim())
    plot_limits['y'] = np.asarray(ax[0].get_ylim())
    x0, x1 = plot.hyperplane_coordinates(w[1:], w[0], plot_limits)
    strt = -w[0]/w[2]

    norm = w[1]*w[1] + w[2]*w[2]
    offset0 = -w[1]/norm*w[0]
    offset1 = -w[2]/norm*w[0]
    h['arrow'] = ax[0].arrow(offset0, offset1, offset0+w[1], offset1+w[2], head_width=0.2)
    # plot a line to represent the separating 'hyperplane'
    h['plane'], = ax[0].plot(x0, x1, 'b-')
    ax[0].set_xlim(plot_limits['x'])
    ax[0].set_ylim(plot_limits['y'])
    ax[0].set_xlabel('$x_0$', fontsize=fontsize)
    ax[0].set_ylabel('$x_1$', fontsize=fontsize)
    h['iter'] = ax[0].set_title('Update 0')
    
    bins = 15
    f_minus = np.dot(phi_minus, w)
    f_plus = np.dot(phi_plus, w)
    ax[1].hist(f_plus, bins, alpha=0.5, label='+1', color='r')
    ax[1].hist(f_minus, bins, alpha=0.5, label='-1', color='g')
    ax[1].legend(loc='upper right')
    return h
}	


\setupplotcode{import mlai.plot as plot}

\plotcode{f, ax = plt.subplots(1, 2, figsize=(14,7))
w, phi_select = init_logistic_regression(phi_plus, phi_minus)
handle = init_logistic_regression_plot(f, ax, phi_plus, phi_minus, w)
mlai.write_figure("logistic-regression_init.svg", directory="\writeDiagramsDir/ml")}

\notes{Learning then proceeds }

\code{def logistic(x):
    """
	Compute the logistic function.
	"""
	return 1/(1+np.exp(x))
	
def update_logistic_regression(w, phi_plus, phi_minus, learn_rate):
    """
    Update the logistic regression weights and bias using stochastic gradient descent.
    
    This function implements one step of the perceptron learning algorithm.
    It randomly selects a training point and updates the weights if the point
    is misclassified.
    
    Mathematical formulation:
    The perceptron update rule is:
    - If y_i = +1 and w^T φ_i ≤ 0: w ← w + η    h(w^Tφ_i) φ_i
    - If y_i = -1 and w^T φ_i > 0: w ← w - η (1-h(w^Tφ_i))φ_i
    
    where η is the learning rate.
    
    :param w: Current weight vector, shape (n_features,)
    :type w: numpy.ndarray
    :param phi_plus: Positive class design matrix, shape (n_plus, n_features)
    :type phi_plus: numpy.ndarray
    :param phi_minus: Negative class design matrix, shape (n_minus, n_features)
    :type phi_minus: numpy.ndarray
    :param learn_rate: Learning rate (step size) for weight updates
    :type learn_rate: float
    :returns: Updated weight vector
    :rtype: numpy.ndarray
    :returns: Updated bias term
    :rtype: float
    :returns: The randomly selected point used for the update
    :rtype: numpy.ndarray
    :returns: True if weights were updated, False otherwise
    :rtype: bool
    
    Examples:
        >>> w = np.array([0.1 0.5, -0.3])
        >>> phi_plus = np.array([[1, 1, 2], [1, 2, 3]])
        >>> phi_minus = np.array([[1, 0, 0], [1, 1, 0]])
        >>> w_new, phi_select, updated = update_perceptron(w, phi_plus, phi_minus, 0.1)
    """
    # select a point at random from the data
	plus_portion = phi_plus.shape[0]/(phi_plus.shape[0] + phi_minus.shape[0])
    choose_plus = np.random.rand(1)<plus_portion
    updated=False
    if choose_plus:
        # choose a point from the positive data
        index = np.random.randint(phi_plus.shape[0])
        phi_select = phi_plus[index, :]
		a = np.dot(w, phi_select)
        if np.dot(w, phi_select) <= 0.:
            # point is currently incorrectly classified
            w += learn_rate*logistic(a)*phi_select
            updated=True
    else:
        # choose a point from the negative data
        index = np.random.randint(phi_minus.shape[0])
        phi_select = phi_minus[index, :]
		a = np.dot(w, phi_select)
        if a > 0.:
            # point is currently incorrectly classified
            w -= learn_rate*(1-logistic(a))*phi_select
    return w, phi_select}


	
\plotcode{def update_logistic_plot(h, f, ax, phi_plus, phi_minus, i, w):
    """
    Update plots after decision boundary has changed.

    :param h: Dictionary containing plot handles from init_logistic_regression.
    :param f: Matplotlib figure object.
    :param ax: Array of matplotlib axes.
    :param phi_plus: Positive class data points.
    :param phi_minus: Negative class data points.
    :param i: Current iteration number.
    :param w: Updated weight vector.
    """
    # Re-plot the hyper plane 
    plot_limits = {}
    plot_limits['x'] = np.asarray(ax[0].get_xlim())
    plot_limits['y'] = np.asarray(ax[0].get_ylim())
    x0, x1 = plot.hyperplane_coordinates(w[1:], w[0], plot_limits)

    # Add arrow to represent hyperplane.
    h['arrow'].remove()
    del(h['arrow'])
    norm = (w[1]*w[1] + w[2]*w[2])
    offset0 = -w[1]/norm*w[0]
    offset1 = -w[2]/norm*w[0]
    h['arrow'] = ax[0].arrow(offset0, offset1, offset0+w[1],
                             offset1+w[2], head_width=0.2)
    
    h['plane'].set_xdata(x0)
    h['plane'].set_ydata(x1)

    h['iter'].set_text('Iteration ' + str(i))
    ax[1].cla()
    bins = 15
    f_minus = np.dot(phi_minus, w)
    f_plus = np.dot(phi_plus, w)
    ax[1].hist(f_plus, bins, alpha=0.5, label='+1', color='r')
    ax[1].hist(f_minus, bins, alpha=0.5, label='-1', color='g')
    ax[1].legend(loc='upper right')

    IPython.display.display(f)
    IPython.display.clear_output(wait=True)
    return h
	
}

\setupplotcode{import IPython
import mlai
import mlai.plot
import matplotlib.pyplot as plt}

\plotcode{diagrams = '\writeDiagramsDir/ml'
seed = 42
max_iters = 30
learn_rate = 0.01
w, phi_select = init_logistic_regression(phi_plus, phi_minus, seed=seed)
count = 0
iterations = 0
setup=True
f2, ax2 = plt.subplots(1, 2, figsize=plot.two_figsize)
handle = init_logistic_regression_plot(f2, ax2, phi_plus, phi_minus, w)
handle['plane'].set_visible(False)
handle['arrow'].set_visible(False)
handle['circle'] = plt.Circle((phi_select[0], phi_select[1]), 0.25, color='b', fill=False)
ax2[0].add_artist(handle['circle'])
mlai.write_figure(figure=f2, filename='logistic-regression{samp:0>3}.svg'.format(samp=count), directory=diagrams, transparent=True)
extent = ax2[0].get_window_extent().transformed(f2.dpi_scale_trans.inverted())
mlai.write_figure(figure=f2, filename='logistic-regression{samp:0>3}.png'.format(samp=count), directory=diagrams, bbox_inches=extent, transparent=True)
count += 1
handle['plane'].set_visible(True)
handle['arrow'].set_visible(True)
mlai.write_figure(figure=f2, filename='logistic-regression{samp:0>3}.svg'.format(samp=count), directory=diagrams, transparent=True)
mlai.write_figure(figure=f2, filename='logistic-regression{samp:0>3}.png'.format(samp=count), directory=diagrams, bbox_inches=extent, transparent=True)

while iterations<max_iters:
    iterations += 1
    w, phi_select = update_logistic_regression(w, phi_plus, phi_minus, learn_rate)
    count+=1
    handle['circle'].center = phi_select[1], phi_select[2]
    mlai.write_figure(figure=f2, filename='logistic-regression{samp:0>3}.svg'.format(samp=count), directory=diagrams, transparent=True)     
    mlai.write_figure(figure=f2, filename='logistic-regression{samp:0>3}.png'.format(samp=count), bbox_inches=extent, directory=diagrams, transparent=True)        
    count+=1
    handle = update_logistic_plot(handle, f2, ax2, phi_plus, phi_minus, iterations, w)
    mlai.write_figure(filename='logistic-regression{samp:0>3}.svg'.format(samp=count),
                      figure=f2,
                      directory=diagrams,
                      transparent=True)
    mlai.write_figure(filename='logistic-regression{samp:0>3}.png'.format(samp=count),
                      figure=f2, 
                      directory=diagrams,
                      bbox_inches=extent,
                      transparent=True)
print('Data passes:', iterations)
}

\setupdisplaycode{import notutils as nu}
\displaycode{nu.display_plots('logistic-regression{samp:0>3}.svg', directory='\writeDiagramsDir/ml', samp=(0, count))}

\slides{
\define{width}{60%}
\startanimation{logistic-regression}{0}{14}
\newframe{\includediagram{\diagramsDir/ml/logistic-regression000}{\width}}{logistic-regression}
\newframe{\includediagram{\diagramsDir/ml/logistic-regression001}{\width}}{logistic-regression}
\newframe{\includediagram{\diagramsDir/ml/logistic-regression002}{\width}}{logistic-regression}
\newframe{\includediagram{\diagramsDir/ml/logistic-regression003}{\width}}{logistic-regression}
\newframe{\includediagram{\diagramsDir/ml/logistic-regression004}{\width}}{logistic-regression}
\newframe{\includediagram{\diagramsDir/ml/logistic-regression005}{\width}}{logistic-regression}
\newframe{\includediagram{\diagramsDir/ml/logistic-regression006}{\width}}{logistic-regression}
\newframe{\includediagram{\diagramsDir/ml/logistic-regression007}{\width}}{logistic-regression}
\newframe{\includediagram{\diagramsDir/ml/logistic-regression008}{\width}}{logistic-regression}
\newframe{\includediagram{\diagramsDir/ml/logistic-regression009}{\width}}{logistic-regression}
\newframe{\includediagram{\diagramsDir/ml/logistic-regression010}{\width}}{logistic-regression}
\newframe{\includediagram{\diagramsDir/ml/logistic-regression011}{\width}}{logistic-regression}
\newframe{\includediagram{\diagramsDir/ml/logistic-regression012}{\width}}{logistic-regression}
\newframe{\includediagram{\diagramsDir/ml/logistic-regression013}{\width}}{logistic-regression}
\newframe{\includediagram{\diagramsDir/ml/logistic-regression014}{\width}}{logistic-regression}
\endanimation
}

\notes{\figure{\includediagram{\diagramsDir/ml/logistic-regression014}{60%}}{The logistic-regression decision boundary.}{logistic-regression-decision-boundary}}

\endif

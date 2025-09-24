\ifndef{basisToNeuralNetworksJax}
\define{basisToNeuralNetworksJax}

\editme

\subsection{Shallow and Deep Learning}

\notes{So far, we have been talking about *linear models* or *shallow learning* as we might think of it. Let's pause for a moment and consider a *fully connected* deep neural network model to relate the two ideas.}

\subsection{From Basis Functions to Neural Networks}

\newslide{Neural Network Prediction Function}

\notes{Under our basis function perspective, we can see that our deep neural network is mathematical composition of basis function models. Each layer contains a separate basis function set, so}
$$
\mappingFunction(\inputVector; \mappingMatrix) = \mappingVector_4 ^\top\basisFunction\left(\mappingMatrix_3 \basisFunction\left(\mappingMatrix_2\basisFunction\left(\mappingMatrix_1 \inputVector\right)\right)\right).
$$

\notes{In this course there are two reasons for looking at the shallow model. Firstly, it is easier to introduce the concepts of regularisation in the linear model regime. Secondly, the matrix forms we see, e.g., expressions like $\basisMatrix^\top \basisMatrix$, appear in both models.}

\notes{For deep learning, we can no longer optimise the parameters of the model through solving a linear system[^quadratic]. Instead, we need to turn to non-linear optimisation algorithms. For deep learning, that's typically stochastic gradient descent.

[^quadratic]: Apart from the last layer of parmeters in models with quadratic loss functions.}

\notes{While it's possible to compute the Hessian in a neural network, @Bishop-exact92, we also find that it varies across the parameter space and will not normally be positive definite. In practice, the number of parameters is normally so large that storing the Hessian is impossible (it has quadratic cost in the number of weights/parameters) due to memory constraints.}

\notes{This means that while the theory of minima in optimisation is well understood, empirical experiments with large neural networks are hard and the lessons of small models do not all translate to the very large systems.}

\notes{We can stay within the framework of linear models but take a step closer to neural network models by introducing functions that are non-linear in the inputs, $\inputVector$, known as *basis functions*.}

\notes{In our session on basis funcitons we showed how linear models can be used to create non linear prediction functions. Amoung the basis functions we considered were the ReLU basis function.}

\loadcode{Model}{mlai}
\loadcode{linear_activation}{mlai}
\loadcode{sigmoid_activation}{mlai}
\loadcode{relu_activation}{mlai}

\loadcode{NeuralNetwork}{mlai}

\subsection{Linear Models as Basis + Weights}

\notes{The generalised linear models we work with allow us to create a model that is non-linear in inputs, but linear in the parameters,
$$
\mappingFunction(\inputVector_i) = \mappingVector^\top \basisFuncVector(\inputVector_i).
$$
We defined a basis, such as the quadratic basis.}

\loadcode{quadratic_basis}{mlai}

\setupplotcode{import matplotlib
# Comment for google colab (no latex available)
matplotlib.rc('text', usetex=True)
matplotlib.rcParams['text.latex.preamble']=[r"\usepackage{amsmath}"]}

\setupplotcode{import mlai.plot as plot}
\plotcode{def deep_nn(diagrams='../diagrams'):
    """Draw a deep neural network."""
    model = plot.network()
    model.add_layer(layer(width=4, label='\inputScalar_{index}',
                    observed=True, text=r'given $\inputVector$'))
    model.add_layer(layer(width=8, label='\hiddenScalar_{1, {index}}',
                    text=r'$\hiddenVector_1=\basisVector\left(\mappingMatrix_1\inputVector \right)$'.replace('\', '\\')))
    model.add_layer(layer(width=1, label='\dataScalar',
                    text=r'$\mappingFunction_2 =\mappingVector_2^\top\hiddenVector_1$'.repalce('\', '\\'),
                    observed=True))
    fig, ax = model.draw()
    ma.write_figure('neural-network.svg',
                      directory=diagrams,
                      figure=fig,
                      transparent=True)

    new_text = ['', '', '', '', '']
    for i, text in enumerate(new_text):
        model.layers[i].text=text
    fig, ax = model.draw()
    ma.write_figure('neural-network.svg',
                      directory="\writeDiagramsDir/ml',
                      figure=fig,
                      transparent=True)}

\figure{\includediagram{\diagramsDir/ml/neural-network}{70%}}{A neural network. Input nodes are shown at the bottom. The hidden layer is the result of applying an affine transformation to the input layer and placing through an activation function.}{deep-neural-network}}

\addreading{Bishop-deeplearning24}{Chapter 8}


\endif


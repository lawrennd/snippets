\ifndef{basisToNeuralNetworks}
\define{basisToNeuralNetworks}

\editme

\subsection{From Basis Functions to Neural Networks}

\notes{So far, we have been talking about *linear models* or *shallow learning* as we might think of it. Let's pause for a moment and consider a *fully connected* deep neural network model to relate the two ideas.}

\slides{* So far: linear models or "shallow learning"
* Consider instead function composition or "deep learning"}

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

\code{from mlai.neural_networks import Activation}

\loadcode{LinearActivation}{mlai.neural_networks}
\loadcode{SigmoidActivation}{mlai.neural_networks}
\loadcode{ReLUActivation}{mlai.neural_networks}

\setupcode{from mlai.models import Model}
\loadcode{NeuralNetwork}{mlai.neural_networks}

\subsection{Linear Models as Basis + Weights}

\notes{The generalised linear models we work with allow us to create a model that is non-linear in inputs, but linear in the parameters,}
$$
\mappingFunction(\inputVector_i) = \mappingVector^\top \basisFuncVector(\inputVector_i).
$$
\notes{We defined a basis, such as the polynomial basis.}

\loadcode{polynomial}{mlai.linear_models}

\installcode{daft}

\setupplotcode{import matplotlib.pyplot as plt
import shutil

if shutil.which('latex') is None:
    plt.rcParams['text.usetex'] = False
else:
    plt.rcParams['text.usetex'] = True
    plt.rcParams['text.latex.preamble']=r'\usepackage{amsmath}'

plt.rcParams.update({'font.size': 22})}

\setupplotcode{import mlai.plot as plot}

\plotcode{plot.neural_network(directory="\writeDiagramsDir/ml/")}

\
\figure{\includediagram{\diagramsDir/ml/neural-network}{70%}}{A neural network. Input nodes are shown at the bottom. The hidden layer is the result of applying an affine transformation to the input layer and placing through an activation function.}{deep-neural-network}

\addreading{Bishop-deeplearning24}{Chapter 8}


\endif


\ifndef{classification}
\define{classification}

\include{_ml/includes/classification-intro.md}
\include{_ml/includes/classification-examples.md}

\editme

\subsection{Hyperplane}

\notes{The objective of classification is to predict the class the class label, $\dataScalar_i$, given the features associated with that data point, $\inputVector_i$, using the *prediction function*. If we are using a linear model, then we can define the prediction function as}\slides* Predict class label $\dataScalar_i$
* Using data features $\inputVector_i$
* Through the prediction function}
$$
\mappingFunction(\inputScalar_i) = \text{sign}\left(\mappingVector^\top \inputVector_i + b\right)\notes{,}
$$
\notes{where the prediction here is `+1` for the positive class and `-1` for the negative class.}

\notes{In this linear model the decision boundary for classification is given by a *hyperplane*. The vector, $\mappingVector$, is the *[normal vector](http://en.wikipedia.org/wiki/Normal_(geometry))* to the hyperplane. Any hyperplane can be described by formula $\mappingVector^\top \inputVector = -b$.}

\notes{Note that this is the same linear form that underpins *linear regression* but here it is being used to define the hyperplane rather than the regression weights}

\newslide{Hyperplane}

\slides{* Boundary for classification given by hyperplane
* Hyperplane defined by the *normal vector* $\mappingVector$.
$$
\mappingVector^\top \inputVector = -b
$$
}

\subsection{Toy Data}

\notes{We'll consider a toy data set and a decision boundary that separates red crosses from green circles.}
\slides{
- Red crosses (+ve) and green circles (-ve).}

\setupcode{import numpy as np}

\code{np.random.seed(seed=1000001)
x_plus = np.random.normal(loc=1.3, size=(30, 2))
x_minus = np.random.normal(loc=-1.3, size=(30, 2))}


\setupplotcode{import mlai
import mlai.plot as plot
import matplotlib.pyplot as plt}

\plotcode{# plot data
fig, ax = plt.subplots(figsize=plot.big_figsize)
ax.plot(x_plus[:, 0], x_plus[:, 1], 'rx')
ax.plot(x_minus[:, 0], x_minus[:, 1], 'go')

plt.tight_layout()
mlai.write_figure("artificial-classification-example.svg", directory="\writeDiagramsDir/ml")}

\figure{\includediagram{\diagramsDir/ml/artificial-classification-example}{80%}}{Red crosses and green circles are sampled from two separate Gaussian distributions with 30 examples of each.}{artificial-classification-examples}


\endif

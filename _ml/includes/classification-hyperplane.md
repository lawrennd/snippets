\ifndef{classificationHyperplane}
\define{classificationHyperplane}

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


\endif

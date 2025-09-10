\ifndef{logisticRegressionPredictionFunction}
\define{logisticRegressionPredictionFunction}

\editme


\subsection{Prediction Function}

\notes{Now we have the basis function let's define the prediction function.}

\setupcode{import numpy as np}
\code{def predict(w, x, basis=mlai.linear, **kwargs):
    "Generates the prediction function and the basis matrix."
    Phi = basis(x, **kwargs)
    f = np.dot(Phi, w)
    return 1./(1+np.exp(-f)), Phi}

\notes{This inverse of the link function is known as the
[logistic](http://en.wikipedia.org/wiki/Logistic_function) (thus the
name logistic regression) or sometimes it is called the sigmoid
function. For a particular value of the input to the link function,
$\mappingFunction_i = \mappingVector^\top
\basisVector(\inputVector_i)$ we can plot the value of the inverse
link function as below.}

\notes{By replacing the inverse link with the sigmoid we can write $\pi$ as a
function of the input and the parameter vector as,
$$
\pi(\inputVector,\mappingVector) = \frac{1}{1+\exp\left(-\mappingVector^\top \basisVector(\inputVector)\right)}.
$$
The process for logistic regression is as follows. Compute the output
of a standard linear basis function composition ($\mappingVector^\top
\basisVector(\inputVector)$, as we did for linear regression) and then
apply the inverse link function, $g(\mappingVector^\top
\basisVector(\inputVector))$.  In logistic regression this involves
*squashing* it with the logistic (or sigmoid) function. Use this
value, which now has an interpretation as a *probability* in a
Bernoulli distribution to form the likelihood. Then we can assume
conditional independence of each data point given the parameters and
develop a likelihod for the entire data set.}

\notes{The Bernoulli likelihood is of the form,
$$
P(\dataScalar_i|\mappingVector, \inputVector) =
\pi_i^{\dataScalar_i} (1-\pi_i)^{1-\dataScalar_i}
$$
which we can think of as clever trick for mathematically switching
between two probabilities if we were to write it as code it would be
better described as

```python
def bernoulli(x, y, pi):
    if y == 1:
        return pi(x)
    else:
        return 1-pi(x)
```
but writing it mathematically makes it easier to write our objective
function within a single mathematical equation.}


\slides{Prediction Function}

\slides{
* Can write $\pi$ as a function of input, parameters, 
  $$\pi(\inputVector,\mappingVector) = \frac{1}{1+
\exp\left(-\mappingVector^\top \basisVector(\inputVector)\right)}.$$
* Compute the output $\mappingVector^\top \basisVector(\inputVector)$
* Apply inverse link function, $\transformationFunction(\mappingVector^\top \basisVector(\inputVector))$. 
* Use this value in a Bernoulli distribution to form the likelihood.
}

\newslide{Bernoulli Reminder}

\slides{
* From last time 
  $$P(\dataScalar_i|\mappingVector, \inputVector) = \pi_i^{\dataScalar_i} (1-\pi_i)^{1-\dataScalar_i}$$

* Trick for switching betwen probabilities

```python
def bernoulli(y, pi):
    if y == 1:
        return pi
    else:
return 1-pi
```
}

\endif

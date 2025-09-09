\ifndef{logisticRegression}
\define{logisticRegression}

\editme

\subsection{Logistic Regression}

\addreading{@Rogers:book11}{Section 5.2.2 up to pg 182}

\notes{A logistic regression is an approach to classification which
extends the linear regression models we've already
explored. Rather than modeling the output of the function directly the
assumption is that we model the *log-odds* with the basis functions.}

\slides{
* Modelling entire density allows any question to be answered
* Also handles missing data
* Comes at possible expense of *strong* assumptions about data generation distribution
}

\newslide{Logistic Regression}

\slides{
* In regression we model probability of $\dataScalar_i |\inputVector_i$ directly
* Allows less flexibility in questions, but more flexibility in model assumptions
}

\notes{The [odds](http://en.wikipedia.org/wiki/Odds) are defined as
the ratio of the probability of a positive outcome, to the probability
of a negative outcome. Just as we saw in our jumper (sweater) example where
$$ 
\log \frac{p(\text{bought})}{p(\text{not bought})} = \weightScalar_0 + \weightScalar_1 \text{age} + \weightScalar_2 \text{latitude} 
$$
If the probability of a positive outcome is denoted by $\pi$, then the odds are computed as
$\frac{\pi}{1-\pi}$. 

Odds are widely used by
[bookmakers](http://en.wikipedia.org/wiki/Bookmaker) in gambling,
although a bookmakers odds won't normalise: i.e. if you look at the
equivalent probabilities, and sum over the probability of all outcomes
the bookmakers are considering, then you won't get one. This is how
the bookmaker makes a profit.  Because a probability is always between
zero and one, the odds are always between $0$ and $\infty$. If the
positive outcome is unlikely the odds are close to zero, if it is very
likely then the odds become close to infinite. Taking the logarithm of
the odds maps the odds from the positive half space to being across
the entire real line. Odds that were between 0 and 1 (where the
negative outcome was more likely) are mapped to the range between
$-\infty$ and $0$. Odds that are greater than 1 are mapped to the
range between $0$ and $\infty$. Considering the log odds therefore
takes a number between 0 and 1 (the probability of positive outcome)
and maps it to the entire real line. The function that does this is
known as the [logit function](http://en.wikipedia.org/wiki/Logit),
$\linkFunction(p_i) = \log\frac{p_i}{1-p_i}$. This function is known as a
*link function*.}

\newslide{Log Odds - 1}
\slides{
* Model the *log-odds* with basis functions
* [Odds](http://en.wikipedia.org/wiki/Odds) are ratio of probability of positive vs negative outcome
}

\newslide{Log Odds - 2} 
\slides{
* Probability is between zero and one
* Odds are: $$ \frac{\pi}{1-\pi} $$
}

\newslide{Log Odds - 3}
\slides{
* Odds are between $0$ and $\infty$
* Logarithm of odds maps them to $-\infty$ to $\infty$
}

\notes{For a standard regression we take,
$$
\mappingFunction(\inputVector) = \mappingVector^\top
\basisVector(\inputVector),
$$
if we want to perform classification we perform a logistic regression.
$$
\log \frac{\pi}{(1-\pi)} = \mappingVector^\top
\basisVector(\inputVector)
$$
where the odds ratio between the positive class and the negative class
is given by
$$
\frac{\pi}{(1-\pi)}
$$
The odds can never be negative, but can take any value from 0 to $\infty$. We have defined the link function as taking the form $g^{-1}(\cdot)$ implying that the inverse link function is given by $g(\cdot)$. Since we have defined,
$$
\linkFunction(\pi) =
\mappingVector^\top \basisVector(\inputVector)
$$
we can write $\pi$ in terms of
the *inverse link* function, $\transformationFunction(\cdot)$ as 
$$
\pi = \transformationFunction(\mappingVector^\top
\basisVector(\inputVector)).
$$}

\newslide{Logit Link Function - 1}
\slides{
* The [Logit function](http://en.wikipedia.org/wiki/Logit) is our link function
* $$\linkFunction(\pi_i) = \log\frac{\pi_i}{1-\pi_i}$$
}

\newslide{Logit Link Function - 2}
\slides{
* For standard regression:
* $$f(\inputVector_i) = \mappingVector^\top \basisVector(\inputVector_i)$$
}

\setupplotcode{import mlai.plot as plot}

\plotcode{plot.logistic('\writeDiagramsDir/ml/logistic.svg')}

\newslide{Logistic function - 3}
\slides{
* [Logistic](http://en.wikipedia.org/wiki/Logistic_function) (or sigmoid) squashes
real line to between 0  & 1. Sometimes also called a 'squashing function'.
\includediagram{\diagramsDir/ml/logistic}
}
\newslide{Logistic funciton - 4}

\slides{
* For classification (logistic regression):
* $$\log \frac{\pi_i}{1-\pi_i} = \mappingVector^\top \basisVector(\inputVector_i)$$
}

\notes{We'll define our prediction, objective and gradient functions below. But before we start, we need to define a basis function for our model. Let's start with the linear basis.

\setupcode{import numpy as np}
\loadcode{linear}{mlai}

\subsection{Prediction Function}

Now we have the basis function let's define the prediction function.

\setupcode{import numpy as np}
\code{def predict(w, x, basis=mlai.linear, **kwargs):
    "Generates the prediction function and the basis matrix."
    Phi = basis(x, **kwargs)
    f = np.dot(Phi, w)
    return 1./(1+np.exp(-f)), Phi}

This inverse of the link function is known as the
[logistic](http://en.wikipedia.org/wiki/Logistic_function) (thus the
name logistic regression) or sometimes it is called the sigmoid
function. For a particular value of the input to the link function,
$\mappingFunction_i = \mappingVector^\top
\basisVector(\inputVector_i)$ we can plot the value of the inverse
link function as below.

\include{_ml/includes/sigmoid-function.md}

By replacing the inverse link with the sigmoid we can write $\pi$ as a
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
develop a likelihod for the entire data set.

The Bernoulli likelihood is of the form,
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

\newslide{Prediction Function}

\slides{
* Can now write $\pi$ as a function of the input and the parameter vector as, 
  $$\pi(\inputVector,\mappingVector) = \frac{1}{1+
\exp\left(-\mappingVector^\top \basisVector(\inputVector)\right)}.$$
* Compute the output of a standard linear basis function composition ($\mappingVector^\top \basisVector(\inputVector)$, as we did for linear regression)
* Apply the inverse link function, $\transformationFunction(\mappingVector^\top \basisVector(\inputVector))$. 
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

\subsection{Maximum Likelihood}

\slides{
* Conditional independence of data:
  $$P(\dataVector|\mappingVector, \inputMatrix) = \prod_{i=1}^\numData P(\dataScalar_i|\mappingVector,
\inputVector_i). $$
}

\notes{To obtain the parameters of the model, we need to maximise the likelihood, or minimise the objective function, normally taken to be the negative log likelihood. With a data conditional independence assumption the likelihood has the form,
$$
P(\dataVector|\mappingVector,
\inputMatrix) = \prod_{i=1}^\numData P(\dataScalar_i|\mappingVector, \inputVector_i). 
$$
which can be written as a log likelihood in the form
$$
\log P(\dataVector|\mappingVector,
\inputMatrix) = \sum_{i=1}^\numData \log P(\dataScalar_i|\mappingVector, \inputVector_i) = \sum_{i=1}^\numData
\dataScalar_i \log \pi_i + \sum_{i=1}^\numData (1-\dataScalar_i)\log (1-\pi_i)
$$
and if we take the probability of positive outcome for the $i$th data point to be given by
$$
\pi_i = \transformationFunction\left(\mappingVector^\top \basisVector(\inputVector_i)\right),
$$
where $\transformationFunction(\cdot)$ is the *inverse* link function, then this leads to an objective function of the form,
$$
\errorFunction(\mappingVector) = -  \sum_{i=1}^\numData \dataScalar_i \log
\transformationFunction\left(\mappingVector^\top \basisVector(\inputVector_i)\right) -
\sum_{i=1}^\numData(1-\dataScalar_i)\log \left(1-\transformationFunction\left(\mappingVector^\top
\basisVector(\inputVector_i)\right)\right).
$$}

\newslide{Log Likelihood}
\slides{
$$\begin{align*}
  \log P(\dataVector|\mappingVector, \inputMatrix) = &
  \sum_{i=1}^\numData \log P(\dataScalar_i|\mappingVector, \inputVector_i) \\ = &\sum_{i=1}^\numData \dataScalar_i \log
  \pi_i \\ & + \sum_{i=1}^\numData (1-\dataScalar_i)\log (1-\pi_i)
\end{align*}$$
}


\setupcode{import numpy as np}
\code{def objective(h, y):
    "Computes the objective function."
	labs = np.asarray(y, dtype=float).flatten()
    posind = np.where(labs==1)
    negind = np.where(labs==0)
    return -np.log(h[posind, :]).sum() - np.log(1-h[negind, :]).sum()}

\notes{As normal, we would like to minimise this objective. This can be done
by differentiating with respect to the parameters of our prediction
function, $\pi(\inputVector;\mappingVector)$, for optimisation. The
gradient of the likelihood with respect to
$\pi(\inputVector;\mappingVector)$ is of the form,
$$
\frac{\text{d}\errorFunction(\mappingVector)}{\text{d}\mappingVector} = -\sum_{i=1}^\numData
\frac{\dataScalar_i}{\transformationFunction\left(\mappingVector^\top
\basisVector(\inputVector)\right)}\frac{\text{d}\transformationFunction(\mappingFunction_i)}{\text{d}\mappingFunction_i}
\basisVector(\inputVector_i) +  \sum_{i=1}^\numData
\frac{1-\dataScalar_i}{1-g\left(\mappingVector^\top
\basisVector(\inputVector)\right)}\frac{\text{d}g(\mappingFunction_i)}{\text{d}\mappingFunction_i}
\basisVector(\inputVector_i)
$$
where we used the chain rule to develop the derivative in terms of
$\frac{\text{d}\transformationFunction(\mappingFunction_i)}{\text{d}\mappingFunction_i}$,
which is the gradient of the inverse link function (in our case the
gradient of the sigmoid function).}

\notes{So the objective function now depends on the gradient of the inverse
link function, as well as the likelihood depends on the gradient of
the inverse link function, as well as the gradient of the log
likelihood, and naturally the gradient of the argument of the inverse
link function with respect to the parameters, which is simply
$\basisVector(\inputVector_i)$.}


\newslide{Objective Function}
\slides{
* Probability of positive outcome for the $i$th data point 
  $$\pi_i = \transformationFunction\left(\mappingVector^\top \basisVector(\inputVector_i)\right),$$
  where $\transformationFunction(\cdot)$ is the *inverse* link function
* Objective function of the form 
  $$\begin{align*}
    E(\mappingVector) = & -  \sum_{i=1}^\numData \dataScalar_i \log
    g\left(\mappingVector^\top \basisVector(\inputVector_i)\right) \\& -
    \sum_{i=1}^\numData(1-\dataScalar_i)\log \left(1-g\left(\mappingVector^\top
    \basisVector(\inputVector_i)\right)\right).
   \end{align*}$$
}

\newslide{Minimise Objective}
\slides{
* Grdient wrt  $\pi(\inputVector;\mappingVector)$
  $$\begin{align*}
  \frac{\text{d}\errorFunction(\mappingVector)}{\text{d}\mappingVector} = &
  -\sum_{i=1}^\numData \frac{\dataScalar_i}{\transformationFunction\left(\mappingVector^\top
  \basisVector(\inputVector)\right)}\frac{\text{d}\transformationFunction(\mappingFunction_i)}{\text{d}\mappingFunction_i}
  \basisVector(\inputVector_i) \\ & +  \sum_{i=1}^\numData
  \frac{1-\dataScalar_i}{1-\transformationFunction\left(\mappingVector^\top
  \basisVector(\inputVector)\right)}\frac{\text{d}\transformationFunction(\mappingFunction_i)}{\text{d}\mappingFunction_i}
  \basisVector(\inputVector_i)
  \end{align*}$$
}

\notes{The only missing term is the gradient of the inverse link
function. For the sigmoid squashing function we have,
$$\begin{align*}
\transformationFunction(\mappingFunction_i) &= \frac{1}{1+\exp(-\mappingFunction_i)}\\
&=(1+\exp(-\mappingFunction_i))^{-1}
\end{align*}$$
and the gradient can be computed as
$$\begin{align*}
\frac{\text{d}\transformationFunction(\mappingFunction_i)}{\text{d} \mappingFunction_i} & =
\exp(-\mappingFunction_i)(1+\exp(-\mappingFunction_i))^{-2}\\
& = \frac{1}{1+\exp(-\mappingFunction_i)}
\frac{\exp(-\mappingFunction_i)}{1+\exp(-\mappingFunction_i)} \\
& = \transformationFunction(\mappingFunction_i) (1-g(\mappingFunction_i))
\end{align*}$$
so the full gradient can be written down as
$$
\frac{\text{d}\errorFunction(\mappingVector)}{\text{d}\mappingVector} = -\sum_{i=1}^\numData
\dataScalar_i\left(1-\transformationFunction\left(\mappingVector^\top \basisVector(\inputVector)\right)\right)
\basisVector(\inputVector_i) +  \sum_{i=1}^\numData
(1-\dataScalar_i)\left(\transformationFunction\left(\mappingVector^\top \basisVector(\inputVector)\right)\right)
\basisVector(\inputVector_i).
$$

\setupcode{import numpy as np}
\code{def gradient(h, Phi, y):
    "Generates the gradient of the parameter vector."
	labs = np.asarray(y, dtype=float).flatten()
    posind = np.where(labs==1)
    dw = -(Phi[posind]*(1-g[posind])).sum(0)
    negind = np.where(labs==0 )
    dw += (Phi[negind]*h[negind]).sum(0)
    return dw[:, None]}

\subsection{Optimisation of the Function}

Reorganising the gradient to find a stationary point of the function
with respect to the parameters $\mappingVector$ turns out to be
impossible. Optimisation has to proceed by *numerical
methods*. Options include the multidimensional variant of
[Newton's method](http://en.wikipedia.org/wiki/Newton%27s_method) or
[gradient based optimisation methods](http://en.wikipedia.org/wiki/Gradient_method)
like we used for optimising matrix factorisation for the movie
recommender system. We recall from matrix factorisation that, for
large data, *stochastic gradient descent* or the Robbins Munro
[@Robbins:stoch51] optimisation procedure worked best for function
minimisation.}

\newslide{Link Function Gradient}
\slides{
* Also need gradient of inverse link function wrt parameters.
\begin{aligned}
\transformationFunction(\mappingFunction_i) &= \frac{1}{1+\exp(-\mappingFunction_i)}\\
&=(1+\exp(-\mappingFunction_i))^{-1}
\end{aligned}
and the gradient can be computed as
\begin{aligned}
\frac{\text{d}\transformationFunction(\mappingFunction_i)}{\text{d} \mappingFunction_i} & =
\exp(-\mappingFunction_i)(1+\exp(-\mappingFunction_i))^{-2}\\
& = \frac{1}{1+\exp(-\mappingFunction_i)}
\frac{\exp(-\mappingFunction_i)}{1+\exp(-\mappingFunction_i)} \\
& = \transformationFunction(\mappingFunction_i) (1-\transformationFunction(\mappingFunction_i))
\end{aligned}
}

\newslide{Objective Gradient}
\slides{
\begin{aligned}
\frac{\text{d}E(\mappingVector)}{\text{d}\mappingVector} = & -\sum_{i=1}^\numData
\dataScalar_i\left(1-\transformationFunction\left(\mappingVector^\top \basisVector(\inputVector)\right)\right)
\basisVector(\inputVector_i) \\ & + \sum_{i=1}^\numData
(1-\dataScalar_i)\left(\transformationFunction\left(\mappingVector^\top \basisVector(\inputVector)\right)\right)
\basisVector(\inputVector_i).
\end{aligned}
}

\newslide{Optimisation of the Function}
\slides{
* Can't find a stationary point of the objective function analytically.
* Optimisation has to proceed by *numerical methods*. 
    * [Newton's method](http://en.wikipedia.org/wiki/Newton%27s_method) or 
    * [gradient based optimisation methods](http://en.wikipedia.org/wiki/Gradient_method)
	* Iterative Reweighted Least Squares
* Similarly to matrix factorisation, for large data *stochastic gradient descent*  (Robbins Munro [@Robbins:stoch51] optimisation procedure) works well.
}

\endif

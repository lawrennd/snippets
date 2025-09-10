\ifndef{logisticRegressionIntro}
\define{logisticRegressionIntro}

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

\endif

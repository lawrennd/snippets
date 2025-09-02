\ifndef{regressionStochasticGradientDescent}
\define{regressionStochasticGradientDescent}

\editme

\subsection{Stochastic Gradient Descent}

* If $\numData$ is small, gradient descent is fine.
* But sometimes (e.g. on the internet $\numData$ could be a billion.
* Stochastic gradient descent is more similar to perceptron.
* Look at gradient of one data point at a time rather than summing across *all* data points) 
* This gives a stochastic estimate of gradient.

\subsection{Stochastic Gradient Descent}

* The real gradient with respect to $m$ is given by 

  $$\frac{\text{d}\errorFunction(m, c)}{\text{d} m} = -2\sum_{i=1}^\numData \inputScalar_i(\dataScalar_i -
m\inputScalar_i - c)$$

  but it has $\numData$ terms in the sum. Substituting in the gradient we can see that the full update is of the form

  $$m_\text{new} \leftarrow
m_\text{old} + 2\learnRate \left[\inputScalar_1 (\dataScalar_1 - m_\text{old}\inputScalar_1 - c_\text{old}) + (\inputScalar_2 (\dataScalar_2 -   m_\text{old}\inputScalar_2 - c_\text{old}) + \dots + (\inputScalar_n (\dataScalar_n - m_\text{old}\inputScalar_n - c_\text{old})\right]$$

  This could be split up into lots of individual updates
$$m_1 \leftarrow m_\text{old} + 2\learnRate \left[\inputScalar_1 (\dataScalar_1 - m_\text{old}\inputScalar_1 -
c_\text{old})\right]$$
$$m_2 \leftarrow m_1 + 2\learnRate \left[\inputScalar_2 (\dataScalar_2 -
m_\text{old}\inputScalar_2 - c_\text{old})\right]$$
$$m_3 \leftarrow m_2 + 2\learnRate
\left[\dots\right]$$
$$m_n \leftarrow m_{n-1} + 2\learnRate \left[\inputScalar_n (\dataScalar_n -
m_\text{old}\inputScalar_n - c_\text{old})\right]$$

which would lead to the same final update.

\subsection{Updating $c$ and $m$}

* In the sum we don't  $m$ and $c$ we use for computing the gradient term at each update. 
* In stochastic gradient descent we *do* change them.
* This means it's not quite the same as steepest desceint.
* But we  can present each data point in a random order, like we did for the
perceptron.
* This makes the algorithm suitable for large scale web use (recently this domain is know as 'Big Data') and algorithms like this are widely used by Google, Microsoft, Amazon, Twitter and Facebook.

\subsection{Stochastic Gradient Descent}

* Or more accurate, since the data is normally presented in a random order we just can write
  $$
  m_\text{new} = m_\text{old} + 2\learnRate\left[\inputScalar_i (\dataScalar_i - m_\text{old}\inputScalar_i - c_\text{old})\right]
  $$

\code{# choose a random point for the update 
i = np.random.randint(x.shape[0]-1)
# update m
m_star = m_star + 2*learn_rate*(x[i]*(y[i]-m_star*x[i] - c_star))
# update c
c_star = c_star + 2*learn_rate*(y[i]-m_star*x[i] - c_star)}

\subsection{SGD for Linear Regression}

Putting it all together in an algorithm, we can
do stochastic gradient descent for our regression data.

\plotcode{num_plots = plot.regression_contour_sgd(x, y, diagrams='\writeDiagramsDir/ml')}

\setupdisplaycode{import notutils as nu
from ipywidgets import IntSlider}
\setupdisplaycode{import notutils as nu}
\displaycode{nu.display_plots('regression_sgd_contour_fit{num:0>3}.svg', 
    directory='\writeDiagramsDir/ml', num=IntSlider(0, 0, num_plots, 1))}

\slides{
\startanimation{regression_sgd_contour_fit}{0}{58}
\newframe{\includediagram{\diagramsDir/ml/regression_sgd_contour_fit000}{\width}}{regression_sgd_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_sgd_contour_fit001}{\width}}{regression_sgd_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_sgd_contour_fit002}{\width}}{regression_sgd_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_sgd_contour_fit003}{\width}}{regression_sgd_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_sgd_contour_fit004}{\width}}{regression_sgd_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_sgd_contour_fit005}{\width}}{regression_sgd_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_sgd_contour_fit006}{\width}}{regression_sgd_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_sgd_contour_fit007}{\width}}{regression_sgd_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_sgd_contour_fit008}{\width}}{regression_sgd_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_sgd_contour_fit009}{\width}}{regression_sgd_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_sgd_contour_fit010}{\width}}{regression_sgd_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_sgd_contour_fit011}{\width}}{regression_sgd_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_sgd_contour_fit012}{\width}}{regression_sgd_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_sgd_contour_fit013}{\width}}{regression_sgd_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_sgd_contour_fit014}{\width}}{regression_sgd_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_sgd_contour_fit015}{\width}}{regression_sgd_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_sgd_contour_fit016}{\width}}{regression_sgd_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_sgd_contour_fit017}{\width}}{regression_sgd_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_sgd_contour_fit018}{\width}}{regression_sgd_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_sgd_contour_fit019}{\width}}{regression_sgd_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_sgd_contour_fit020}{\width}}{regression_sgd_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_sgd_contour_fit021}{\width}}{regression_sgd_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_sgd_contour_fit022}{\width}}{regression_sgd_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_sgd_contour_fit023}{\width}}{regression_sgd_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_sgd_contour_fit024}{\width}}{regression_sgd_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_sgd_contour_fit025}{\width}}{regression_sgd_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_sgd_contour_fit026}{\width}}{regression_sgd_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_sgd_contour_fit027}{\width}}{regression_sgd_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_sgd_contour_fit028}{\width}}{regression_sgd_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_sgd_contour_fit029}{\width}}{regression_sgd_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_sgd_contour_fit030}{\width}}{regression_sgd_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_sgd_contour_fit031}{\width}}{regression_sgd_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_sgd_contour_fit032}{\width}}{regression_sgd_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_sgd_contour_fit033}{\width}}{regression_sgd_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_sgd_contour_fit034}{\width}}{regression_sgd_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_sgd_contour_fit035}{\width}}{regression_sgd_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_sgd_contour_fit036}{\width}}{regression_sgd_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_sgd_contour_fit037}{\width}}{regression_sgd_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_sgd_contour_fit038}{\width}}{regression_sgd_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_sgd_contour_fit039}{\width}}{regression_sgd_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_sgd_contour_fit040}{\width}}{regression_sgd_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_sgd_contour_fit041}{\width}}{regression_sgd_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_sgd_contour_fit042}{\width}}{regression_sgd_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_sgd_contour_fit043}{\width}}{regression_sgd_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_sgd_contour_fit044}{\width}}{regression_sgd_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_sgd_contour_fit045}{\width}}{regression_sgd_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_sgd_contour_fit046}{\width}}{regression_sgd_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_sgd_contour_fit047}{\width}}{regression_sgd_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_sgd_contour_fit048}{\width}}{regression_sgd_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_sgd_contour_fit049}{\width}}{regression_sgd_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_sgd_contour_fit050}{\width}}{regression_sgd_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_sgd_contour_fit051}{\width}}{regression_sgd_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_sgd_contour_fit052}{\width}}{regression_sgd_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_sgd_contour_fit053}{\width}}{regression_sgd_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_sgd_contour_fit054}{\width}}{regression_sgd_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_sgd_contour_fit055}{\width}}{regression_sgd_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_sgd_contour_fit056}{\width}}{regression_sgd_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_sgd_contour_fit057}{\width}}{regression_sgd_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_sgd_contour_fit058}{\width}}{regression_sgd_contour_fit}
\endanimation
}

\notes{\figure{\includediagram{\diagramsDir/ml/regression_sgd_contour_fit058}{60%}}{Stochastic gradient descent for linear regression.}{regression-sgd-contour0fit-58}}

\endif

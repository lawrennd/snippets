\ifndef{regressionGradientDescent}
\define{regressionGradientDescent}

\editme

\subsection{Steepest Descent}

\slides{* Minimize the sum of squares error function. 
* One way of doing that is gradient descent. 
* Initialize with a guess for $m$ and $c$ 
* update that guess by subtracting a portion of the gradient from the guess. 
* Like walking down a hill in the steepest direction of the hill to get to the
bottom.}

\subsection{Algorithm}

* We start with a guess for $m$ and $c$.

\code{m_star = 0.0
c_star = -5.0}

\subsection{Offset Gradient}

* Now we need to compute the gradient of the error
function, firstly with respect to $c$,
    $$
	\frac{\text{d}\errorFunction(m, c)}{\text{d} c} = -2\sum_{i=1}^\numData (\dataScalar_i - m\inputScalar_i - c)
	$$

* This is computed in python as follows

\code{c_grad = -2*(y-m_star*x - c_star).sum()
print("Gradient with respect to c is ", c_grad)}

\subsection{Deriving the Gradient}

To see how the gradient was derived, first note that
the $c$ appears in every term in the sum. So we are just differentiating $(\dataScalar_i -
m\inputScalar_i - c)^2$ for each term in the sum. The gradient of this term with respect to
$c$ is simply the gradient of the outer quadratic, multiplied by the gradient
with respect to $c$ of the part inside the quadratic. The gradient of a
quadratic is two times the argument of the quadratic, and the gradient of the
inside linear term is just minus one. This is true for all terms in the sum, so
we are left with the sum in the gradient.

\subsection{Slope Gradient}

The gradient with respect tom $m$ is similar, but now the
gradient of the quadratic's argument is $-\inputScalar_i$ so the gradient with respect to
$m$ is

$$\frac{\text{d}\errorFunction(m, c)}{\text{d} m} = -2\sum_{i=1}^\numData \inputScalar_i(\dataScalar_i - m\inputScalar_i -
c)$$

which can be implemented in python (numpy) as

\code{m_grad = -2*(x*(y-m_star*x - c_star)).sum()
print("Gradient with respect to m is ", m_grad)}

\subsection{Update Equations}

* Now we have gradients with respect to $m$ and $c$.
* Can update our inital guesses for $m$ and $c$ using the gradient. 
* We don't want to just subtract the gradient from $m$ and $c$, 
* We need to take a *small* step in the gradient direction. 
* Otherwise we might overshoot the minimum. 
* We want to follow the gradient to get to the minimum, the gradient
changes all the time.

\subsection{Move in Direction of Gradient}

\setupplotcode{import mlai.plot as plot}
\plotcode{f, ax = plt.subplots(figsize=plot.big_figsize)
plot.regression_contour(f, ax, m_vals, c_vals, E_grid)
ax.plot(m_star, c_star, 'g*', markersize=20)
ax.arrow(m_star, c_star, -m_grad*0.1, -c_grad*0.1, head_width=0.2)
mlai.write_figure(filename='regression_contour_step001.svg', directory='\writeDiagramsDir/ml/', transparent=True)}

\figure{\includediagram{\diagramsDir/ml/regression_contour_step001}{60%}}{Single update descending the contours of the error surface for regression.}{regression-contour-step-1}

\subsection{Update Equations}

* The step size has already been introduced, it's again known as the learning rate and is denoted by $\learnRate$. 
  $$
  c_\text{new}\leftarrow c_{\text{old}} - \learnRate \frac{\text{d}\errorFunction(m, c)}{\text{d}c}
$$ 

* gives us an update for our estimate of $c$ (which in the code we've been calling `c_star` to represent a common way of writing a parameter estimate, $c^*$) and
$$
m_\text{new} \leftarrow m_{\text{old}} - \learnRate \frac{\text{d}\errorFunction(m, c)}{\text{d}m}
$$
* Giving us an update for $m$.

\subsection{Update Code}

* These updates can be coded as

\code{print("Original m was", m_star, "and original c was", c_star)
learn_rate = 0.01
c_star = c_star - learn_rate*c_grad
m_star = m_star - learn_rate*m_grad
print("New m is", m_star, "and new c is", c_star)}

\section{Iterating Updates}

* Fit model by descending gradient.

\subsection{Gradient Descent Algorithm}

\code{num_plots = plot.regression_contour_fit(x, y, diagrams='\writeDiagramsDir/ml')}

\setupdisplaycode{import notutils as nu
from ipywidgets import IntSlider}

\displaycode{nu.display_plots('regression_contour_fit{num:0>3}.svg', directory='\writeDiagramsDir/ml', num=IntSlider(0, 0, num_plots, 1))}

\slides{
\define{width}{60%}
\startanimation{regression_contour_fit}{1}{28}
\newframe{\includediagram{\diagramsDir/ml/regression_contour_fit000}{\width}}{regression_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_contour_fit001}{\width}}{regression_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_contour_fit002}{\width}}{regression_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_contour_fit003}{\width}}{regression_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_contour_fit004}{\width}}{regression_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_contour_fit005}{\width}}{regression_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_contour_fit006}{\width}}{regression_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_contour_fit007}{\width}}{regression_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_contour_fit008}{\width}}{regression_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_contour_fit009}{\width}}{regression_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_contour_fit010}{\width}}{regression_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_contour_fit011}{\width}}{regression_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_contour_fit012}{\width}}{regression_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_contour_fit013}{\width}}{regression_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_contour_fit014}{\width}}{regression_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_contour_fit015}{\width}}{regression_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_contour_fit016}{\width}}{regression_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_contour_fit017}{\width}}{regression_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_contour_fit018}{\width}}{regression_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_contour_fit019}{\width}}{regression_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_contour_fit020}{\width}}{regression_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_contour_fit021}{\width}}{regression_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_contour_fit022}{\width}}{regression_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_contour_fit023}{\width}}{regression_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_contour_fit024}{\width}}{regression_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_contour_fit025}{\width}}{regression_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_contour_fit026}{\width}}{regression_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_contour_fit027}{\width}}{regression_contour_fit}
\newframe{\includediagram{\diagramsDir/ml/regression_contour_fit028}{\width}}{regression_contour_fit}
\endanimation
}

\notes{\figure{\includediagram{\diagramsDir/ml/regression_contour_fit028}{60%}}{Batch gradient descent for linear regression}{regression-contour-fit-28}}

\endif

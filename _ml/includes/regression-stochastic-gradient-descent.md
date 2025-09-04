\ifndef{regressionStochasticGradientDescent}
\define{regressionStochasticGradientDescent}

\editme

\subsection{Stochastic Gradient Descent}

\notes{While batch gradient descent is possible for small datasets, it becomes computationally prohibitive when dealing with large-scale data. Consider modern internet applications where you might have millions or billions of data points - computing the full gradient by summing over all data points in each iteration would be extremely slow.

Stochastic Gradient Descent (SGD) offers an elegant solution by approximating the full gradient using just one (or a few) randomly selected data points at each iteration. This approach:

1. *Scales to large datasets*: Each update requires only O(1) computation regardless of dataset size
2. *Enables online learning*: We can process data as it arrives, updating our model incrementally
3. *Provides regularization*: The noise in stochastic updates can help escape local minima (though less relevant for convex problems like linear regression)
4. *Mirrors biological learning*: Similar to how the perceptron processes one example at a time

The key insight is that while each individual gradient estimate is noisy, on average it points in the correct direction toward the minimum.}
\slides{
* If $\numData$ is small, gradient descent is fine.
* But sometimes (e.g. on the internet) $\numData$ could be a billion.
* Stochastic gradient descent is more similar to perceptron.
* Look at gradient of one data point at a time rather than summing across *all* data points) 
* This gives a stochastic estimate of gradient.}

\subsection{Stochastic Gradient Descent}

\notes{To understand how stochastic gradient descent works mathematically, let's examine how the full batch gradient can be decomposed into individual per-example contributions. This decomposition reveals why we can update parameters using just one data point at a time.

The batch gradient is a sum over all data points:
$$\frac{\text{d}\errorFunction(m, c)}{\text{d} m} = -2\sum_{i=1}^\numData \inputScalar_i(\dataScalar_i - m\inputScalar_i - c)$$

When we substitute this into our parameter update equation, we get:
$$m_\text{new} \leftarrow m_\text{old} + 2\learnRate \left[\sum_{i=1}^\numData \inputScalar_i (\dataScalar_i - m_\text{old}\inputScalar_i - c_\text{old})\right]$$

The key insight is that this single large update is mathematically equivalent to a sequence of smaller updates, each using just one data point. However, there's an important difference in practice - in SGD, we update the parameters after each individual contribution rather than keeping them fixed throughout the sum.}
\slides{
* The real gradient with respect to $m$ is given by 
  $$
  \frac{\text{d}\errorFunction(m, c)}{\text{d} m} = -2\sum_{i=1}^\numData \inputScalar_i(\dataScalar_i -
m\inputScalar_i - c)
  $$}

\newslide{Decompose the Sum}
\slides{
  but it has $\numData$ terms in the sum. Substituting in the gradient we can see that the full update is of the form
\begin{aligned}
  m_\text{new} \leftarrow
m_\text{old} \\ 
& + 2\learnRate \left[\inputScalar_1 (\dataScalar_1 - m_\text{old}\inputScalar_1 - c_\text{old}) \right. \\ 
& + (\inputScalar_2 (\dataScalar_2 -   m_\text{old}\inputScalar_2 - c_\text{old}) \\ 
& + \dots + (\inputScalar_n (\dataScalar_n - m_\text{old}\inputScalar_n - c_\text{old})\right]
\end{aligned}}

\newslide{}
\slides{
  This could be split up into lots of individual updates
$$m_1 \leftarrow m_\text{old} + 2\learnRate \left[\inputScalar_1 (\dataScalar_1 - m_\text{old}\inputScalar_1 -
c_\text{old})\right]$$
$$m_2 \leftarrow m_1 + 2\learnRate \left[\inputScalar_2 (\dataScalar_2 -
m_\text{old}\inputScalar_2 - c_\text{old})\right]$$
$$m_3 \leftarrow m_2 + 2\learnRate
\left[\dots\right]$$
$$m_n \leftarrow m_{n-1} + 2\learnRate \left[\inputScalar_n (\dataScalar_n -
m_\text{old}\inputScalar_n - c_\text{old})\right]$$}

\newslide{}

\slides{
which would lead to the same final update.}

\subsection{Updating $c$ and $m$}

\notes{Here's where stochastic gradient descent fundamentally differs from batch gradient descent. In batch gradient descent, we compute the full gradient using fixed parameter values $m_{\text{old}}$ and $c_{\text{old}}$ for all data points, then make one large update.

In stochastic gradient descent, we update the parameters after processing each individual data point. This means:

1. *Dynamic parameters*: The values of $m$ and $c$ change as we process each example, so later examples in the sequence see updated parameter values
2. *Approximate gradient*: Since parameters change during the "sum," we're not computing the true batch gradient - we're using a stochastic approximation
3. *Online processing*: We can process data points as they arrive, making the algorithm suitable for streaming data

This dynamic updating is what makes SGD both powerful and noisy. The noise can actually be beneficial - it provides a form of regularization and can help escape poor local minima in more complex problems.}

\slides{
* In the sum we don't change $m$ and $c$ we use for computing the gradient term at each update. 
* In stochastic gradient descent we *do* change them.
* This means it's not quite the same as steepest descent.}

\newslide{}
\slides{
* But we can present each data point in a random order, like we did for the
perceptron.
* This makes the algorithm suitable for large-scale data use 
}

\subsection{Stochastic Gradient Descent}

\notes{In practice, stochastic gradient descent simplifies to a very clean algorithm. Since we process data points in random order, each SGD update uses the gradient contribution from just one randomly selected example. The update equations become:

For the slope parameter
$$
m_\text{new} = m_\text{old} + 2\learnRate\left[\inputScalar_i (\dataScalar_i - m_\text{old}\inputScalar_i - c_\text{old})\right].
$$
For the intercept parameter
$$c_\text{new} = c_\text{old} + 2\learnRate\left[(\dataScalar_i - m_\text{old}\inputScalar_i - c_\text{old})\right].
$$
Notice how these look exactly like the per-example terms from our batch gradient, but now we apply them immediately rather than accumulating them in a sum.}

\slides{
* Since the data is presented in a random order we write
  $$
  m_\text{new} = m_\text{old} + 2\learnRate\left[\inputScalar_i (\dataScalar_i - m_\text{old}\inputScalar_i - c_\text{old})\right]
  $$}

\notes{The implementation is straightforward: randomly select a data point, compute its contribution to the gradient, and immediately update the parameters. This process repeats for many iterations, with each iteration using a different random example.}

\code{# choose a random point for the update 
i = np.random.randint(x.shape[0]-1)
# update m
m_star = m_star + 2*learn_rate*(x[i]*(y[i]-m_star*x[i] - c_star))
# update c
c_star = c_star + 2*learn_rate*(y[i]-m_star*x[i] - c_star)}

\subsection{SGD for Linear Regression}

\notes{Let's now run the complete stochastic gradient descent algorithm and visualize how it differs from batch gradient descent. The key differences you'll observe:

1. *Noisier path*: SGD takes a much more erratic path through parameter space because each update is based on just one noisy example
2. *More iterations needed*: While each iteration is faster ($O(1)$ vs $O(n)$), SGD typically needs more iterations to converge
3. *Never fully converges*: SGD will continue to "bounce around" near the minimum due to the noise in gradient estimates
4. *Practical efficiency*: Despite the noise, SGD often reaches good solutions faster in wall-clock time for large datasets

The animation shows how the stochastic approximation creates a much more chaotic but ultimately effective optimization trajectory.}

\slides{Putting it all together in an algorithm, we can
do stochastic gradient descent for our regression data.}

\plotcode{num_plots = plot.regression_contour_sgd(x, y, diagrams='\writeDiagramsDir/ml')}

\setupdisplaycode{import notutils as nu
from ipywidgets import IntSlider}
\setupdisplaycode{import notutils as nu}
\displaycode{nu.display_plots('regression_sgd_contour_fit{num:0>3}.svg', 
    directory='\writeDiagramsDir/ml', num=IntSlider(0, 0, num_plots, 1))}

\newslide{}

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

\notes{\figure{\includediagram{\diagramsDir/ml/regression_sgd_contour_fit058}{60%}}{Stochastic gradient descent for linear regression showing the noisy but effective optimization path.}{regression-sgd-contour-fit-58}}

\notes{The final visualisation demonstrates the behaviour of SGD compared to batch gradient descent:

**Optimization Path Characteristics:**

- *Erratic trajectory*: The path zigzags chaotically through parameter space rather than following smooth contours
- *Local exploration*: The algorithm continues to explore around the minimum even after finding a good solution
- *Effective convergence*: Despite the noise, SGD successfully navigates to the optimal region

**Practical Implications:**

- *Computational efficiency*: Each SGD iteration processes just one example, making it ideal for large datasets where computing the full gradient is prohibitive
- *Online learning capability*: The algorithm can adapt to new data points as they arrive, enabling real-time model updates
- *Regularization effect*: The noise in SGD can prevent overfitting and help escape poor local minima in more complex optimization landscapes

**Trade-offs:**

- *Convergence vs. efficiency*: SGD trades smooth convergence for computational speed - it may never fully settle but reaches good solutions quickly
- *Hyperparameter sensitivity*: Learning rate tuning becomes more critical as too large values can cause divergence, while too small values slow convergence excessively

This stochastic approach forms the foundation for training modern machine learning models, particularly deep neural networks where batch gradient computation is computationally intractable.}

\subsection{Mini-Batch}

\notes{In practice we normally use mini-batches for gradient descent. Rather than computing the gradient with respect to one point, you compute gradient with respect to a small batch of points.}

\slides{* In practice use mini-batches.
  * Instead of computing gradient of one example.
  * Use a small batch of examples.}

\codeassignment{Can you write your own implementation of mini-batch gradient ascent for the regression problem? Allow the user to choose the mini-batch size.}{}{15}

\endif

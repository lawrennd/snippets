\ifndef{perceptron}
\define{perceptron}


\editme 

\subsection{The Perceptron}

\notes{The Perceptron (@Rosenblatt-perceptron58) is perhaps the oldest machine learning algorithm. The algorithm was inspired by ideas of statistical pattern recognition and was developed by Frank Rosenblatt at Cornell University in the 1950s.} 
\slides{* Developed in 1957 by Rosenblatt.
* Take a data point at, $\inputVector_i$.
* Predict class, $\dataScalar_i=1$ if $\sum_j\weightScalar_{j} \inputVector_{i, j} + b  > 0$ 
* Otherwise predict $\dataScalar_i=-1$.
}
\subsection{Mathematical Drawing of Decision Boundary}

\notes{We draw a hyper plane at decision boundary. The *decision boundary* is where a point moves from being classified as -1 to +1. For our two dimensional feature space it is defined by
$$
\text{sign}(\inputVector^\top \mappingVector) = \text{sign}(w_0 + w_1\inputScalar_{i,1} + w_2 \inputScalar_{i, 2})
$$
where $\inputScalar_{i, 1}$ is first feature $\inputScalar_{i, 2}$ is second feature and assume $\inputScalar_{0,i}=1$, in other words it plays the role of the bias, $b$. So setting $w_0 = b$ we have
$$
\text{sign}\left(w_1 \inputScalar_{i, 1} + w_2 \inputScalar_{i, 2} + b\right)
$$}
\slides{
* Decision boundary defined by hyperplane
* Classification: $\text{sign}(\inputVector^\top \mappingVector)$
* Two features: $w_1\inputScalar_{i,1} + w_2\inputScalar_{i,2} + b$
* Boundary where prediction switches from -1 to +1
}

\subsection{Reminder: Equation of Plane}

\notes{The prediction function is 
$$
\text{sign}\left(w_1 \inputScalar_{i, 1} + w_2 \inputScalar_{i, 2} + b\right)
$$
and the equation of a plane is 
$$
w_1 \inputScalar_{i, 1} + w_2 \inputScalar_{i, 2} + b = 0
$$ 
or
$$
w_1 \inputScalar_{i, 1} + w_2 \inputScalar_{i, 2} = -b.
$$ 
This is also the precise point that the argument of the $\text{sign}(\cdot)$ function is zero in our Perceptron algorithm. So it's the point at which a point switches from being classified negative to being classified positive (or vice versa).

The next step is to initialise the Preceptron model and draw a decision boundary.}
\slides{
* Plane equation: $w_1 \inputScalar_{i, 1} + w_2 \inputScalar_{i, 2} + b = 0$
* Decision boundary where $\text{sign}(\cdot)$ argument equals zero}

\newslide{Reminder: Equation of Plane}
\slides{
* Rearrange to plot: $\inputScalar_2 = -\frac{(b+\inputScalar_1w_1)}{w_2}$
* Separating hyperplane divides feature space
}

\subsection{Perceptron Algorithm: Initialisation Maths}

\notes{There's no single way to initialise an algorithm like the Perceptron, but here's a way that is informative because it helps see why the Perceptron works. We will take a randomly chosen data point, $i$, and set
$$
\mappingVector = \dataScalar_i \inputVector_i.
$$
Why is this sensible? Well if the predicted label of the $i$th point is 
$$
\text{sign}(\mappingVector^\top\inputVector_i)
$$
then setting $\mappingVector$ to $\dataScalar_i\inputVector_i$ implies
$$
\text{sign}(\mappingVector^\top\inputVector_i) = \text{sign}(\dataScalar_i\inputVector_i^\top \inputVector_i) = \dataScalar_i
$$
which means that the point we've selected will be correctly classified.

For simple data sets like our artifical red and green crosses, this algorithm can actually be so good that it gets the decision boundary very close from the start.}
\slides{
* Set $\mappingVector$ with random selected point $i$
  $$
  \mappingVector = \dataScalar_i \inputVector_i.
  $$
* Why? Consider
  $$
  \text{sign}(\mappingVector^\top\inputVector_i)
  $$}
  
\newslide{Perceptron Algorithm: Initialisation Maths}
\slides{
* Setting $\mappingVector$ to $\dataScalar_i\inputVector_i$ implies
$$
\text{sign}(\mappingVector^\top\inputVector_i) = \text{sign}(\dataScalar_i\inputVector_i^\top \inputVector_i) = \dataScalar_i
$$
}
\loadcode{init_perceptron}{mlai}

\subsection{Drawing Decision Boundary}

\setupplotcode{import mlai.plot as plot}

\plotcode{f, ax = plt.subplots(1, 2, figsize=(14,7))
w, b, x_select = init_perceptron(x_plus, x_minus)
handle = plot.init_perceptron(f, ax, x_plus, x_minus, w, b)
mlai.write_figure("perceptron_init.svg", directory="\writeDiagramsDir/ml")}

\figure{\includediagram{\diagramsDir/ml/perceptron_init}{80%}}{Initial perceptron setup showing data points and initial decision boundary.}{perceptron-init}


\notes{The decision boundary is where the output of the function
changes from -1 to +1 (or vice versa) so it's the point at which the
argument of the $\text{sign}$ function is zero. So in other words, the
decision boundary is given by the *line* defined by $\inputScalar_1
w_1 + \inputScalar_2 w_2 = -b$ (where we have dropped the index $i$
for convenience). In this two dimensional space the decision boundary
is defined by a line. In a three dimensional space it would be defined
by a *plane* and in higher dimensional spaces it is defined by
something called a
[*hyperplane*](http://en.wikipedia.org/wiki/Hyperplane). This equation
is therefore often known as the *separating hyperplane* because it
defines the hyperplane that separates the data. To draw it in 2-D we
can choose some values to plot from $\inputScalar_1$ and then find the
corresponding values for $\inputScalar_2$ to plot using the
rearrangement of the hyperplane formula as follows
$$
\inputScalar_2 = -\frac{(b+\inputScalar_1w_1)}{w_2}
$$
Of course, we can also choose to specify the values for $\inputScalar_2$ and compute the values for $\inputScalar_1$ given the values for $\inputScalar_2$,
$$
\inputScalar_1 = -\frac{b + \inputScalar_2w_2}{w_1}
$$}

\slides{* Plot
$$
\inputScalar_2 = -\frac{(b+\inputScalar_1 w_1)}{w_2}
$$

*or* specify $\inputScalar_2$ and compute $\inputScalar_1$ given the values for $\inputScalar_2$,
$$
\inputScalar_1 = -\frac{b + \inputScalar_2w_2}{w_1}
$$}

\subsection{Switching Formulae}

\notes{Sometimes we need to use the first formula, and sometimes we need to use the second. Which formula we use depends on how the separating hyperplane leaves the plot. 

We want to draw the separating hyperplane in the bounds of the plot which is showing our data. To think about which equation to use, let's consider two separate situations (actually there are a few more). 

1. If the separating hyperplane leaves the top and bottom of the plot then we want to plot a line with values in the $y$ direction (given by $\inputScalar_2$) given by the upper and lower limits of our plot. The values in the $x$ direction can then be computed from the formula for the plane. 

2. Conversely if the line leaves the sides of the plot then we want to plot a line with values in the $x$ direction given by the limits of the plot. Then the values in the $y$ direction can be computed from the formula. Whether the line leaves the top/bottom or the sides of the plot is dependent on the relative values of $w_1$ and $w_2$. 

This motivates a simple `if` statement to check which situation we're in.}

\slides{* Use of first or second formula
* Depends on how hyperplane leaves plot
}

\newslide{Code for Perceptron}

\loadcode{update_perceptron}{mlai}

\notes{The code for plotting the perceptron boundary is also provided. Here note how many more lines are required for plotting than are required for updating! The plotting code runs an entire optimisation of the Perceptron algorithm showing the histrogram of points projected onto the *normal vector*, $\mappingVector$.}

\setupplotcode{import mlai.plot as plot}

\plotcode{plots = plot.perceptron(x_plus, x_minus, seed=1000001, diagrams='\writeDiagramsDir/mlai')}

\setupdisplaycode{import notutils as nu}
\displaycode{nu.display_plots('perceptron{samp:0>3}.svg', directory='\writeDiagramsDir/ml', samp=(0, plots))}

\slides{
\define{width}{60%}
\startanimation{perceptron}{0}{14}
\newframe{\includediagram{\diagramsDir/ml/perceptron000}{\width}}{perceptron}
\newframe{\includediagram{\diagramsDir/ml/perceptron001}{\width}}{perceptron}
\newframe{\includediagram{\diagramsDir/ml/perceptron002}{\width}}{perceptron}
\newframe{\includediagram{\diagramsDir/ml/perceptron003}{\width}}{perceptron}
\newframe{\includediagram{\diagramsDir/ml/perceptron004}{\width}}{perceptron}
\newframe{\includediagram{\diagramsDir/ml/perceptron005}{\width}}{perceptron}
\newframe{\includediagram{\diagramsDir/ml/perceptron006}{\width}}{perceptron}
\newframe{\includediagram{\diagramsDir/ml/perceptron007}{\width}}{perceptron}
\newframe{\includediagram{\diagramsDir/ml/perceptron008}{\width}}{perceptron}
\newframe{\includediagram{\diagramsDir/ml/perceptron009}{\width}}{perceptron}
\newframe{\includediagram{\diagramsDir/ml/perceptron010}{\width}}{perceptron}
\newframe{\includediagram{\diagramsDir/ml/perceptron011}{\width}}{perceptron}
\newframe{\includediagram{\diagramsDir/ml/perceptron012}{\width}}{perceptron}
\newframe{\includediagram{\diagramsDir/ml/perceptron013}{\width}}{perceptron}
\newframe{\includediagram{\diagramsDir/ml/perceptron014}{\width}}{perceptron}
\endanimation
}

\notes{\figure{\includediagram{\diagramsDir/ml/perceptron014}{60%}}{The perceptron decision boundary.}{perceptron-decision-boundary}}

\subsection{Perceptron Reflection}

\notes{It's worth having some reflections on the Perceptron and what it does. The algorithm is simple enough that you can go through the exact updates. What is it doing? When will it fail? What happens when you can't separate the classes with a linear hyperplane? Why does this stop the algorithm converging? How might you fix the algorithm to make it converge?}

\slides{
* Algorithm updates are intuitive and interpretable
* What happens when classes aren't linearly separable?
}
\newslide{Perceptron Reflections}
\slides{
* Non-convergence indicates inseparable data
* Possible fix: anneal learning rate
* Non-linear extensions: basis functions, kernel methods, multi-layer networks
}

\subsection{The Objective Function}

\notes{Another question is where is the objective function? I like the Percptron because if you study the algorithm you get an insight into what its doing and that gives an intuition about how its updating the parameters. But it's not easy to see how that connects to an objective function. Very often to define an algorithm its much easier to start with an *objective function* (otherwise known as a loss function, an error function or a cost function).}

\slides{
* Perceptron algorithm lacks explicit objective function
* Updates provide intuition but not clear optimization target
* Objective functions (loss/error/cost) often easier starting point
* Connection between algorithm and objective not immediately obvious
}

\endif

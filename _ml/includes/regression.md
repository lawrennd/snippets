\ifndef{regression}
\define{regression}
\editme

\subsection{Objective Functions and Regression}

\notes{In classification we're predicting discrete values, we use the sign function in the Perceptron algorithm to convert from a continuous value to a discrete by interpreting the continuos values as defining a (hyper)plane. In regression we're trying to predict a continuous real-valued output rather than a discrete class label. Our goal is to find a function that maps input features to real-valued predictions.

For linear regression, we assume a simple linear relationship between input and output. For a single feature, our prediction function takes the form
$$
\mappingFunction(\inputScalar_i) = m\inputScalar_i + c
$$
where $m$ is the slope and $c$ is the intercept. How should we find the best values for these parameters?

This is where the objective function comes in. We need a way to measure how well our current parameter values fit the data. The least squares objective function provides a principled approach by measuring the sum of squared differences between our predictions and the true values
$$
\errorFunction(m, c) = \sum_{i=1}^\numData (\dataScalar_i - \mappingFunction(\inputScalar_i))^2
$$
The algorithm's job is to find the values of $m$ and $c$ that minimize this error function.}

\slides{
* Classification: map feature to class label.
* Regression: map feature to real value
 }
 \newslide{Regression} 
 \slides{* Our *prediction function* is
    $$\mappingFunction(\inputScalar_i) = m\inputScalar_i + c$$

* Need an *algorithm* to fit it. }

\newslide{Least Squares}

\slides{
* Least squares: minimise an error.

$$\errorFunction(m, c) = \sum_{i=1}^\numData (\dataScalar_i - \mappingFunction(\inputScalar_i))^2$$}

\newslide{Regression}

\notes{To demonstrate how regression works, we'll create an artificial dataset where we know the true underlying relationship. This allows us to test whether our algorithm can recover the parameters we used to generate the data.

We start by creating some random input values from a normal distribution. These will serve as our feature values $\inputScalar_i$.}

\slides{
* Create an artifical data set.
}

\setupcode{import numpy as np
import matplotlib.pyplot as plt
import mlai}
\code{x = np.random.normal(size=(4, 1))}

\notes{We now need to decide on a *true* value for $m$ and a *true* value for $c$ to use for generating the data. In real-world scenarios, we don't know these values - that's what we're trying to learn. But for this demonstration, we'll choose specific values so we can verify our algorithm works correctly.}

\slides{* *true* value for $m$ `m_true = 1.4`
* *true* value for $c$ `c_true = -3.1` }

\code{m_true = 1.4
c_true = -3.1}

\notes{Now we can generate our target values using the linear relationship. The mathematical formula $\dataScalar_i = m\inputScalar_i + c$ translates directly into code. This creates an exact linear relationship - each point will lie exactly on the line defined by our chosen slope and intercept.}

\newslide{}

\slides{We can use these values to create our artificial data. The formula 
$$\dataScalar_i = m\inputScalar_i + c$$ is translated to code as follows:

`y = m_true*x+c_true`}

\code{y = m_true*x+c_true}

\newslide{Plot of Data}

\notes{Plotting our artificial data helps us visualise the linear relationship we've created. Since we generated the data deterministically using our linear function, all points should lie exactly on a straight line. This gives us a baseline to understand how the algorithm should perform in the ideal case.}

\slides{We can now plot the artifical data we've created.}

\setupplotcode{import matplotlib.pyplot as plt}

\plotcode{plt.plot(x, y, 'r.', markersize=10) # plot data as red dots
plt.xlim([-3, 3])
mlai.write_figure(filename='regression.svg', directory='\writeDiagramsDir/ml', transparent=True)}

\figure{\includediagram{\diagramsDir/ml/regression}{60%}}{A simple linear regression.}{linear-regression}

\notes{As expected, these points lie exactly on a straight line since we generated them deterministically. However, real-world data is rarely this perfect. There are always measurement errors, unknown factors, and random variations that cause data to deviate from perfect relationships.}

\newslide{Plot of data}

\slides{* Points lie exactly on a straight line
* Not very realistic
* Corrupt them with Gaussian 'noise'.}

\subsection{Noise Corrupted Plot}

\notes{To make our artificial dataset more realistic, we add Gaussian noise to our target values. This simulates the random variations we'd encounter in real data. The noise has zero mean, so it doesn't systematically bias our data, but it does add random scatter around the true linear relationship.

The standard deviation of the noise (0.5 in this case) controls how much the data deviates from the perfect line. Larger noise values make the regression problem more challenging, while smaller values keep the data closer to the underlying linear trend.}

\code{noise = np.random.normal(scale=0.5, size=(4, 1)) # standard deviation of the noise is 0.5
y = m_true*x + c_true + noise
plt.plot(x, y, 'r.', markersize=10)
plt.xlim([-3, 3])
mlai.write_figure(filename='regression_noise.svg', directory='\writeDiagramsDir/ml', transparent=True)}

\figure{\includediagram{\diagramsDir/ml/regression_noise}{60%}}{A simple linear regression with noise.}{linear-regression-noise}

\endif

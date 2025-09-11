\ifndef{linearRegressionStatsmodels}
\define{linearRegressionStatsmodels}

\editme

\subsection{Model Diagnostics and Linear Regression}

\notes{In linear regression, we model the relationship between a continuous response variable $\dataScalar_i$ and input variables $\inputVector_i$ through a linear function with Gaussian noise:

$$\dataScalar_i = \mappingFunction(\inputVector_i) + \noiseScalar_i$$

where $\mappingFunction(\inputVector_i) = \mappingVector^\top\inputVector_i = \sum_{j=1}^D \weightScalar_j\inputScalar_{i,j}$ and $\noiseScalar_i \sim \gaussianSamp{0}{\dataStd^2}$

This gives us a probabilistic model:

$$p(\dataScalar_i|\inputVector_i) = \gaussianDist{\dataScalar_i}{\mappingVector^\top\inputVector_i}{\dataStd^2}$$

The key components are:

* $\dataScalar_i$ is the target/response variable we want to predict
* $\inputVector_i$ contains the input features/explanatory variables  
* $\mappingVector$ contains the parameters/coefficients we learn
* $\noiseScalar_i$ represents random Gaussian noise with variance $\dataStd^2$

For the full dataset, we can write this in matrix form:

$$\dataVector = \inputMatrix\mappingVector + \noiseVector$$

where $\dataVector = [\dataScalar_1,\ldots,\dataScalar_N]^\top$, $\inputMatrix$ contains the input vectors as rows, and $\noiseVector \sim \gaussianSamp{\zerosVector}{\dataStd^2\eye}$.

The expected value of our prediction is:

$$\mathbb{E}[\dataScalar_i|\inputVector_i] = \mappingVector^\top\inputVector_i$$

This linear model forms the foundation for generalized linear models like logistic regression, where we'll adapt the model for classification by transforming the output through a non-linear function.}

\newslide{Linear Regression Model}

\slides{* Linear regression models continuous response $\dataScalar_i$ vs inputs $\inputVector_i$:
  $$\dataScalar_i = \mappingFunction(\inputVector_i) + \noiseScalar_i$$
  where $\mappingFunction(\inputVector_i) = \mappingVector^\top\inputVector_i$ 
  
* Probabilistic model:
  $$p(\dataScalar_i|\inputVector_i) = \gaussianDist{\dataScalar_i}{\mappingVector^\top\inputVector_i}{\dataStd^2}$$
}

\newslide{Linear Regression in Matrix Form}

\slides{* Matrix form:
  $$\dataVector = \inputMatrix\mappingVector + \noiseVector$$
  
* Expected prediction:
  $$\mathbb{E}[\dataScalar_i|\inputVector_i] = \mappingVector^\top\inputVector_i$$
}

\setupcode{import statsmodels.api as sm
import pods}

\code{# Demo of linear regression using python statsmodels.
data = pods.datasets.olympic_marathon_men()
xlim = (1876,2044)
x = data['X']
y = data['Y']
}

\notes{The `statsmodels` package makes it easy to add the constant term to the matrix.}

\code{# Add constant term to design matrix
print(x.shape)
x = sm.add_constant(x)
print(x.shape)}

\code{model = sm.OLS(y, x)}

\notes{Using `statsmodels` we don't need to implement the QR decomposition directly we can simply fit the model.}

\code{results = model.fit()}

\notes{The model results also contain a lot more than just the regression weights. Various diagnostic statistics are also computed including checks on the residuals (i.e. $y_i - f_i$) which *should* be Gaussian (or normal) distributed.}

\notes{We can show obtain our predictions, $f$ from the model as follows.}

\code{f = results.predict(x)}

\notes{And plot them against the actual data.}

\setupplotcode{import matplotlib.pyplot as plt
import mlai
import mlai.plot}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
ax.plot(x[:, 1], y, '.')

# Plot the fitted line
xpred = np.array(xlim)
xpred = sm.add_constant(xpred)
fpred = results.predict(xpred)

ax.plot(xpred, fpred, '-')
ax.set_xlim(xlim)

ax.set_xlabel('Year')
ax.set_ylabel('Time')

mlai.write_figure("linear-regression-olympic-marathon-statsmodels.svg", directory="\writeDiagramsDir/statistics")}

\figure{\includediagram{\diagramsDir/statistics/linear-regression-olympic-marathon-statsmodels}{50%}}{Plot of the `statsmodels` fit to the olympic marathon data.}{linear-regression-olympic-marathon}

\code{results.summary()}

\notes{The summary helps us evaluate our model fit and identify potential areas for improvement. Since we're working with one-dimensional data (year vs time), we can visualise everything easily to complement these statistical measures.}

\notes{The model fit statistics show a moderately strong fit, with an R-squared of 0.730 indicating that our model explains 73.0% of the variance in the data. The adjusted R-squared of 0.721 confirms this isn't just due to overfitting (which is unsurprising given we are only fitting a linear model). The very low F-statistic p-value (1.85e-09) confirms the model's overall significance.}

\notes{The AIC (11.33) and BIC (14.13) information criteria values are used to compare the model against alternatives we might try.}

\newslide{Model Fit Statistics}
\slides{
* Model fit statistics help assess overall performance:
  * R-squared shows variance explained 
  * F-statistic tests if model is useful
  * AIC/BIC help compare models
}

\notes{Looking at the model parameters, we see a coefficient of -0.0116 for our predictor, with a small standard error (0.001). The $t$-statistic of -8.710 and p-value of less than 0.001 indicate this effect is highly significant. The 95% confidence interval [-0.014, -0.009] gives us good confidence in our estimate. The negative coefficient confirms the expected downward trend in marathon times over the years.}


\newslide{Parameter Estimates}
\slides{
* Parameter estimates tell us about relationships:
  * Coefficients show effect direction/size
  * Standard errors show uncertainty 
  * $p$-values test significance
}

\newslide{Residual Diagnostics}

\slides{
* Residual diagnostics check assumptions:
  * Tests for normality and autocorrelation
  * Look for patterns that violate assumptions
}

\newslide{Visual Inspection}
\slides{
* Visual inspection is crucial:
  * With 1D data we can plot everything
  * Helps spot patterns statistics might miss
  * Shows if relationship makes practical sense
}

\setupplotcode{import matplotlib.pyplot as plt
import mlai
import mlai.plot}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
ax.hist(y.flatten()-f, bins=15)
ax.set_xlabel('residual')
mlai.write_figure("residuals-histogram-olympic-marathon.svg", directory="\writeDiagramsDir/statistics")}

\figure{\includediagram{\diagramsDir/statistics/residuals-histogram-olympic-marathon}{50%}}{The histogram of the residuals of the fit to the Olympic Marathon data.}{residuals-histogram-olympic-marathon}

\notes{We can see in the histogram that the residuals are not Gaussian (normal) distributed. Looking at the diagnostics we see the same challenges. The histogram doesn't show us the autocorrelation, that comes from the Durbin-Watson statistic.}

\notes{1. The Durbin-Watson statistic (0.981) indicates positive autocorrelation in the residuals. This suggests we might want to
   
   * Consider time series modeling approaches
   * Add polynomial terms to capture non-linear trends
   * Investigate if there are distinct "eras" in marathon times

2. The Jarque-Bera test ($p$-value 8.32e-14) tells us our residuals aren't normally distributed. The skew (1.947) and kurtosis (8.746) values show the distribution is strongly right-skewed with very heavy tails. This is due to the outlier in 1904. We could deal with this through transformation of the response variable, robust regression or by dropping the outlier. 

3. The large condition number (9.94e+04) suggests potential numerical instability or multicollinearity issues. This is because we haven't centred and scaled the model. 

The beauty of having one-dimensional data is that we can plot everything to visually confirm these statistical findings. It allows us to visually assess the linearity assumption, identify potential outliers (such as the 1904 point) and spot any systematic patterns in the residuals. 

This visual inspection, combined with our statistical diagnostics, will guide our next steps in improving the model.}

\newslide{Linear Regression Fit}

\figure{\includediagram{\diagramsDir/data-science/linear-regression-olympic-marathon-men-statsmodels}{80%}}{Linear regression fit to Olympic marathon men's times using `statsmodels`.}{linear-regression-olympic-marathon-men-statsmodels}


\notes{Looking at our plot and model diagnostics, we can now better understand the large condition number (1.08e+05) in our results. This high value likely stems from using raw year values (e.g., 1896, 1900, etc.) as our predictor variable. Such large numbers can lead to numerical instability in the computations.

To address this, we will look at centering the years around their mean and scaling the years to a smaller range. }

\notes{Looking at the plot we can see more about our our data.  The 1904 St. Louis Olympics appears as a clear outlier, contributing to the non-normal residuals (Jarque-Bera p=0.00432) and right-skewed distribution (skew=1.385).}

\slides{
* 1904 St. Louis Olympics: Major outlier
  * Explains non-normal residuals 
  * Contributes to right skew
}


\notes{There are also regimes in the data, such as the rapid improvement in times pre-WWI, the disruption and variation during the war years, the more steady, consistent progress post-WWII. These regime changes help explain the strong positive autocorrelation (Durbin-Watson=0.242) in our residuals.}

\newslide{Data Regimes}

\slides{
* Three distinct regimes visible:
  * Pre-WWI: Rapid improvement
  * War years: Disrupted progress
  * Post-WWII: Steady improvement
}

\notes{This suggests we could improve the model by adding additional features such as polynomial terms to capture non-linear trends, indicator variables for different time periods and interaction terms between features. We could also consider variables accounting for external factors like temperature or course conditions.}

\newslide{Model Improvements}

\slides{
* Model improvements possible with extra features:
  * Polynomial terms
  * Period indicators
  * Interaction terms
  * External factors
}

\notes{To incorporate multiple features into our model, we need a systematic way to organize this additional information. This brings us back to the concept of the design matrix.}

\subsubsection{Design Matrix}

\slides{
* The design matrix $\designMatrix$ stores our features
* Each row represents one data point
* Each column represents one feature
* For $n$ data points and $p$ features:
  $$\designMatrix = \begin{bmatrix} 
  \designScalar_{11} & \designScalar_{12} & \cdots & \designScalar_{1p} \\
  \designScalar_{21} & \designScalar_{22} & \cdots & \designScalar_{2p} \\
  \vdots & \vdots & \ddots & \vdots \\
  \designScalar_{n1} & \designScalar_{n2} & \cdots & \designScalar_{np}
  \end{bmatrix}$$
* Also called the feature matrix or model matrix
}

\notes{The design matrix, often denoted as $\designMatrix$, is a key component of a statistical model. It organizes our feature data in a structured way that facilitates model fitting and analysis. Each row of the design matrix represents a single observation or data point, while each column represents a different feature or predictor variable.

For $n$ observations and $p$ features, the design matrix takes the form:

$$\designMatrix = \begin{bmatrix} 
\designScalar_{11} & \designScalar_{12} & \cdots & \designScalar_{1p} \\
\designScalar_{21} & \designScalar_{22} & \cdots & \designScalar_{2p} \\
\vdots & \vdots & \ddots & \vdots \\
\designScalar_{n1} & \designScalar_{n2} & \cdots & \designScalar_{np}
\end{bmatrix}$$

For example, if we're predicting house prices, each row might represent a different house, with columns for features like: square footage, number of bedrooms, yyear built, plot size.

The design matrix provides a compact way to represent all our feature data and is used directly in model fitting. When we write our linear model as $\dataVector = \designMatrix\mappingVector + \noiseVector$, the design matrix $\designMatrix$ is multiplied by our parameter vector $\mappingVector$ to generate predictions.}


\setupcode{import statsmodels.api as sm
import pods
import numpy as np}

\code{# Demo of additional features with interactions regression usying python statsmodels.
data = pods.datasets.olympic_marathon_men()
x = data['X']
y = data['Y']
xlim = (1876,2044)
}

\notes{Now we process our input data to create the design matrix.}

\code{def marathon_design_matrix(x, product_terms=True):
	"""This function augments the input matrix with indicator variables that state the year."""
    
    # Scale the year to avoid numerical issues
    x_scaled = (x - 1900) / 100  # Center around 1900 and scale to century units
    Phi = x_scaled

    # Add to design matrix indicator variable for 1914-1945
    Phi = np.hstack([Phi, ((x[:, 0] >= 1914) & (x[:, 0] <= 1945)).astype(np.float64)[:, np.newaxis]])

    # Add to design matrix indicator variable for post-1945
    Phi = np.hstack([Phi, (x[:, 0] > 1945).astype(np.float64)[:, np.newaxis]])
	if product_terms:
        # Add product terms that multiply the scaled year and the indicator variables.
        Phi = np.hstack([Phi, x_scaled[:, 0:1] * Phi[:, 1:2], x_scaled[:, 0:1] * Phi[:, 2:3]])
	Phi = sm.add_constant(Phi)
	return Phi
}


\code{# Create the model
Phi = marathon_design_matrix(x)
model = sm.OLS(y, Phi)}

\notes{Now we can fit the model.}

\code{# Do the linear fit
results = model.fit()}

\setupplotcode{import matplotlib.pyplot as plt
import mlai
from mlai import plot}

\plotcode{fig, ax = plt.subplots(figsize=mlai.plot.big_wide_figsize)
ax.plot(x[:, 0], y, '.')

# Plot the fitted line
xpred = np.linspace(xlim[0], xlim[1], 100)[:, np.newaxis]
Phipred = marathon_design_matrix(xpred)

fpred = results.predict(Phipred)

ax.plot(xpred, fpred, '-')

ax.set_xlabel('Year')
ax.set_ylabel('Time')
ax.set_xlim(xlim)

mlai.write_figure("linear-regression-olympic-marathon-men-augmented-statsmodels.svg", directory="\writeDiagramsDir/data-science")}

\figure{\includediagram{\diagramsDir/data-science/linear-regression-olypmic-marathon-men-augmented-statsmodels}{80%}}{Plot of the fit obtained when we include indicator variables that identify the pre-1914, across war, and post-war eras.}{linear-regression-olypmic-marathon-men-augmented-statsmodels}

\notes{Let's check the summary of the results.}

\code{results.summary()}

\notes{Using indicator variables for historical periods (and without relying on quadratic terms), the model shows a strong improvement over the simpler linear model, with an R-squared of 0.877 and an adjusted R-squared of 0.851. This indicates that about 87% of the variance in marathon times is explained by our model. The overall model significance is high (F-statistic $p=3.70\times 10^{-10}$), and the information criteria are AIC $=-4.164$, BIC $=4.244$.}

\notes{Key parameter estimates (with 95% confidence intervals) are:

* Intercept (const): $4.5876$ (SE $0.113$), $t=40.533$, $p=0.000$, CI $[4.354, 4.821]$
* $x_1$ (base time trend): $-3.6127$ (SE $1.634$), $t=-2.211$, $p=0.037$, CI $[-6.984, -0.241]$
* $x_2$ (war period indicator): $-0.7523$ (SE $0.480$), $t=-1.567$, $p=0.130$, CI $[-1.743, 0.239]$
* $x_3$ (post war indicator): $-0.9399$ (SE $0.211$), $t=-4.449$, $p=0.000$, CI $[-1.376, -0.504]$
* $x_4$ (wartime time trend): $2.8799$ (SE $2.310$), $t=1.247$, $p=0.225$, CI $[-1.888, 7.648]$
* $x_5$ (post war time trend): $3.0493$ (SE $1.646$), $t=1.853$, $p=0.076$, CI $[-0.348, 6.446]$

These results suggest a strong negative time trend and statistically significant effects for some period indicators, with others being suggestive but not conclusive.}

\notes{However, there are some concerns:

1. The Jarque–Bera test ($p=1.34\times 10^{-24}$) indicates non-normal residuals. Skewness is $2.393$ and kurtosis is $11.065$.
2. The Durbin–Watson statistic is $2.101$, suggesting little residual autocorrelation.
3. The condition number is $127$, indicating the design is reasonably well conditioned relative to polynomial/interaction-augmented alternatives.

The indicator-variable model captures key regime differences and substantially improves fit over the baseline linear model. One side-effect of using abrupt indicator boundaries is that the fitted curve is discontinuous at regime change years. This can create edge effects where adjacent observations on either side of a boundary receive different offsets even if they are close in time. 

If continuity is needed we could consider

- Replacing hard indicators with smooth transition functions (e.g., logistic ramps centered on boundary years)
- Adding interaction terms with polynomial or spline bases to allow the trend to bend smoothly through transitions
- Using piecewise-linear or spline regression with continuity (and optionally slope) constraints at knots
- Hierarchical/regularized models that shrink jump sizes toward zero unless strongly supported by data

These approaches preserve the idea of regime structure while avoiding artificial jumps at the boundaries.}

\endif

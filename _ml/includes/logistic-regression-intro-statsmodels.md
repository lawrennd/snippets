\ifndef{logisticRegressionIntroStatsModels}
\define{logisticRegressionIntroStatsModels}

\editme

\subsection{Logistic Regression}

\notes{In logistic regression, we model the relationship between a binary response variable $\dataScalar_i \in \{0,1\}$ and input variables $\inputVector_i$ using the logistic function. Unlike linear regression, we cannot directly model the probability using a linear function since probabilities must lie between 0 and 1.

The logistic regression model uses the sigmoid function to map any real-valued input to the range [0,1]:

$$p(\dataScalar_i = 1|\inputVector_i) = \sigma(\mappingVector^\top\inputVector_i) = \frac{1}{1 + \exp(-\mappingVector^\top\inputVector_i)}$$

where $\sigma(\cdot)$ is the sigmoid function and $\mappingVector^\top\inputVector_i = \sum_{j=1}^D \weightScalar_j\inputScalar_{i,j}$ is the linear predictor.

The key components are:
- $\dataScalar_i \in \{0,1\}$ is the binary target/response variable
- $\inputVector_i$ contains the input features/explanatory variables  
- $\mappingVector$ contains the parameters/coefficients we learn
- $\sigma(\cdot)$ is the sigmoid activation function that maps $(-\infty, \infty) \to (0, 1)$

The model assumes that given the features $\inputVector_i$, the response $\dataScalar_i$ follows a Bernoulli distribution:

$$\dataScalar_i|\inputVector_i \sim \text{Bernoulli}(\sigma(\mappingVector^\top\inputVector_i))$$

This gives us the likelihood:

$$p(\dataScalar_i|\inputVector_i) = \sigma(\mappingVector^\top\inputVector_i)^{\dataScalar_i} \left(1 - \sigma(\mappingVector^\top\inputVector_i)\right)^{1-\dataScalar_i}$$

The log-odds (logit) transformation provides a linear relationship:

$$\log\left(\frac{p(\dataScalar_i = 1|\inputVector_i)}{1 - p(\dataScalar_i = 1|\inputVector_i)}\right) = \mappingVector^\top\inputVector_i$$

This means the coefficients $\mappingVector$ represent the change in log-odds for a unit change in the corresponding feature.}

\newslide{Logistic Regression Model}

\slides{* Logistic regression models binary response $\dataScalar_i \in \{0,1\}$ vs inputs $\inputVector_i$:
  $$p(\dataScalar_i = 1|\inputVector_i) = \sigma(\mappingVector^\top\inputVector_i)$$
  where $\sigma(z) = \frac{1}{1 + \exp(-z)}$ is the sigmoid function
  
* Bernoulli distribution:
  $$\dataScalar_i|\inputVector_i \sim \text{Bernoulli}(\sigma(\mappingVector^\top\inputVector_i))$$
}

\newslide{Log-Odds and Linear Predictor}

\slides{* Log-odds (logit) transformation:
  $$\text{logit}(p) = \log\left(\frac{p}{1-p}\right) = \mappingVector^\top\inputVector_i$$
  
* Coefficients represent change in log-odds:
  $$\Delta \text{logit}(p) = \weightScalar_j \Delta \inputScalar_j$$
}

\endif

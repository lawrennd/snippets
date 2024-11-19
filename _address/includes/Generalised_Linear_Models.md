\ifndef{generalisedLinearModels}
\define{generalisedLinearModels}

\editme

\subsection{Generalised Linear Models}

\notes{We have a set of explanatory variables $x \in X$ and a set of response variables $y \in Y$. The data is provided to us in pairs $D = \{x_i, y_i\}_N$ where $x_i$ and $y_i$ are in correspondence. Our aim is to build a model that allows us to predict the response variable $y_i$ from its corresponding explanatory variable $x_i$.}

\notes{Linear regression makes the assumption that the relationship between the response variable and the explanatory variable can be written as a linear combination. Furthermore, it assumes that the observations of the response variable have been corrupted by an additive Gaussian noise process,}

$$ y_i = \sum_{i=1}^{d} \beta_i x_{id} + E, $$

\notes{where $E \sim \mathcal{N}(0, \sigma^2)$.}

\notes{While both the explanatory and response variable are deterministic, due to the noise corrupting the observations, our predictions under the model are random. In order to extract a point estimate we therefore take the expected value,}


$$ \mathbb{E}[y_i | x_i] = \mathbb{E} \left( \sum_{i=1}^{d} \beta_i x_{id} + E \right), $$

$$ = \sum_{i=1}^{d} \beta_i x_{id} + \mathbb{E}[E], $$

$$ = \sum_{i=1}^{d} \beta_i x_{id} + 0. $$

\notes{Traditionally the linear regression model above is motivated by an additive noise assumption that corrupts the observed response. An equivalent explanation is to absorb the noise directly into the response variable and consider it a linear model of a normal distributed response,}

$$ y_i = \sum_{i=1}^{d} \beta_i x_{id} + \varepsilon, $$

$$ y_i + \varepsilon = \sum_{i=1}^{d} \beta_i x_{id}, $$

$$ \hat{y}_i = \sum_{i=1}^{d} \beta_i x_{id}, $$

$$ \hat{y}_i \sim \mathcal{N} \left( y_i, \sigma^2 \right) = \mathcal{N} \left( \sum_{i=1}^{d} \beta_i x_{id}, \sigma^2 \right), $$

\notes{where, as we previously derived, the linear predictor directly parametrises the mean or the first moment of the random response variable.}

\notes{If we want to generalise the setting, we can think of scenarios where the response variable follows a different distribution. This could be a Bernoulli distributed response, as in binary classification, or Poisson distributed if we are describing discrete events. Specifically, we will look at models where the first moment of the response variable can be parametrised as a function of a linear combination of the explanatory variables,}

$$ g(\mathbb{E}[y_i | x_i]) = \sum_{i=1}^{d} \beta_i x_{id}, $$

\notes{where the function $g(\cdot)$ is known as a link function, connecting the expected value and the linear predictor (for the linear regression case above the link function is the identity).}

\notes{While the above formulation is the one that is most commonly used in the statistics literature, in a machine learning setting we can think of a transformation of a linear mapping as}

$$ \mathbb{E}[y_i | x_i] = g^{-1} \left( \sum_{i=1}^{d} \beta_i x_{id} \right), $$

\notes{If you are familiar with simple compositional function models, such as neural networks, you can see how these are recursive formulations of similar structures. An article that describes neural networks in the light of the models we will describe can be found [here](https://towardsdatascience.com/glms-part-iii-deep-neural-networks-as-recursive-generalized-linear-URL).}

\notes{The class of models that can be described using the equations above are commonly referred to as Generalised Linear Models (GLM) (McCullagh et al., 1989), where the generalisation comes from the fact that we consider the response variable to follow an Exponential Dispersion Family distribution ([wiki](https://en.wikipedia.org/wiki/Exponential_dispersion_model)). This family is a rich class of probability distributions that contains most of the distributions you may be familiar with. Each distribution is defined through two parameters: the location parameter and a scale parameter. The link function plays the role of "linking" the value of the linear predictor to the location parameter of the distribution.}

\notes{Many classical statistical models can be written in the language of generalised linear models. Below, a list of models that fall into this category is shown ([source](https://online.stat.psu.edu/stat504/lesson/6/6.1)). Each model is characterised by three different components: an exponential dispersion family distribution of the response, a link function, and a linear predictor from the explanatory variables.}

\notes{

| Model                | Response Variable | Link              | Explanatory Variable |
|----------------------|-------------------|-------------------|-----------------------|
| Linear Regression    | Normal           | Identity          | Continuous            |
| Logistic Regression  | Binomial         | Logit             | Mixed                 |
| Poisson Regression   | Poisson          | Log               | Mixed                 |
| ANOVA                | Normal           | Identity          | Categorical           |
| ANCOVA               | Normal           | Identity          | Mixed                 |
| Loglinear            | Poisson          | Log               | Categorical           |
| Multinomial Response | Multinomial      | Generalized Logit | Mixed                 |}

\notes{The exponential dispersion family can be written in the following canonical form,}

$$ f(y; \theta, \phi) = \exp \left( \frac{\theta y - b(\theta)}{a(\phi)} + c(y, \phi) \right), $$

\notes{where $\theta$ is the location and $\phi$ the scale parameter, respectively. A special instantiation of this is the Gaussian distribution,}

$$ f(y; \mu, \sigma^2) = \exp \left( \frac{\mu y - \frac{1}{2} \mu^2}{\sigma^2} - \frac{y^2}{2\sigma^2} - \frac{1}{2} \ln(2\pi\sigma^2) \right),$$

\notes{where we can identify,}

$$ \theta = \mu, $$

$$ \phi = \sigma^2, $$

$$ b(\theta) = \frac{1}{2} \theta^2, $$

$$ a(\phi) = \phi, $$

$$ c(y, \phi) = \frac{y^2}{2\phi} - \frac{1}{2} \ln(2\pi\phi). $$

\notes{The benefit of writing the distribution in this general form is that we can easily derive a general expression for both the first and the second moments of the predictive distribution,}

$$ \mathbb{E}[y | x] = \frac{\partial}{\partial \theta} b(\theta), $$

$$ \mathbb{V}[y | x] = a(\phi) \frac{\partial^2}{\partial \theta^2} b(\theta). $$

\notes{This means that given a GLM, we can compute predictions and our uncertainty about those predictions in closed form. We will now proceed to look at how we can fit these models to data and learn the parameters $\beta$ that connect the explanatory variables with the response.}

\endif
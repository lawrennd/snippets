\ifndef{emukitSensitivityAnalysis}
\define{emukitSensitivityAnalysis}
\define{emukitSensitivityAnalysis}

\editme

\subsection{Emukit Sensitivity Analysis}


\notes{This introduction is based on [Introduction to Global Sensitivity Analysis with Emukit](https://github.com/EmuKit/emukit/blob/master/notebooks/Emukit-tutorial-sensitivity-montecarlo.ipynb) written by Mark Pullin, Javier Gonzalez, Juan Emmanuel Johnson and Andrei Paleyes. Some references include [@Kennedy-predicting00;@Sobol-sensitivity90;@Sobol-global01;@Saltelli-sensitivity04;@Saltelli-global08;@Saltelli-variance10]}

> A possible definition of sensitivity analysis is the following: The study of
> how uncertainty in the output of a model (numerical or otherwise) can be
> apportioned to different sources of uncertainty in the model input [@Saltelli-sensitivity04]. A related practice is 'uncertainty analysis', which focuses
> rather on quantifying uncertainty in model output. Ideally, uncertainty
> and sensitivity analyses should be run in tandem, with uncertainty analysis
> preceding in current practice.
>
> In Chapter 1 of @Saltelli-global08

\newslide{What is Sensitivity Analysis?}

\slides{* Study of how output uncertainty relates to input uncertainty
* Determines which inputs contribute most to output variations
* Complements uncertainty analysis which quantifies output uncertainty
* Best practice: Run uncertainty analysis first, then sensitivity analysis}

\setupcode{import numpy as np
import matplotlib.pyplot as plt

from matplotlib import colors as mcolors
from matplotlib import cm}

\installcode{mlai}

\installcode{GPy}
\installcode{pyDOE}
\installcode{EmuKit}

\setupcode{import mlai
import mlai.plot as plot}

\notes{Sensitivity analysis is a statistical technique widely used to test the reliability of real systems. Imagine a simulator of taxis picking up customers in a city like the one showed in the [Emukit playground](https://github.com/amzn/emukit-playground). The profit of the taxi company depends on factors like the number of taxis on the road and the price per trip. In this example, a global sensitivity analysis of the simulator could be useful to decompose the variance of the profit in a way that can be assigned to the input variables of the simulator.}

\notes{There are different ways of doing a sensitivity analysis of the variables of a simulator. In this notebook we will start with an approach based on Monte Carlo sampling that is useful when evaluating the simulator is cheap. If evaluating the simulator is expensive, emulators can then be used to speed up computations. We will show this in the last part of the notebook. Next, we start with a few formal definitions and literature review so we can understand the basics of Sensitivity Analysis and how it can be performed with Emukit.}


\subsection{Local Sensitivity Analysis}

\notes{Given any function, $\mappingFunctionTwo(\cdot)$, we might be interested in how sensitive that function is to variations in its input space. One route to determining this is to compute the partial derivatives of that function with respect to its inputs,
$$
\frac{\partial}{\partial\inputScalar_i} \mappingFunctionTwo(\inputVector).
$$
The matrix of all these partial derivatives is known as the Jacobian.}

\slides{* Examines function sensitivity around a specific point
* Uses partial derivatives (Jacobian matrix)
* Only valid near operating point
* Limited view - doesn't capture global behavior
* Useful for small perturbations around operating point}

\notes{These types of local sensitivity analysis can be used for determining the effect of changing an input variable around an operating point. But they don't give us an understanding of the response of the target function to variations in the input across the domain of inputs. For this, we need to look to *global sensitivity analysis*.}



\subsection{Global Sensitivity Analysis}

\slides{* Examines sensitivity across entire input domain
* Uses ANOVA/Hoeffding-Sobol decomposition
* Based on total variance of function
* Requires assumptions about input distributions
* More comprehensive than local analysis}

\notes{In global sensitivity analysis, rather than looking around a single operating point, we're interested in the overall sensitivity of a function to its inputs, or combinations of inputs, across its entire domain. The key tool in determining this sensitivity is known as the ANOVA decomposition, or the *Hoeffding-Sobol decomposition*.}

\newslide{The Maths}
\slides{* Total variance of function:
  $$\text{var}\left(\mappingFunctionTwo(\inputVector)\right) = \expectationDist{\mappingFunctionTwo(\inputVector)^2}{p(\inputVector)} - \expectationDist{\mappingFunctionTwo(\inputVector)}{p(\inputVector)}^2$$

* Expectation defined as:
  $$\expectationDist{h(\inputVector)}{p(\inputVector)} = \int_\inputVector h(\inputVector) p(\inputVector) \text{d}\inputVector$$

* $p(\inputVector)$ represents probability distribution of inputs}

\notes{For global sensitivity analysis, we need to make an assumption about how inputs are going to vary to create different values of the function. The fundamental object we're interested in is the total variance of the function,
$$
\text{var}\left(\mappingFunctionTwo(\inputVector)\right) = \expectationDist{\mappingFunctionTwo(\inputVector)^2}{p(\inputVector)} - \expectationDist{\mappingFunctionTwo(\inputVector)}{p(\inputVector)}^2,
$$
where
$$
\expectationDist{h(\inputVector)}{p(\inputVector)} = \int_\inputVector h(\inputVector) p(\inputVector) \text{d}\inputVector
$$
is the expectation of the function $h(\inputVector)$ under the density $p(\inputVector)$, which represents the probability distribution of inputs we're interested in.}

\newslide{Input Density}

\slides{* Assume inputs are independent
* Each input uniformly distributed
* Scale inputs to [0,1] interval
* Simplifies analysis while maintaining generality}

\newslide{Input Density Mathematics}

\slides{* Independent inputs means:
  $$p(\inputVector) = \prod_{i=1}^\dataDim p(\inputScalar_i)$$
* Uniform distribution on [0,1]:
  $$\inputScalar_i \sim \uniformSamp{0}{1}$$}

\subsection{Hoeffding-Sobol Decomposition}

\newslide{Decomposition}

\slides{* Function decomposed into sum of terms:
  $$\mappingFunctionTwo(\inputVector) = \mappingFunctionTwo_0 + \sum_{i=1}^\dataDim \mappingFunctionTwo_i(\inputScalar_i) + \sum_{i<j}^{\dataDim} \mappingFunctionTwo_{ij}(\inputScalar_i,\inputScalar_j)$$
  $$+ \sum_{i<j<k}^{\dataDim} \mappingFunctionTwo_{ijk}(\inputScalar_i,\inputScalar_j,\inputScalar_k) + \cdots + \mappingFunctionTwo_{1,2,\dots,\dataDim}(\inputScalar_1,\dots,\inputScalar_\dataDim)$$}

\newslide{Decomposition Terms}

\slides{* Terms represent:
    * Constant ($\mappingFunctionTwo_0$)
    * Individual effects ($\mappingFunctionTwo_i$)
    * Interaction effects ($\mappingFunctionTwo_{ij}$)
    * Higher-order interactions}

\newslide{Base Terms}

\slides{* Constant term is overall expectation:
  $$\mappingFunctionTwo_0 = \expectationDist{\mappingFunctionTwo(\inputVector)}{p(\inputVector)}$$
* Individual effects:
  $$\mappingFunctionTwo_i(\inputScalar_i) = \expectationDist{\mappingFunctionTwo(\inputVector)}{p(\inputVector_{\sim i})} - \mappingFunctionTwo_0$$
* Where $p(\inputVector_{\sim i})$ means marginalizing out $i$th variable:
  $$p(\inputVector_{\sim i}) = \int p(\inputVector) \text{d}\inputScalar_i$$}

\newslide{Interaction Terms}

\slides{* Two-way interactions:
  $$\mappingFunctionTwo_{i,j}(\inputScalar_i, \inputScalar_j) = \expectationDist{\mappingFunctionTwo(\inputVector)}{p(\inputVector_{\sim i,j})} - \mappingFunctionTwo_i - \mappingFunctionTwo_j - \mappingFunctionTwo_0$$
* Higher order terms follow similar pattern
* Each term requires computing lower-order terms first}

\notes{The Hoeffding-Sobol, or ANOVA, decomposition of a function allows us to write it as,
$$
\begin{align*}
\mappingFunctionTwo(\inputVector) = & \mappingFunctionTwo_0 + \sum_{i=1}^\dataDim \mappingFunctionTwo_i(\inputScalar_i) + \sum_{i<j}^{\dataDim} \mappingFunctionTwo_{ij}(\inputScalar_i,\inputScalar_j) + \cdots \\
& + \mappingFunctionTwo_{1,2,\dots,\dataDim}(\inputScalar_1,\inputScalar_2,\dots,\inputScalar_\dataDim),
\end{align*}
$$
where
$$
\mappingFunctionTwo_0 = \expectationDist{\mappingFunctionTwo(\inputVector)}{p(\inputVector)
$$
and
$$
\mappingFunctionTwo_i(\inputScalar_i) = \expectationDist{\mappingFunctionTwo(\inputVector)}{p(\inputVector_{\sim i})} - \mappingFunctionTwo_0,
$$
where we're using the notation $p(\inputVector_{\sim i})$ to represent the input distribution with the $i$th variable marginalised,
$$
p(\inputVector_{\sim i}) = \int p(\inputVector) \text{d}\inputScalar_i
$$
Higher order terms in the decomposition represent interactions between inputs,
$$
\mappingFunctionTwo_{i,j}(\inputScalar_i, \inputScalar_j) = \expectationDist{\mappingFunctionTwo(\inputVector)}{p(\inputVector_{\sim i,j})} - \mappingFunctionTwo_i(\inputScalar_i) - \mappingFunctionTwo_j(\inputScalar_j) - \mappingFunctionTwo_0
$$
and similar expressions can be written for higher order terms up to $\mappingFunctionTwo_{1,2,\dots,\dataDim}(\inputVector)$.}

\notes{Note that to compute each of these individual terms, you need to first compute the low order terms, and then compute the high order terms. This can be problematic when $\dataDim$ is large.}

\notes{We're interested in the variance of the function $\mappingFunctionTwo$, so implicitly we're assuming that the square of this function is integrable across its domain, i.e., we're assuming that $\expectationDist{\mappingFunctionTwo(\inputVector)^2}{p(\inputVector)}$ exists and is finite.}

\newslide{Variance Decomposition}

\slides{* Sobol decomposition components are orthogonal
* Leads to variance decomposition:
  $$\text{var}(\mappingFunctionTwo) = \expectationDist{\mappingFunctionTwo(\inputVector)^2 }{p(\inputVector)} - \mappingFunctionTwo_0^2$$}

\newslide{ANOVA Decomposition}

\slides{* Decomposes into sum of variance terms:
  $$\text{var}(\mappingFunctionTwo) = \sum_{i=1}^\dataDim \text{var}\left(\mappingFunctionTwo_i(\inputScalar_i)\right) + \sum_{i<j}^{\dataDim} \text{var}\left(\mappingFunctionTwo_{ij}(\inputScalar_i,\inputScalar_j)\right) + \cdots$$
* Known as ANOVA (Analysis of Variance) decomposition
* Each term represents variance from different input interactions}

\newslide{Sobol Indices}

\slides{* Rescale variance components by total variance
* Gives Sobol indices:
  $$S_\ell = \frac{\text{var}\left(\mappingFunctionTwo(\inputVector_\ell)\right)}{\text{var}\left(\mappingFunctionTwo(\inputVector)\right)}$$
* $\ell$ represents different input combinations
* See @Durrande-anova13 for elegant approach using covariance structure}

\notes{The Sobol decomposition has some important properties, in particular, its components are orthogonal, so this means that when we substitute it in to the variance, we have,
$$
\begin{align*}
\text{var}(\mappingFunctionTwo) = & \expectationDist{\mappingFunctionTwo(\inputVector)^2 }{p(\inputVector)} - \expectationDist{\mappingFunctionTwo(\inputVector)}{p(\inputVector)}^2 \\
 = & \expectationDist{\mappingFunctionTwo(\inputVector)^2 }{p(\inputVector)} - \mappingFunctionTwo_0^2\\
 = & \sum_{i=1}^\dataDim \text{var}\left(\mappingFunctionTwo_i(\inputScalar_i)\right) + \sum_{i<j}^{\dataDim} \text{var}\left(\mappingFunctionTwo_{ij}(\inputScalar_i,\inputScalar_j)\right)  + \cdots \\ & + \text{var}\left(\mappingFunctionTwo_{1,2,\dots,\dataDim}(\inputScalar_1,\inputScalar_2,\dots,\inputScalar_\dataDim)\right).
\end{align*}
$$
So, this decomposition gives us a decomposition of the function in terms of variances. It's for this reason that it's sometimes known as an ANOVA decomposition. ANOVA stands a for *analysis of variance*. The ANOVA decomposition decomposes the function into additive variance parts that are each stemming from interactions between different inputs.}

\notes{As is common in various analyses of variance, we can rescale the components with the *total variance* of the function. These rescaled components are known as *Sobol indicies*.
$$
S_\ell = \frac{\text{var}\left(\mappingFunctionTwo(\inputVector_\ell)\right)}{\text{var}\left(\mappingFunctionTwo(\inputVector)\right)},
$$
where the $\ell$ represents the relevent set of indices for the different combinations of inputs.}

\notes{In practice, for an elegant approach that exploits a particular covariance function structure to perform global sensitivity analysis see @Durrande-anova13.}

\newslide{Sobol Indices: The Intuition}

\slides{* Sobol indices tell us "how much each input matters"
* Values between 0 and 1:
    * 0 means input has no effect
    * 1 means output variance entirely due to this input
* Can analyze:
    * Individual inputs ($S_i$)
    * Pairs of inputs ($S_{ij}$)
    * Higher-order interactions
* Sum of all indices = 1}

\section{Example: the Ishigami function}

\newslide{Ishigami Function Example: Overview}

\slides{* Will explore sensitivity analysis using Ishigami test function
* Selected because it allows exact calculation of Sobol indices
* In real applications, exact calculation rarely possible
* Will demonstrate progression of methods:
    1. Exact calculation (possible for Ishigami)
    2. Monte Carlo estimation (general but expensive)
    3. GP emulation (efficient approximation)}

\notes{In this section, we'll work through a practical example of sensitivity analysis using the Ishigami function. We've specifically chosen this function because it's one of the rare cases where we can calculate Sobol indices exactly. This gives us a valuable reference point for understanding approximate methods.

However, it's important to note that in real-world applications, exact calculation of sensitivity indices is often impossible. The methods we'll demonstrate progress from:
1. Exact calculation (possible only for special cases like Ishigami)
2. Monte Carlo estimation (applicable generally but computationally expensive)
3. Gaussian process emulation (an efficient approximation method for expensive functions)

Through this progression, you'll understand both the ideal case and the practical approaches needed in real applications.}

\notes{We illustrate the exact calculation of the Sobol indices with the three-dimensional Ishigami function of [@Ishigami-importance90].} 

\include{_uq/includes/ishigami-function.md}

\subsection{Total Variance}

\notes{The total variance $\text{var}(\dataScalar)$ in this example is}

\code{print(ishigami.variance_total)}

\notes{which is the sum of the variance of $\text{var}\left(\mappingFunctionTwo_1(\inputScalar_1)\right)$, $\text{var}\left(\mappingFunctionTwo_2(\inputScalar_2)\right)$ and $\text{var}\left(\mappingFunctionTwo_{1,3}(\inputScalar_{1,3})\right)$}

\code{print(ishigami.variance_x1, ishigami.variance_x2, ishigami.variance_x13)
print(ishigami.variance_x1 + ishigami.variance_x2 + ishigami.variance_x13)}

\subsection{First Order Sobol Indices using Monte Carlo}

\notes{The first order Sobol indices are a measure of "first order sensitivity" of each input variable. They account for the proportion of variance of $\dataScalar$ explained by changing each variable alone while marginalizing over the rest. Recall that the Sobol index of the $i$th variable is computed as}
$$
S_i = \frac{\text{var}\left(\mappingFunctionTwo_i(\inputScalar_i)\right)}{\text{var}\left(\mappingFunctionTwo(\inputVector)\right)}.
$$
\notes{This value is standardized using the total variance, so it is possible to account for a fractional contribution of each variable to the total variance of the output.}

\notes{The Sobol indices for higher order interactions $S_{i,j}$ are computed similarly. Due to the normalization by the total variance, the the sum of all Sobol indices equals to one.}

\notes{In most cases we are interested in the first order indices. The Ishigami function has the benefit that these can be computed analytically. In `EmuKit` you can extract these values with the code.}

\code{ishigami.main_effects}

\notes{But in general, these indices need to be sampled using Monte Carlo or one of the quasi-Monte Carlo methods we've seen in the model-free experimental design. Details are given in [@Sobol-global01].}

\notes{With Emukit, the first-order Sobol indices can be easily computed. We first need to define the space where the target simulator is analyzed.}

\setupcode{from emukit.sensitivity.monte_carlo import ModelFreeMonteCarloSensitivity}

\code{np.random.seed(10)  # for reproducibility

num_monte_carlo_points = 10000  # Number of MC samples
senstivity_ishigami = ModelFreeMonteCarloSensitivity(target_simulator, space)
main_effects, total_effects, _ = senstivity_ishigami.compute_effects(num_monte_carlo_points = num_monte_carlo_points)
print(main_effects)}

\notes{We compare the true effects with the Monte Carlo effects in a bar-plot. The total effects are discussed later.}

\slides{* First plot compares true Sobol indices with Monte Carlo estimates
* Shows relative importance of each input variable
* Demonstrates accuracy of Monte Carlo sampling approach}

\setupplotcode{import pandas as pd}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)

d = {'Sobol True': ishigami.main_effects,
     'Monte Carlo': main_effects}

pd.DataFrame(d).plot(kind='bar', ax=ax)
ax.set_title('First-order Sobol indices - Ishigami')
ax.set_ylabel('% of explained output variance')

mlai.write_figure(filename='first-order-sobol-indices-ishigami.svg', directory='\writeDiagramsDir/uq')}

\figure{\includediagram{\diagramsDir/uq/first-order-sobol-indices-ishigami}{80%}}{The non-zero components of the Ishigami function.}{first-order-sobol-indices-ishigami}

\subsection{Total Effects Using Monte Carlo}

\notes{Computing high order sensitivity indices can be computationally very demanding in high dimensional scenarios and measuring the total influence of each variable on the variance of the output is infeasible. To solve this issue the *total* indices are used which account for the contribution to the output variance of $\inputScalar_i$ including all variance caused by the variable alone and all its interactions of any order. 

The total effect for $\inputScalar_i$ is given by:
$$ 
S_{Ti} = \frac{\expectationDist{\text{var}_{\inputScalar_i} (\dataScalar \mid \inputVector_{\sim i})}{p(\inputVector_{\sim i})}}{\text{var}\left(\mappingFunctionTwo(\inputVector)\right)} = 1 - \frac{\text{var}_{\inputVector_{\sim i}} \expectationDist{\dataScalar \mid \inputVector_{\sim i}}{p(\inputVector_{\sim i})}}{\text{var}\left(\mappingFunctionTwo(\inputVector)\right)}
$$

Note that the sum of $S_{Ti}$ is not necessarily one in this case unless the model is additive. In the Ishigami example the value of the total effects is}

\code{ishigami.total_effects}

\notes{As in the previous example, the total effects can be computed with Monte Carlo. In the next plot we show the comparison with the true total effects.}

\slides{* Next plot shows total effects - including all variable interactions
* Compares true values with Monte Carlo estimates
* Demonstrates how variables influence output through interactions}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)

d = {'Sobol True': ishigami.total_effects,
     'Monte Carlo': total_effects}

pd.DataFrame(d).plot(kind='bar', ax=ax)
ax.set_title('Total effects - Ishigami')
ax.set_ylabel('Effects value')

mlai.write_figure(filename='total-effects-ishigami.svg', directory='\writeDiagramsDir/uq')}

\figure{\includediagram{\diagramsDir/uq/total-effects-ishigami}{80%}}{The total effects from the Ishigami function as computed via Monte Carlo estimate alongside the true total effects for the Ishigami function.}{total-effects-ishigami}

\subsection{Computing the Sensitivity Indices Using the Output of a Model}

\notes{In the example used above the Ishigami function is very cheap to evaluate. However, in most real scenarios the functions of interest are expensive, and we need to limit ourselves to a few number of evaluations. Using Monte Carlo methods is infeasible in these scenarios as a large number of samples are typically required to provide good estimates of the Sobol indices.}

\notes{An alternative in these cases is to use Gaussaian process emulator of the function of interest trained on a few inputs and outputs [@Marrel-sobol09]. If the model is properly trained, its mean prediction which is cheap to evaluate, can be used to compute the Monte Carlo estimates of the Sobol indices, the variance from the GP emulator can also be used to assess our uncertainty about the Sobol indices. Let's see how we can do this in Emukit.}

\notes{We start by generating 100 samples in the input domain. Note that this a just 1% of the number of samples that we used to compute the Sobol coefficients using Monte Carlo.}

\setupcode{from emukit.core.initial_designs import RandomDesign}

\code{design = RandomDesign(space)
x = design.get_samples(500)
y = ishigami.fidelity1(x)[:,np.newaxis]}

\notes{Now, we fit a standard Gaussian process to the samples, and we wrap it as an Emukit model.}

\setupcode{from GPy.models import GPRegression
from emukit.model_wrappers import GPyModelWrapper
from emukit.sensitivity.monte_carlo import MonteCarloSensitivity}

\code{model_gpy = GPRegression(x,y)
model_emukit = GPyModelWrapper(model_gpy)
model_emukit.optimize()}

\notes{The final step is to compute the coefficients using the class `ModelBasedMonteCarloSensitivity` which directly calls the model and uses its predictive mean to compute the Monte Carlo estimates of the Sobol indices. We plot the true estimates, those computed using 10000 direct evaluations of the object using Monte Carlo and those computed using a Gaussian process model trained on 100 evaluations.}

\code{num_mc = 10000
senstivity_ishigami_gpbased = MonteCarloSensitivity(model = model_emukit, input_domain = space)
main_effects_gp, total_effects_gp, _ = senstivity_ishigami_gpbased.compute_effects(num_monte_carlo_points = num_mc)}

\slides{* Final plots compare three approaches:
    * True Sobol indices
    * Direct Monte Carlo estimation
    * GP-based estimation
* Shows how GP emulator can approximate sensitivity with fewer samples}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)

main_effects_gp = {ivar: main_effects_gp[ivar][0] for ivar in main_effects_gp}

d = {'Sobol True': ishigami.main_effects,
     'Monte Carlo': main_effects,
     'GP Monte Carlo':main_effects_gp}

pd.DataFrame(d).plot(kind='bar', ax=ax)
plt.title('First-order Sobol indices - Ishigami')
plt.ylabel('% of explained output variance')

mlai.write_figure(filename='first-order-sobol-indices-gp-ishigami.svg', directory='\writeDiagramsDir/uq')}

\figure{\includediagram{\diagramsDir/uq/first-order-sobol-indices-gp-ishigami}{80%}}{First order Sobol indices as estimated by Monte Carlo and GP-emulator based Monte Carlo.}{first-order-sobol-indices-gp-ishigami}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)

total_effects_gp = {ivar: total_effects_gp[ivar][0] for ivar in total_effects_gp}

d = {'Sobol True': ishigami.total_effects,
     'Monte Carlo': total_effects,
     'GP Monte Carlo':total_effects_gp}

pd.DataFrame(d).plot(kind='bar', ax=ax)
ax.set_title('Total effects - Ishigami')
ax.set_ylabel('% of explained output variance')

mlai.write_figure(filename='total-effects-sobol-indices-gp-ishigami.svg', directory='\writeDiagramsDir/uq')}

\newslide{}

\figure{\includediagram{\diagramsDir/uq/total-effects-sobol-indices-gp-ishigami}{80%}}{Total effects as estimated by Monte Carlo and GP based Monte Carlo.}{total-effects-sobol-indices-gp-ishigami}

\notes{We observe some discrepancies with respect to the real value of the Sobol index when using the Gaussian process, but we get a fairly good approximation with a very reduced number of evaluations of the original target function.}

\subsection{Conclusions}
\slides{* Sobol indices tool for explaining variance of output as coponents of input variables.}
\notes{The Sobol indices are a tool for explaining the variance of the output of a function as components of the input variables. Monte Carlo is an approach for computing these indices if the function is cheap to evaluate. Other approaches are needed when $\mappingFunctionTwo(\cdot)$ is expensive to compute.}


\endif

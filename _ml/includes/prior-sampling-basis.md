\ifndef{priorSamplingBasis}
\define{priorSamplingBasis}
\editme

\subsection{Generating from the Model}

\slides{
$$
\dataVector = \basisMatrix \mappingVector + \noiseVector
$$ 

* Sample
  $$
  \mappingVector \sim \gaussianSamp{0}{\alpha\eye}
  $$
  $$
  \noiseVector \sim \gaussianSamp{\zerosVector}{\dataStd^2}
  $$ 
  with $\alpha=1$ and $\dataStd^2 = 0.01$.
}

\notes{
A very important aspect of probabilistic modelling is to *sample* from your model to see what type of assumptions you are making about your data. In this case that involves a two stage process.

1. Sample a candiate parameter vector from the prior.
2. Place the candidate parameter vector in the likelihood and sample functions conditiond on that candidate vector.
3. Repeat to try and characterise the type of functions you are generating.

Given a prior variance (as defined above) we can now  sample from the prior distribution and combine with a basis set to see what assumptions we are making about the functions *a priori* (i.e. before we've seen the data). Firstly we compute the basis function matrix. We will do it both for our training data, and for a range of prediction locations (`x_pred`).}

\include{_ml/includes/olympic-marathon-polynomial-sample.md}

\notes{There are two distributions we are interested in though. We have just been sampling from the *prior* distribution to see what sort of functions we get *before* looking at the data. In Bayesian inference, we also need to compute the *posterior* distribution and sample from that density.}

\endif

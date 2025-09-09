\ifndef{basisFunctionsFittingToData}
\define{basisFunctionsFittingToData}

\editme


\subsection{Fitting to Data}

  
\notes{Now we are going to consider how these basis functions can be adjusted to fit to
a particular data set. We will return to the olympic marathon data from last
time. First we will scale the output of the data to be zero mean and variance 1.}

\include{_datasets/includes/olympic-marathon-data.md}


\newslide{Notebook Example}

\slides{* In the notebook you are asked to scale the weights to fit functions to Olympic Marathon data.}

\comment{\writeassignment{Now we are going to redefine our polynomial basis. Have a careful look at the operations we perform on `x` to create `z`. We use `z` in the polynomial computation. What are we doing to the inputs? Why do you think we are changing `x` in this manner?}{10}}



\setupdisplaycode{import matplotlib.pyplot as plt
import notutils as nu}
\displaycode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
yhat = (y - offset)/scale

_ = ax.plot(x, yhat, 'r.',markersize=10)
nu.display_prediction(basis=dict(radial=mlai.radial, 
	                                        polynomial=mlai.polynomial, 
											tanh=mlai.hyperbolic_tangent, 
											fourier=mlai.fourier, 
											relu=mlai.relu), 
                                 data_limits=xlim,
                                 fig=fig, ax=ax,
                                 offset=0.,
                                 wlim = (-4., 4.),
                                 num_basis=4)}

\codeassignment{Use the tool provided above to try and find the best
fit you can to the data. Explore the parameter space and give the weight values
you used for the 

(a) polynomial basis
(b) Radial basis
(c) Fourier basis

Write your answers in the code box below creating a new vector of parameters (in the correct order!) for each basis.}{
# (a) polynomial
###### Edit these lines #####
# w_0 =
# w_1 = 
# w_2 = 
# w_3 =
##############################
# w_polynomial = np.asarray([[w_0], [w_1], [w_2], [w_3]]) 

# (b) radial
###### Edit these lines #####
# w_0 =
# w_1 = 
# w_2 = 
# w_3 =
##############################
# w_rbf = np.asarray([[w_0], [w_1], [w_2], [w_3]]) 

# (c) fourier
###### Edit these lines #####
# w_0 =
# w_1 = 
# w_2 = 
# w_3 =
##############################
# w_fourier = np.asarray([[w_0], [w_1], [w_2], [w_3]])}{15}

\code{np.asarray([[1, 2, 3, 4]]).shape}

\subsection{Basis Function Models}

\slides{* The *prediction function* is now defined as }
  $$
  \mappingFunction(\inputVector_i) = \sum_{j=1}^\numBasisFunc \mappingScalar_j \basisFunc_{i, j}
  $$

\newslide{Vector Notation}
\slides{
* Write in vector notation,}
  $$
  \mappingFunction(\inputVector_i) = \mappingVector^\top \basisVector_i
  $$

\endif

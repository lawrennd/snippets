\ifndef{thinkingInHighDimensions}
\define{thinkingInHighDimensions}

\editme

\subsection{Thinking in High Dimensions}

\notes{A recurring plot that is shown in talks on machine learning,
particularly those on clustering, is a configuration of data points in
two dimensions such as those below.}

\notes{At first glance, the
data appears quite realistic. The density of the data points varies
considerably as we move around the plot. The data seems to be
clustered, but not in a uniform manner: some clusters are tighter than
others. The clusters also seem to be somewhat randomly distributed
around the plot. At some point during the talk, a slide containing a
fit to the data.}

\notes{This figure
shows the means and variances of a mixture of multivariate (two
dimensional) Gaussian densities\index{mixture of Gaussians}
(@McLachlan-mix88).  The fit seems to be a good approximation to
the data.}

\notes{Models of this type can also be justified by appeals to our intuition.
The way I like to think of these mixture models is as a summary of the
data by a series of prototypes (represented by the means of the
Gaussian components of the mixture density). These prototypes are
subject to distortions. The density associated with each component
represents the range of distortions that the data can undergo. In the
case of the mixture of Gaussians, the distortions are of the form of
adding zero mean, Gaussian\index{Gaussian density} distributed, random
noise with a particular covariance matrix.}

\subsection{Mixtures of Gaussians}

\setupplotcode{import mlai
import mlai.plot as plot}
    
\code{for j in range(2):
  model = plot.mog(20, 200)
  
  if model.d > 2:
      model = model.project(2)
      
  model_type = model.type
  model_type = model_type[0].upper() + model_type[1:]
  
  file_name = f'dem-artificial-{model_type}{j+1}'
  
  # First plot with ovals
  fig, ax = plt.subplots()
  ax.set_position([0.05, 0.05, 0.9, 0.9])
  plot.mog_plot_2d(model, ax)
  
  pi_vals = np.linspace(-np.pi, np.pi, 200)
  for i in range(model.m):
      ax.plot(model.mean[i,0], model.mean[i,1], 'o', 
              linewidth=2, markersize=10)
      x = np.vstack([np.sin(pi_vals), np.cos(pi_vals)]).T
      el = x @ model.U[i]
      ax.plot(model.mean[i,0] + el[:,0], 
              model.mean[i,1] + el[:,1],
              linewidth=2)
      
  x_lim = np.array([model.Y[:,0].min(), model.Y[:,0].max()]) * 1.1
  y_lim = np.array([model.Y[:,1].min(), model.Y[:,1].max()]) * 1.1
  ax.set_xlim(x_lim)
  ax.set_ylim(y_lim)
  ax.set_xticks([-2, -1, 0, 1, 2])
  ax.set_yticks([-2, -1, 0, 1, 2])
  
  mlai.write_figure(f'{file_name}_slides', 
                    '\writeDiagramsDir/dimred')
  
  # Second plot without ovals
  fig, ax = plt.subplots(figsize=plot.big_figsize)
  ax.set_position([0.05, 0.05, 0.9, 0.9])
  plot.mog_plot_2d(model, ax)
  
  ax.set_xlim(x_lim)
  ax.set_ylim(y_lim) 
  ax.set_xticks([-2, -1, 0, 1, 2])
  ax.set_yticks([-2, -1, 0, 1, 2])
  
  ma.write_figure(filename=f'{file_name}NoOvals_slides',
                    directory='\writeDiagramsDir/dimred')}

\figure{\includediagram{\diagramsDir/dimred/dem-artificial-mog-1}{40%}}{Two dimensional Gaussian data set.}{artificial-mog-1-no-ovals}

\figure{\includediagram{\diagramsDir/dimred/dem-artificial-mog-2}{40%}}{Two dimensional data sets. Complex structure not a problem for mixtures of Gaussians.}{artificial-mog-2}

    
\section{High Dimensional Data}

\subsection{Thinking in High Dimensions}

\slides{* Two dimensional plots of Gaussians can be misleading.
* Our low dimensional intuitions can fail dramatically. 
* Two major issues:
  1. In high dimensions all the data moves to a 'shell'. There is nothing near the mean!
  2. Distances between points become constant.
  3. These affects apply to many densities.
* Let's consider a Gaussian "egg".}

Such a model seems intuitively appealing. When the
\emph{\gls{expectation_maximization}} approach to optimizing such
powerful models was first described by \cite{Dempster:EM77} the
statistics community it must have seemed to some that the main
remaining challenge for density estimation was principally
computational. There are, of course, applications for which for which
a mixture of Gaussians\index{mixture of Gaussians} is an appropriate
model (\emph{e.g.}  low dimensional data). Such applications are not
the focus of \emph{this} book. We are more interested in the failings
of the Gaussian mixture\index{mixture of Gaussians}. There are two
foundation assumptions which underpin this model. We described them
both in our early appeal to intuition. The first assumption is that
the data is generated through prototypes\index{data prototypes}. We
will not consider this assumption further. We will focus on the second
assumption: how the prototypes are corrupted to obtain the data we
observe. For the Gaussian mixture\index{mixture of Gaussians} model
the prototypes are corrupted by Gaussian noise with a particular
covariance. It is this second assumption that we would like to
consider first. In particular, we are going to examine the special
case where the covariance is given by a constant diagonal matrix. We
will see that the behavior of a Gaussian in low dimensional space can
be quite misleading when we develop intuitions as to how these
densities behave in higher dimensions. By higher dimensionality we can
think of dimensionality that is difficult to visualize directly,
\emph{i.e.}\ dimensionality greater than $\dataDim=3$.

\subsection{Dimensionality Greater than Three}

In higher dimensions \emph{models} that seem reasonable in two or
three dimensions can fail dramatically. Note the emphasis on models.
In this section, we are not making any statements about how a
`realistic' data set behaves in higher dimensions, we are making
statements about modeling failures in higher dimensions. In particular
we will focus on what assumptions the model makes about where the data
is distributed in higher dimensions. We will illustrate the ideas
through introducing the Gaussian egg. The Gaussian egg is a hard
boiled egg that consists of three parts: the yolk of the egg, the
white of the egg and a thin boundary shell between the yolk and the
white.  In an over boiled egg the boundary layer is often green from
iron sulfide formed by reactions between the white and the yolk,
giving a bad taste. We therefore refer to this as the ``green'' of the
egg. We will consider spherical Gaussian distributions which have
covariance matrices of the form $\dataStd^2\eye$. We define the
volume of the density associated with the yolk as part of the egg that
is within $0.95\dataStd$ of the mean. The green is defined to be the
region from $0.95\dataStd$ to $1.05\dataStd$. Finally, the yolk is all
the density beyond $1.05\dataStd$. We assume the density of the egg
varies according to the Gaussian density, so that the density at the
center of the egg is highest, and density falls off with the
exponentiated negative squared Euclidean distance from the mean. We
take the overall mass of our egg to be one. The question we now ask is
how much of our egg's mass is now taken up by the three component
parts: the green, the white and the yolk. The proportions of the mass
are dependent on the dimensionality of our egg.

The answer is found through integrating over the Gaussian. For a one
dimensional egg we can find the portion of the Gaussian that sits
inside 0.95 of a standard deviation's distance from the mean as
\[
\int_{-0.95\dataStd}^{0.95\dataStd} \gaussianDist{\dataScalar}{0}{\dataStd^{2}} \text{d}\dataScalar.
\]
The other portions can be found similarly. For higher dimensional
Gaussians the integral is slightly more difficult. To compute it, we
will switch from considering the Gaussian density that governs the
data directly to the density over squared distances from the mean that
the Gaussian implies. Before we introduce that approach, we show three
low dimensional Gaussian eggs in
\reffigrange{fig:oneDGaussianEgg}{fig:threeDGaussianEgg} indicating
their associated masses for the yolk, the green and the white.
% 
\begin{figure}
  \begin{center}
    \includegraphics[width=0.4\textwidth]{../diagrams/oneDgaussian_nobrown}
  \end{center}

  \caption{Volumes associated with the one dimensional Gaussian
    egg. Here the yolk has 65.8\%, the green has 4.8\% and the white
    has 29.4\% of the mass. }\label{fig:oneDGaussianEgg}
\end{figure}

\begin{figure}
  \begin{center}
    \includegraphics[width=0.4\textwidth]{../diagrams/twoDgaussian_nobrown2}
  \end{center}

  \caption{Volumes associated with the regions in the two dimensional
    Gaussian egg. The yolk contains 59.4\%, the green contains 7.4\%
    and the white 33.2\%.}\label{fig:twoDGaussianEgg}

\end{figure}
\begin{figure}
  \begin{center}
    \includegraphics[width=0.4\textwidth]{../diagrams/threeDgaussian_nobrown}
  \end{center}

  \caption{Volumes associated with the regions in the three
    dimensional Gaussian egg. Here the yolk has 56.1\% the green has
    9.2\% the white has 34.7\%.}\label{fig:threeDGaussianEgg}
\end{figure}


\subsection{The Gaussian Egg}

\notes{* See also Exercise 1.4 in @Bishop:book95

\figure{}
  
\setuphelpercode{import numpy as np
from scipy.stats import norm, multivariate_normal
import matplotlib.pyplot as plt
import mlai
import mlai.plot as plot}

\helpercode{plot.gaussian_volume_1D(directory='\writeDiagramsDir/dimred/')
plot.gaussian_volume_2D(directory='\writeDiagramsDir/dimred/')
plot.gaussian_volume_3D(directory='\writeDiagramsDir/dimred/')}

\slides{
One D: \colorbox{lightpurple}{
        \textcolor{yellow}{65.8\%}, \color{ironsulf}4.8\%
        \textcolor{white}{29.4\%}}}
Two D: \colorbox{lightpurple}{\textcolor{yellow}{59.4\%},
        \color{ironsulf}7.4\% \textcolor{white}{33.2\%}}}

Three D: \colorbox{lightpurple}{
        \textcolor{yellow}{56.1\%}, \color{ironsulf}9.2\%,
        \textcolor{white}{34.7\%}}}
 }
 
\newslide{Mathematics}

\slides{**What is the density of probability mass?**

For a d-dimensional Gaussian distribution:

1. **Individual components**: $y_{i,k} \sim \mathcal{N}(0, \sigma^2)$
2. **Squared components**: $y_{i,k}^2 \sim \sigma^2 \chi_1^2$ (scaled chi-squared)
3. **Gamma distribution**: $y_{i,k}^2 \sim \text{Gamma}(\frac{1}{2}, \frac{1}{2\sigma^2})$
4. **Sum of squares**: $\sum_{k=1}^d y_{i,k}^2 \sim \text{Gamma}(\frac{d}{2}, \frac{1}{2\sigma^2})$
5. **Expected value**: $\langle \sum_{k=1}^d y_{i,k}^2 \rangle = d\sigma^2$
6. **Normalized sum**: $\frac{1}{d}\sum_{k=1}^d y_{i,k}^2 \sim \text{Gamma}(\frac{d}{2}, \frac{d}{2\sigma^2})$
7. **Expected normalized**: $\langle \frac{1}{d}\sum_{k=1}^d y_{i,k}^2 \rangle = \sigma^2$}

\setupplotcode{import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gamma, chi2
import mlai
import mlai.plot as plot}

\code{def plot_distance_distributions():
    """Plot distance distributions for different dimensions"""
    fig, axes = plt.subplots(1, 3, figsize=(12, 4))
    
    # 1D case
    x = np.linspace(0, 10, 100)
    chi2_1d = chi2.pdf(x, df=1)
    axes[0].plot(x, chi2_1d, 'b-', linewidth=2, label='χ²(1)')
    axes[0].set_title('1D: χ² distribution')
    axes[0].set_xlabel('Distance²')
    axes[0].set_ylabel('Density')
    axes[0].legend()
    axes[0].grid(True, alpha=0.3)
    
    # 2D case
    gamma_2d = gamma.pdf(x, a=1, scale=1)
    axes[1].plot(x, gamma_2d, 'r-', linewidth=2, label='Gamma(1,1)')
    axes[1].set_title('2D: Gamma distribution')
    axes[1].set_xlabel('Distance²')
    axes[1].set_ylabel('Density')
    axes[1].legend()
    axes[1].grid(True, alpha=0.3)
    
    # High-dimensional case
    gamma_high = gamma.pdf(x, a=5, scale=0.2)
    axes[2].plot(x, gamma_high, 'g-', linewidth=2, label='Gamma(5,0.2)')
    axes[2].set_title('High-D: Concentrated Gamma')
    axes[2].set_xlabel('Distance²')
    axes[2].set_ylabel('Density')
    axes[2].legend()
    axes[2].grid(True, alpha=0.3)
    
    plt.tight_layout()
    return fig

fig = plot_distance_distributions()
mlai.write_figure(filename='distance-distributions', directory='\writeDiagramsDir/dimred')}

\slides{
\begin{center}
  \only<1>{Square of sample from Gaussian is scaled chi-squared
    density}
  \only<2>{Chi squared density is a variant of the gamma
    density with shape parameter $a=\frac{1}{2}$, rate parameter
    $b=\frac{1}{2\dataStd^{2}}$, $\gammaDist
    xab=\frac{b^{a}}{\Gamma\left(a\right)}x^{a-1}e^{-bx}$.}
  \only<3-4>{Addition
    of gamma random variables with the same rate is gamma with sum
    of shape parameters ($y_{i,k}$s are
    independent)}
  \only<5>{Scaling of gamma density scales the rate
    parameter}
\end{center}
}
\newslide{Where is the Mass?}

\slides{* Squared distances are gamma distributed.}
\begin{figure}

\setupplotcode{import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gamma
import mlai
import mlai.plot as plot}

\plotcode{
# Set up dimensions
x = np.arange(0, 11)
D = 2.0**x
lim1 = 0.95
lim2 = 1.05
lim3 = 100

# Compute values of cumulative gammas
y = gamma.cdf(lim1*lim1, D/2, scale=2/D)
y2 = gamma.cdf(lim2*lim2, D/2, scale=2/D)
y3 = gamma.cdf(lim3*lim3, D/2, scale=2/D)

# Create figure
fig, ax = plt.subplots(figsize=plot.big_figsize)

# Compute patch outlines
xp1 = np.concatenate([[x[0]], x, [x[-1]], [x[0]]])
p1 = np.concatenate([[0], y, [0], [0]])
xp2 = np.concatenate([[x[0]], x, x[::-1]])
p2 = np.concatenate([[y[0]], y2, y[::-1]])
xp3 = np.concatenate([[x[0]], x, x[::-1]])
p3 = np.concatenate([[y2[0]], y3, y2[::-1]])

# Draw patches
ax.fill(xp1, p1, color=[1, 1, 0], alpha=0.7)
ax.fill(xp2, p2, color=[0, 0.7, 0.5], alpha=0.7)
ax.fill(xp3, p3, color=[1, 1, 1], alpha=0.7)

# Set exponentiated labels
ax.set_xticks(x)
ax.set_xticklabels([str(int(2**xi)) for xi in x])
ax.set_yticks([0, 0.25, 0.5, 0.75, 1])
ax.set_xlabel('dimension', fontsize=12)
ax.tick_params(labelsize=23)

mlai.write_figure(filename='dimension-mass.svg', 
                  directory='\writeDiagramsDir/dimred')}
				  
				  
\figure{\includediagram{\diagramsDir/dimension-mass}{40%}}{Plot of probability mass versus dimension. Plot shows the
    volume of density inside 0.95 of a standard deviation (yellow),
    between 0.95 and 1.05 standard deviations (green), over 1.05
    and standard deviations (white).}{dimension-mass}

\subsection{Distribution of Mass against Dimensionality }

\notes{For the three low dimensional Gaussians, we note that the allocation
of the egg's mass to the three zones changes as the dimensionality
increases. The green and the white increase in mass and the yolk
decreases in mass. Of greater interest to us is the behavior of this
distribution of mass in higher dimensions. It turns out we can compute
this through the cumulative distribution function of the gamma
density. }

\notes{We will compute the distribution of the density mass in the three
regions by assuming each data point is sampled independently from our
spherical covariance Gaussian density,
\[
\dataVector_{i, :} \sim \gaussianSamp{\zerosVector}{\dataStd^2\eye}
\]
where $\dataVector_{i, :}$ is the $i$th data point. Independence
across features also means we can consider the density associated with
the $k$th feature of the $i$th data point, $\dataScalar_{i,k}$,
\[
\dataScalar_{i,k}\sim\gaussianSamp{0}{\dataStd^{2}}.
\]
We are interested in the squared distance of any given sample from the
mean. Our choice of a zero mean Gaussian density means that the
squared distance of each feature from the mean is easily computed as
$\dataScalar_{i,k}^2$. We can exploit a useful characteristic of the
Gaussian to describe the density of these squared distances. The
squares of a Gaussian distributed random variable are known to be
distributed according the *chi-squared density*,
\[
\dataScalar_{i,k}^{2}\sim\dataStd^{2}\chi_{1}^{2},
\]
The chi squared density is a special case of the gamma
density  with shape
parameter $a=\frac{1}{2}$ and rate parameter
$b=\frac{1}{2\dataStd^{2}}$,
\[
\gammaDist{x}{a}{b}=\frac{b^{a}}{\Gamma\left(a\right)}x^{a-1}e^{-bx}.
\]}

\include{_statistics/includes/the-gamma-density.md}

\notes{So we have the squared distance from the mean for a single feature being given
by
\[
\dataScalar_{i,k}^{2}\sim\gammaSamp{\frac{1}{2}}{\frac{1}{2\dataStd^{2}}}.
\]
Of course, we are interested in the distance from the mean of the data
point given by $\dataVector_{i,:}=\left[\dataScalar_{i,1}, \dots,
  \dataScalar_{i,\dataDim}\right]^\top$. The \emph{squared} distance
from the mean of the $i$th data point will be given by
$\sum_{k=1}^\dataDim \dataScalar_{i,k}^2$. Fortunately, the properties
of the gamma density\index{gamma density} (see \refbox{box:gamma})
mean we can also compute the density of the resulting random variable,
in particular we have
\[
\sum_{k=1}^{\dataDim}y_{i,k}^{2}\sim\gammaSamp{\frac{\dataDim}{2}}{\frac{1}{2\dataStd^{2}}}.
\]
We can compute the mean and standard deviation of the squared distance
for each point from the mean,
\[
\expectation{\sum_{k=1}^{\dataDim}y_{i,k}^{2}}=\dataDim\dataStd^{2},
\]
which, we note, scales linearly with the dimensionality of the
data. The average squared distance of each feature will be distributed as
follows,
\[
\frac{1}{\dataDim}\sum_{k=1}^{\dataDim}y_{i,k}^{2}\sim\gammaSamp{\frac{\dataDim}{2}}{\frac{\dataDim}{2\dataStd^{2}}}
\]
the mean for which is simply the variance of the underlying Gaussian
density,
\[
\expectation{\frac{1}{\dataDim}\sum_{k=1}^{\dataDim}y_{i,k}^{2}}=\dataStd^{2}.
\]
We can use this gamma density to work out how much of the mass of the
Gaussian egg is in the different zones. The cumulative distribution
function for the gamma density,
\[
\gammaCdf{z}{a}{b} = \int_0^{x}\gammaDist{z}{a}{b} \text{d} z,
\]
doesn't have a nice analytical form, but implementations of it are
provided for many programming languages including R, \textsc{Matlab},
Octave and Python. We can use the cumulative distribution to give the
probability of the squared distance falling under a certain value. For
the data point to be in the yolk, we expect its squared distance from
the mean to be under $(0.95\dataStd)^2$. For the data point to be in
the green we expect its squared distance from the mean to be between
$(0.95/\dataStd)^2$ and $(1.05/\dataStd)^2$. Data in the white will
have a squared distance from the mean greater than
$(1.05/\dataStd)^2$.}
%
\figure{\includediagram{\diagramsDir/dimred/distance2}{40%}}{Distance from mean of the density (circle) to a given data point (square).}{distance2}

\subsection{Looking at Gaussian Samples}

\notes{The theory has shown us that data sampled from a Gaussian density in
very high dimensions will live in a shell around one standard
deviation from the mean of the Gaussian. This is perhaps surprising
because we are used to thinking of Gaussians being distributions where
most of the data is near the mean of the density. But this is because
we are used to looking at low dimensional Gaussian densities. In this
regime most of the data is near the mean. One useful property of the
Gaussian density is that all the marginal densities are also
Gaussian. This means that when we see a two dimensional Gaussian we
can think of it as a three dimensional Gaussian with one dimension
marginalized. The effect of this marginalization is to project the
third dimension down onto the other two by summing across it. This
means when we see a two dimensional Gaussian on a page such as that in
\reffig{fig:projectedGaussian}, we can think of a corresponding three
dimensional Gaussian which has this two dimensional Gaussian as a
marginal. That three dimensional Gaussian would have data going into
and coming out of the page. The projection down to two dimensions
makes that data look like it is close to the mean, but when we expand
up to the three dimensional Gaussian some of that data moves away from
the mean. Following this line of argument, we can ask what if the plot
is the two dimensional marginal of a truly four dimensional
Gaussian. Now some more of the data that appears close to the mean in
the two dimensional Gaussian (and perhaps was close to the mean in the
three dimensional Gaussian) is also projected away. We can continue
applying this argument until we can be certain that there is no data
left near the mean. So the gist of the argument is as follows. When
you are looking at a low dimensional projection of a high dimensional
Gaussian, it does appear that there is a large amount of data close to
the mean. But, when we consider that the data near the mean has been
projected down from potentially many dimensions we understand that in
fact there is very little data near the mean.}

\setupplotcode{}

\plotcode{
    close all
    a = randn(2);
    a = a*a';
    Y = gsamp([0, 0], a, 300);
    a = plot(Y(:, 1), Y(:, 2), 'rx');
    set(a, 'linewidth', 3);
    %set(a, 'markersize', 10);
    %set(gca, 'fontsize', 20)
    zeroAxes(gca);
    printLatexPlot('twoDGaussianSamples', '../../../dimred/tex/diagrams/', 0.8*textWidth)
}

\figure{\includediagram{\diagramsDir/dimred/projected-2d-gaussian}{40%}}{Looking at a projected Gaussian. This plot shows, in two
    dimensions, samples from a potentially very high dimensional
    Gaussian density. The mean of the Gaussian is at the origin. There
    appears to be a lot of data near the mean, but when we bear in
    mind that the original data was sampled from a much higher
    dimensional Gaussian we realize that the data has been projected
    down to the mean from those other dimensions that we are not
    visualizing.}{projected-2d-gaussian}

\subsection{High Dimensional Gaussians and Interpoint Distances}

\notes{Our analysis above showed that for spherical Gaussians in high
dimensions the density of squared distances from the mean collapses
around the expected value of one standard deviation. Another related
effect is the distribution of *interpoint* squared distances. It
turns out that in very high dimensions, the interpoint squared
distances become equal. This has knock on effects for many learning
algorithms: for example in nearest neighbors classification algorithms a test data point is assigned
a label based on the labels of the $k$ nearest neighbors from the
training data. If all interpoint squared distances were close to equal
then the stability of these $k$ neighbors with respect to small data
perturbations would be poor.}

\notes{\tk{Something wrong here} Can show this for Gaussians with a similar proof to the above,
\[
\dataScalar_{i,k}\sim\gaussianSamp 0{\dataStd_{k}^{2}}\quad\quad\dataScalar_{j,k}\sim\gaussianSamp 0{\dataStd_{k}^{2}}
\]
\[
\dataScalar_{i,k}-\dataScalar_{j,k}\sim\gaussianSamp 0{2\dataStd_{k}^{2}}]
\]
\[
\left(\dataScalar_{i,k}-\dataScalar_{j,k}\right)^{2}\sim\gammaSamp{\frac{1}{2}}{\frac{1}{4\dataStd_{k}^{2}}}
\]
Once again we can consider the specific case where the data is
spherical, $\dataStd_{k}^{2}=\dataStd^{2}$, as we can always
individually rescale the data input dimensions to ensure this is the
case
\[
\sum_{k=1}^{\dataDim}\left(\dataScalar_{i,k}-\dataScalar_{j,k}\right)^{2}\sim\gammaSamp{\frac{\dataDim}{2}}{\frac{1}{4\dataStd^{2}}}
\]
\[
\frac{1}{\dataDim}\sum_{k=1}^{\dataDim}\left(\dataScalar_{i,k}-\dataScalar_{j,k}\right)^{2}\sim\gammaSamp{\frac{\dataDim}{2}}{\frac{D}{4\dataStd^{2}}}
\]
The dimension normalized squared distance between points is Gamma
distributed.  Mean is $2\dataStd^{2}$. Variance is
$\frac{8\dataStd^{2}}{D}$.}

\newslide{Looking at Gaussian Samples}

  \begin{figure}
\setupplotcode{import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import multivariate_normal
import mlai
import mlai.plot as plot}

\code{# Generate random covariance matrix
np.random.seed(42)  # For reproducibility
a = np.random.randn(2, 2)
cov_matrix = a @ a.T

# Sample from multivariate Gaussian
mean = np.array([0, 0])
Y = np.random.multivariate_normal(mean, cov_matrix, 300)

# Create plot
fig, ax = plt.subplots(figsize=plot.big_figsize)
ax.plot(Y[:, 0], Y[:, 1], 'rx', markersize=4)
ax.set_xlim([Y[:, 0].min()*1.1, Y[:, 0].max()*1.1])
ax.set_ylim([Y[:, 1].min()*1.1, Y[:, 1].max()*1.1])
ax.set_aspect('equal')
ax.grid(True, alpha=0.3)

mlai.write_figure(filename='two-d-gaussian-samples.svg', 
                  directory='\writeDiagramsDir/dimred')}



\newslide{Interpoint Distances}

\slides{* The other effect in high dimensions is all points become
    equidistant.
* Can show this for Gaussians with a similar proof to the
    above:
    
    **Interpoint Distance Analysis:**
    
    For two points $i$ and $j$ in d-dimensional space:
    
    1. **Individual components**: $y_{i,k} \sim \mathcal{N}(0, \sigma_k^2)$ and $y_{j,k} \sim \mathcal{N}(0, \sigma_k^2)$
    2. **Difference**: $y_{i,k} - y_{j,k} \sim \mathcal{N}(0, 2\sigma_k^2)$
    3. **Squared difference**: $(y_{i,k} - y_{j,k})^2 \sim \text{Gamma}(\frac{1}{2}, \frac{1}{4\sigma_k^2})$
    
    For spherical Gaussian where $\sigma_k^2 = \sigma^2$:
    
    4. **Sum of squared differences**: $\sum_{k=1}^d (y_{i,k} - y_{j,k})^2 \sim \text{Gamma}(\frac{d}{2}, \frac{1}{4\sigma^2})$
    5. **Normalized distance**: $\frac{1}{d}\sum_{k=1}^d (y_{i,k} - y_{j,k})^2 \sim \text{Gamma}(\frac{d}{2}, \frac{d}{4\sigma^2})$
    
    **Key Results:**
    - Mean distance: $2\sigma^2$
    - Variance: $\frac{8\sigma^2}{d}$ (decreases with dimension!)
    - All points become equidistant as $d \to \infty$
}


\newslide{Central Limit Theorem and Non-Gaussian Case}

\slides{* We can compute the density of squared distance *analytically*
    for spherical, independent Gaussian data.
* More generally, for *independent* data, the *central
      limit theorem* applies.

  * The mean squared distance in high dimensional space is the mean
      of the variances.
  * The variance about the mean scales as $\dataDim^{-1}$.}


\newslide{Summary}

\slides{* In high dimensions if individual dimensions are *independent*
    the distributions behave counter intuitively.
* All data sits at one standard deviation from the mean.
* The densities of squared distances can be analytically
    calculated for the Gaussian case.
* For non-Gaussian \emph{independent} systems we can invoke the central
    limit theorem.
* Next we will consider example data sets and see how their interpoint
    distances are distributed.}

\endif

 

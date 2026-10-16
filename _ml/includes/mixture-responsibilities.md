\ifndef{mixtureResponsibilities}
\define{mixtureResponsibilities}

\editme

\subsection{Mixture Responsibilities}

\notes{Hard clustering gives every point a single label: point $i$ belongs to component $c(i)$ and to no other. A *mixture* model instead treats the component index as a latent variable and returns a full posterior over components. Write $\pi_c = p(c)$ for the prior weight of component $c$, and $p(\dataVector_i\mid c)$ for that component's density at the point. Bayes' rule then yields the *responsibility*
$$
r_{ic}
=
p(c\mid\dataVector_i)
=
\frac{
\pi_c\, p(\dataVector_i\mid c)
}{
\sum_{c'} \pi_{c'}\, p(\dataVector_i\mid c')
}.
$$
The row $(r_{i1},\ldots,r_{iC})$ is a discrete distribution over components for point $i$. Hard assignment is the special case that replaces this row by a one-hot vector at $\arg\max_c r_{ic}$.}

\slides{
* Hard clustering: one label $c(i)$ per point
* Mixture: component is latent; posterior over components
* Responsibility $r_{ic}=p(c\mid\dataVector_i)$
* Row $(r_{i1},\ldots,r_{iC})$ sums to one
* Hard assignment $=$ one-hot at $\arg\max_c r_{ic}$
}

\setupplotcode{import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
import mlai
import mlai.plot as plot}

\plotcode{rng = np.random.default_rng(0)
# Two isotropic Gaussian components in 2D
means = np.array([[-1.2, 0.0], [1.2, 0.3]])
# Shared noise scale: small → sharp responsibilities; large → soft
sigma2_sharp = 0.35
sigma2_soft = 2.0
priors = np.array([0.5, 0.5])
# Probe points along the line joining the means
probes = np.array([
    [-1.2, 0.0],
    [-0.4, 0.1],
    [0.0, 0.15],
    [0.4, 0.2],
    [1.2, 0.3],
])

def responsibilities(X, means, sigma2, priors):
    # log N(x|m, sigma2 I) up to shared additive constant over components
    # when all components share sigma2 and dimension
    log_lik = np.stack([
        -0.5 * np.sum((X - m) ** 2, axis=1) / sigma2
        for m in means
    ], axis=1)
    log_post = log_lik + np.log(priors)[None, :]
    log_post -= log_post.max(axis=1, keepdims=True)
    post = np.exp(log_post)
    return post / post.sum(axis=1, keepdims=True)

# Sample cloud for context
cloud = np.vstack([
    rng.normal(means[0], np.sqrt(sigma2_sharp), size=(40, 2)),
    rng.normal(means[1], np.sqrt(sigma2_sharp), size=(40, 2)),
])
colours = ['#4C72B0', '#DD8452']

fig, axes = plt.subplots(1, 2, figsize=plot.big_wide_figsize)
for ax, sigma2, title in [
    (axes[0], sigma2_sharp, rf'sharp ($\sigma^2={sigma2_sharp:g}$)'),
    (axes[1], sigma2_soft, rf'soft ($\sigma^2={sigma2_soft:g}$)'),
]:
    R = responsibilities(probes, means, sigma2, priors)
    ax.scatter(cloud[:, 0], cloud[:, 1], s=12, c='#bbbbbb',
               alpha=0.7, zorder=1)
    for c, m in enumerate(means):
        ax.plot(*m, 'o', color=colours[c], markersize=10, zorder=3,
                label=rf'component ${c}$')
        # one-sd contour
        ell = Ellipse(m, 2 * np.sqrt(sigma2), 2 * np.sqrt(sigma2),
                      fill=False, ec=colours[c], lw=1.5, ls='--', zorder=2)
        ax.add_patch(ell)
    # stacked responsibility bars at probe locations
    bar_w, bar_h = 0.35, 0.9
    for x, r in zip(probes, R):
        y0 = x[1] + 0.55
        ax.add_patch(plt.Rectangle(
            (x[0] - bar_w / 2, y0), bar_w * r[0], bar_h,
            color=colours[0], zorder=4, clip_on=False))
        ax.add_patch(plt.Rectangle(
            (x[0] - bar_w / 2 + bar_w * r[0], y0), bar_w * r[1], bar_h,
            color=colours[1], zorder=4, clip_on=False))
        ax.plot(x[0], x[1], 'k.', markersize=8, zorder=5)
    ax.set_xlim(-2.6, 2.6)
    ax.set_ylim(-2.0, 2.8)
    ax.set_aspect('equal')
    ax.set_title(title)
    ax.set_xlabel('$x_1$')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
axes[0].set_ylabel('$x_2$')
axes[0].legend(loc='lower left', fontsize=9)
fig.suptitle(r'Responsibilities $r_{ic}=p(c\mid x_i)$ at five probes '
             r'(bar $=$ soft weights)', y=1.02)
fig.tight_layout()
mlai.write_figure('mixture-responsibilities.svg',
                  directory='\writeDiagramsDir/ml')}

\newslide{Soft Weights, Not Labels}

\notes{The figure places five probe points between two isotropic Gaussian components and draws, above each probe, a bar whose blue/orange split is the responsibility vector $(r_{i1},r_{i2})$. When the component variance $\noiseStd^2$ is small, probes near a mean are almost one-hot --- soft assignment collapses toward hard labels. When $\noiseStd^2$ is large, the same probes carry substantial mass on *both* components. The mathematical object has not changed: only the component densities $p(\dataVector_i\mid c)$, and therefore the posteriors $r_{ic}$, have become flatter.}

\figure{\includediagram{\diagramsDir/ml/mixture-responsibilities}{90%}}{Two Gaussian components (means as markers; dashed circles at one standard deviation). Grey points are a sample cloud. Stacked bars above five probes show $r_{i1}$ (blue) and $r_{i2}$ (orange). Left: sharp densities. Right: larger shared $\sigma^2$, softer responsibilities.}{mixture-responsibilities}

\slides{
* Bar above each probe $=$ responsibility vector
* Small $\noiseStd^2$: near one-hot (almost hard)
* Large $\noiseStd^2$: mass shared across components
* Same formula; flatter densities $\Rightarrow$ softer $r_{ic}$
}

\newslide{Log-Space Softmax}

\notes{In practice one computes responsibilities in the log domain,
$$
\log r_{ic}
=
\log\pi_c + \log p(\dataVector_i\mid c)
-
\mathrm{logsumexp}_{c'}
\bigl(\log\pi_{c'} + \log p(\dataVector_i\mid c')\bigr),
$$
which is a softmax of the log-joint scores $\log\pi_c + \log p(\dataVector_i\mid c)$. That is the same numerical pattern as multilogue's soft lens weights: each ``component'' is a PPCA Gaussian on a framing lens, $\log p(\dataVector_i\mid c)$ is the PPCA log-likelihood of a cluster centroid, and the resulting row is the mixture weight over lenses. The noise floor that sets each PPCA's factor rank is the same $\noiseStd^2$ that softens these responsibilities.}

\slides{
* $\log r_{ic} = \log\pi_c + \log p(x_i\mid c) - \mathrm{logsumexp}$
* Softmax of log-joint scores
* Multilogue: component $=$ PPCA lens; $x_i=$ cluster centroid
* Same $\noiseStd^2$ sets PPCA rank *and* softens $r_{ic}$
}

\endif

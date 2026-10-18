\ifndef{ppcaNoiseFloor}
\define{ppcaNoiseFloor}

\editme

\subsection{PPCA Noise Floor and Factor Rank}

\notes{Start with a *single* PPCA component. Its noise variance $\noiseStd^2$ is not only a fit parameter --- it is a *threshold on that component's eigenvalue spectrum*. The maximum-likelihood loading retains only factors whose eigenvalues exceed the noise,
$$
\lambda_k > \noiseStd^2,
$$
and discards the rest into the isotropic residual $\noiseStd^2\eye$ [@Tipping-probpca99]. Raising $\noiseStd^2$ therefore lowers that component's factor rank $q$ automatically: the noise floor climbs the scree, and every bar it overtakes ceases to be a latent direction. No separate model-order search is required.}

\slides{
* *One* PPCA component: retain factors with $\lambda_k > \noiseStd^2$
* Factors below the noise are absorbed into $\noiseStd^2\eye$
* Raising $\noiseStd^2$ lowers *that* component's rank $q$
* The noise floor *is* the model-order rule for the component
}

\setupplotcode{import numpy as np
import matplotlib.pyplot as plt
import mlai
import mlai.plot as plot}

\plotcode{# Two synthetic screes: one elongated lens, one flatter
# (eigenvalues of member-centroid covariances, as in mixture-of-PPCA)
sigma2 = 0.5
spectra = {
    'Lens A (elongated)': np.array([2.4, 1.1, 0.65, 0.22, 0.12, 0.08, 0.05]),
    'Lens B (flatter)': np.array([0.95, 0.72, 0.28, 0.18, 0.11, 0.07, 0.04]),
}
colours = {'keep': '#4C72B0', 'drop': '#C0C0C0', 'floor': '#C44E52'}

fig, axes = plt.subplots(1, 2, figsize=plot.big_wide_figsize, sharey=True)
for ax, (name, lambdas) in zip(axes, spectra.items()):
    idx = np.arange(1, len(lambdas) + 1)
    keep = lambdas > sigma2
    q = int(keep.sum())
    ax.bar(idx[keep], lambdas[keep], color=colours['keep'],
           label=rf'retained ($\lambda>\sigma^2$)', zorder=2)
    ax.bar(idx[~keep], lambdas[~keep], color=colours['drop'],
           label=rf'discarded ($\lambda\leq\sigma^2$)', zorder=2)
    ax.axhline(sigma2, color=colours['floor'], lw=2.0, ls='--',
               label=rf'noise floor $\sigma^2={sigma2:g}$', zorder=3)
    ax.set_xticks(idx)
    ax.set_xlabel(r'factor index $k$')
    ax.set_title(rf'{name}: $q={q}$')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
axes[0].set_ylabel(r'eigenvalue $\lambda_k$')
axes[0].legend(loc='upper right', fontsize=9)
fig.suptitle(r'Same shared $\sigma^2$: different per-component rank $q$',
             y=1.02)
fig.tight_layout()
mlai.write_figure('ppca-noise-floor-scree.svg',
                  directory='\writeDiagramsDir/dimred')

# How q falls as the floor rises
sigma_grid = np.logspace(-1.2, 0.6, 40)
fig, ax = plt.subplots(figsize=plot.big_figsize)
for name, lambdas, style in [
    ('Lens A', spectra['Lens A (elongated)'], '-'),
    ('Lens B', spectra['Lens B (flatter)'], '--'),
]:
    q_of_sigma = [int((lambdas > s).sum()) for s in sigma_grid]
    ax.step(sigma_grid, q_of_sigma, where='post', lw=2.0, ls=style,
            label=name)
ax.axvline(sigma2, color=colours['floor'], lw=1.5, ls=':',
           label=rf'$\sigma^2={sigma2:g}$ (scree above)')
ax.set_xscale('log')
ax.set_xlabel(r'noise variance $\sigma^2$')
ax.set_ylabel(r'retained rank $q(\sigma^2)$')
ax.set_yticks(range(0, 8))
ax.set_title(r'Raising the noise floor lowers $q$')
ax.legend(loc='upper right')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
fig.tight_layout()
mlai.write_figure('ppca-noise-floor-rank.svg',
                  directory='\writeDiagramsDir/dimred')}

\newslide{From One Component to Many}

\notes{In a *mixture* of PPCA components --- for example one Gaussian per framing lens, each fitted to its own member centroids --- the truncation rule does not change. Apply it *independently* to each component: component $c$ has its own eigenvalue spectrum $\{\lambda_k^{(c)}\}$, and retains
$$
q_c = \#\{k:\lambda_k^{(c)} > \noiseStd_c^2\}.
$$
What *can* change is whether the noise levels $\noiseStd_c^2$ are free per component or tied to a single shared value $\noiseStd^2$. Those are different modeling choices. Independent floors let each component pick its rank in isolation. A shared floor couples the ranks: the same threshold is drawn across every scree.}

\slides{
* Mixture: apply $\lambda_k > \noiseStd^2$ *per component*
* Each component has its own scree and its own $q_c$
* Choice: separate $\noiseStd_c^2$, or one shared $\noiseStd^2$
* Sharing couples the ranks; the truncation rule itself is unchanged
}

\newslide{Shared Floor, Different Ranks}

\notes{The figure below takes the shared-floor choice. Two components (labelled as lenses) each have their own scree; one horizontal line marks a common $\noiseStd^2$. Component A is elongated: three eigenvalues clear the floor, so $q_A=3$. Component B is flatter: only two clear it, so $q_B=2$. The truncation rule ran separately on each spectrum; the *sharing* of $\noiseStd^2$ is what makes those ranks respond to a single knob. That is the ARD-style truncation used in multilogue's soft PPCA layer (`retain = lambdas > sigma2` inside each lens).}

\figure{\includediagram{\diagramsDir/dimred/ppca-noise-floor-scree}{90%}}{Two mixture components, each with its own eigenvalue scree, under one *shared* noise floor $\sigma^2=0.5$. The discard rule is applied independently: A keeps $q=3$, B keeps $q=2$.}{ppca-noise-floor-scree}

\slides{
* Shared $\noiseStd^2$: same horizontal floor on every scree
* Rule still per-component $\Rightarrow$ different $q_c$
* Elongated A: $q=3$; flatter B: $q=2$
}

\newslide{Rank as a Function of $\noiseStd^2$}

\notes{Sweeping the shared floor makes the coupling explicit. As $\noiseStd^2$ rises, each component's $q_c(\noiseStd^2)$ falls in steps --- one step each time the floor overtakes an eigenvalue *of that component*. The elongated component sheds factors later than the flatter one. Choose the shared floor, and every component's dimensionality follows.}

\figure{\includediagram{\diagramsDir/dimred/ppca-noise-floor-rank}{70%}}{Per-component retained rank $q_c$ against a *shared* $\sigma^2$. The dotted line marks the floor used in the bar plot. Steps occur where that floor crosses an eigenvalue of the given component.}{ppca-noise-floor-rank}

\slides{
* Each $q_c(\noiseStd^2)$ falls in steps as the shared floor rises
* Elongated components keep factors longer
* One knob sets every component's rank
}

\newslide{Why Share the Floor?}

\notes{Sharing $\noiseStd^2$ is what makes the construction honest when the same component Gaussians are later used for soft assignment across the mixture. A direction declared ``noise'' inside one component should not also drive sharp, brittle responsibilities between components. One floor keeps the geometry of each PPCA Gaussian and the softness of the mixture weights commensurate. Selecting that shared floor --- for example by stability of the soft weights across independent runs --- is a later step; the screes already show *what* the floor controls, once you have chosen to share it.}

\slides{
* Shared $\noiseStd^2$ also enters soft mixture likelihoods
* Directions below the floor should not drive sharp assignments
* One floor keeps geometry and soft weights commensurate
* *Which* shared floor to pick is a separate selection problem
}

\endif

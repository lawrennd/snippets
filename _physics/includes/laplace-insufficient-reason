\ifndef{laplaceInsufficientReason}
\define{laplaceInsufficientReason}

\editme

\subsection{Laplace and the Principle of Insufficient Reason}

\include{_physics/includes/laplace-portrait.md}

\newslides{Principle of Insufficient Reason}

\slides{Week 1: Laplace suggested that we treat ignorance with probability. He applied this idea in his estimates of probabilities. He asked himself the question how should we assign $p$ when we know almost nothing?}

\slidesincremental{
* $n$ mutually exclusive, exhaustive outcomes
* Nothing distinguishes one from another
* Assign equal probability: $p_i = 1/n$
}

\speakernotes{Bridge from week 1 (gremlin / ignorance as probability) to MaxEnt. Keep this short: insufficient reason is the zero-constraint special case.}

\notes{In the *Philosophical Essay on Probabilities* [@Laplace-essai14], Laplace argues that probability is relative in part to our ignorance and in part to our knowledge. When we know only that one of $n$ mutually exclusive and exhaustive outcomes must occur, and nothing induces us to prefer one over another, we should assign
\begin{align}
p_i = \frac{1}{n}, \qquad i = 1,\ldots,n.
\end{align}
This is his *principle of insufficient reason* (also called the principle of indifference). It is the least-committal assignment consistent with the information we have: namely, none beyond the list of possibilities and normalisation.}

\notes{The same idea appears in the passage we called Laplace's gremlin in week 1: if several cases are equally possible and nothing favours one, we cannot announce any particular outcome with certainty, and the natural probability weights them equally.}

\newslides{Example: Will the sun rise tomorrow?}

\slides{This is Laplace's example from: *Philosophical Essay on Probabilities* [@Laplace-essai14].}

\includegooglebook{1YQPAAAAQAAJ}{PA16}

\notes{Laplace wondered, what is the probability that the sun will rise tomorrow? We've seen it rise every day so is it 100%?}

\slidesincremental{
* Unknown daily rate $\theta\in[0,1]$; insufficient reason $\Rightarrow$ uniform prior on $\theta$
* Every day is a success: after $n$ rises, belief $\propto\theta^{n}$
* Predictive: $P(\text{rises tomorrow})=\dfrac{n+1}{n+2}$
* Sunrise for $n=1{,}826{,}213$ days: odds $1{,}826{,}214$ to one
* Laplace's caveat: astronomy makes the true odds *incomparably greater*
}

\speakernotes{Board the short derivation. Emphasise: (i) the example is genuine; (ii) Laplace applies insufficient reason to $\theta$, not to tomorrow's binary outcome alone; (iii) every observation is a success — the sun always rises in the data; (iv) he immediately rejects treating the numerical answer as the scientific probability of sunrise.}

\setupplotcode{import numpy as np
import matplotlib.pyplot as plt
import mlai}

\plotcode{# Always visualise: current belief (prior) × likelihood → posterior,
# then a reset frame where the posterior becomes the new prior (colour change;
# likelihood and old prior disappear) before the next update.
# Jumps use likelihood ∝ θ^{Δn} for Δn further sunrises.
theta = np.linspace(0.001, 0.999, 1000)
milestones = [1, 2, 3, 20]  # cumulative sunrises after each update
ymax = (milestones[-1] + 1) * 1.05
diagrams = '\writeDiagramsDir/ml'
prior_c = [1, 0, 0]
lik_c = [0, 0, 1]
post_c = [1, 0, 1]
frame = 0

def _belief(n):
    return (n + 1) * theta**n

def _lik_shape(delta):
    # unnormalised θ^{Δn}; max-scaled for display (label keeps ∝)
    kern = theta**delta
    return kern / kern.max() * (ymax * 0.4)

def _save(ax, texts):
    global frame
    for yfrac, txt, col in texts:
        ax.text(0.05, ymax * yfrac, txt, fontsize=15, color=col)
    frame += 1
    mlai.write_figure(f'laplace-succession{frame:03d}.svg', directory=diagrams)

def _axes():
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, ymax)
    ax.set_xlabel(r'$\theta$')
    ax.set_ylabel(r'density')
    return fig, ax

# Frame 1: prior only
fig, ax = _axes()
ax.plot(theta, _belief(0), color=prior_c, linewidth=3)
_save(ax, [
    (0.90, r'prior (insufficient reason)', prior_c),
    (0.80, r'$P(\mathrm{next})=\frac{1}{2}$', 'k'),
])

n_prev = 0
for n_next in milestones:
    delta = n_next - n_prev
    lik = _lik_shape(delta)
    if delta == 1:
        lik_label = r'likelihood: one more sunrise $\propto\theta$'
    else:
        lik_label = r'likelihood: %d more sunrises $\propto\theta^{%d}$' % (delta, delta)

    # prior + likelihood
    fig, ax = _axes()
    ax.plot(theta, _belief(n_prev), color=prior_c, linewidth=3)
    ax.plot(theta, lik, color=lik_c, linewidth=3)
    _save(ax, [
        (0.90, r'belief after $%d$ sunrise(s)' % n_prev, prior_c),
        (0.78, lik_label, lik_c),
    ])

    # prior + likelihood + posterior
    fig, ax = _axes()
    ax.plot(theta, _belief(n_prev), color=prior_c, linewidth=2, alpha=0.5)
    ax.plot(theta, lik, color=lik_c, linewidth=2, alpha=0.5)
    ax.plot(theta, _belief(n_next), color=post_c, linewidth=3)
    _save(ax, [
        (0.90, r'posterior $\propto$ belief $\times$ likelihood', post_c),
        (0.78, r'after $%d$ sunrise(s): $P(\mathrm{next})=\frac{%d}{%d}$'
         % (n_next, n_next + 1, n_next + 2), 'k'),
    ])

    # reset: posterior becomes the new prior; likelihood and old prior gone
    # (skip after the final milestone so we end on the peaked posterior)
    if n_next != milestones[-1]:
        fig, ax = _axes()
        ax.plot(theta, _belief(n_next), color=prior_c, linewidth=3)
        _save(ax, [
            (0.90, r'posterior $\rightarrow$ new prior', prior_c),
            (0.78, r'ready for the next update', 'k'),
        ])

    n_prev = n_next

n_frames = frame}

\slides{\define{width}{70%}
\startanimation{laplace-succession}{1}{12}
\newframe{\includediagram{\diagramsDir/ml/laplace-succession001}{\width}}{laplace-succession}
\newframe{\includediagram{\diagramsDir/ml/laplace-succession002}{\width}}{laplace-succession}
\newframe{\includediagram{\diagramsDir/ml/laplace-succession003}{\width}}{laplace-succession}
\newframe{\includediagram{\diagramsDir/ml/laplace-succession004}{\width}}{laplace-succession}
\newframe{\includediagram{\diagramsDir/ml/laplace-succession005}{\width}}{laplace-succession}
\newframe{\includediagram{\diagramsDir/ml/laplace-succession006}{\width}}{laplace-succession}
\newframe{\includediagram{\diagramsDir/ml/laplace-succession007}{\width}}{laplace-succession}
\newframe{\includediagram{\diagramsDir/ml/laplace-succession008}{\width}}{laplace-succession}
\newframe{\includediagram{\diagramsDir/ml/laplace-succession009}{\width}}{laplace-succession}
\newframe{\includediagram{\diagramsDir/ml/laplace-succession010}{\width}}{laplace-succession}
\newframe{\includediagram{\diagramsDir/ml/laplace-succession011}{\width}}{laplace-succession}
\newframe{\includediagram{\diagramsDir/ml/laplace-succession012}{\width}}{laplace-succession}
\endanimation}

\notes{\figure{\includediagram{\diagramsDir/ml/laplace-succession012}{70%}}{Each update is belief $\times$ likelihood $\rightarrow$ posterior; a reset frame then promotes the posterior to the new prior (likelihood cleared). Early steps use one more sunrise ($\propto\theta$); the jump to $n=20$ uses the likelihood for $17$ further rises ($\propto\theta^{17}$).}{laplace-succession-figure}}

\newslides{Entropy Day by Day}

\slides{Track differential entropy of the belief $p(\theta)$ as sunrises arrive.}

\slidesincremental{
* Prior: $p(\theta)=1$ on $[0,1]$ $\Rightarrow$ $H_0=0$
* After $n$ rises: $p(\theta)=(n+1)\theta^{n}$
* $H_n=\dfrac{n}{n+1}-\log(n+1)$ (nats)
* Day $n$ information gain: $I_n=H_{n-1}-H_n=\log\!\left(1+\dfrac{1}{n}\right)-\dfrac{1}{n(n+1)}$
}

\speakernotes{Board the one-line integral for $H_n$. Emphasise: entropy of the *belief about* $\theta$ falls (becomes more negative); that fall is the information gained. Uniform$[0,1]$ has $H=0$ by convention of differential entropy — not ``zero uncertainty'' in the Shannon discrete sense.}

\notes{The animation peels probability mass toward $\theta=1$. Quantify that with the differential entropy of the belief,
\begin{align}
H[p] = -\int_0^1 p(\theta)\log p(\theta)\,\mathrm{d}\theta.
\end{align}
Under insufficient reason the prior is uniform on $[0,1]$, so $p(\theta)=1$ and
\begin{align}
H_0 = -\int_0^1 1\cdot\log 1\,\mathrm{d}\theta = 0.
\end{align}
After $n$ sunrises the normalised belief is $p_n(\theta)=(n+1)\theta^{n}$. Substitute and use $\int_0^1\theta^{n}\,\mathrm{d}\theta=1/(n+1)$ together with $\int_0^1\theta^{n}\log\theta\,\mathrm{d}\theta=-1/(n+1)^2$:
\begin{align}
H_n
  &= -\int_0^1 (n+1)\theta^{n}\bigl(\log(n+1)+n\log\theta\bigr)\,\mathrm{d}\theta
   = \frac{n}{n+1}-\log(n+1).
\end{align}
Each sunrise *reduces* this entropy (the number becomes more negative as the density sharpens). The information gained on day $n$ is the drop
\begin{align}
I_n = H_{n-1}-H_n
    = \log\!\left(1+\frac{1}{n}\right)-\frac{1}{n(n+1)}.
\end{align}
The first day buys $I_1=\log 2-\tfrac12\approx 0.193$ nats; the second buys slightly more ($I_2\approx 0.239$); thereafter $I_n$ falls, asymptotically like $1/(2n^2)$. After Laplace's $n\approx 1.8\times 10^6$ days, $H_n\approx 1-\log n$ is large and negative, and each further day adds almost no information about $\theta$.}

\setupplotcode{import numpy as np
import matplotlib.pyplot as plt
import mlai}

\plotcode{ns = np.arange(0, 21)
H = ns / (ns + 1) - np.log(ns + 1)
I = np.full_like(H, np.nan, dtype=float)
I[1:] = np.log(1 + 1 / ns[1:]) - 1 / (ns[1:] * (ns[1:] + 1))

fig, ax = plt.subplots(figsize=(8, 4.5))
ax.plot(ns, H, 'o-', color=[1, 0, 1], linewidth=2, label=r'$H_n$')
ax.plot(ns[1:], I[1:], 's-', color=[0, 0, 1], linewidth=2, label=r'$I_n=H_{n-1}-H_n$')
ax.axhline(0, color='k', linewidth=0.8)
ax.set_xlabel(r'number of sunrises $n$')
ax.set_ylabel('nats')
ax.legend(fontsize=14)
ax.set_title(r'Belief entropy and information gained per sunrise')
mlai.write_figure('laplace-succession-entropy.svg', directory='\writeDiagramsDir/ml')}

\slides{
\includediagram{\diagramsDir/ml/laplace-succession-entropy}{70%}
}

\notes{\figure{\includediagram{\diagramsDir/ml/laplace-succession-entropy}{70%}}{Differential entropy $H_n$ of $p(\theta)$ after $n$ sunrises, and the information $I_n$ gained on day $n$. The prior sits at $H_0=0$; each success drives $H_n$ downward.}{laplace-succession-entropy-figure}}

\notes{A second, coarser reading is the binary entropy of tomorrow's predictive probability $p_n=(n+1)/(n+2)$:
\begin{align}
h(p_n)=-p_n\log p_n-(1-p_n)\log(1-p_n),
\end{align}
which starts at $h(1/2)=\log 2$ and falls toward $0$ as $p_n\to 1$. That tracks uncertainty about the *next day*, whereas $H_n$ tracks uncertainty about the latent rate $\theta$.}

\notes{Laplace applies insufficient reason not only to discrete outcomes, but to an unknown daily rate $\theta\in[0,1]$. Knowing nothing about $\theta$, he places a uniform prior $p(\theta)=1$ on the unit interval. Every recorded day is a *success*: the sun rose. After $n$ independent rises the likelihood is $\theta^n$, so
\begin{align}
p(\theta\mid n\text{ rises}) \propto \theta^{n},
\end{align}
and the probability of one further rise is the posterior mean
\begin{align}
P(\text{rises tomorrow}\mid n\text{ rises})
  = \int_0^1 \theta\, p(\theta\mid n\text{ rises})\,\mathrm{d}\theta
  = \frac{n+1}{n+2}.
\end{align}
This is *Laplace's rule of succession* (the same “$+1$, $+2$” that later appears as Laplace smoothing). In modern notation the posterior is $\mathrm{Beta}(n+1,1)$; after each new sunrise it becomes $\mathrm{Beta}(n+2,1)$, more sharply peaked at $\theta=1$, while the predictive odds move from $1{:}1$ toward certainty without ever quite reaching it.}

\notes{Laplace did not have the Beta distribution by name, and he did not need the Laplace approximation for this result. In the 1774 memoir on inverse probability he evaluates the normalising integrals exactly — what we now write as $\int_0^1 \theta^{n}\,\mathrm{d}\theta = 1/(n+1)$ — via what he called Euler's series. The Beta language is modern packaging of that calculation. The *Laplace approximation* (a local Gaussian expansion of an integrand about its mode) is a different tool, also named after him; it is not how the rule of succession was obtained.}

\notes{In the Essay he takes the oldest historical epoch as five thousand years, or $n=1{,}826{,}213$ days of recorded sunrise, and concludes that — *on this information alone* — the odds on tomorrow's sunrise are $1{,}826{,}214$ to one. He then adds, in the next sentence, that for anyone who recognises the astronomical regularity of days and seasons the probability is *incomparably greater*. The sunrise calculation is a demonstration of the rule under deliberate ignorance of mechanism, not Laplace's estimate of whether the sun will rise.}

\notes{So the preliminary example already shows the pattern we need: insufficient reason supplies the prior of ignorance; each success updates it and peels a little more mass away from small $\theta$; the predictive probability is not the raw frequency $n/n=1$.}

\newslides{From Insufficient Reason to MaxEnt}

\slidesincremental{
* Insufficient reason: uniform when we know only the outcomes (or only $\theta\in[0,1]$)
* Rule of succession: same idea, after observing counts
* Jaynes: maximise $H(p)$ subject to whatever we *do* know
* No extra constraints $\Rightarrow$ MaxEnt recovers $p_i = 1/n$
* Mean energy (or other moments) $\Rightarrow$ exponential family
}

\speakernotes{The punchline: MaxEnt is Laplace's principle with constraints. Uniform / rule of succession are the empty-moment cases; Boltzmann and the Gaussian arrive when we add moment constraints.}

\notes{The principle of insufficient reason, and the rule of succession built from it, answer the case where our information is a list of possibilities and (optionally) raw counts. As soon as we know more — a mean face value on a die, a mean energy, a variance — equal weights, or a uniform prior on a single rate, may fail to encode that information. Jaynes' maximum entropy principle extends Laplace's idea: among all distributions that match the stated constraints, choose the one that maximises Shannon entropy $H(p)=-\sum_i p_i\log p_i$. That choice is maximally noncommittal with respect to everything else.

With only the normalisation constraint $\sum_i p_i=1$, MaxEnt recovers Laplace's uniform assignment $p_i=1/n$. With an additional mean-energy constraint, the same calculation yields Boltzmann weights. With mean and variance, it yields a Gaussian. The exponential family is therefore the family of distributions that generalise insufficient reason from “we know nothing” (or “we know only these counts”) to “we know these moments and nothing more.”}

\notes{Critiques of bare indifference (Bertrand's paradox and related reparameterisation puzzles) motivate the need for an explicit state space and explicit constraints — which is exactly what the MaxEnt formalism supplies. We will not pursue those paradoxes here; the operational fix is to state what is held fixed before maximising $H$. Laplace's own sunrise caveat makes the same point in plain language: once you know the mechanism, you no longer pretend to know only the counts.}

\endif

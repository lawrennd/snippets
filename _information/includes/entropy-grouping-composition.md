\ifndef{entropyGroupingComposition}
\define{entropyGroupingComposition}

\editme

\subsection{Grouping Composition}

\slides{You rarely need the bottom number. Ask a coarser question and stop.}

\slidesincremental{
* "Is it five or above?" --- two outcomes, odds $1:2$
* "Low or high?" --- two outcomes, odds $1:1$: the die *is* a fair coin
* The coarse-grained state has its own entropy, $H(G)$
}

\speakernotes{Start from the practical move: I don't care which face, only whether it is five or above. Or I want a 50/50 decision and I only have a die --- low/high is a coin. In both cases I have stopped part way down the tree. The point of the section is what happens to the entropy when I stop, and when I carry on.}

\notes{Often we do not need to know the exact outcome. If all I care about is whether the die shows five or above, I can stop once that is settled. If I need a fair 50/50 decision and only have a die, I can call $\{1,2,3\}$ "low" and $\{4,5,6\}$ "high"; the die, coarse-grained, *is* a fair coin. In both cases we have replaced the fine variable $X$ (the face) with a coarse variable $G=g(X)$ (the group), and $G$ has its own entropy: $H(G)=\log_2 2 = 1$ bit for the coin, and $H(G)=H(\tfrac{2}{3},\tfrac{1}{3})\approx 0.918$ bits for "five or above". That number is the uncertainty in the coarse-grained state, and it is all we pay if we stop there.}

\setupplotcode{import numpy as np
import matplotlib.pyplot as plt
import mlai
import mlai.plot as plot}

\plotcode{def entropy(p):
    p = np.asarray(p, dtype=float)
    p = p[p > 0]
    return -np.sum(p * np.log2(p))

def draw_die_tree(ax, groups, names, title):
    faces = [f for g in groups for f in g]
    xface = np.linspace(0.08, 0.92, len(faces))
    xpos = dict(zip(faces, xface))
    w = np.array([len(g) for g in groups]) / 6.0
    yroot, ygroup, yface = 0.92, 0.55, 0.15
    ax.plot(0.5, yroot, 'o', color='k', markersize=10)
    ax.text(0.5, yroot + 0.05, 'die', ha='center', va='bottom', fontsize=12)
    cols = ['tab:blue', 'tab:orange', 'tab:green']
    for i, g in enumerate(groups):
        xg = np.mean([xpos[f] for f in g])
        ax.plot([0.5, xg], [yroot, ygroup], '-', color=cols[i], lw=1 + 6 * w[i])
        ax.text((0.5 + xg) / 2 + (0.03 if xg > 0.5 else -0.03), (yroot + ygroup) / 2,
                'w=%d/6' % len(g), ha='left' if xg > 0.5 else 'right',
                fontsize=11, color=cols[i])
        ax.plot(xg, ygroup, 's', color=cols[i], markersize=12)
        ax.text(xg, ygroup + 0.04, names[i], ha='center', va='bottom', fontsize=11)
        for f in g:
            ax.plot([xg, xpos[f]], [ygroup, yface], '-', color=cols[i], lw=1.2)
            ax.plot(xpos[f], yface, 'o', color=cols[i], markersize=8)
            ax.text(xpos[f], yface - 0.06, str(f), ha='center', va='top', fontsize=12)
    Hw = entropy(w)
    Hres = np.sum([wi * np.log2(len(g)) for wi, g in zip(w, groups)])
    ax.text(1.02, (yroot + ygroup) / 2, 'H(G) = %.3f' % Hw, fontsize=11, va='center')
    ax.text(1.02, (ygroup + yface) / 2, 'H(X|G) = %.3f' % Hres, fontsize=11, va='center')
    ax.text(1.02, 0.0, 'total = %.3f bits' % (Hw + Hres), fontsize=11, va='center',
            fontweight='bold')
    ax.set_title(title, fontsize=13)
    ax.set_xlim(-0.05, 1.3)
    ax.set_ylim(-0.12, 1.05)
    ax.axis('off')

fig, axs = plt.subplots(1, 2, figsize=plot.big_wide_figsize)
draw_die_tree(axs[0], [[1, 2, 3, 4], [5, 6]], ['below 5', '5 or above'],
              'Is it five or above?')
draw_die_tree(axs[1], [[1, 2, 3], [4, 5, 6]], ['low', 'high'],
              'Low or high? (a fair coin)')
mlai.write_figure(filename='die-coarse-graining-trees.svg',
                  directory='\writeDiagramsDir/information')}

\figure{\includediagram{\diagramsDir/information/die-coarse-graining-trees}{90%}}{Two coarse-grainings of a fair die. The top level is the coarse question, with branch widths set by the group probabilities $w_i$; the bottom level is the residual detail. Stopping at the squares costs $H(G)$. Going all the way down costs $H(G)+H(X\mid G)$, which is $\log_2 6$ for either cut.}{die-coarse-graining-trees}

\newslide{Coarse-Grained Entropies Compose}

\slides{Stopping costs $H(G)$. Carrying on adds the residual. The total never changes.}

\slidesmall{
$$
H(X)=\underbrace{H(w)}_{\text{coarse state}}+\underbrace{\sum_i w_i\, H(p_i)}_{\text{residual detail}}
$$
}

\slidesincremental{
* $w_i$: probability of group $i$; $p_i$: distribution *inside* group $i$
* Five or above: $0.918 + \left(\tfrac{2}{3}\cdot 2 + \tfrac{1}{3}\cdot 1\right) = 0.918 + 1.667 = \log_2 6$
* Coin: $1 + \log_2 3 = \log_2 6$
}

\notes{Partition the outcomes of $X$ into groups labelled by $i$, with group probabilities $w_i$ and within-group distributions $p_i$. Then
\begin{align}
H(X)=H(w)+\sum_i w_i\, H(p_i).
\end{align}
The first term is the entropy of the coarse-grained state; the second is the average uncertainty left once the group is known. For "five or above", $H(w)=H(\tfrac{2}{3},\tfrac{1}{3})\approx 0.918$ and the residual is $\tfrac{2}{3}\log_2 4+\tfrac{1}{3}\log_2 2\approx 1.667$; for the coin, $1+\log_2 3$. Both sum to $\log_2 6$. Different cuts split the bill differently, but the bill is the same.

If $G=g(X)$ is the group label, the identity is exactly the chain rule
\begin{align}
H(X)=H(G)+H(X\mid G),
\end{align}
because $G$ is a function of $X$ (so $H(G\mid X)=0$) and $H(X\mid G)=\sum_i w_i H(p_i)$.}

\speakernotes{This is the chain rule for a deterministic grouping $G=g(X)$: $H(X)=H(G)+H(X\mid G)$. Board that identification.}

\newslide{Coarse-Graining a Coarse-Graining}

\slides{Coarse-grainings nest, and their entropies add stage by stage.}

\plotcode{stages = [
    ['five or above?', [entropy([2 / 3., 1 / 3.]), (2 / 3.) * 2 + (1 / 3.) * 1],
     ['H(G)', 'H(X|G)']],
    ['low or high?', [1.0, np.log2(3)], ['H(G)', 'H(X|G)']],
    ['five+, pair, face',
     [entropy([2 / 3., 1 / 3.]), (2 / 3.) * 1, 1.0],
     ['H(G)', "H(G'|G)", "H(X|G')"]],
]
cols = ['tab:blue', 'tab:orange', 'tab:green']
fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
for j, (name, parts, labels) in enumerate(stages):
    left = 0.0
    for k, (val, lab) in enumerate(zip(parts, labels)):
        ax.barh(j, val, left=left, color=cols[k], edgecolor='k', height=0.6)
        ax.text(left + val / 2, j, '%s\n%.3f' % (lab, val), ha='center', va='center',
                fontsize=9, color='black', fontweight='bold')
        left += val
ax.axvline(np.log2(6), color='k', ls='--')
ax.text(np.log2(6), -0.5, r'$\log_2 6 = %.3f$ bits' % np.log2(6),
        ha='center', va='bottom', fontsize=11)
ax.set_yticks(range(len(stages)))
ax.set_yticklabels([s[0] for s in stages], fontsize=11)
ax.invert_yaxis()
ax.set_xlabel('bits', fontsize=11)
ax.set_xlim(0, 3.0)
for s in ['top', 'right']:
    ax.spines[s].set_visible(False)
mlai.write_figure(filename='die-coarse-graining-budget.svg',
                  directory='\writeDiagramsDir/information')}

\figure{\includediagram{\diagramsDir/information/die-coarse-graining-budget}{90%}}{The entropy budget of a die under different coarse-grainings. Each bar is a sequence of questions, each segment the entropy paid at that stage. The third bar refines "five or above" into pairs $\{1,2\},\{3,4\},\{5,6\}$ and then into faces. You may stop after any segment; the cost so far is the entropy of the coarse-grained state you have reached.}{die-coarse-graining-budget}

\notes{Coarse-grainings can themselves be coarse-grained. Refine "five or above" ($G$) into pairs $G'\in\{\{1,2\},\{3,4\},\{5,6\}\}$ and then into faces. Each stage is a grouping of the next, so the chain rule applies at every level:
\begin{align}
H(X)=H(G)+H(G'\mid G)+H(X\mid G').
\end{align}
Numerically $0.918+0.667+1=\log_2 6$. The middle term is $\tfrac{2}{3}$ because "below five" still has two pairs to choose between (1 bit) while "five or above" is already a single pair (0 bits). The practical reading: the entropy of whatever coarse-grained state you stop at is the running total up to that point, $H(G')=H(G)+H(G'\mid G)$, and refining further simply adds the next term. Nothing is double-counted and nothing is lost.}

\newslide{Reverse Direction}

\slides{Learning the face determines the group for free. What is left to find after the group?}

\slidesincremental{
* $H(G\mid X)=0$: the coarse label is redundant given $X$
* Information *extracted* by the group: $I(X;G)=H(G)$
* Information *still to find*: $H(X\mid G)$
}

\notes{In the reverse direction, observing $X$ fixes $G$ with no leftover uncertainty. The mutual information $I(X;G)=H(G)-H(G\mid X)=H(G)$ is exactly the price of the coarse question. After you know the group, the remaining work is $H(X\mid G)$ --- which of the fine outcomes inside that group. Coarse-graining *keeps* $H(G)$ as your description and *discards* $H(X\mid G)$:
\begin{align}
\text{information lost by coarse-graining}
  = H(X\mid G)
  = \sum_i w_i\, H(p_i).
\end{align}
Using the die as a coin keeps one bit and throws away $\log_2 3$.}

\newslide{Why the Total Is Invariant}

\slides{Entropy is the uncertainty that is consistent no matter how you decompose a question into stages.}

\slidesincremental{
* Any partition, any nesting: the stages sum to the same $H(X)$
* That consistency is special to the Shannon form [@Khinchin-information57; @Baez-characterisation11]
* Pointer only today
}

\speakernotes{Khinchin pointer only --- consistency under staged questions characterises Shannon $H$; no proof today. Cite Baez--Fritz--Leinster as the later categorical form of the same demand.}

\notes{Every bar in the budget figure ends at $\log_2 6$, whichever cut came first and however many stages we used. That invariance under regrouping is not an accident of base-two logarithms; it is part of what characterises Shannon entropy among candidate uncertainty measures [@Khinchin-information57]. Categorical accounts make the same demand precise [@Baez-characterisation11]. For this lecture it is enough that staged questions *add*, so a coarse-grained state has a well-defined entropy and coarse-graining has a well-defined price.}


\endif

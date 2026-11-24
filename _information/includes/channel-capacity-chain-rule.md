\ifndef{channelCapacityChainRule}
\define{channelCapacityChainRule}

\editme

\subsection{Channels and Capacity}

\newslide{Two Identities}

\slides{The chain rule, and mutual information defined from it.}

\slidesincremental{
* Chain rule: $H(X,Y) = H(X) + H(Y\mid X)$
* Mutual information: $I(X;Y) = H(X)-H(X\mid Y) = H(X)+H(Y)-H(X,Y)$
* $I(X;Y)\ge 0$, with equality iff $X$ and $Y$ are independent
}

\notes{The chain rule $H(X,Y)=H(X)+H(Y\mid X)$ says the uncertainty in a pair is the uncertainty in the first plus what is left in the second once the first is known. Mutual information is the overlap: how much knowing $Y$ reduces uncertainty about $X$, $I(X;Y)=H(X)-H(X\mid Y)$. Substituting the chain rule gives the symmetric form $H(X)+H(Y)-H(X,Y)$. It is the KL divergence between the joint and the product of the marginals, so it is never negative and is zero only when $X$ and $Y$ are independent.}

\newslide{What a Channel Is}

\slides{A channel is a conditional distribution $p(y\mid x)$, used over and over.}

\slidesincremental{
* Send one of $M$ messages using $n$ uses of the channel
* Rate $R = \tfrac{1}{n}\log_2 M$ bits per use
* Reliable: probability of decoding the wrong message $\to 0$ as $n\to\infty$
}

\notes{Shannon's setting [@Shannon-mathematical48] has three parts. A channel takes an input symbol $x$ and returns an output $y$ with probability $p(y\mid x)$, independently at each use. A code assigns each of $M$ messages a block of $n$ input symbols. The rate is how many bits of message each channel use carries, $R=\tfrac{1}{n}\log_2 M$. A rate is called achievable if there are codes at that rate whose probability of decoding error goes to zero as the blocks get longer. Note what the definition does not ask for: no single use of the channel need be reliable. Reliability is bought with block length.}

\newslide{Capacity}

\slides{$C=\max_{p(x)} I(X;Y)$, in bits per use.}

\slidesincremental{
* No-go: above $C$, the error probability cannot go to zero
* Achievability: every $R<C$ is achievable
* The proof picks codes at random: it shows good codes exist but does not build one
* The maximising $p(x)$ says how good codes use the input alphabet
}

\notes{The noisy-channel coding theorem [@Shannon-mathematical48; @Cover:elements91, ch. 7] has two halves. The converse is a no-go: at any rate above $C$ the probability of error stays bounded away from zero, whatever code you use. The achievability half says every rate below $C$ can be reached. Shannon's proof draws the codewords at random from the capacity-achieving input distribution $p^*(x)$ and shows that the average code does well, so some code must. It is an existence proof. Building practical codes that come close to $C$ took another fifty years.

Two special cases help. A *noiseless deterministic* channel, where each input gives one fixed output, has $H(Y\mid X)=0$, so $I(X;Y)=H(Y)$. Its capacity is $\log_2$ of the number of distinct outputs it can produce. If two inputs share an output, the channel can no longer tell them apart, and capacity falls. A channel whose output is independent of its input has $I(X;Y)=0$ for every $p(x)$ and capacity zero.}

\setupplotcode{import numpy as np
import matplotlib.pyplot as plt
import mlai}

\plotcode{def Hb(q):
    q = np.clip(q, 1e-12, 1 - 1e-12)
    return -q*np.log2(q) - (1 - q)*np.log2(1 - q)

p = np.linspace(0, 1, 401)
fig, ax = plt.subplots(figsize=(7, 4))
for eps in [0.0, 0.05, 0.1, 0.25, 0.5]:
    py1 = p*(1 - eps) + (1 - p)*eps          # P(Y=1)
    I = Hb(py1) - Hb(eps)                    # I(X;Y) = H(Y) - H(Y|X)
    line, = ax.plot(p, I, linewidth=2, label=f'$\\epsilon={eps}$')
    ax.scatter([0.5], [1 - Hb(eps)], s=50, color=line.get_color(), zorder=3)
ax.set_xlabel('input bias $p(x=1)$')
ax.set_ylabel('$I(X;Y)$ (bits)')
ax.set_ylim(-0.02, 1.05)
ax.legend(title='flip probability')
ax.set_title('Binary symmetric channel: $C = 1 - H_2(\\epsilon)$')
plt.tight_layout()
mlai.write_figure('bsc-capacity.svg', directory='\writeDiagramsDir/ml')}

\figure{\includediagram{\diagramsDir/ml/bsc-capacity}{70%}}{Mutual information of a binary symmetric channel against the input bias, for several flip probabilities $\epsilon$. Each curve peaks at a uniform input (dots), giving capacity $C=1-H_2(\epsilon)$. At $\epsilon=1/2$ the output is independent of the input and $C=0$.}{bsc-capacity}

\notes{The binary symmetric channel flips each bit with probability $\epsilon$. With $P(X=1)=p$ the output has $P(Y=1)=p(1-\epsilon)+(1-p)\epsilon$, and $H(Y\mid X)=H_2(\epsilon)$ whatever the input, so
$$
I(X;Y)=H_2\big(p(1-\epsilon)+(1-p)\epsilon\big)-H_2(\epsilon).
$$
The first term is largest when the output is uniform, which happens at $p=1/2$, so $C=1-H_2(\epsilon)$. A channel that flips one bit in ten still carries just over half a bit per use, reliably, if you code over long enough blocks.}

\addreading{@Shannon-mathematical48}{noisy channel coding / capacity}
\addreading{@Cover:elements91}{Chapter 7}

\endif

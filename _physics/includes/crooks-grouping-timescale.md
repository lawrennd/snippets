\ifndef{crooksGroupingTimescale}
\define{crooksGroupingTimescale}

\editme

\subsection{Crooks Length and Timescale Separation}

\slides{Thermodynamic length assumes the within-group term has already settled.}

\slidesincremental{
* Path $\lambda(t)$ on the \emph{equilibrium} manifold: each point is a $\pi_{\lambda}$
* That is local equilibrium along the drive: $p_i\approx\pi_i(\lambda)$, $w$ (or $\theta$) moves
* Excess work prices changing $H(w)$ / natural parameters too fast
}

\speakernotes{Callback to week 2--3 grouping. Crooks bound is the cost of moving coarse coordinates while micro-conditionals track their instantaneous equilibrium.}

\notes{Week 2--3: under timescale separation, $S=H(w)+\sum_i w_i H(\pi_i)$ with only $w$ (or the exponential-family parameter $\theta$) free to change slowly. Crooks' thermodynamic length is defined on a path of equilibrium states --- each $\lambda$ labels a stationary $\pi_\lambda$. The linear-response bound $\langle W_{\mathrm{ex}}\rangle\ge\mathcal{L}^2/\tau$ therefore prices protocols that move the coarse description before the system has had infinite time to track. Finite-time driving from week 2 is exactly ``$w(t)$ changing while we hope $p_i$ stays near $\pi_i$.'' When that hope fails, the within-group KL divergences $D(p_i\|\pi_i)$ contribute extra dissipation beyond the equilibrium-manifold length.}

\endif

\ifndef{wellingCrooksFluctuation}
\define{wellingCrooksFluctuation}

\editme

\subsection{From Fluctuation Theorem to Length}

\newslides{Crooks (1999): Fluctuation Theorem}

\slides{Before length: the exact nonequilibrium relation that the second law and the $\mathcal{L}^2/\tau$ bound sit inside.}

$$
\frac{P(W)}{P_R(-W)} = e^{\beta(W-\Delta F)}
$$

\slidesincremental{
* Forward protocol: work distribution $P(W)$
* Reverse protocol: $P_R(-W)$
* $\Delta F$: equilibrium free-energy difference between endpoints
}

\speakernotes{Scaffolding only. Do not derive the theorem from a master equation. State it, then extract second law and the near-equilibrium expansion that recovers thermodynamic length.}

\notes{Crooks' fluctuation theorem [@Crooks-fluctuation99] relates the work distribution of a forward protocol to that of the time-reversed protocol. For a system driven between two equilibrium endpoints at inverse temperature $\beta$,
$$
\frac{P(W)}{P_R(-W)} = e^{\beta(W-\Delta F)},
$$
where $\Delta F$ is the free-energy difference of those endpoints. This is an exact statement about *trajectories*, not yet a length on the equilibrium manifold.}

\newslides{Jarzynski and the Second Law}

\slidesincremental{
* Integrate Crooks $\Rightarrow$ Jarzynski: $\langle e^{-\beta W}\rangle = e^{-\beta\Delta F}$
* Jensen's inequality: $\langle W\rangle \ge \Delta F$
* Excess work $W_{\mathrm{ex}} = W - \Delta F$ is nonnegative on average
}

\notes{Integrating the fluctuation theorem recovers Jarzynski's equality [@Jarzynski-nonequilibrium97],
$$
\langle e^{-\beta W}\rangle = e^{-\beta\Delta F}.
$$
Jensen's inequality on the convex map $x\mapsto e^{-\beta x}$ then gives $\langle W\rangle \ge \Delta F$: the second law for isothermal work, as an *average* over trajectories. Define excess work $W_{\mathrm{ex}}=W-\Delta F$. Then $\langle W_{\mathrm{ex}}\rangle\ge 0$, with equality only for reversible protocols.}

\newslides{Near Equilibrium: Length Appears}

\slidesincremental{
* Far from equilibrium: Crooks/Jarzynski (exact, distributional)
* Near equilibrium, slow driving: expand $\langle W_{\mathrm{ex}}\rangle$ in linear response
* Leading cost is Fisher--Rao length of the protocol: $\langle W_{\mathrm{ex}}\rangle \ge \mathcal{L}^2/\tau$
}

\notes{The fluctuation theorem holds arbitrarily far from equilibrium. Near equilibrium, for a slow protocol $\lambda(t)$ of duration $\tau$ that stays close to the instantaneous equilibrium state, linear response expands the mean excess work. The quadratic form that appears is the Fisher information metric $\mathcal{I}(\lambda)$ on the manifold of equilibrium states. Defining thermodynamic length
$$
\mathcal{L} = \int_0^\tau \sqrt{\dot\lambda^\top \mathcal{I}(\lambda)\,\dot\lambda}\,dt
$$
yields the bound $\langle W_{\mathrm{ex}}\rangle \ge \mathcal{L}^2/\tau$ [@Crooks-length07]. Geodesics of $\mathcal{I}$ are therefore the leading-order minimum-dissipation protocols --- the geometric consequence of the fluctuation relation, not a separate postulate.}

\newslides{Two Papers, One Story}

\slidesincremental{
* Crooks (1999): $P(W)/P_R(-W)=e^{\beta(W-\Delta F)}$ --- exact
* Jarzynski: $\langle e^{-\beta W}\rangle=e^{-\beta\Delta F}$ $\Rightarrow$ $\langle W\rangle\ge\Delta F$
* Crooks (2007): near equilibrium, $\langle W_{\mathrm{ex}}\rangle\ge\mathcal{L}^2/\tau$ with Fisher--Rao $\mathcal{L}$
}

\speakernotes{GAIST Chapter 17 stops at Crooks (1999)/Jarzynski. We continue to the geometric packaging. Same author; different regimes; one narrative.}

\notes{[@Welling-generative26] Chapter 17 derives the fluctuation theorem and Jarzynski's equality, then stops: it does not define thermodynamic length, does not put a Fisher--Rao metric on equilibrium states, and does not cite Crooks (2007). Fisher information appears later in GAIST (Section 22.6) as the osmotic term $\nabla\log\rho$ in the Schrödinger-bridge action --- a different object from the Fisher matrix $g_{ij}$ on the board today. Read GAIST Ch.~17 for the trajectory-level story; read Crooks (2007) for the geometric consequence we define next.}

\addreading{@Crooks-fluctuation99}{fluctuation theorem (statement)}
\addreading{@Jarzynski-nonequilibrium97}{equality; second-law corollary}
\addreading{@Welling-generative26}{Chapter 17 (fluctuation theorem; stops before length)}

\endif

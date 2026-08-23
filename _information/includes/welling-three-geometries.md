\ifndef{wellingThreeGeometries}
\define{wellingThreeGeometries}

\editme

\notes{\subsection{GAIST on the Wasserstein and Schrödinger Geometries}}

\notes{Chapter 14 of [@Welling-generative26] is the discrete-time Schrödinger bridge: minimise $D_{\mathrm{KL}}[Q\|P]$ subject to fixed endpoint marginals $q_0 = \mu$ and $q_{t_f} = \nu$. When the reference $P$ is uniform this is Jaynes' maximum caliber --- MaxEnt over paths. The algorithm is iterative proportional fitting. Chapter 22 retells the same story in continuous time: Wasserstein distance via Monge, Kantorovich and Benamou--Brenier (Section 22.2); dissipated work as the OT action (Section 22.3); the Schrödinger bridge as OT plus an osmotic Fisher-information term (Section 22.6).}

\notes{Section 22.3 states a thermodynamic speed limit
$$
\Sigma_{\tau_f} \ge \frac{W_2^2[\rho_0,\rho_{\tau_f}]}{T\tau_f}
$$
and a finite-time correction to Landauer [@Landauer-irreversibility61], following Proesmans, Ehrich and Bechhoefer (2020). That inequality is tight in the Wasserstein geometry. It is *not* Crooks' $\mathcal{L}^2/\tau$ bound. GAIST presents $W_2^2/(T\tau)$ as the thermodynamic speed limit because the book is working in overdamped dissipative dynamics with a ground-cost interpretation. We are not collapsing the three geometries: Fisher--Rao / Crooks remains the near-equilibrium length on the equilibrium manifold; Wasserstein is minimum ground-cost of moving mass; the Schrödinger bridge is the maximum-entropy interpolation.}

\newslides{GAIST on Week 8}

\slidesincremental{
* Ch.~14 and 22: Schrödinger bridge and $W_2$
* Speed limit there is $W_2^2/(T\tau)$, not $\mathcal{L}^2/\tau$
* Finite-time Landauer is Section 22.3
}

\notes{Read Chapter 14 and Sections 22.2--22.3 for the Wasserstein and Schrödinger prescriptions. Keep Crooks (2007) for Fisher--Rao. Peyré and Cuturi remain the place to get the OT intuition without the physics.}

\addreading{@Welling-generative26}{Chapter 14 and Sections 22.2--22.3}

\endif

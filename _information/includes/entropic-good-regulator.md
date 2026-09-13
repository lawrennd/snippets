\ifndef{entropicGoodRegulator}
\define{entropicGoodRegulator}

\editme

\subsection{Purely Entropic Good Regulator}

\notes{Conant and Ashby define successful regulation by minimising the entropy of the outcome $Z$: $H(Z)\to\min$. A regulator is a conditional $p(R\mid S)$. Among optimal regulators there is a simplest one for which $p(R\mid S)$ is deterministic, $R=h(S)$. That mapping is the sense in which the regulator is a ``model'' of the system [@Conant-Ashby70]. It need not be one-to-one: states that demand the same response may share an $r$. The model is therefore task-specific and compressed, not a replica of the world.}

\newslides{Requisite Variety, Entropically}

\slides{Residual outcome uncertainty is disturbance entropy minus information the regulator has about the disturbance.}

\slidesincremental{
* Disturbance $D$, response $R$, essential variable $E$
* $H(E)\ge H(D)-I(D;R)$
* Useless variety appears as small $I(D;R)$
}

\speakernotes{Named colour for LO13, not a new outcome. Ashby's requisite variety in Shannon form [@Ashby-introduction56]. Perfect regulation $H(E)=0$ forces $I(D;R)=H(D)$.}

\notes{Write Ashby's law of requisite variety in Shannon form. With disturbance $D$, regulatory response $R$, and essential/outcome variable $E$, the usual bound is
$$
H(E)\ge H(D)+H(R\mid D)-H(R).
$$
Mutual information rewrites the last two terms at once:
$$
H(E)\ge H(D)-I(D;R).
$$
Verbally: residual uncertainty after regulation is at least the uncertainty in the disturbance minus the information the regulator has about that disturbance. Having many controller states helps only when those states are correlated with $D$. Large $H(R\mid D)$ is large wasted variety.}

\notes{For perfect regulation, $H(E)=0$, the bound requires $I(D;R)\ge H(D)$. But $I(D;R)\le H(D)$, so
$$
I(D;R)=H(D),\qquad H(D\mid R)=0.
$$
The regulator's state then distinguishes every disturbance state that matters for control. That is the entropic reading of ``the regulator must embody a model.''}

\newslides{Two Cybernetic Questions}

\slidesincremental{
* Requisite variety: how much regulatory information?
* Good Regulator: how must that information be structured?
* A good regulator is a sufficient model for action
}

\speakernotes{Do not conflate the two. Quantity versus structure. The mapping $h:S\to R$ is the structure answer.}

\notes{Separate the two classical results. Requisite variety asks how much regulatory information is required. The Good Regulator Theorem asks how that information must be structured: as a (possibly many-to-one) model $R=h(S)$ of the distinctions in $S$ that matter for the outcome [@Conant-Ashby70]. A controller with $10^{100}$ unused states fails the second question even when it appears to pass the first.}

\newslides{Good Regulator Meets the Bottleneck}

\slides{Minimise model information subject to sufficiently low outcome entropy --- the course's reading, not Conant and Ashby's equation.}

\slidesincremental{
* Control form: $\min I(S;R)$ subject to $H(Z)\le\epsilon$
* Deterministic $R=h(S)$ gives $I(S;R)=H(R)$
* Merge states that share an action; keep those that do not
}

\speakernotes{IB was LO10. Here it names the cybernetic slogan in the module's grammar. Do not attribute the IB optimisation to Conant and Ashby.}

\notes{The information bottleneck asks for a compact $T$ that preserves relevance $I(T;Y)$. In control language the closely related problem is
$$
\min_{p(r\mid s)} I(S;R)\quad\text{subject to}\quad H(Z)\le\epsilon.
$$
That is the natural course-compatible reinterpretation of the Good Regulator idea: build the smallest internal model that preserves everything needed for successful regulation. Conant and Ashby do not write this optimisation; do not attribute it to them. When $R=h(S)$ is deterministic, $H(R\mid S)=0$ and $I(S;R)=H(R)$, so minimising model complexity is minimising $H(R)$ while retaining the distinctions in $S$ that the outcome demands. States that share an action merge; states that demand different actions remain distinguishable. That is relevant compression.}

\notes{Chain $D\to X\to T\to A$. Data processing gives $I(D;T)\le I(D;X)$ and $I(D;A)\le I(D;T)$: processing cannot manufacture missing environmental information. Put the three tools together for LO13: DPI forbids creating $I$; requisite variety demands enough relevant $I$; the Good Regulator organises that $I$ as a model; the information bottleneck says the efficient model keeps only action-relevant information. Landauer then prices acquiring, storing, updating, and erasing that model. The punchline for notes and the questions page: a good regulator is not a complete model of the world; it is a sufficient model for action. The purely entropic reading is minimise model information subject to sufficiently low outcome entropy.}

\addreading{@Conant-Ashby70}{the Good Regulator Theorem}
\addreading{@Ashby-introduction56}{requisite variety; Shannon form}

\endif

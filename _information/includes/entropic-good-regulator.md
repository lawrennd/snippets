\ifndef{entropicGoodRegulator}
\define{entropicGoodRegulator}

\editme

\subsection{Purely Entropic Good Regulator}

\notes{Conant and Ashby define successful regulation by minimising the entropy of the outcome $Z$: $H(Z)\to\min$ [@Conant-Ashby70]. A regulator is a policy $\pi(a\mid s)=p(a\mid s)$.  This is an existence result that comes from the concavity of Shannon entropy: among optimal regulators there is a simplest one with zero conditional action entropy, $H(A\mid S)=0$, equivalently $A=h(S)$. That is the sense in which the regulator is a ``model'' of the system --- a deliberately weak sense, as the caveats below make precise.}

\newslides{Requisite Variety, Entropically}

\slides{Residual outcome uncertainty is disturbance entropy minus information the regulator has about the disturbance.}

\slidesincremental{
* Disturbance $D$, response $R$, essential variable $E$
* $H(E)\ge H(D)-I(D;R)$
* Useless variety appears as small $I(D;R)$
}

\speakernotes{Named tool for LO13, not a new outcome. Ashby's requisite variety in Shannon form [@Ashby-introduction56]. Quantity, not structure. Perfect regulation $H(E)=0$ forces $I(D;R)=H(D)$.}

\notes{Write Ashby's law of requisite variety in Shannon form. With disturbance $D$, regulatory response $R$, and essential/outcome variable $E$, the usual bound is
$$
H(E)\ge H(D)+H(R\mid D)-H(R).
$$
Mutual information rewrites the last two terms at once:
$$
H(E)\ge H(D)-I(D;R).
$$
Verbally: residual uncertainty after regulation is at least the uncertainty in the disturbance minus the information the regulator has about that disturbance. Having many controller states helps only when those states are correlated with $D$. Large $H(R\mid D)$ is large wasted variety. Requisite variety asks how much regulatory information is required. The Good Regulator Theorem asks how that information may be structured.}

\newslides{Setup: Regulate by Minimising $H(Z)$}

\slides{One shot, not an MDP: choose a policy $\pi(a\mid s)$ to minimise outcome entropy.}

\slidesincremental{
* State $S$, action $A$, outcome $Z\sim p(z\mid s,a)$
* Objective: $\min_\pi H(Z)$
* Model (weak): $H(A\mid S)=0$, i.e.\ $A=h(S)$
}

\speakernotes{LO13. Board this setup. Not Bellman, not reward. Entropy of $Z$ is Conant and Ashby's success criterion. Ten to twelve minutes for the proof block.}

\notes{Fix $p(s)$ and a channel $p(z\mid s,a)$. Regulation is the choice of a conditional $\pi(a\mid s)$. There is no time index and no value function: a single decision. Success is $\min H(Z)$, not reward maximisation. Define $A$ to be a model of $S$ when $H(A\mid S)=0$, equivalently when there is a function $h$ with $A=h(S)$ almost surely. That definition is operational and weak; optimality, not the definition, will force which maps matter.}

\newslides{Concentration: Concavity of Entropy}

\slides{Randomising between outcome-distinct actions cannot minimise $H(Z)$.}

\slidesincremental{
* At state $s$, mix $a_1,a_2$ with $\psi(s,a_1)=z_1\ne z_2=\psi(s,a_2)$
* Transfer mass $\alpha$: $(u,v)\mapsto(u-\alpha,v+\alpha)$
* $g''(\alpha)<0$: interior mixture is not a minimum
}

\speakernotes{Board $g(\alpha)=-(u-\alpha)\log(u-\alpha)-(v+\alpha)\log(v+\alpha)$. Strict concavity is the engine. Deterministic $\psi$ for this lemma.}

\notes{Assume first a deterministic outcome map $Z=\psi(S,A)$. Suppose an allegedly optimal policy randomises, at some $s$ with $p(s)>0$, between actions $a_1$ and $a_2$ that produce different outcomes $z_1\ne z_2$. Transfer probability $\alpha$ from $(s,a_1)$ to $(s,a_2)$. Only two probabilities in the marginal of $Z$ change: $(u,v)\mapsto(u-\alpha,v+\alpha)$. Their contribution to entropy is
$$
g(\alpha)=-(u-\alpha)\log(u-\alpha)-(v+\alpha)\log(v+\alpha),
$$
with
$$
g''(\alpha)=-\frac{1}{u-\alpha}-\frac{1}{v+\alpha}<0.
$$
So $g$ is strictly concave. An interior mixture cannot be a minimum of $H(Z)$: move mass in one of the two directions and entropy falls. Contradiction. Therefore, at an optimum, whenever the policy randomises in state $s$, all actions in the support must produce the same outcome. Equivalently, for deterministic $\psi$, every optimal policy satisfies $H(Z\mid S=s)=0$ for every $s$ with $p(s)>0$.}

\newslides{Good Regulator Theorem}

\slides{Among $H(Z)$-minimisers there exists a deterministic policy: $H(A\mid S)=0$.}

\slidesincremental{
* Pick one action per $s$ among those sharing $z^\ast(s)$
* $A=h(S)$ leaves $p(z)$, hence $H(Z)$, unchanged
* Stochastic channel: same existence via extreme points
}

\speakernotes{Theorem: exists optimal $\pi$ with $H(A\mid S)=0$. Not every optimal policy is deterministic --- only that a simplest one is. Course close remains: entropy forbids; probability prescribes.}

\notes{If several actions at $s$ all produce the same $z^\ast(s)$, choose one of them and discard the unnecessary randomisation. Do this independently for every $s$ to obtain $A=h(S)$. The marginal of $Z$ is unchanged, so $H(Z)$ is unchanged: the new deterministic regulator remains optimal, and $H(A\mid S)=0$. That is the entropy form of the Good Regulator Theorem [@Conant-Ashby70].}

\notes{The deterministic-$\psi$ assumption is not needed for existence. With a genuinely stochastic channel $p(z\mid s,a)$, the marginal $p(z)$ is linear in the policy $\pi$. The space of policies is a product of probability simplices; its extreme points are exactly the deterministic policies. Since $H(Z)$ is concave in $p(z)$, $H(Z)$ is concave as a function of $\pi$. A concave function on a compact polytope attains a minimum at an extreme point. Hence there always exists a deterministic entropy-minimising policy, and $H(A\mid S)=0$ survives even when the world is stochastic. What does not survive is the stronger claim $H(Z\mid S=s)=0$: irreducible environmental noise can leave $Z$ uncertain.}

\newslides{Two Caveats}

\slides{The theorem is weaker than the popular slogan.}

\slidesincremental{
* Weak model: constant $A=a_0$ also has $H(A\mid S)=0$
* Low $H(Z)$ means predictable, not desirable
* Catastrophe with $H(Z)=0$ is ``optimal'' under entropy alone
}

\speakernotes{Do not collapse $H(A\mid S)=0$ into ``$A$ contains a rich model of $S$.'' Faithful models need $H(S\mid A)=0$ as well. Desirability needs a goal set $G$, not entropy alone.}

\notes{Calling $H(A\mid S)=0$ a model is a deliberately weak definition. A regulator that always does the same thing, $A=a_0$, also has $H(A\mid S)=0$ and $I(A;S)=0$. The theorem does not say that every optimal regulator contains lots of information about the system. It says that an optimal regulator can be chosen as a deterministic function of state. Whether that map is informative depends on the regulation problem: optimality, not the definition, rules out useless constants when state-dependent action is required.}

\notes{Minimising $H(Z)$ only makes the result predictable. It does not make the result desirable. A controller that reliably produces catastrophe has $H(Z)=0$. If $G$ denotes good outcomes, maximising $\Pr(Z\in G)$ and minimising $H(Z)$ are different objectives. Either maximise goal achievement first and entropy second, or define $Z$ as an error variable so that concentration at $Z=0$ coincides with success. Keep that fence in front of the phrase ``Good Regulator.''}

\newslides{After the Theorem: IB Gloss}

\slides{IB gloss, not the theorem: keep only distinctions that matter for action.}

\slidesincremental{
* $\min I(S;A)$ subject to $H(Z)\le\epsilon$ --- course reading
* Deterministic $A=h(S)$ gives $I(S;A)=H(A)$
* Do not attribute that optimisation to Conant and Ashby
}

\speakernotes{IB was LO10. This gloss sits after the earned theorem. Course punchline remains Week 1: entropy forbids; probability prescribes.}

\notes{The information bottleneck asks for a compact representation that preserves relevance. In control language a closely related problem is
$$
\min_{p(a\mid s)} I(S;A)\quad\text{subject to}\quad H(Z)\le\epsilon.
$$
That is a course-compatible reinterpretation of the Good Regulator idea --- not Conant and Ashby's equation, and not a consequence of $H(A\mid S)=0$ alone. Sufficient statistics for the outcome need the further condition $I(A;Z)=I(S;Z)$. When $A=h(S)$ is deterministic, $I(S;A)=H(A)$, so minimising model complexity is minimising $H(A)$ while retaining the distinctions in $S$ that the outcome demands. States that share an action may merge; states that demand different actions must remain distinguishable. That gloss is relevant compression. It is optional colour after the theorem, not the theorem itself.}

\notes{Chain $D\to X\to T\to A$. Data processing gives $I(D;T)\le I(D;X)$ and $I(D;A)\le I(D;T)$: processing cannot manufacture missing environmental information. Put the tools together for LO13: DPI forbids creating $I$; requisite variety demands enough relevant $I$; the Good Regulator supplies an optimal deterministic organisation $H(A\mid S)=0$; the information bottleneck is how one may spend $I$ on action-relevant distinctions. Landauer prices acquiring, storing, updating, and erasing whatever model is kept. The course close is unchanged: entropy forbids; probability prescribes. The Good Regulator is an earned theorem inside that fence, not the fence.}

\addreading{@Conant-Ashby70}{the Good Regulator Theorem}
\addreading{@Ashby-introduction56}{requisite variety; Shannon form}

\endif

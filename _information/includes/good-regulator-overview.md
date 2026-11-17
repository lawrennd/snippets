\ifndef{goodRegulatorOverview}
\define{goodRegulatorOverview}

\editme

\subsection{Good Regulator Overview}

\notes{Overview only. Full Conant--Ashby development --- concavity argument, existence of a deterministic optimum, and the two caveats in depth --- is the Week 8 review. Today's job is the setup, the notation, and the slogan and its two caveats. Diagrams follow Joery's oneshot figure in the good-regulator notes: disturbance $D$, system state $S$, action $A$, reguland $Z$.}

\newslide{Notation: $D$, $S$, $A$, $Z$}

\slides{The CGF was $\psi(\boldsymbol{\theta})$. After the break, $A$ is *action*.}

\slidesincremental{
* $D$: disturbance
* $S$: system state
* $A$: action (the regulator's response; Conant--Ashby often write $R$)
* $Z$: reguland / outcome (Ashby's essential variable)
}

\speakernotes{Board the four letters once. Classic cybernetics used $R$ for the regulator; we use $A$ for action so the policy language matches Weeks 7--8. The log-partition / CGF is $\psi$, so there is no clash with action. Do not prove anything yet.}

\notes{Conant and Ashby [@Conant-Ashby70] often label the regulator $R$. We write $A$ for the action so the policy $\pi(a\mid s)$ is first-class. The reguland --- the variable whose entropy successful regulation minimises --- is $Z$. The system state is $S$; the disturbance is $D$. The cumulant generating function earlier today was $\psi(\boldsymbol{\theta})=\log Z(-\boldsymbol{\theta})$; that $Z$ was the partition function, not the reguland --- different objects, same letter in the physics tradition.}

\newslide{Two Setups}

\figure{\columns{\includediagram{\diagramsDir/information/good-regulator-cause-controlled}{100%}}{\includediagram{\diagramsDir/information/good-regulator-error-controlled}{100%}}{50%}{50%}}{Cause-controlled regulation (left) acts on the disturbance $D$; error-controlled regulation (right) acts on the state $S$ that $D$ caused.}{good-regulator-two-setups}

\slidesincremental{
* Cause-controlled: act on $D$ (or on a model of $D$)
* Error-controlled: act on the state $S$ that $D$ caused
* DPI: $I(A;D)\le I(S;D)$ when $A$ only sees $S$
}

\speakernotes{Spend the clock on the diagrams. Cause control reads the disturbance before it enters the essential variable; error control corrects after the fact. Most modern RL policies are error-controlled on the observed state. Week 8 returns to why the simplest optimum factors as a model.}

\notes{A disturbance $D$ causes events in a system $S$; the regulator counters with an action $A$; the pair produces a reguland $Z=\phi(S,A)$ [@Conant-Ashby70]. Cause-controlled regulation acts on $D$ (or on an inferred model of $D$). Error-controlled regulation acts on the state $S$ caused by $D$, so by the data-processing inequality $I(A;D)\le I(S;D)$. Both diagrams are shown above; the existence proof that an $H(Z)$-optimal policy may be taken deterministic waits for Week 8.}

\newslide{What ``Good'' Means Today}

\slides{Success is low entropy in the reguland --- with two caveats.}

\slidesincremental{
* Objective sketch: $\min_{\pi(a\mid s)} H(Z)$
* Slogan: every good regulator must be a model of the system
* Weak reading of ``model'': $H(A\mid S)=0$, i.e.\ $A=h(S)$
* Full theorem and caveats: Week 8 review
}

\speakernotes{Name the objective and the slogan. Do not board the concavity transfer $g(\alpha)$. Two fences only: constant $A=a_0$ also has $H(A\mid S)=0$; low $H(Z)$ is predictable, not desirable. Worksheet 4 Exchange 1 has already asked them what GRT has to do with general intelligence --- leave the depth for Week 8.}

\notes{Successful regulation, for Conant and Ashby, minimises the entropy of the reguland: $\min_\pi H(Z)$. Among optima there exists a deterministic policy $A=h(S)$, equivalently $H(A\mid S)=0$. That is the sense in which the regulator is a ``model'' --- deliberately weak. Do not collapse the slogan into ``$A$ contains a rich model of $S$'': a constant action also has $H(A\mid S)=0$. Do not confuse low $H(Z)$ with a desirable outcome. Requisite variety in Shannon form will use the same letters: residual uncertainty satisfies $H(Z)\ge H(D)-I(D;A)$ when $A$ is the regulatory response. Week 8 reviews the theorem properly and applies it to capability claims.}

\newslide{Requisite Variety}

\slides{Quantity bound, not the structure theorem.}

\slidesincremental{
* $H(Z)\ge H(D)-I(D;A)$
* Useless variety: large $H(A)$ with small $I(D;A)$
* Ashby: how much regulatory information is required
* GRT (Week 8): how that information may be structured
}

\speakernotes{One slide. Same $A$ and $Z$ as the diagrams. Perfect regulation $H(Z)=0$ forces $I(D;A)=H(D)$ under the usual bound.}

\notes{Ashby's law of requisite variety in Shannon form [@Ashby-introduction56], written in today's letters: residual uncertainty in the reguland is at least the disturbance entropy minus the information the action carries about the disturbance. Requisite variety asks how much relevant $I$ is required; the Good Regulator Theorem asks how that $I$ may be organised. Full development of both, with the concavity argument, is Week 8.}

\addreading{@Conant-Ashby70}{the Good Regulator Theorem}
\addreading{@Ashby-introduction56}{requisite variety; Shannon form}

\endif

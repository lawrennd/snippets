\ifndef{goodRegulatorOverview}
\define{goodRegulatorOverview}

\editme

\subsection{Good Regulator Overview}

\notes{W. Ross Ashby was one of the founders of the field of cybernetics. Along with others such as Jack Good, Alan Turing, Horace Barlow and Donald MacKay he was a founder of the Ratio Club, a group of British cyberneticists.}

\notes{One of his initial contributions was the law of requisite variety. It predates Shannon's entropy, but it can be viewed in entropic terms. The variety of a system is its number of distinct states. Simply put, the law highlights that a regulating system can only control as many elements in the regulated system as it has variety. Or if we have a regulator with $2^M$ distinct states and a reguland of $2^N$ distinct states, we can only control all those states if $M=N$. 

\notes{Today we are looking at another of his important contributions, work with Roger Conant on the *good regulator theorem*. Our notation departs slightly from Conant and Ashby's they use $R$ instead of $A$ in teh below. We will consider a system with a disturbance $D$, system state $S$, action $A$, reguland $Z$.}

\newslide{Notation: $D$, $S$, $A$, $Z$}

\slides{The CGF was $\psi(\boldsymbol{\theta})$. After the break, $A$ is *action*.}

\slidesincremental{
* $D$: disturbance
* $S$: system state
* $A$: action (the regulator's response; Conant--Ashby often write $R$)
* $Z$: reguland / outcome (Ashby's essential variable)
}

\notes{Conant and Ashby [@Conant-Ashby70] often label the regulator $R$. We write $A$ for the action so the policy in reinforcement learning notation is $\pi(a\mid s)$. The reguland is the the variable whose entropy successful regulation minimises, Conant and Ashby use $Z$. The system state is $S$; the disturbance is $D$. The cumulant generating function earlier today was $\psi(\boldsymbol{\theta})=\log Z(-\boldsymbol{\theta})$; that $Z$ was the partition function, not the reguland - different objects, same letter in the physics tradition.}

\newslide{Two Setups}

\figure{\columns{\includediagram{\diagramsDir/information/good-regulator-cause-controlled}{100%}}{\includediagram{\diagramsDir/information/good-regulator-error-controlled}{100%}}{50%}{50%}}{Cause-controlled regulation (left) acts on the disturbance $D$; error-controlled regulation (right) acts on the state $S$ that $D$ caused.}{good-regulator-two-setups}

\slidesincremental{
* Cause-controlled: act on $D$ (or on a model of $D$)
* Error-controlled: act on the state $S$ that $D$ caused
* DPI: $I(A;D)\le I(S;D)$ when $A$ only sees $S$
}
\notes{A disturbance $D$ causes events in a system $S$; the regulator counters with an action $A$; the pair produces a reguland $Z=\phi(S,A)$ [@Conant-Ashby70]. Cause-controlled regulation acts on $D$ (or on an inferred model of $D$). Error-controlled regulation acts on the state $S$ caused by $D$, so by the data-processing inequality $I(A;D)\le I(S;D)$.}

\newslide{What "Good" Means Today}

\slides{Success is low entropy in the reguland --- with two caveats.}

\slidesincremental{
* Objective sketch: $\min_{\pi(a\mid s)} H(Z)$
* Slogan: every good regulator must be a model of the system
* Weak reading of "model": $H(A\mid S)=0$, i.e.\ $A=h(S)$
* Full theorem and caveats: Week 8 review
}

\speakernotes{Name the objective and the slogan. Do not board the concavity transfer $g(\alpha)$. Two fences only: constant $A=a_0$ also has $H(A\mid S)=0$; low $H(Z)$ is predictable, not desirable. Worksheet 4 Exchange 1 has already asked them what GRT has to do with general intelligence --- leave the depth for Week 8.}

\notes{Successful regulation, for Conant and Ashby, minimises the entropy of the reguland: $\min_\pi H(Z)$. Among optima there exists a deterministic policy $A=h(S)$, equivalently $H(A\mid S)=0$. That is the sense in which the regulator is a "model". It doesn't mean that "$A$ contains a rich model of $S$": a constant action also has $H(A\mid S)=0$. Do not confuse low $H(Z)$ with a desirable outcome. Requisite variety in Shannon form will use the same letters: residual uncertainty satisfies $H(Z)\ge H(D)-I(D;A)$ when $A$ is the regulatory response. }

\newslide{Requisite Variety}

\slidesincremental{
* $H(Z)\ge H(D)-I(D;A)$
* Useless variety: large $H(A)$ with small $I(D;A)$
* Ashby: how much regulatory information is required
* GRT (Week 8): how that information may be structured
}

\notes{Ashby's law of requisite variety in Shannon form [@Ashby-introduction56] says that residual uncertainty in the reguland is at least the disturbance entropy minus the information the action carries about the disturbance. Requisite variety asks how much relevant $I$ is required; the Good Regulator Theorem asks how that $I$ may be organised.}

\addreading{@Conant-Ashby70}{the Good Regulator Theorem}
\addreading{@Ashby-introduction56}{requisite variety; Shannon form}

\endif

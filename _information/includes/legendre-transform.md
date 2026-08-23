\ifndef{legendreTransform}
\define{legendreTransform}

\editme

\subsection{The Legendre Transform}

\notes{You have already performed a Legendre transform. In week 1 the Helmholtz free energy
$$
F = U - TS
$$
changed the independent variable from entropy to temperature. The same subtraction, of a product of a conjugate pair, is what relates the log-partition function of an exponential family to its entropy. The object has a name. It is the reason the exponential family has two coordinate charts, and it is why the geometry of weeks 5--6 is *dually* flat rather than merely Riemannian.}

\slidesincremental{
* Week 1: $F = U - TS$
* Same subtraction, new name
* Why the exponential family has two charts
}

\newslide{Swap the Independent Variable}

\notes{Take a smooth convex function $\phi(x)$. Its derivative $y = \phi'(x)$ is a change of coordinate: each slope $y$ labels a unique point on the graph. The *Legendre transform* writes the same information as a function of that slope,
$$
\phi^*(y) = xy - \phi(x),
$$
with $x$ recovered from $y$ by inversion. Differentiating the conjugate recovers the original coordinate, $x = (\phi^*)'(y)$. The pair inverts. Nothing is added and nothing is lost. You have changed which quantity you treat as independent.}

\slides{
$$
y = \phi'(x),\qquad \phi^*(y) = xy - \phi(x)
$$
* Convex $\phi$: the slope is a coordinate
* $\phi^*$ is the same information, different argument
* The pair inverts: $x = (\phi^*)'(y)$
}

\newslide{Helmholtz Was the First Example}

\notes{Internal energy $U$ is naturally a function of entropy. Temperature is the slope, $T = \partial U/\partial S$. Helmholtz free energy
$$
F(T) = U - TS
$$
is the Legendre transform that makes $T$ the independent variable. That is why a bath, which fixes temperature rather than entropy, is described by $F$ and not by $U$. Week 1's accounting $F = U - TS = -kT\log Z$ is this transform plus the Boltzmann occupation.}

\slidesincremental{
* $U(S)$: energy as a function of entropy
* $T = \partial U/\partial S$: the slope
* $F(T) = U - TS$: same physics, bath coordinates
}

\newslide{Entropy as Conjugate of the Log-Partition}

\notes{The log-partition function $A(\boldsymbol{\theta})$ of an exponential family is convex: its Hessian is the Fisher information, which is a covariance and therefore positive semidefinite. The moment parameters are the slope,
$$
\boldsymbol{\eta} = \nabla A(\boldsymbol{\theta}) = \mathbb{E}_{\boldsymbol{\theta}}[T(\mathbf{x})].
$$
The convex conjugate is
$$
A^*(\boldsymbol{\eta}) = \boldsymbol{\theta}\cdot\boldsymbol{\eta} - A(\boldsymbol{\theta}).
$$
Shannon entropy, measured relative to the base measure, is the other sign of the same pair,
$$
H = A(\boldsymbol{\theta}) - \boldsymbol{\theta}\cdot\boldsymbol{\eta} = -A^*(\boldsymbol{\eta}).
$$
This is the formula already on the board from the exponential family. It is not a new identity. It is the Helmholtz move, written in natural parameters: $A$ plays the role of a generating function, $\boldsymbol{\theta}$ and $\boldsymbol{\eta}$ are the conjugate pair, and $H$ is what remains after the product is subtracted.}

\slides{
$$
\boldsymbol{\eta} = \nabla A(\boldsymbol{\theta}),\qquad H = A(\boldsymbol{\theta}) - \boldsymbol{\theta}\cdot\boldsymbol{\eta}
$$
* $A$ is convex: Hessian $=$ Fisher $=$ covariance
* $A^*(\boldsymbol{\eta}) = \boldsymbol{\theta}\cdot\boldsymbol{\eta} - A = -H$
* Same move as $F = U - TS$
}

\newslide{Bernoulli: Check the Arithmetic}

\notes{For a Bernoulli with success probability $p$, the natural parameter is the logit $\theta = \log(p/(1-p))$ and the log-partition is $A(\theta) = \log(1+e^{\theta})$. The moment parameter is $\eta = \sigma(\theta) = p$. Then
$$
H = \log(1+e^{\theta}) - \theta\,p,
$$
which is exactly the binary entropy $-p\log p - (1-p)\log(1-p)$. If the subtraction does not recover $H$, the signs are wrong. This is the week's check, on the same family that Quiz 2 will use.}

\slides{
Bernoulli: $\theta = \mathrm{logit}(p)$, $A = \log(1+e^{\theta})$, $\eta = p$
$$
H = A - \theta p = -p\log p -(1-p)\log(1-p)
$$
* If the subtraction misses $H$, the signs are wrong
}

\newslide{Two Charts, Named for Later}

\notes{The pair $(\boldsymbol{\theta},\boldsymbol{\eta})$ is two coordinate systems on the same manifold. Amari calls them $e$-coordinates and $m$-coordinates. Dual flatness is the statement that each chart is affine for one of the two connections, and that the two potentials $A(\boldsymbol{\theta})$ and $A^*(\boldsymbol{\eta})$ generate the metric as Hessians. Week 5 defines that geometry. Week 6 uses it: MaxEnt is an $m$-projection because the constraint is written in $\boldsymbol{\eta}$, while the exponential family itself is a straight line in $\boldsymbol{\theta}$. Week 7 repeats the same transform for the matrix exponential family: von Neumann entropy is the Legendre conjugate of the quantum log-partition. Define the transform today. Do not yet ask what a dual connection is.}

\slidesincremental{
* $\boldsymbol{\theta}$: $e$-coordinates (natural parameters)
* $\boldsymbol{\eta}$: $m$-coordinates (moments)
* Dual flatness: week 5
* $m$-projection: week 6
}

\endif

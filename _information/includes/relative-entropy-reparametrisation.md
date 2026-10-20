\ifndef{relativeEntropyReparametrisation}
\define{relativeEntropyReparametrisation}

\editme

\subsection{Relative Entropy Fixes the Coordinate Dependence}

\slides{KL divergence is invariant under invertible reparametrisation. Differential entropy is not.}

\notes{Take two densities $f$ and $g$ on the same space and transform both by the same invertible map $y=\phi(x)$. Each density picks up the factor $1/|\phi'|$, which cancels inside the logarithm:
\begin{align}
D(f_Y\|g_Y)
  &= \int f_Y\ln\frac{f_Y}{g_Y}\,dy
   = \int f_X\ln\frac{f_X/|\phi'|}{g_X/|\phi'|}\,dx
   = D(f_X\|g_X).
\end{align}
Relative entropy (and mutual information) is therefore a property of the pair of distributions, not of the coordinate chart. It also has a clean discrete limit: with a common binning, $D(p^\Delta\|q^\Delta)\to D(f\|g)$ as $\Delta\to 0$, with no divergent $-\ln\Delta$ term.}

\slidesmall{
$$
D(f_Y\|g_Y)=D(f_X\|g_X)
$$
}

\slidesincremental{
* Both densities transform by the same Jacobian — it cancels
* Discrete KL converges; differential entropy does not
* Mutual information is likewise reparametrisation-invariant
}

\newslide{Differential Entropy Is Relative Entropy Against $m$}

\slides{Ordinary $h$ hides a reference density $m$ — usually ``Lebesgue in the coordinate we chose''.}

\slidesmall{
$$
h_m(f)=-\int f\ln\frac{f}{m}\,dx=-D(f\|m)
$$
}

\slidesincremental{
* Taking $m$ uniform in $x$ recovers ordinary $h$
* Jaynes: limiting density of discrete points — the bin width promoted to a density
* Change coordinates $\Leftrightarrow$ change the undeclared $m$
}

\speakernotes{This is the hinge for week 5 MaxEnt: maximising $h$ is maximising $-D(f\|m)$ for a forgotten $m$. Name Jaynes' limiting density of discrete points; do not digress into measure theory.}

\notes{Differential entropy is relative entropy against a reference density $m$ that is usually left unwritten. Taking $m$ uniform (Lebesgue) in the coordinate $x$ recovers the textbook $h$. Jaynes' limiting density of discrete points is the same idea: the binning measure of the previous section, written as a density. Once $m$ is explicit, the Maxwell--Boltzmann story becomes: different choices of ``equally likely a priori'' yield different maximum-entropy distributions under the same energy constraint.}

\endif

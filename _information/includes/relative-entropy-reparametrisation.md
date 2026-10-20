\ifndef{relativeEntropyReparametrisation}
\define{relativeEntropyReparametrisation}

\editme

\subsection{KL Fixes the Coordinate Dependence}

\slides{KL divergence is invariant under invertible reparametrisation. Differential entropy is not.}

\notes{Take two densities $f$ and $g$ on the same space and transform both by the same invertible map $y=\phi(x)$. Each density picks up the factor $1/|\phi'|$, which cancels inside the logarithm:
\begin{align}
\text{KL}(f_Y\|g_Y)
  &= \int f_Y\ln\frac{f_Y}{g_Y}\,dy
   = \int f_X\ln\frac{f_X/|\phi'|}{g_X/|\phi'|}\,dx
   = \text{KL}(f_X\|g_X).
\end{align}
KL divergence (and mutual information) is therefore a property of the pair of distributions, not of the coordinate chart. It also has a clean discrete limit: with a common binning, $\text{KL}(p^\Delta\|q^\Delta)\to \text{KL}(f\|g)$ as $\Delta\to 0$, with no divergent $-\ln\Delta$ term. Physics often calls $\text{KL}$ relative entropy; we keep one symbol.}

\slidesmall{
$$
\text{KL}(f_Y\|g_Y)=\text{KL}(f_X\|g_X)
$$
}

\slidesincremental{
* Both densities transform by the same Jacobian — it cancels
* Discrete KL converges; differential entropy does not
* Mutual information is likewise reparametrisation-invariant
}

\newslide{Differential Entropy Is KL Against $m$}

\slides{Ordinary $h$ hides a reference density $m$ — usually ``Lebesgue in the coordinate we chose''.}

\slidesmall{
$$
h_m(f)=-\int f\ln\frac{f}{m}\,dx=-\text{KL}(f\|m)
$$
}

\slidesincremental{
* Taking $m$ uniform in $x$ recovers ordinary $h$
* Jaynes: limiting density of discrete points — the bin width promoted to a density
* Change coordinates $\Leftrightarrow$ change the undeclared $m$
}

\speakernotes{This is the hinge for week 5 MaxEnt: maximising $h$ is maximising $-\text{KL}(f\|m)$ for a forgotten $m$. Name Jaynes' limiting density of discrete points; do not digress into measure theory.}

\notes{Differential entropy is KL divergence against a reference density $m$ that is usually left unwritten. Taking $m$ uniform (Lebesgue) in the coordinate $x$ recovers the textbook $h$. Jaynes' limiting density of discrete points is the same idea: the binning measure of the previous section, written as a density. Once $m$ is explicit, the Maxwell--Boltzmann story becomes: different choices of ``equally likely a priori'' yield different maximum-entropy distributions under the same energy constraint.}

\endif

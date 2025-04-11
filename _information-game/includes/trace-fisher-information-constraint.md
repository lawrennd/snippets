\ifndef{traceFisherInformationConstraint}
\define{traceFisherInformationConstraint}

\editme

\subsection{Trace Constraint on Fisher Information: Resolving Scale Indeterminacy}

\notes{The Fisher Information Matrix $G(\boldsymbol{\theta})$ evolves during the system's unfolding and its trace represents the total distinguishability or information capacity of the system. 
$$
\mathrm{tr}(G(\boldsymbol{\theta})) = C.
$$}
\notes{For analytical purposes, we can impose a constraint on $C$, not to modify the underlying entropy maximization dynamics, but to serve as a route to resolving the scale indeterminacy that arises within the system, making analysis easier.}

\notes{The trace constraint is justified by the compact structure of the manifold (minimum entropy value of 0, maximum of $N$). On a compact manifold, continuous functions have bounded derivatives, meaning the entropy gradient $\nabla S = G(\boldsymbol{\theta})\boldsymbol{\theta}$ is bounded. The trace constraint makes this boundedness explicit and quantifiable in the analysis.}

\notes{Mathematically, the trace has an interpretation as the "total variance" of the system,
$$
\mathrm{tr}(G(\boldsymbol{\theta})) = \sum_i G_{ii} = \sum_i \mathrm{Var}(H_i),
$$
i.e. the sum of variances of all observables in the system.}

\notes{This clarifies that a constraint on trace, we eliminate the degree of freedom corresponding to overall scale, allowing us to focus on the relative distribution of information among parameters. The hope is that this makes it easier to identify the reference frames, i.e. the directions with small eigenvalues of $G$ evolve slowly and serve as reference points (e.g. $M$). The *active variables*, i.e. the directions with large eigenvalues that evolve quickly relative to the reference frame (e.g. $X$). *Information trade-offs* occur when a given $G_{ii}$ increases, because other $G_{jj}$ must decrease to maintain the trace constraint.}

\notes{Again, just to emphasise, this is a constraint that we impose only in analysis, not by modifying the underlying dynamics where we let the system evolve naturally according to $\frac{\text{d}\boldsymbol{\theta}}{\text{d}t} = G(\boldsymbol{\theta})\boldsymbol{\theta}$. However, when analysing at each point we normalize $G_{\text{normalized}}(\boldsymbol{\theta}) = C \times \frac{G(\boldsymbol{\theta})}{\mathrm{Tr}(G(\boldsymbol{\theta}))}$ and use $G_{\text{normalized}}$ to identify relative information allocation and structural changes.}

\notes{This preserves the natural evolution while removing the scale indeterminancy to enable us to monitor the emergence of structure. The  constraint encodes a conservation principle for information that helps resolve the fundamental indeterminacy of "which parameter is changing versus which is providing a reference frame?". This question can now be answered internally without the need for external reference points.}

\endif


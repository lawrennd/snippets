\ifndef{pcaAndMatrixFactorisation}
\define{pcaAndMatrixFactorisation}

\editme

\subsection{Relationship to Matrix Factorization}

\slides{* PCA is closely related to matrix factorisation.
* Instead of $\latentMatrix$, $\mappingMatrix$
* Define Users $\mathbf{U}$ and items $\mathbf{V}$
}
\notes{We can use the robot naviation example to realise that PCA (and
factor analysis) are very reminiscient of the \refnotes{*matrix
factorization* example}{matrix-factorization} that we used for
introducing objective functions. In that system we used slightly
different notation, $\mathbf{u}_{i, :}$ for *user* location in our
metaphorical library and $\mathbf{v}_{j, :}$ for *item* location in
our metaphorical library. To see how these systems are somewhat
analagous, now let us think about the user as the robot and the items
as the wifi access points. We can plot the relative location of
both. This process is known as "SLAM": simultaneous *localisation* and
*mapping*. A latent variable model of the type we have developed is
one way of performing SLAM. We have an estimate of the *landmarks* in
the system (in this case WIFI access points) and we have an estimate
of the robot position. These are analagous to the estimate of the
user's position and the estimate of the items positions in the
library. In the matrix factorisation example users are informing us
what items they are 'close' to by expressing their preferences, in the
robot localization example the robot is informing us what access point
it is close to by measuring signal strength.}

\notes{From a personal perspective, I find this analogy
quite comforting. I think it is very arguable that one of the mechanisms through
which we (as humans) may have developed higher reasoning is through the need to
navigate around our environment, identifying landmarks and associating them with
our search for food. If such a system were to exist, the idea that it could be
readily adapted to other domains such as categorising the nature of the
different foodstuffs we were able to forage is intriguing.}

\notes{From an algorithmic
perspective, we also can now realise that matrix factorization and latent
variable modelling are effectively the same thing. The only difference is the
objective function and our probabilistic (or lack of probabilistic) treatment of
the variables. But the prediction function for both systems,}\slides{* Matrix factorisation:}
$$
f_{i, j} =
\mathbf{u}_{i, :}^\top \mathbf{v}_{j, :} 
$$
\notes{for matrix factorization or}\slides{PCA:}
$$
f_{i, j} = \latentVector_{i, :}^\top \weightVector_{j, :} 
$$
\notes{for probabilistic PCA and factor analysis are the same.}


\endif

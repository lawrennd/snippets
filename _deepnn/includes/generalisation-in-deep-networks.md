\ifndef{generalisationInDeepNetworks}
\define{generalisationInDeepNetworks}

\editme

\subsection{Generalisation in Deep Networks}

\notes{Neural nets are heavily overparameterised. Classical generalisation bounds based purely on hypothesis class complexity are pessimistic. Empirically, training algorithms exhibit an inductive bias toward solutions that generalise.}

\slides{* Classical view: model class + loss determine generalisation
* Deep view: optimisation algorithm (SGD variants) also determines which interpolating solution is found
* Phenomena: double descent; NTK/infinite-width limits; role of initialisation and gradient noise}

\newslide{Factors Affecting Generalisation}

\slides{* *Data representativeness*: train/test distribution alignment
* *Number of training points*: more samples narrow feasible solutions
* *Model class size*: larger classes require more data}

\notes{In the overparameterised regime there is not a single training optimum but a \emph{set} of zero-training-loss solutions (an interpolation manifold). Gradient-based optimisation tends to prefer certain members of this set that generalise better ("nice interpolants"). This preference is an \emph{inductive bias} of the algorithm.}

\notes{Additional reading placeholders: Hanin and Rolnick (2019) on typical linear-region counts; Pérez et al. (2019) on parameter-to-function bias toward simplicity; Arora et al. (2019) on deep linear models and implicit biases from parametrisation and initialisation.}

\endif

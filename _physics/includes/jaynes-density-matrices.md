\ifndef{jaynesDensityMatrices}
\define{jaynesDensityMatrices}

\editme

\subsection{Jaynes on Density Matrices}

\notes{In his 1957 papers and later works, Jaynes acknowledged that his maximum entropy formalism could be extended to quantum systems using density matrices.}

\slides{
* Jaynes recognized density matrices as quantum extension
* Same maximum entropy principle applies
* Von Neumann entropy: $S = -\text{Tr}(\rho \log \rho)$
* Provides unified approach to classical and quantum systems
}

\notes{As Jaynes noted in his 1962 Brandeis lectures: "Assignment of initial probabilities must, in order to be useful, agree with the initial information we have (i.e., the results of measurements of certain parameters). For example, we might know that at time $t = 0$, a nuclear spin system having total (measured) magnetic moment $M(0)$, is placed in a magnetic field $H$, and the problem is to predict the subsequent variation $M(t)$... What initial density matrix for the spin system $\rho(0)$, should we use?"}

\notes{Jaynes recognized that we should choose the density matrix that maximizes the von Neumann entropy,
\begin{align}
S = -\text{Tr}(\rho \log \rho),
\end{align}
subject to constraints from our measurements,
\begin{align}
\text{Tr}(\rho M_{op}) = M(0),
\end{align}
where $M_{op}$ is the operator corresponding to total magnetic moment.}

\notes{The solution is the quantum version of the maximum entropy distribution,
\begin{align}
\rho = \frac{1}{Z}\exp(-\lambda_1 A_1 - \lambda_2 A_2 - \cdots - \lambda_m A_m),
\end{align}
where $A_i$ are the operators corresponding to measured observables, $\lambda_i$ are Lagrange multipliers, and $Z = \text{Tr}[\exp(-\lambda_1 A_1 - \cdots - \lambda_m A_m)]$ is the partition function.}

\notes{This unifies classical entropies and density matrix entropies under the same information-theoretic principle. It clarifies that quantum states with minimum entropy (pure states) represent maximum information, while mixed states represent incomplete information.}

\notes{Jaynes further noted that "strictly speaking, all this should be restated in terms of quantum theory using the density matrix formalism. This will introduce the $N!$ permutation factor, a natural zero for entropy, alteration of numerical values if discreteness of energy levels becomes comparable to $k_BT$, etc."}

\endif 
\ifndef{typesOfUncertainty}
\define{typesOfUncertainty}

\editme

\section{Types of Uncertainty}

\notes{When considering uncertainty in computational and physical systems, we can identify three fundamental types:}

\subsection{Aleatoric Uncertainty}

\notes{Also known as statistical or stochastic uncertainty, this represents the inherent randomness in a system or noise in our measurements. This type of uncertainty cannot be reduced by collecting more data about the current system state.}

\subsection{Epistemic Uncertainty}

\notes{This represents uncertainty due to our lack of knowledge about the underlying system. Unlike aleatoric uncertainty, epistemic uncertainty can in principle be reduced by gathering more information or data about the system.}

\subsection{Computational Uncertainty}

\notes{This is uncertainty that arises from:
* Finite computational resources
* Numerical approximations
* Truncation errors
* Rounding errors in floating-point arithmetic

This form of uncertainty is particularly relevant when dealing with complex numerical computations or simulations.}

\notes{As highlighted by von Neumann in 1947, even deterministic calculations can benefit from probabilistic treatment:

> "[round-off errors] are strictly very complicated but uniquely defined number theoretical functions [of the inputs], yet our ignorance of their true nature is such that we best treat them as random variables."
}

\endif

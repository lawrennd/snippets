\ifndef{qftAsExponentialCalculus}
\define{qftAsExponentialCalculus}

\subsection{A Unifying View: QFT as Calculus on the Exponential Map}

\notes{This section is aimed at computer scientists encountering QFT for the first time.
The goal isn't to define QFT from scratch, but to give a \emph{single algebraic mechanism}
that explains why standard perturbative constructions (Dyson series, time ordering,
generating functionals, connected correlators) have the shapes they do.

The mechanism is: \textbf{Fréchet derivatives of the exponential map}, plus \textbf{trace/log}
to convert "unnormalized weights" into probabilities and cumulants.

We'll start in finite dimensions (matrices), where everything is honest and computable,
and then explain what changes in field theory (infinite-dimensional, unbounded operators,
and why Euclidean signatures are technically friendlier than Minkowski).}

\slides{
\newslides{QFT as exponential calculus (for CS)}
\begin{itemize}
\item \textbf{Mechanism:} derivatives of \(X\mapsto e^X\) (Fr\'echet/Duhamel)
\item \textbf{Then:} \(Z=\mathrm{tr}(e^X)\), \(W=\log Z\) give moments vs cumulants
\item \textbf{Payoff:} time ordering + factorials come from simplex integrals
\end{itemize}
}

\subsubsection{Start where it is exact: matrix exponentials}

\notes{For a time-independent Hamiltonian (or generator) \(H\), the evolution operator is
\(U(t)=e^{-itH}\) (real time) or \(e^{-\beta H}\) (imaginary time/stat mech).

If we perturb \(H\mapsto H+\lambda V\), the key object is the derivative
\(\frac{\mathrm{d}}{\mathrm{d}\lambda}e^{H+\lambda V}\big|_{\lambda=0}\).
Because \(H\) and \(V\) may not commute, the "pull down \(V\)" trick fails.

The correct replacement is the Duhamel/Fr\'echet formula:
\[
L_{\exp}(H,V)=\int_0^1 e^{(1-s)H}\,V\,e^{sH}\,\mathrm{d}s.
\]

Computationally, this derivative can be extracted as an off-diagonal block of a larger
block upper-triangular matrix exponential. This is the same trick used in numerical
linear algebra and autodiff through \texttt{expm}.}

\slides{
\newslides{Exact prototype: matrix exp + Duhamel}
\begin{itemize}
\item Want: \(\frac{\mathrm{d}}{\mathrm{d}\lambda}e^{H+\lambda V}\big|_0\)
\item Noncommuting case: can't "pull \(V\) down"
\item Fix: \(L_{\exp}(H,V)=\int_0^1 e^{(1-s)H}Ve^{sH}\,\mathrm{d}s\)
\end{itemize}
}

\subsubsection{Where time ordering comes from}

\notes{If the perturbation is \emph{time-dependent}, the solution is written as a
time-ordered exponential:
\[
U(t)=\mathcal{T}\exp\!\left(\int_0^t A(\tau)\,\mathrm{d}\tau\right).
\]

Expanding the exponential gives nested integrals.
Time ordering is not an extra rule: it is the combinatorics of the exponential series,
repackaged as integrals over simplices
\(\{0\le \tau_k\le\cdots\le \tau_1\le t\}\).

In other words: the Dyson series is the exponential map, differentiated/expanded in the
presence of noncommuting insertions.}

\slides{
\newslides{Dyson series = simplex integrals}
\begin{itemize}
\item Time-dependent: \(U(t)=\mathcal{T}\exp(\int_0^t A(\tau)\,d\tau)\)
\item Expand \(\exp\): integrals over ordered times (simplices)
\item Ordering + factorials arise from exponential combinatorics
\end{itemize}
}

\subsubsection{Partition functions and connected correlators}

\notes{Statistical mechanics and Euclidean QFT organize around
\[
Z(\theta)=\mathrm{tr}\,e^{H(\theta)},\qquad W(\theta)=\log Z(\theta).
\]

This is the same pattern as a log-sum-exp:
\(\log\sum_x e^{\text{score}(x)}\), except the sum becomes a trace and the score becomes an operator.
Differentiating \(Z\) gives (unnormalized) moments; differentiating \(W=\log Z\) gives
connected correlators / cumulants.

Second derivatives of \(W\) are "fluctuation metrics" (Fisher information classically;
BKM/Kubo--Mori in the quantum case). All of these are still derivatives of
\(\exp\) composed with \(\mathrm{tr}\) and \(\log\).}

\slides{
\newslides{Generating functionals = log-trace-exp}
\begin{itemize}
\item \(Z(\theta)=\mathrm{tr}\,e^{H(\theta)}\), \(W(\theta)=\log Z(\theta)\)
\item \(\nabla W\): expectations; \(\nabla^2 W\): connected correlations/metrics
\item Same algebra as log-sum-exp, but with operators
\end{itemize}
}

\subsubsection{What changes in QFT (and why Euclidean is friendlier)}

\notes{In QFT, \(H\) (and fields) are typically unbounded operators on infinite-dimensional
Hilbert spaces, and traces may diverge. So we treat the finite-dimensional story as a
\emph{regulator-level} prototype: put the system in finite volume, discretize, or otherwise
regularize so \(Z=\mathrm{tr}\,e^{-\beta H}\) exists, do calculations, then remove the regulator.

Euclidean formulations are often technically friendlier because \(e^{-\beta H}\) is a
positivity-preserving "heat-like" exponential, while real-time \(e^{-itH}\) is oscillatory.
This difference shows up as: traces/positivity/measure-theoretic control are easier to keep
in Euclidean signature than in Minkowski signature.

So the right meta-message for CS:
\begin{itemize}
\item When the construction stays inside \(\exp\)+derivatives+\(\mathrm{tr}/\log\) with good control,
the theory is usually well-behaved.
\item When positivity/trace-class control/representation assumptions fail, the "formal"
manipulations can stop corresponding to well-defined objects.
\end{itemize}}

\slides{
\newslides{QFT caveat: infinite dimensions}
\begin{itemize}
\item QFT needs regulators: unbounded ops, traces may diverge
\item Euclidean: \(e^{-\beta H}\) (heat-like) keeps positivity/control
\item Minkowski: \(e^{-itH}\) is oscillatory; control is subtler
\end{itemize}
}

\notes{If you want a slogan: \textbf{perturbative QFT is controlled differentiation of the exponential map}.
It doesn't replace the full foundations of QFT, but it explains (a) why Dyson expansions look the way they do,
and (b) why partition functions and connected correlators are derivatives of \(\log\mathrm{tr}\,e^{(\cdot)}\).}
\endif

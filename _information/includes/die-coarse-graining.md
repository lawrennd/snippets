\ifndef{dieCoarseGraining}
\define{dieCoarseGraining}

\editme

\subsection{Coarse-Graining a Die}

\slides{A fair die has $H(X)=\log_2 6\approx 2.58$ bits. }

\speakernotes{Stage the question: does every yes/no cost one bit?}

\slidesincremental{
* First cut: odd or even?
* Second cut: is it a six?
* Same total either way --- different prices for the first answer
}

\speakernotes{Board both partitions. Odd/even is balanced so exactly 1 bit. ``Is it six?'' is *not* one bit --- students often assume every binary question buys a bit. That is the MacKay moral applied to grouping.}

\notes{Take a fair six-sided die, $X\in\{1,\ldots,6\}$ with $p(x)=1/6$, so
\begin{align}
H(X)=\log_2 6 = 1 + \log_2 3 \approx 2.585 \text{ bits}.
\end{align}
Ask questions in two stages: first learn which *group* the face falls in, then resolve the face inside the group.}

\newslide{Odd or Even: Exactly One Bit}

\slides{Groups $\{1,3,5\}$ and $\{2,4,6\}$ are equiprobable.}

\slidesmall{
$$
H(G_{\mathrm{parity}})=1 \text{ bit},
\qquad
H(X\mid G_{\mathrm{parity}})=\log_2 3 \approx 1.585 \text{ bits}
$$
}

\slidesincremental{
* Group label: fair coin --- one bit
* Inside either group: three equally likely faces
* Total: $1+\log_2 3=\log_2 6$
}

\notes{Let $G_{\mathrm{parity}}=0$ on even faces and $1$ on odd. Then $w=(1/2,1/2)$, so $H(G_{\mathrm{parity}})=1$. Conditional on the group, three faces remain, each with probability $1/3$, so $H(X\mid G_{\mathrm{parity}})=\log_2 3$. The stages add:
\begin{align}
H(G_{\mathrm{parity}})+H(X\mid G_{\mathrm{parity}})
  = 1+\log_2 3
  = \log_2 6
  = H(X).
\end{align}}

\newslide{"Is It a Six?": Not One Bit}

\slides{A yes/no question is one bit only when the two answers are equiprobable.}

\slidesmall{
$$
w=\Bigl(\tfrac16,\tfrac56\Bigr),
\qquad
H(G_{\mathrm{six}})=h_2\Bigl(\tfrac16\Bigr)\approx 0.65 \text{ bits}
$$
}

\slidesincremental{
* Yes ($X=6$): no residual uncertainty
* No: five faces left, $H=\log_2 5$
* Remaining: $\tfrac56\log_2 5\approx 1.93$ bits
* Total again $\approx 0.65+1.93=2.58=\log_2 6$
}

\notes{Let $G_{\mathrm{six}}=\mathbf{1}_{\{X=6\}}$. The group weights are unbalanced, $w=(1/6,5/6)$, so the binary entropy of the first answer is
\begin{align}
H(G_{\mathrm{six}})
  = h_2\Bigl(\tfrac16\Bigr)
  = -\tfrac16\log_2\tfrac16-\tfrac56\log_2\tfrac56
  \approx 0.650 \text{ bits},
\end{align}
\emph{not} one bit. After a ``yes'' the face is known ($H=0$). After a ``no'' five faces remain ($H=\log_2 5$). Averaging,
\begin{align}
H(X\mid G_{\mathrm{six}})
  = \tfrac16\cdot 0 + \tfrac56\log_2 5
  \approx 1.935 \text{ bits}.
\end{align}
Again $H(G_{\mathrm{six}})+H(X\mid G_{\mathrm{six}})=H(X)$. Note that ``$\ge 4$?'' on a fair die is *also* a balanced cut ($\{1,2,3\}$ vs $\{4,5,6\}$), so it *is* one bit --- the unbalanced example has to be chosen carefully.}

\newslide{Same Total, Different First Cut}

\slides{However you slice the questions, you pay $\log_2 6$ in total.}

\slidesincremental{
* Odd/even first: pay $1$, then $\log_2 3$
* Six-or-not first: pay $\approx 0.65$, then $\approx 1.93$
* Coarse-graining keeps only the group term and *throws away* the rest
}

\endif

\ifndef{dieCoarseGraining}
\define{dieCoarseGraining}

\editme

\subsection{Coarse-Graining a Die}

\slides{The game let us invent any yes/no. A cube, like the pans, will not.}

\speakernotes{Same moral as MacKay, new instrument. Twenty questions was the idealised world. The balance already spoiled it. The die spoils it again: six faces, not $2^k$. $\{1,2,3\}$ versus $\{4,5,6\}$ is one grouping the cube affords. Odd versus even is another --- not the next question. After the first grouping three faces remain, as three balls remained on the pans.}

\slidesincremental{
* Fair die: $H(X)=\log_2 6\approx 2.58$ bits --- not an integer
* One grouping the cube affords: $\{1,2,3\}$ versus $\{4,5,6\}$
* A *different* grouping, not a nested question: odd versus even
}

\notes{Take a fair six-sided die, $X\in\{1,\ldots,6\}$ with $p(x)=1/6$, so
\begin{align}
H(X)=\log_2 6 = 1 + \log_2 3 \approx 2.585 \text{ bits}.
\end{align}
In the information game we may ask any yes/no we can name. The pans already showed that a physical instrument will not always realise the split the budget wants. The cube is the same lesson on a smaller object. Its sample space has six atoms, not $2^k$. A grouping is a partition the *mechanism* affords --- looking at the face through some physical cut. The lead cut combines $\{1,2,3\}$ against $\{4,5,6\}$. Odd versus even is not the next question inside that grouping: it is a different cut of the original six. After a $3$--$3$ split, three faces remain. Three cannot be split by a fair yes/no, just as three remaining balls could not sit evenly on the pans. Nested 1-bit questions would need a power of two --- an eight-sided die, which would still live in the game's world. This cube does not.}

\newslide{Low or High: One Question, Three Faces}

\slides{Is the face in $\{1,2,3\}$ or $\{4,5,6\}$? One yes/no combines three faces.}

\slidesmall{
$$
H(G_{\text{low}})=1 \text{ bit},
\qquad
H(X\mid G_{\text{low}})=\log_2 3 \approx 1.585 \text{ bits}
$$
}

\slidesincremental{
* Group label: fair coin --- one bit
* Inside either group: three equally likely faces
* Total: $1+\log_2 3=\log_2 6$
}

\speakernotes{Board $\{1,2,3\}$ versus $\{4,5,6\}$. This is one grouping the cube affords, not a three-sided die. We keep the coarse label and refuse the face. The residual is $\log_2 3$ --- mechanism will not sell that remainder as a bit.}

\notes{Let $G_{\mathrm{low}}=0$ on $\{1,2,3\}$ and $1$ on $\{4,5,6\}$. Then $w=(1/2,1/2)$, so $H(G_{\mathrm{low}})=1$. Conditional on the group, three faces remain, each with probability $1/3$, so $H(X\mid G_{\mathrm{low}})=\log_2 3$. The stages add:
\begin{align}
H(G_{\mathrm{low}})+H(X\mid G_{\mathrm{low}})
  = 1+\log_2 3
  = \log_2 6
  = H(X).
\end{align}
The first answer names the group. The residual $\log_2 3$ is the information the mechanism threw away by combining three faces into one physical cut. That residual is *not* a second 1-bit question the cube still owes us.}

\newslide{Mechanism: Three Faces Left}

\slides{*Mechanism.* Three faces remain. We cannot ask a nested fair yes/no.}

\slidesmall{
$$
h_2\Bigl(\tfrac13\Bigr)\approx 0.92 < 1 \text{ bit}
$$
}

\slidesincremental{
* After low/high: $\{1,2,3\}$ or $\{4,5,6\}$ --- three faces
* Odd versus even *inside* either group is $2$ versus $1$ --- the known-ball tax again
* An eight-sided die would still be the game: $4$--$4$, then $2$--$2$, then $1$--$1$
}

\speakernotes{Echo the pans: three balls left, cannot put one and a half on a pan. If a student offers odd/even as the follow-up, board it inside $\{1,2,3\}$: odd $\{1,3\}$, even $\{2\}$. That is $h_2(1/3)$, not $1$. The twenty-questions tree needs $2^k$ leaves. Six is the mechanism refusing. Eight would still live in the idealised world.}

\notes{Suppose we have learned $G_{\mathrm{low}}=0$, so the face is in $\{1,2,3\}$. Asking odd or even now splits $\{1,3\}$ against $\{2\}$. The answers are not equiprobable: $w=(2/3,1/3)$, so the question is worth $h_2(1/3)\approx 0.92$ bits, not one bit. That is the same tax as three remaining balls padded with a known normal. Successive balanced 1-bit questions form a binary tree of equal splits. That tree has $2^k$ leaves. A six-sided die cannot sit on it, because the *instrument* has six faces. An eight-sided die can: first $\{1,2,3,4\}$ versus $\{5,6,7,8\}$, then a $2$--$2$ split inside the named half, then a $1$--$1$ split --- three fair coins, $H=\log_2 8=3$ bits exactly. That object would still live in the information game. This cube does not. So we do not invent a nested question the mechanism cannot ask. We go back to all six faces and name a *different* grouping the cube *does* afford.}

\newslide{Odd or Even: A Different Grouping the Cube Affords}

\slides{Go back to all six faces. Odd versus even is another physical cut, not the next question.}

\slidesmall{
$$
H(G_{\mathrm{parity}})=1 \text{ bit},
\qquad
H(X\mid G_{\mathrm{parity}})=\log_2 3 \approx 1.585 \text{ bits}
$$
}

\slidesincremental{
* Same accounting as low/high --- a *different* grouping the cube affords
* Not the second question after $\{1,2,3\}$ versus $\{4,5,6\}$
* Mechanism offers cuts; it does not offer the game's next bit
}

\notes{Let $G_{\mathrm{parity}}=0$ on even faces and $1$ on odd, as a partition of the original six, not of a group we already named. Then $w=(1/2,1/2)$, so $H(G_{\mathrm{parity}})=1$, and $H(X\mid G_{\mathrm{parity}})=\log_2 3$ as before. The stages add to $\log_2 6$ again. Low/high and odd/even are two equally good 1-bit groupings the *cube* affords. They keep different distinctions. They do not nest, because the instrument is not a free questioner. Asking both would give four cells $\{1,3\}$, $\{2\}$, $\{5\}$, $\{4,6\}$ --- not four equiprobable atoms, and not two bits. Which grouping you choose is which physical cut you look through. The next snippet will name that cut as an abstraction. The point today is that mechanism, not the information budget, chose the menu.}

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

\speakernotes{MacKay callback: a yes/no is one bit only when the mechanism realises an even split. The pans taught that; ``is it a six?'' says it on the cube.}

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
Again $H(G_{\mathrm{six}})+H(X\mid G_{\mathrm{six}})=H(X)$. The low/high cut *is* one bit because the two groups are equiprobable. The six-or-not cut is not.}

\newslide{Same Total, Mechanism Chooses the Cut}

\slides{The budget still adds to $\log_2 6$. The cube decides which splits exist.}

\slidesincremental{
* Low/high, *or* odd/even: each pays $1$, then $\log_2 3$ --- separately
* Six-or-not: pay $\approx 0.65$, then $\approx 1.93$
* If you *stop* at low/high, the die *is* a coin --- composition next
}

\speakernotes{Do not board the grouping identity here. The next include is the tree: stop at the squares and $H(G)$ is all you pay. Low/high is the 50/50 use of a die.}

\endif

\ifndef{expectationEntropyExample}
\define{expectationEntropyExample}
\editme

\newslide{Computing Expectations Example}

\slides{
* Consider the following distribution.

$y$        |  1  |  2  |  3  |  4
-----------|-----|-----|-----|-----
$P\left(y\right)$ |  0.3|  0.2|  0.1|  0.4

* What is the mean of the distribution?
* What is the standard deviation of the distribution?
* Are the mean and standard deviation representative of the distribution form?
* What is the expected value of $-\log P(y)$?}

\newslide{Expectations Example: Answer}

\slides{
* We are given:

$y$               |   1   |   2   |   3   |   4
------------------|-------|-------|-------|-------
$P\left(y\right)$ |  0.3  |  0.2  |  0.1  |  0.4
$y^2$             |   1   |   4   |   9   |  16
$-\log(P(y))$     | 1.204 | 1.609 | 2.302 | 0.916

* Mean: $1\times 0.3 + 2\times 0.2 + 3 \times 0.1 + 4 \times 0.4 = 2.6$
* Second moment: $1 \times 0.3 + 4 \times 0.2 + 9 \times 0.1 + 16 \times 0.4 = 8.4$
* Variance: $8.4 - 2.6\times 2.6 = 1.64$
* Standard deviation: $\sqrt{1.64} = 1.2806$
}

\newslide{Expectations Example: Answer II}

\slides{
* We are given that:

$y$               |   1   |   2   |   3   |   4
------------------|-------|-------|-------|-------
$P\left(y\right)$ |  0.3  |  0.2  |  0.1  |  0.4
$y^2$             |   1   |   4   |   9   |  16
$-\log(P(y))$     | 1.204 | 1.609 | 2.302 | 0.916

* Expectation $-\log(P(y))$: $0.3\times 1.204 + 0.2\times 1.609 + 0.1\times 2.302 +0.4\times 0.916 = 1.280$}

\notes{That last number is Shannon entropy in nats: $H(p)=\mathbb{E}_{p}[-\log p(y)]=-\sum_y p(y)\log p(y)$. Same arithmetic under another name.}

\endif

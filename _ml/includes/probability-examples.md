\ifndef{probabilityExamples}
\define{probabilityExamples}
\editme

\include{_ml/includes/expectation-entropy-example.md}

\newslide{Sample Based Approximation Example}

\slides{
* You are given the following values samples of heights of students,

    $i$   |   1  |    2 |  3   |   4  |   5  |    6
----------|------|------|------|------|------|------
    $y_i$ |  1.76|  1.73| 1.79 | 1.81 | 1.85 |  1.80

* What is the sample mean?
* What is the sample variance?
* Can you compute sample approximation expected value of $-\log P(y)$?
}

\newslide{Sample Based Approximation Example: Answer}

\slides{
* We can compute:

$i$        |    1    |    2    |    3    |    4    |    5    |    6
-----------|---------|---------|---------|---------|---------|--------
$y_i$      |   1.76  |   1.73  |   1.79  |   1.81  |   1.85  |   1.80
$y^2_i$    |  3.0976 |  2.9929 |  3.2041 |  3.2761 |  3.4225 |  3.2400

* Mean: $\frac{1.76 + 1.73 + 1.79 + 1.81 + 1.85 + 1.80}{6} = 1.79$
* Second moment: $ \frac{3.0976 + 2.9929 + 3.2041 + 3.2761 + 3.4225 + 3.2400}{6} = 3.2055$
* Variance: $3.2055 - 1.79\times1.79 = 1.43\times 10^{-3}$
* Standard deviation: $0.0379$
* No, you can’t compute it. You don’t have access to $P(y)$ directly.}


\newslide{Sample Based Approximation Example}

\slides{
* You are given the following values samples of heights of students,

    $i$   |   1  |    2 |  3   |   4  |   5  |    6
----------|------|------|------|------|------|------
    $y_i$ |  1.76|  1.73| 1.79 | 1.81 | 1.85 |  1.80

* Actually these "data" were sampled from a Gaussian with mean 1.7 and standard deviation 0.15. Are your estimates close to the real values? If not why not?}

\endif

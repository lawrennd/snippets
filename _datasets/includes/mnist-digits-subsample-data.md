\ifndef{mnistDigitsSubsampleData}
\define{mnistDigitsSubsampleData}

\editme

\subsection{Subsample of the MNIST Data}

\notes{We will look at a sub-sample of the MNIST digit data set.

THE MNIST DATABASE of handwritten digits was created by Yann LeCun, Corinna Cortes and Christopher J. C. Burges. More details can be found at Yann's site <http://yann.lecun.com/exdb/mnist/>

The data is a modified version of a data set from the US National Institute of Standards and Technology ([NIST](https://www.nist.gov/).

First load in the MNIST data set from scikit learn. This can take a little while because it's large to download.}

\slides{* MNIST digits data from LeCun, Cortes & Burges
* More details at <http://yann.lecun.com/exdb/mnist/>
* Based on a date from the [NIST](https://www.nist.gov/)
}

\setupcode{from sklearn.datasets import fetch_openml}
\code{mnist = fetch_openml('mnist_784')}

\notes{Sub-sample the dataset to make the training faster.}

\setupcode{import numpy as np}
\code{np.random.seed(0)
digits = [0,1,2,3,4]
N_per_digit = 100
Y = []
labels = []
for d in digits:
    imgs = mnist['data'][mnist['target']==str(d)]
    Y.append(imgs.loc[np.random.permutation(imgs.index)[:N_per_digit]])
    labels.append(np.ones(N_per_digit)*d)
Y = np.vstack(Y).astype(np.float64)
labels = np.hstack(labels)
Y /= 255}

\notes{Now let's visualise some examples from our subsampled dataset to get a sense of what the data looks like.}

\include{_datasets/includes/mnist-digits-plot.md}

\endif

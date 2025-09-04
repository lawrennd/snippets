\ifndef{classificationExamples}
\define{classificationExamples}
\editme

\subsection{Classification Examples}

\slides{
* Classifiying hand written digits from binary images (automatic zip code reading)
* Detecting faces in images (e.g. digital cameras).
* Who a detected face belongs to (e.g. Facebook, DeepFace)
}

\notes{There are many difference examples of classification problems. One of theoldest is the classification of hand written digits from binary images. The MNIST data was for a long time considered one of the most difficult data sets. 

\notes{When we download this data we are making use of open source code, through the [scikit learn](https://scikit-learn.org/stable/) project, and the [OpenML](https://www.openml.org/) project which provides open access to data.}

\notes{This reflects a tradition of openness in machine learning that has enabled the tools to be deployed.}

\include{_datasets/includes/mnist-digits-subsample-data.md}}

\notes{While the MNIST data doesn't capture all the nuances of the challenges we face in modern machine learning. It has been an important benchmark data set for and can still be a useful data set for learning about classfication algorithms.}

\newslides{Classification Examples}

\slides{
* Classifying type of cancer given gene expression data.
* Categorization of document types (different types of news article on the
internet)
}

\endif

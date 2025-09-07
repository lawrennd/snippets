\ifndef{validationShortIntro}
\define{validationShortIntro}
\editme

\subsection{Validation}

\notes{Next we will explore techniques for model selection that make use of validation data. Data that isn't seen by the model in the learning (or fitting) phase, but is used to *validate* our choice of model from amoungst the different designs we have selected.

In machine learning, we are looking to minimise the value of our objective function $E$ with respect to its parameters $\mappingVector$. We do this by considering our training data. We minimize the value of the objective function as it's observed at each training point. However we are really interested in how the model will perform on future data. For evaluating that we choose to *hold out* a portion of the data for evaluating the quality of the model.

We will review the different methods of model selection on the Olympics marathon data.}

\endif

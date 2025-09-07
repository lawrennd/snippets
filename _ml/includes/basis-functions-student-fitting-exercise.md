\ifndef{basisFunctionsStudentFittingExercise}
\define{basisFunctionsStudentFittingExercise}

\editme

\subsection{Fitting the Model Yourself}

\notes{You now have everything you need to fit a non- linear (in the inputs) basis function model to the marathon data.}

\codeassignment{Choose one of the basis functions you have explored
above. Compute the design matrix on the covariates (or input data), `x`. Use the
design matrix and the response variable `y` to solve the following linear system
for the model parameters `w`.
$$
\basisVector^\top\basisVector\mappingVector = \basisVector^\top \dataVector
$$
Compute the corresponding error on the training data. How does it
compare to the error you were able to achieve fitting the basis above? Plot the
form of your prediction function from the least squares estimate alongside the
form of you prediction function you fitted by hand.}{}{35}

\endif

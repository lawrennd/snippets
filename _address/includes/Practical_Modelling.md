\ifndef{practicalModelling}
\define{practicalModelling}

\editme

\subsection{Practical Modelling}

\subsubsection{Linear modelling}

\notes{You probably inferred in the previous exercise, that age-profiles of individual cities are heavilly impacted by students. Let's use data from the 2021 Census to try and predict age profile information of all cities.}

\notes{What we actually will be predicting, is the share of population in a given city that is of a certain age, given NS-SEC information. Let's normalise the `age_df` and select the share of 21-year-olds in each city. This is the value we are trying to predict.}

\code{norm_age_df = age_df.div(age_df.sum(axis=1), axis=0)
norm_age_df[21]}

\exercise{We don't have any data to make a model yet - let's change that. Select features to use, starting with the relative student population of each city (`L15` in `TS062`). Make a LinearRegression model to find the relationship between the student population in a city, and the percentage of 21 year olds there. Use the model to make predictions and examine the predictive power by plotting the correlation of `y` and `y_pred`.}

\exercise{Now repeat the above analysis using all 9 NS-SEC classification values as features. Interpret the results, including correlation. Does the new model perform better?}

\subsubsection{Regularisation}

\notes{The prediction results achieved by your second model should be more accurate, with a correlation of about 97%. However, when using as many parameters as we are (9), we need to be wary of overfitting.}

\exercise{Examine if the model is overfitting using *k-fold cross-validation*. Randomly split the dataset into *k* subsets. Train a model, leaving one selected subset out for testing. Record the test performance on that subset. Iterate this for all subsets. Do the results you get differ depending on the value of *k*? Plot this relationship. Does this match your expectations?}

\exercise{If you found evidence of overfitting, address this by employing both L1 and L2 regularisation. Compare the results against your baseline model. How did you choose alpha values? What do the results say about potential feature selection?}

\subsubsection{Prediction}

\exercise{Among the models created above, choose the one you believe performs *best*, and apply it to the entire dataset. Fit a separate linear model for each of the age groups (0-99). Note down the model coefficients and plot them.}   

\exercise{Write a function that given a cities' NS-SEC breakdown, predicts it's age profile, and plot's it against the ground truth. Play around with the method to find cities where your model works very well, but also ones where it works poorly.}

\subsection{Conclusions}

\notes{This has been quite a short introduction to a set of very useful models. We have cut quite a few corners theoretically but importantly this is something that we have to do when working as data-scientist. We need to be able to apply models while there is still some uncertainty in how they work and be able to translate this uncertainty to how we interpret the results that we get. You are by no means expected to be experts on GLMs at all but you should be able to use them. The next part of your challenge is now to include the models that we have built up and use them in the coursework. Try to first visualise the data, make a clear narrative of why you are selecting a specific model and try to use the tools that we derived her in order to provide context to the predictions that you make. The statsmodel package gives you a rich set of tools that you should be able to include directly into your project. Importantly, remember that the most important thing is to be able to say why a model does what it does not necessarily choosing the right model.
During the lecture Neil mentioned the idea that what separates statisticians from machine learners is that the former cares about β while the machine learners cares about $\hat{y}$ (the predictions). If you look at the statmodels package this concept becomes very clear. Using the GLM code as we did in the first exercise doesn’t actually provide us with the uncertainty in the predictions only in the parameters. It was because of this we changed from the GLM model class to OLS when using the basis functions.}

\endif
\ifndef{dsailPoriniNaiveBayes}
\define{dsailPoriniNaiveBayes}

\editme

\subsection{Address: Naive Bayesian Prediction Model}


\notes{Using the data we collected in the Access stage and understood in Assess, we can now Address our question, and create a naive Bayesian classification model for predicting the probability of a camera sighting a species on a given day.

$$
P(1 \mid c, s, d) = \frac{P(1, c, s, d)}{P(c, s, d)}
$$

$$
\text{Using chain rule:} \quad P(1, c, s, d) = P(1) \cdot P(c, s, d \mid 1)
$$

$$
\text{Using conditional independence:} \quad P(c, s, d \mid 1) = P(c \mid 1) \cdot P(s \mid 1) \cdot P(d \mid 1)
$$


$$
P(1 \mid c, s, d) = \frac{P(1) \cdot P(c \mid 1) \cdot P(s \mid 1) \cdot P(d \mid 1)}{P(c,s,d)}
$$

$$
\text{Using Bayes' rule:} \quad  P(c \mid 1) = \frac{P(1 \mid c) \cdot P(c)}{P(1)} \quad \text{(and similarly for $s$ and $d$)}
$$

$$
\Rightarrow P(1 \mid c, s, d) = \frac{P(1) \cdot \frac{P(1 \mid c) \cdot P(c)}{P(1)} \cdot \frac{P(1 \mid s) \cdot P(s)}{P(1)} \cdot \frac{P(1 \mid d) \cdot P(d)}{P(1)}}{P(c,s,d)}
$$

$$
= \frac{P(1 \mid c) \cdot P(1 \mid s) \cdot P(1 \mid d) \cdot P(c) \cdot P(s) \cdot P(d)}{P(1)^2 \cdot P(c,s,d)}
$$

$$
\text{Assuming independence:}
$$

$$
P(1 \mid c,s,d)=\frac{P(1 \mid c) \cdot P(1 \mid s) \cdot P(1 \mid d)}{P(1)^2}
$$

$$
\begin{align*}
&c = \text{camera ID (e.g., C001)} \\
&s = \text{species (e.g., IMPALA)} \\
&d = \text{smoothed date (e.g., month, or Gaussian-filtered day)}
\end{align*}
$$}

\codeassignment{Implement the model below.}{from typing import Union
import pandas as pd
import numpy as np
from datetime import date as DateType

def bayes_sighting_probability(df, camera, species, date) -> float:
    """
    Removes a specific observation and estimates the probability of sighting
    a given species at a given camera on a specific date.

    Parameters:
        df (pd.DataFrame): DataFrame with MultiIndex columns (camera, species) and datetime.date index.
        camera (str): Camera ID (e.g. 'C001').
        species (str): Species name (e.g. 'IMPALA').
        date (str or datetime.date or pd.Timestamp): Date of the observation.

    Returns:
        float: Estimated sighting probability - TODO.
    """
    if isinstance(date, str) or isinstance(date, pd.Timestamp):
        date = pd.to_datetime(date).date()

    df_blind = df.copy()
    df_blind.loc[date, (camera, species)] = None

    #TODO

    raise NotImplementedError("Prediction logic not implemented yet.")
}{25}

\notes{Well done! We should now have a working Access-Assess-Address data science pipeline! Let's see how it does.}

\code{#}

\subsubsection{Evaluation}

\notes{The data is extremely sparse, with less than 1% of values being `1`. This is a challenge, as checking naive accuracy would make always-zero a very very good predictor.

Let's evaluate our prediction system using `log-loss` i.e. `cross-entropy`:

$$
\mathcal{L} = - \frac{1}{N} \sum_{i=1}^{N}
\Big[
    y_i \, \log(\hat{p}_i) + (1 - y_i) \, \log(1 - \hat{p}_i)
\Big]
$$}

\codeassignment{Implement the loss function below.}{def cross_entropy(y_true, y_pred):
    #TODO
    raise NotImplementedError("Cross entropy not implemented yet.")

def evaluate_prediction_system(df, your_function, max_samples=1000):
    # Randomly sample up to 1000, if full evaluation taking too long
    np.random.seed(42)
    coords = [(date, camera, species) for date in df.index for (camera, species) in df.columns]
    if len(coords) > max_samples:
        coords = np.random.choice(len(coords), size=max_samples, replace=False)
        coords = [coords[i] if isinstance(coords[i], tuple) else
                  [(date, camera, species) for date in df.index for (camera, species) in df.columns][coords[i]]
                  for i in range(len(coords))]
    else:
        coords = coords

    y_true = []
    y_pred = []

    for date, camera, species in coords:
        value = df.loc[date, (camera, species)]
        y_true.append(value)
        prob = your_function(df, camera, species, date)
        y_pred.append(prob)

    return cross_entropy(y_true, y_pred)

# Let's pass our function to be evaluated. This could take quite some time if your function is complex.
evaluate_prediction_system(binary_df, bayes_sighting_probability)}{20}


\notes{For reference, predicting a constant probability (eg. 0.5%) gives a loss of around 0.026. This should be the benchmark number we want to improve on. If your model does better than that, well done!}

\notes{*Note: our approach included look-ahead bias - making predictions based on data that we would not have access to at the time. For real-life deployment, we would need to limit our training data to before individual test cases.*}
\endif

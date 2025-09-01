\ifndef{dsailPoriniAnalysisImprovements}
\define{dsailPoriniAnalysisImprovements}

\editme

\subsection{Improving the Method: Correlated Variables}

\notes{The model above was quite simplified, and it disregarded any correlations between the three variables. Since cameras are close to each other, maybe they are more likely to capture the same animals on the same day? Maybe some animals like or avoid some areas, or some other animals? If any of the above is true, we can't really be using simple Bayes' rule classification.}

\codeassignment{Analyse the data again to find the strongest relationships which can be used to improve predictions. Plot correlation matrices and other helpful charts.

Have a short read through the [DSAIL-Porini paper](https://www.sciencedirect.com/science/article/pii/S2352340922010666) for inspiration about other probability analyses that can be done here.}{}{20}

\notes{Exercise Extension: Use what you found to improve your prediction model, and compare it against the previous one.}

\code{from typing import Union
import pandas as pd
import numpy as np
from datetime import date as DateType

def improved_sighting_probability(df, camera, species, date) -> float:
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

    #TODO Exercise 6 Extended

    raise NotImplementedError("Prediction logic not implemented yet.")}


\subsection{Extended Exercises}

\notes{We didn't use all of the available data when we just classified days as "sighting" or "no sighting". Extend your analysis to include all the information in the file, like numbers of sightings, and numbers of animals in the photos.

This will be quite challenging due to burst shots - assess the dataset and come up with a good definition of what a burst is, and a data structure that has the information you chose as important.

Example burst data:
- Camera, Date, Species
- Time Start, Time End
- Number of photos
- Average/most animals in a photo

*Particular challenge around deduplicating multi-species sightings.*}


\codeassignment{Use this additional data and repeat the analysis you did above. Aim to further improve predictions and write a new function like `burst_sighting_probability('C001', 'IMPALA', '2021-12-24')`.}{}{10}

\codeassignment{Compare the results and note the improvement (or lack thereof) against the two previous prediction functions you created.}

\codeassignment{What other benefits does your new system provide? Can you modify it to provide more predictions, like expected number of sightings, number of animals?}


\endif



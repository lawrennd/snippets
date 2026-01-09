\ifndef{dsailPoriniBurstDetectionAnalysis}
\define{dsailPoriniBurstDetectionAnalysis}

\editme

\subsection{Extended Analysis: Burst Detection}

\notes{We didn't use all of the available data when we just classified days as "sighting" or "no sighting". Change your analysis to include the number of sightings and the number of animals in the photos.

This will be quite challenging due to burst shots - assess the dataset and come up with a good definition of what a burst is, and a data structure that has the information you chose as important.

Example burst data:
- Camera, Date, Species
- Time Start, Time End
- Number of photos
- Average/most animals in a photo

Particular hardship around deduplicating multi-species sightings.}

\codeassignment{Use this additional data and repeat the analysis you did above. Further improve predictions and write a new function like `burst_sighting_probability('C001', 'IMPALA', '2021-12-24')`.}

\codeassignment{Compare the results and note the improvement (or lack thereof) against the two previous prediction functions you created.}

\codeassignment{What other benefits does your new system provide? Can you modify it to provide more predictions, like the expected number of sightings, the number of animals?}

\endif

\endif

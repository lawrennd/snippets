\ifndef{dsailPoriniProbabilityAnalysis}
\define{dsailPoriniProbabilityAnalysis}

\editme

\subsection{Statistical Analysis of Sighting Patterns}

\codeassignment{Now let's create a simple prediction system for whether a specific `camera` captured a `species` on a given `date`. Let's use the whole dataset, except for the prediction target date.

Before we jump into addressing the question, let's further assess the data. Calculate and plot average probabilities for dates, species, and cameras. You may want to implement some smoothing over dates, or group them into longer ranges.}{if not isinstance(df.index, (pd.DatetimeIndex, pd.PeriodIndex, pd.TimedeltaIndex)):
        df = df.copy()
        df.index = pd.to_datetime(df.index, errors="coerce")
df = df.sort_index()

# raw daily mean across all (camera, species)
avg_by_date_raw = df.mean(axis=1)


# set and apply smooth frequency
smooth_freq = "ME" # Monthly average, "YE" would be yearly
avg_by_date_smooth = avg_by_date_raw.resample(smooth_freq).mean()

# plot raw + smoothed
plt.figure(figsize=(12, 5))
plt.plot(avg_by_date_raw.index, avg_by_date_raw.values, alpha=0.4, label="Daily (raw)")
plt.plot(avg_by_date_smooth.index, avg_by_date_smooth.values, linewidth=2, label=f"Smoothed (Monthly Average)")
plt.title("Average Sighting Probability Over Time")
plt.xlabel("Date"); plt.ylabel("Probability"); plt.legend()
plt.show()

#Print these commands to help you understand what they do
#print(binary_df.index)
#print(binary_df.mean(axis=0))
#print(binary_df.mean(axis=0).groupby(level=1).mean())

#TODO Plot species and camera averages}{15}

\notes{Extension: which of these relationships that you found are statistically significant?}

\code{# TODO}

\endif



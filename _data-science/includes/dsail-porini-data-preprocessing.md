\ifndef{dsailPoriniDataPreprocessing}
\define{dsailPoriniDataPreprocessing}

\editme

\subsection{Sighting Predictions}

\notes{We will use the dataset to create a simple prediction model for the likelihood of animal sightings.

Let's follow a minimal example of the Access-Assess-Address framework!

Reminder about Neil's article on the framework [here](https://inverseprobability.com/talks/notes/access-assess-address-a-pipeline-for-automated-data-science.html).}

\subsubsection{Access}

Access is already done, partly years ago by the DSAIL team, and two cells above by us. Example tasks within access would be:
- Setting up the cameras in the woods (done)
- Collecting the pictures (done)
- Labeling the dataset (done)
- Making the excel file online accessible (done)
- Downloading the file (done just now)}

\code{porini_df.head()}

\subsubsection{Assess}

\notes{Have a look at the dataset for any issues that could stop us from being able to cleanly analyse it.

Some issues:
- Timestamps not readilly available. Hidden in image filenames.
- No timestamps available for one of the cameras.
- No Camera ID, but can be deduced from coordinates.

Decide how it would be best to address these and potentially other issues with the data.

We would like an output dataframe that has a column for counts each animal was spotted by each camera, and rows for each day in the available range. You might want to use this opportunity to practice [Pandas MultiIndex](https://pandas.pydata.org/docs/user_guide/advanced.html).}


\setupcode{import pandas as pd
import numpy as np
import re}

\code{# Copy original
df = porini_df.copy()

# Normalize species and parse counts
df["Species"] = df["Species"].astype(str).str.strip()

# Extract timestamp from filename
pat = re.compile(r"(\d{4})-(\d{2})-(\d{2})-(\d{2})-(\d{2})-(\d{2})")
def parse_ts(name):
    m = pat.search(str(name))
    if not m:
        return pd.NaT
    y, M, d, h, m_, s = map(int, m.groups())
    return pd.Timestamp(y, M, d, h, m_, s)

df["timestamp"] = df["Filename"].map(parse_ts)
df["date"] = df["timestamp"].dt.date

# Camera ID from rounded lat/lon
df["Latitude"] = df["Latitude"].round(4)
df["Longitude"] = df["Longitude"].round(4)
coord_key = df["Latitude"].astype(str) + "," + df["Longitude"].astype(str)
codes, _ = pd.factorize(coord_key)
df["camera_id"] = pd.Series(codes).map(lambda i: f"C{int(i)+1:03d}")

# Extract camera coordinates dictionary (rounded)
camera_coords = (
    df.drop_duplicates(subset="camera_id")[["camera_id", "Latitude", "Longitude"]]
      .set_index("camera_id")
      .sort_index()
      .apply(tuple, axis=1)
      .to_dict()
)

# Group and count: number of pictures per species per camera per day
daily = (
    df.dropna(subset=["date"])
      .groupby(["date", "camera_id", "Species"])
      .size()
      .reset_index(name="photo_count")
      .pivot_table(index="date", columns=["camera_id", "Species"], values="photo_count", aggfunc="sum")
      .fillna(0)
      .astype(int)
      .sort_index()
)

# Fill missing dates
if not daily.empty:
    full_idx = pd.date_range(start=daily.index.min(), end=daily.index.max(), freq="D").date
    daily = daily.reindex(full_idx).fillna(0).astype(int)
    daily.index.name = "date"

print(camera_coords)
daily.tail()}

\notes{Huh, looks like we have some more issues.
- "Impala, Monkey" is not a species - should be counted towards two!
- "Can't Tell" shouldn't be a species at all.
- Some columns don't exist (eg. `C011` has no `ZEBRA`). Let's just fill them with zeros.

Additionally, there probably weren't `1577` impalas spotted on Christmas Eve 2021. This is a result of burst shots repetitively capturing the same animal. For now, let's just treat the data as binary, whether at least one photo was taken on that day.
}

\codeassignment{Use the cell below to implement the changes discussed above, and potentially additional issues.}{binary_df = daily.copy()}{15}

\endif



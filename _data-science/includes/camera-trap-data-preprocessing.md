\ifndef{cameraTrapDataPreprocessing}
\define{cameraTrapDataPreprocessing}

\editme

\subsection{Assess: Data Quality and Preprocessing}

\notes{Have a look at the dataset for any issues that could stop us from being able to cleanly analyse it. This is the "Assess" phase of our framework.

Some issues we can identify:
- Timestamps not readily available - hidden in image filenames
- No timestamps available for one of the cameras
- No explicit Camera ID, but can be deduced from coordinates
- Multi-species entries (e.g., "Impala, Monkey") need to be handled
- Invalid entries like "Can't Tell" should be removed
- Burst photography creates inflated counts}

\notes{We want an output dataframe that has counts of each animal spotted by each camera, with rows for each day in the available range. This is a classic data reshaping problem.}

\setupcode{import pandas as pd
import numpy as np
import re}

\code{# Copy original data to preserve it
df = porini_df.copy()

# Normalize species names
df["Species"] = df["Species"].astype(str).str.strip()

# Extract timestamp from filename using regex
pat = re.compile(r"(\d{4})-(\d{2})-(\d{2})-(\d{2})-(\d{2})-(\d{2})")

def parse_timestamp(filename):
    """Extract datetime from camera trap filename"""
    m = pat.search(str(filename))
    if not m:
        return pd.NaT
    y, M, d, h, m_, s = map(int, m.groups())
    return pd.Timestamp(y, M, d, h, m_, s)

df["timestamp"] = df["Filename"].map(parse_timestamp)
df["date"] = df["timestamp"].dt.date

# Create Camera ID from rounded coordinates
df["Latitude"] = df["Latitude"].round(4)
df["Longitude"] = df["Longitude"].round(4)
coord_key = df["Latitude"].astype(str) + "," + df["Longitude"].astype(str)
codes, _ = pd.factorize(coord_key)
df["camera_id"] = pd.Series(codes).map(lambda i: f"C{int(i)+1:03d}")

# Extract camera coordinates dictionary
camera_coords = (
    df.drop_duplicates(subset="camera_id")[["camera_id", "Latitude", "Longitude"]]
      .set_index("camera_id")
      .sort_index()
      .apply(tuple, axis=1)
      .to_dict()
)

print("Camera coordinates:")
for cam_id, coords in camera_coords.items():
    print(f"  {cam_id}: {coords}")

# Group and count: photos per species per camera per day
daily_counts = (
    df.dropna(subset=["date"])
      .groupby(["date", "camera_id", "Species"])
      .size()
      .reset_index(name="photo_count")
      .pivot_table(index="date", columns=["camera_id", "Species"], 
                   values="photo_count", aggfunc="sum")
      .fillna(0)
      .astype(int)
      .sort_index()
)

# Fill missing dates to create complete time series
if not daily_counts.empty:
    full_idx = pd.date_range(start=daily_counts.index.min(), 
                            end=daily_counts.index.max(), freq="D").date
    daily_counts = daily_counts.reindex(full_idx).fillna(0).astype(int)
    daily_counts.index.name = "date"

print(f"\nDaily counts shape: {daily_counts.shape}")
daily_counts.tail()}

\notes{This preprocessing step transforms our raw observational data into a structured format suitable for time series analysis and machine learning. The systematic approach ensures we don't lose important information while making the data analytically tractable.}
\endif

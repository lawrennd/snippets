\ifndef{dsailPoriniDataJoining}
\define{dsailPoriniDataJoining}

\editme

\subsection{Joining Datasets}

\codeassignment{Geospatial data is particularly useful because it is the most common index in the world, over which so many datasets can be joined. Find the coordiante information in the dataset, and plot it on top of an OSM map.

You may want to deduplicate the coordinates before you plot!}{daily_bin = daily.copy()
# Step 1: Flatten the multi-index and reshape the dataframe

daily_bin.columns = pd.MultiIndex.from_tuples(daily_bin.columns)

# Step 2: Create a new clean dataframe
binary_rows = []

for (cam, species_str), series in daily_bin.items():
    # Split species (e.g. "IMPALA, MONKEY") into a list of individual species
    # ignore the "CAN'T TELL" species 
    species_list = [] #TODO

    for species in species_list:

      col = pd.Series(series, index=series.index)
      # Convert every value to 1 if any sightings, otherwise 0
      col_bin = 
      binary_rows.append((cam, species, col_bin))

# Step 3: Rebuild dataframe as binary_df

binary_df = pd.DataFrame({
    (cam, species): values
    for cam, species, values in binary_rows
}, index=daily_bin.index)

# Step 4: Create MultiIndex and 
binary_df.columns = pd.MultiIndex.from_tuples(binary_df.columns)
binary_df = binary_df.sort_index(axis=1, level=[0, 1])

# Step 5: Ensure all possible (camera, species) pairs exist

# Get all unique cameras and species used across all rows and store as a list
all_cameras = [] #TODO
all_species = [] #TODO

# Build full column MultiIndex
full_columns = pd.MultiIndex.from_product([all_cameras, all_species], names=["camera_id", "Species"])

# Reindex to include all possible combinations, fill missing with 0
binary_df = binary_df.reindex(columns=full_columns, fill_value=0)

#binary_df.tail()
binary_df}{15}

\endif



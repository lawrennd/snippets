\ifndef{osmFeatureExtraction}
\define{osmFeatureExtraction}

\editme

\subsection{Features for Machine Learning}

\notes{We have the POI information on all tourist places structured in a geodataframe. To work with them in a machine learning algorithm, it will be easier to convert them to a pandas DataFrame.}

\setupcode{import pandas as pd}

\code{pois_df = pd.DataFrame(pois)
pois_df['latitude'] = pois_df.apply(lambda row: row.geometry.centroid.y, axis=1)
pois_df['longitude'] = pois_df.apply(lambda row: row.geometry.centroid.x, axis=1)

tourist_places_df = pois_df[pois_df.tourism.notnull()]
print(len(tourist_places_df))
tourist_places_df}

\notes{Now we can create a feature vector by counting different types of points of interest. This transforms the geographic data into numerical features that machine learning algorithms can work with.}

\code{poi_types = [
    ("amenity", None),
    ("amenity", "school"),
    ("amenity", "hospital"),
    ("amenity", "restaurant"),
    ("amenity", "cafe"),
    ("shop", None),
    ("tourism", None),
    ("tourism", "hotel"),
    ("tourism", "museum"),
    ("leisure", None),
    ("leisure", "park"),
    ("historic", None),
    ("amenity", "place_of_worship"),
]

poi_counts = {}

for key, value in poi_types:
    if key in pois_df.columns:
        if value:  # count only that value
            poi_counts[f"{key}:{value}"] = (pois_df[key] == value).sum()
        else:  # count any non-null entry
            poi_counts[key] = pois_df[key].notnull().sum()
    else:
        poi_counts[f"{key}:{value}" if value else key] = 0

poi_counts_df = pd.DataFrame(list(poi_counts.items()), columns=["POI Type", "Count"])
poi_counts_df # feature vector}

\notes{This creates a feature vector that represents the characteristics of a place through the count of different amenities and points of interest. Such features can capture the economic, cultural, and social aspects of different locations.}

\endif

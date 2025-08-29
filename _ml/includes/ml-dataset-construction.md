\ifndef{mlDatasetConstruction}
\define{mlDatasetConstruction}

\editme

\subsection{Feature Extraction Function}

\notes{Use the code above to write a function, that given a set of coordinates, outputs a feature vector.}

\code{features = [
    ("building", None),
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
]}

\code{def get_feature_vector(latitude, longitude, box_size_km=2, features=None):
    """
    Given a central point (latitude, longitude) and a bounding box size,
    query OpenStreetMap via OSMnx and return a feature vector.

    Parameters
    ----------
    latitude : float
        Latitude of the center point.
    longitude : float
        Longitude of the center point.
    box_size_km : float
        Size of the bounding box in kilometers
    features : list of tuples
        List of (key, value) pairs to count.

    Returns
    -------
    feature_vector : dict
        Dictionary of feature counts, keyed by (key, value).
    """
    
    # Convert km to degrees (approximate)
    box_size_deg = box_size_km / 111.0
    
    # Construct bbox from lat/lon and box_size
    north = latitude + box_size_deg/2
    south = latitude - box_size_deg/2
    west = longitude - box_size_deg/2
    east = longitude + box_size_deg/2
    bbox = (west, south, east, north)
    
    # Query OSMnx for features
    all_tags = {}
    for key, value in features:
        if key not in all_tags:
            all_tags[key] = True
    
    try:
        pois = ox.features_from_bbox(bbox, all_tags)
        pois_df = pd.DataFrame(pois)
        
        # Count features matching each (key, value) in features
        feature_counts = {}
        for key, value in features:
            if key in pois_df.columns:
                if value:  # count only that value
                    feature_counts[f"{key}:{value}"] = (pois_df[key] == value).sum()
                else:  # count any non-null entry
                    feature_counts[key] = pois_df[key].notnull().sum()
            else:
                feature_counts[f"{key}:{value}" if value else key] = 0
        
        return feature_counts
    
    except Exception as e:
        print(f"Error extracting features for {latitude}, {longitude}: {e}")
        # Return zero counts if extraction fails
        feature_counts = {}
        for key, value in features:
            feature_counts[f"{key}:{value}" if value else key] = 0
        return feature_counts}

\subsection{Building a Dataset}

\notes{You will want it to query the area around the following cities.}

\code{cities_kenya = {
    "Nyeri, Kenya": {"latitude": -0.4371, "longitude": 36.9580},
    "Nairobi, Kenya": {"latitude": -1.2921, "longitude": 36.8219},
    "Mombasa, Kenya": {"latitude": -4.0435, "longitude": 39.6682},
    "Kisumu, Kenya": {"latitude": -0.0917, "longitude": 34.7680}
}

cities_england = {
    "Cambridge, England": {"latitude": 52.2053, "longitude": 0.1218},
    "London, England": {"latitude": 51.5072, "longitude": -0.1276},
    "Sheffield, England": {"latitude": 53.3811, "longitude": -1.4701},
    "Oxford, England": {"latitude": 51.7520, "longitude": -1.2577},
}}

\notes{Here we will collect the feature vectors for all cities into one dataset. If you wrote the above code well, the following should just run - but do take a minute to understand what's happening.}

\setupcode{pd.set_option('future.no_silent_downcasting', True)}

\code{def build_feature_dataframe(city_dicts, features, box_size_km=1):
    results = {}
    for country, cities in city_dicts:
        for city, coords in cities.items():
            vec = get_feature_vector(
                coords["latitude"],
                coords["longitude"],
                box_size_km=box_size_km,
                features=features
            )
            vec["country"] = country
            results[city] = vec
    return pd.DataFrame(results).T

df = build_feature_dataframe(city_dicts=[("Kenya", cities_kenya), ("England", cities_england)], features=features, box_size_km=1)

X = df.drop(columns="country").fillna(0)
y = df["country"]}

\notes{This systematic approach to feature extraction allows us to compare places quantitatively, turning qualitative geographic information into data that machine learning algorithms can process.}

\endif

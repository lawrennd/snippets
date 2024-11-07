\ifndef{assessingOsm}
\define{assessingOsm}

\editme

\subsection{Assessing the Available OpenStreetMap Features}

\notes{In the course assessment you will be given the task of constructing a prediction system for various indicators at a given location. We expect that knowledge of the local region around the property should be helpful in making those predictions. To evaluate this we will now look at [OpenStreetMap](https://www.openstreetmap.org) as a data source.}

\notes{In this section, you should follow the methodology used in the above example to extract summary OSM information that can be useful in making predictions about an area. Use code from the example to construct a function that summarises the number of various points of interest in a target area. You should write reusable code that allows you to explore the characteristics of different points of interest.}

\code{def count_pois_near_coordinates(latitude: float, longitude: float, tags: dict, distance_km: float = 1.0) -> dict:
    """
    Count Points of Interest (POIs) near a given pair of coordinates within a specified distance.
    Args:
        latitude (float): Latitude of the location.
        longitude (float): Longitude of the location.
        tags (dict): A dictionary of OSM tags to filter the POIs (e.g., {'amenity': True, 'tourism': True}).
        distance_km (float): The distance around the location in kilometers. Default is 1 km.
    Returns:
        dict: A dictionary where keys are the OSM tags and values are the counts of POIs for each tag.
    """}

\notes{Now that you have written reusable code, choose the tags you want to query. This should be different from the tags used in the example. You can also search for specific tags like this: `"amenity": ["university", ...`.}

\code{# Modify this dict
tags = {
    "amenity": ["university"],
    "historic": True,
    "leisure": True,
    "shop": True,
    "tourism": True,
    "religion": True,
}}

\notes{Here there are 13 UK locations.}

\code{locations_dict = {
    "Cambridge": (52.2054, 0.1132),
    "Oxford": (51.7570, -1.2545),
    "Euston Square": (51.5246, -0.1340),
    "Temple": (51.5115, -0.1160),
    "Kensington": (51.4988, -0.1749),
    "Barnsley": (53.5526, -1.4797),
    "Mansfield": (53.1472, -1.1987),
    "Wakefield": (53.6848, -1.5039),
    "Sunderland": (54.9069, -1.3838),
    "Rotherham": (53.4300, -1.3568),
    "Doncaster": (53.5228, -1.1288),
    "Chesterfield": (53.2350, -1.4210),
    "Huddersfield": (53.6450, -1.7794)
    }}

\exercise{Use your code to query the OSM feature counts for each of them, and combine them into one dataframe.}

\exercise{Use k-means clustering or another clustering method to try to find clusters of similar areas, based on nearby OSM features.}

\exercise{Investigate the locations yourself, and assign them categories based on your interpretation. Visualise and compare your manual assignments against your clustering results.}

\exercise{Normalise your dataframe and compute a distance matrix for the locations. Visualise it, and compare the outcode with your previous clustering results.}

\exercise{Which features you included were correlated among each other? Investigate and plot a feature correlation matrix. What do these results say about your feature selection?}

\endif

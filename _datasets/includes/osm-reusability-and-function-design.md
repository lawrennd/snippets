\ifndef{osmReusabilityAndFunctionDesign}
\define{osmReusabilityAndFunctionDesign}

\editme

\subsection{Reusability and Function Design}

\codeassignment{Use the code above to write a function that given a set of coordinates and a placename (eg. `Nyeri, Kenya`), outputs a visualisation of the area, with optional highlighted features.}{import osmnx as ox
import matplotlib.pyplot as plt
import math

def plot_city_map(place_name, latitude, longitude, box_size_km=2, poi_tags=None):
    """
    Plot a simple city map with area boundary, buildings, roads, nodes, and optional POIs.

    Parameters
    ----------
    place_name : str
        Name of the place (used for boundary + plot title).
    latitude, longitude : float
        Central coordinates.
    box_size_km : float
        Size of the bounding box in kilometers (default 2 km).
    poi_tags : dict, optional
        Tags dict for POIs (e.g. {"amenity": ["school", "restaurant"]}).
    """
    return NotImplementedError("not implemented yet")}{15}

\code{plot_city_map('Nyeri, Kenya', -0.4371, 36.9580, 5, poi_tags=tags)}

\codeassignment{Plot the area around one of these English cities, and compare it with Nyeri. What do you notice? What assumptions did you make in your code that are now not holding? Go back to the relevant part of the code and fix it.}{plot_city_map('Cambridge, England', 52.205, 0.1218, 5, poi_tags=tags)}{15}

\endif

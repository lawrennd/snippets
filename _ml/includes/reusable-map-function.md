\ifndef{reusableMapFunction}
\define{reusableMapFunction}

\editme

\subsection{Creating Reusable Code}

\notes{Use the code above to write a function, that given a set of coordinates and a placename (eg. `Nyeri, Kenya`), outputs a visualisation of the area, with optional highlighted features.}

\setupcode{import osmnx as ox
import matplotlib.pyplot as plt
import math}

\code{def plot_city_map(place_name, latitude, longitude, box_size_km=2, poi_tags=None):
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
    # Convert km to degrees (approximate)
    box_size_deg = box_size_km / 111.0  # rough conversion
    
    # Create bounding box
    north = latitude + box_size_deg/2
    south = latitude - box_size_deg/2
    west = longitude - box_size_deg/2
    east = longitude + box_size_deg/2
    bbox = (west, south, east, north)
    
    try:
        # Get graph from location
        graph = ox.graph_from_bbox(bbox)
        # City area
        area = ox.geocode_to_gdf(place_name)
        # Street network
        nodes, edges = ox.graph_to_gdfs(graph)
        # Buildings
        buildings = ox.features_from_bbox(bbox, tags={"building": True})
        
        # POIs if specified
        if poi_tags:
            pois = ox.features_from_bbox(bbox, poi_tags)
        
        # Create the plot
        fig, ax = plt.subplots(figsize=(6,6))
        area.plot(ax=ax, color="tan", alpha=0.5)
        buildings.plot(ax=ax, facecolor="gray", edgecolor="gray")
        edges.plot(ax=ax, linewidth=1, edgecolor="black", alpha=0.3)
        nodes.plot(ax=ax, color="black", markersize=1, alpha=0.3)
        
        if poi_tags and 'pois' in locals():
            pois.plot(ax=ax, color="green", markersize=5, alpha=1)
            
        ax.set_xlim(west, east)
        ax.set_ylim(south, north)
        ax.set_title(place_name, fontsize=14)
        plt.show()
        
    except Exception as e:
        print(f"Error plotting {place_name}: {e}")
        print("This might be due to limited data availability or network issues")}

\notes{Now we can test our function with the original location:}

\code{plot_city_map('Nyeri, Kenya', -0.4371, 36.9580, 5, poi_tags=tags)}

\notes{And compare it with an English city:}

\code{plot_city_map('Cambridge, England', 52.205, 0.1218, 5, poi_tags=tags)}

\notes{What do you notice? What assumptions did you make in your code that are now not holding? The function approach allows us to easily compare different locations and identify patterns or differences in urban structure.}

\endif

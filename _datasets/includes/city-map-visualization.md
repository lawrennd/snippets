\ifndef{cityMapVisualization}
\define{cityMapVisualization}

\editme

\subsection{Visualizing Geographic Data}

\notes{This gives us the relevant points of interest (part of the map). If we'd like to see the entire street network, we can download the entire graph from the location.}

\code{# Get graph from location
graph = ox.graph_from_bbox(bbox)
# City area
area = ox.geocode_to_gdf(place_name)
# Street network
nodes, edges = ox.graph_to_gdfs(graph)
# Buildings
buildings = ox.features_from_bbox(bbox, tags={"building": True})}

\notes{Which we can then render as follows.}

\plotcode{fig, ax = plt.subplots(figsize=(6,6))
area.plot(ax=ax, color="tan", alpha=0.5)
buildings.plot(ax=ax, facecolor="gray", edgecolor="gray")
edges.plot(ax=ax, linewidth=1, edgecolor="black", alpha=0.3)
nodes.plot(ax=ax, color="black", markersize=1, alpha=0.3)
pois.plot(ax=ax, color="green", markersize=5, alpha=1)
ax.set_xlim(west, east)
ax.set_ylim(south, north)
ax.set_title(place_name, fontsize=14)
plt.show()}

\notes{Sanity check. Head over to <https://www.openstreetmap.org/#map=14/-0.43710/36.95800> and compare your map against the real thing.}

\notes{This visualization provides a comprehensive view of the urban landscape, showing the relationship between different geographic features. The combination of street networks, buildings, and points of interest gives us insight into the structure and character of the place.}

\endif

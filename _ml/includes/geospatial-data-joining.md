\ifndef{geospatialDataJoining}
\define{geospatialDataJoining}

\editme

\subsection{Joining Datasets with Geospatial Data}

\notes{Geospatial data is particularly useful because it is the most common index in the world, over which so many datasets can be joined. Location provides a natural way to integrate disparate data sources and add contextual information to our analyses.

In this exercise, we'll extract coordinate information from the camera trap dataset and visualize it on an OpenStreetMap base layer. This demonstrates how wildlife monitoring data can be integrated with geographic information systems.}

\exercise{Find the coordinate information in the camera trap dataset, and plot it on top of an OSM map. You may want to deduplicate the coordinates before you plot!}

\code{# Extract unique camera locations
unique_locations = porini_df[['Latitude', 'Longitude']].drop_duplicates()
print(f"Found {len(unique_locations)} unique camera locations")

# Display the coordinates
unique_locations.head()}

\notes{Once we have the coordinates, we can use the mapping functions from our Fynesse library to visualize them in geographic context:}

\code{# Example of plotting camera locations
# You can use your plot_city_map function to show the area
# Then overlay the camera positions as additional points

import matplotlib.pyplot as plt
# Basic scatter plot of camera locations
plt.figure(figsize=(10, 8))
plt.scatter(unique_locations['Longitude'], unique_locations['Latitude'], 
           c='red', s=100, alpha=0.7, label='Camera Locations')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('DSAIL-Porini Camera Trap Locations')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()}

\notes{This geographic visualization immediately reveals the spatial distribution of the monitoring network and can help us understand the ecological context of our observations. The clustering or spread of cameras can influence the patterns we observe in the data.}

\endif

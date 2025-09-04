\ifndef{openstreetmapData}
\define{openstreetmapData}

\editme

\subsection{OpenStreetMap Data}

\notes{We will download data of Nyeri, Kenya, which has the following latitude and longitude.}

\code{place_name = "Nyeri, Kenya"
latitude = -0.4371
longitude = 36.9580
placestub = place_name.lower().replace(' ', '-').replace(',','')}

\notes{We'll create a bounding box which is 0.02 degrees wide, 1 degree is around 111km (circumference of the Earth is around 40,000 km and 40,000/360=111km). Note: will this approximation work well in all countries?}

\code{box_width = 0.1 # About 11 km
box_height = 0.1
north = latitude + box_height/2
south = latitude - box_height/2
west = longitude - box_width/2
east = longitude + box_width/2
bbox = (west, south, east, north)}

\notes{This bounding box defines the geographic area we want to analyze. The choice of size is important - too small and we miss important context, too large and we may include irrelevant features or face performance issues.}

\subsection{Downloading and Visualizing Geospatial Data}

\include{_datasets/includes/poi-extraction-osm.md}

\include{_datasets/includes/city-map-visualization.md}

\endif





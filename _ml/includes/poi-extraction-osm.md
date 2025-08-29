\ifndef{poiExtractionOsm}
\define{poiExtractionOsm}

\editme

\subsection{Points of Interest Extraction}

\notes{Now we'll download a set of points of interest from OpenStreetMap. We can specify the points of interest we're interested in by building a small dictionary containing their labels as follows. A Point of Interest is a location with certain importance in the geographic area. They can vary from amenities to touristic places as you can see in the following.}

\code{# Retrieve POIs
tags = {
    "amenity": True,
    "buildings": True,
    "historic": True,
    "leisure": True,
    "shop": True,
    "tourism": True,
    "religion": True,
    "memorial": True
}}

\notes{We can use osmnx to download all such points of interest within a given bounding box.}

\code{pois = ox.features_from_bbox(bbox, tags)}

\notes{That operation can take some time, particularly as the bounding box grows larger. Once it is complete we can check how many points of interest we have found, and examine their contents in more detail.}

\code{print(len(pois))
pois.head()}

\notes{We notice a few things:

- Points of interest do not have a consistent OpenStreetMap element_type, some are `node`, others are `relation` and we also have `way`. You can find out more about elements in OpenStreetMap on [this wiki page](https://wiki.openstreetmap.org/wiki/Elements). This will become important when tidying up the data for next stage processing.

- Many of the values are missing. In SQL we would express a missing value as NULL. But in pandas a missing value is expressed as not-a-number, NaN. This is quite a common standard, but it is not the only standard. Sometimes data is collected and coded with an "unreasonable" value for a missing value. For example, someone might set missing values for heights to -999. The concept is that this is an obviously void "height" and would trigger a human user to check whether it's a missing value. Of course, this is obvious to humans, but not necessarily to a computer!}

\notes{Nodes, ways and relations in OpenStreetMap all have different keys associated with them. The data is not structured in standard database columns. Different points of interest might have different keys present or absent.}

\endif

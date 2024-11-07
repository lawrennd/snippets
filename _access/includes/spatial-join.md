\ifndef{spatialJoin}
\define{spatialJoin}

\editme

\subsection{Joining Spatial Data}

\subsubsection{Matching OpenStreetMap and House Prices data}

\notes{In this exercise you will download the geographies of houses from OpenStreetMap and map them to visualise the records you see in the house price dataset. This is a data linking and validation exercise.}

\notes{The latitude and longitude of Cambridge are as follows:}

\code{place_name = "Cambridge"
latitude = 52.1951
longitude = 0.1313}

\notes{We want to execute an SQL query on your database to select all houses in a 1km x 1km region around the centre of Cambridge that have been part of housing transactions since 2020.}

\notes{This operation can take a very long time. This is because the table is not indexed on coordinate data, and therefore the query has to check tens of millions of rows. This can be fixed by constructing an index on the `latitude` and `longitude` values, using `BTREE` to make a joint index. *Note that indexing can take a long time.* Consider also indexing your table by other variables you might find useful later.}

\exercise{Index the table on the coordinate data using a `BTREE` and index other columns you might find useful.}

\exercise{Write an SQL query on your database to select all houses in a 1km x 1km region around the centre of Cambridge that have been part of housing transactions since 2020.}

\exercise{Get information about all the buildings in that area from OpenStreetMaps (`'building': True`). You will need their address information (`addr:housenumber`, `addr:street`, `addr:postcode`, ...) and geometry polygon (`geometries_from_bbox`). Construct a dataframe that lists all OSM buildings in the area that have a full address, along with their area (in square meters). Plot a map of the area, using color to mark the buildings with addresses and the ones without.}

\exercise{Match the houses you found in the price paid dataset with the buildings on OpenStreetMaps based on their addresses.
Can this be applied to all building types?
Are there any PP transactions which you couldn't match to an OSM building, or any OSM buildings you coulnd't match to a PP transaction? If so, what could be the reason for this?
Do you employ any techniques to find non-exact matches? If yes, what matches would you have missed without it? Are you encountering false positive matches?
Use this address matching to merge the two dataframes.}

\exercise{Examine the relationship between the price and area of a property.
- What other variables do you need to account for?
- Is the correlation as strong as you would expect?
- What factors could be impacting this?

Visualise the relationships you found.}

\notes{Demonstrate the reusability of your code by executing the same analysis for Oxford.}

\code{place_name = "Oxford"

latitude = 51.7520
longitude = -1.2577}

\exercise{Replicating the same analysis for Oxford. You do not need to answer all the questions again, but you should show that your code works for this new input without the need to modify it. You should use the Fynesse library for this. Finish by plotting a map of the area and the correlation you find.}

\subsection{Conclusions}

\notes{You should find some of the code you wrote above useful in your final assessment. Make sure you wrote the code to be reusable and efficient, and do include it in your Fynesse library. The functions you are particularly likely to reuse are the OSM feature search, and map visualisation functions.}

\exercise{Add relevant code to your Fynesse library. Demonstrate this was successful by installing your library below and calling at least two example functions.}

\endif

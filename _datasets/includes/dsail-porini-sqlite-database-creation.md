\ifndef{sqliteDatabaseCreation}
\define{sqliteDatabaseCreation}

\editme

\subsection{Database Integration with SQLite}

\notes{Throughout the course you will work with various datasets and data formats. An SQL database is one of the most common ways to store large amounts of data. We recognise that many of you may be familiar with this already, but let's use this example to build a small toy database of animal sightings based on the excel file and the dataframes we created.}

\codeassignment{- Create a local database (eg. `sqlite3`).
- Add a table with animal sighting data.
- Add a table with camera coordinates data.
- Set indices on columns you might search by (eg. `CameraID`, `Date`). Make sure the index types make sense!
- Look into multi column indices, and set one on `Latitude` and `Longitude`.
- Demonstrate success with a couple SQL queries, eg. counting `IMPALA` sightings within a `200m` square around `-0.3866, 36.9649`.

Helpful links:

[SQL Intro, Creating Tables, Indices, Joins](https://www.w3schools.com/sql/sql_intro.asp)

[Multi-Column Indices](https://stackoverflow.com/questions/179085/multiple-indexes-vs-multi-column-indexes)

Remember to include reusable code from this and previous exercises in your Fynesse library!}{}{20}


\endif



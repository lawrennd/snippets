\ifndef{osmAccessAssessAddress}
\define{osmAccessAssessAddress}

\editme

\subsection{Access, Assess, Address Framework}


\notes{The Access-Assess-Address framework provides a systematic approach to data science projects:

- **Access**: How do we get the data? This includes APIs, web scraping, database queries, file formats, etc.
- **Assess**: How do we evaluate data quality, understand its structure, and validate our assumptions?
- **Address**: How do we answer the specific question or solve the problem at hand?}

\subsection{Applying the Framework}

Using the lessons from the article, have a look at the functionality you created, and identify generalisable Access, Assess and Address functionality that could come in useful in the future.

**Access functionality** 

What we've created:
- Connection to OpenStreetMap API via OSMnx

What we might need to have done:
- Legal, ethical considerations.

**Assess functionality** 

What we've created:
- `plot_city_map()`: visualizes OSM data for any location
- `get_feature_vector()`: Extracts quantitative features from geographic coordinates
- Visualization of geographic data to understand structure
- Feature counting and summarization
- Dimensionality reduction for pattern visualization

What we could create
- Data quality checks (handling missing data, failed queries)

**Address functionality** 

What we've created:
- Machine learning pipeline for location classification
- Evaluation on test sets
- Analysis of model performance and potential biases}

\endif

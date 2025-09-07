\ifndef{movieBodyCountData}
\define{movieBodyCountData}

\editme

\subsection{Movie Body Count Data}
\slides{* Data containing movie information (year, length, rating, genre, IMDB Rating).}
\notes{This is a data set created by Simon Garnier and Rany Olson for exploring the differences between R and Python for data science. The data contains information about different movies, augmented by estimates about how many on-screen deaths are contained in the movie. The data is scraped from <http://www.moviebodycounts.com>. The data contains the following features for each movie: `Year`, `Body_Count`, `MPAA_Rating`, `Genre`, `Director`, `Actors`, `Length_Minutes`, `IMDB_Rating`.}

\code{data = pods.datasets.movie_body_count()['Y']}

\notes{The data is provided to us in the form of a pandas data frame. We can see the features we're provided with by inspecting the columns of the data frame.}

\code{print(', '.join(movies.columns))}

\notes{Once it is loaded in the data can be summarised using the `describe` method in pandas.}

\notes{Quick Data Assess - let's make sure the rows are unique.}

\code{data['Name'] = data['Film']+' ('+data['Year'].astype(str)+')'
data[data['Name'].duplicated(keep=False)]}

\code{data = data.drop_duplicates(subset=['Name'])
data = data.reset_index(drop=True)
data}

\endif

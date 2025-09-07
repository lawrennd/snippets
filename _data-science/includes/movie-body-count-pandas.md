\ifndef{movieBodyCountPandas}
\define{movieBodyCountPandas}

\editme

\section{Movie Body Count Data Example}

\notes{There is a crisis in the movie industry, deaths are
occuring on a massive scale. In every feature film the body count is tolling up.
But what is the cause of all these deaths? Let's try and investigate.}

\notes{For our first example of data science, we take inspiration from work by [researchers at NJIT](http://www.theswarmlab.com/r-vs-python-round-2/). They researchers were comparing the qualities of Python with R (my brief thoughts on the subject are available in a Google+ post here: https://plus.google.com/116220678599902155344/posts/5iKyqcrNN68). They put together a data base of results from the  the "Internet Movie Database" and the [Movie Body Count](http://www.moviebodycounts.com/) website which will allow us to do some preliminary investigation.}

\notes{We will make use of data that has already been 'scraped' from the [Movie Body Count](http://www.moviebodycounts.com/) website. Code and the data is available at [a github repository](https://github.com/sjmgarnier/R-vs-
Python/tree/master/Deadliest%20movies%20scrape/code). Git is a version control
system and github is a website that hosts code that can be accessed through git.
As well as accessing the code
via github you can also [download the zip file](https://github.com/sjmgarnier/R-vs-Python/archive/master.zip).}

\include{_datasets/include/movie-body-count-data.md}

\notes{In jupyter and jupyter notebook it is possible to see a list of
all possible functions and attributes by typing the name of the object
followed by `.<Tab>` for example in the above case if we type `data.<Tab>`
it show the columns available (these are attributes in pandas
dataframes) such as `Body_Count`, and also functions, such as
.describe().}

\notes{For functions we can also see the
documentation about the function by following the name with a question mark.
This will open a box with documentation at the bottom which can be closed with
the x button.}

\code{data.describe?}

\notes{The film deaths data is stored in an object known as a 'data
frame'. Data frames come from the statistical family of programming
languages based on `S`, the most widely used of which is
[`R`](http://en.wikipedia.org/wiki/R_(programming_language)). The data
frame gives us a convenient object for manipulating data. The describe
method summarizes which columns there are in the data frame and gives
us counts, means, standard deviations and percentiles for the values
in those columns. To access a column directly we can write}

\include{_data-science/includes/movie-body-count-visualise.md}

\endif

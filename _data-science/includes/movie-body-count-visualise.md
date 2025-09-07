\ifndef{movieBodyCountVisualise}
\define{movieBodyCountVisualise}

\editme

\subsection{Plotting the Data}

\code{print(data['Year'])
#print(data['Body_Count'])}

\notes{This shows the number of deaths per film across the years. We
can plot the data as follows.}

\setupcode{# this ensures the plot appears in the web browser
%matplotlib inline 
import matplotlib.pyplot as plt # this imports the plotting library in python}

\code{plt.plot(data['Year'], data['Body_Count'], 'rx')}

\notes{You may be curious what the arguments we give to `plt.plot` are
for, now is the perfect time to look at the documentation}

\code{plt.plot?}

\notes{We immediately note that some films have a lot of deaths, which
prevent us seeing the detail of the main body of films. First lets
identify the films with the most deaths.}

\code{data[data['Body_Count']>200]}

\notes{Here we are using the command `data['Kill_Count']>200` to index
the films in the pandas data frame which have over 200 deaths. To sort
them in order we can also use the `sort` command. The result of this
command on its own is a data series of `True` and `False`
values. However, when it is passed to the `data` data frame it returns
a new data frame which contains only those values for which the data
series is `True`. We can also sort the result. To sort the result by
the values in the `Kill_Count` column in *descending* order we use the
following command.}

\code{data[data['Body_Count']>200].sort_values(by='Body_Count', ascending=False)}

\notes{We now see that the 'Lord of the Rings' is a large outlier with
a very large number of kills. We can try and determine how much of an
outlier by histograming the data.}

\notes{\subsection{Plotting the Data}}

\code{data['Body_Count'].hist(bins=20) # histogram the data with 20 bins.
plt.title('Histogram of Film Kill Count')}

\writeassignment{Read on the internet about the following python
libraries: `numpy`, `matplotlib`, `scipy` and `pandas`. What functionality does
each provide python. What is the `pylab` library and how does it relate to the
other libraries?}{10}

\notes{We could try and remove these outliers, but another approach would be plot the logarithm of the counts against the year.}

\code{plt.plot(data['Year'], data['Body_Count'], 'rx')
ax = plt.gca() # obtain a handle to the current axis
ax.set_yscale('log') # use a logarithmic death scale
# give the plot some titles and labels
plt.title('Film Deaths against Year')
plt.ylabel('deaths')
plt.xlabel('year')}

\notes{Note a few things. We are interacting with our data. In
particular, we are replotting the data according to what we have
learned so far. We are using the progamming language as a *scripting*
language to give the computer one command or another, and then the
next command we enter is dependent on the result of the previous. This
is a very different paradigm to classical software engineering.  In
classical software engineering we normally write many lines of code
(entire object classes or functions) before compiling the code and
running it. Our approach is more similar to the approach we take
whilst debugging. Historically, researchers interacted with data using
a *console*. A command line window which allowed command entry. The
notebook format we are using is slightly different.  Each of the code
entry boxes acts like a separate console window. We can move up and
down the notebook and run each part in a different order. The *state*
of the program is always as we left it after running the previous
part.}

\endif

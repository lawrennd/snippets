\ifndef{footballMultiColumnIndex}
\define{footballMultiColumnIndex}

\editme

\subsection{Multi-column Index}

\notes{Sometimes you will be repetitively looking for data that fits multiple criteria at once. The most common example would be coordinates - latitude and longitude.

Imagine if, when looking for houses within 10km of Mt Kenya, you had to search through all the houses on earth one by one. That would be very inefficient. But single indices on latitude and longitude would still not help you that much - there are millions of houses within 10km of the equator, in Kongo, Ecuador, Indonesia - you would first narrow it down to all of those, and then have to search through them again, with respect to longitude.}

\figure{\includepng{\diagramsDir/datasets/world-map-continents-oceans}}{80%}{}

\notes{That's why we have multi-column indices. The simplest example would be a map - given a detailed map, I can easily find the area I'm looking for data in.}

\notes{Using our `players` example, let's look for players who are both tall and strong.}

\code{start = time.time()
query = """
SELECT playerid, height, strength
FROM players
WHERE height > 190 AND strength > 90
"""
cur.execute(query)
results = cur.fetchall()
print(time.time() - start)

print(len(results))}

\notes{Now, if we set individual indices, this becomes much faster:}

\code{queries = [
    "CREATE INDEX IF NOT EXISTS idx_players_height ON players(height);",
    "CREATE INDEX IF NOT EXISTS idx_players_strength ON players(strength);",
]

for q in queries:
    cur.execute(q)}

\code{start = time.time()
query = """
SELECT playerid, height, strength
FROM players
WHERE height > 190 AND strength > 90
"""
cur.execute(query)
results = cur.fetchall()
print(time.time() - start)

print(len(results))}

\code{queries = [
"CREATE INDEX idx_players_height_strength ON players(height, strength);"
]

for q in queries:
    cur.execute(q)}

\code{start = time.time()
query = """
SELECT playerid, height, strength
FROM players
WHERE height > 190 AND strength > 90
"""
cur.execute(query)
results = cur.fetchall()
print(time.time() - start)

print(len(results))}

\notes{Looks like this is not actually that good of an example - performance didn't change much, maybe actually got worse. Don't be alarmed, this is just because our table is quite small (27000 rows), and traversing the indices takes more time than just reading the table. The difference will be huge on larger datasets though, so remember about these!}

\notes{Remember to close the connection}

\code{conn.close()}

\subsubsection{Pandas MultiIndex}

\notes{Despite similar name, and pertaining to similar things, a Pandas MultiIndex is not what we described above. It's not an index where you can search over multiple columns, but rather a *hierarchical* index, where you're looking over multiple columns as if they were one key.}

\code{tpl_df = pd.read_csv('football_data/teamplayerlinks.csv')
tpl_df = tpl_df.set_index(['teamid', 'jerseynumber'])
tpl_df = tpl_df.sort_index()
tpl_df.tail()}

\notes{Then, we can neatly look up the stats of the player who plays with `#9` for team `241 - FC Barcelona`.}

\code{tpl_df.loc[241, 9]}

\notes{This falls in the *syntactic sugar* category of things, not really improving performace, just allowing for neat code.}

\endif

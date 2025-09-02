\ifndef{footballSqlIndexing}
\define{footballSqlIndexing}

\editme

\subsection{Indexing}

\subsubsection{Background}

\notes{A database is not a special piece of hardware, it can live on any medium. It's just an organized collection of data stored in a structured way, allowing efficient storage, retrieval, and management of information.

What we usually mean by a database is just a standard digital implementation of such a system.}

\figure{\includejpg{\diagramsDir/datasets/british-geological-survey}{50%}}{Photo by British Geological Survey}{british-geological-survey}

\notes{What makes databases special is the structure - the information is conveyed in a way that allows for complicated lookup operations to be completed quickly.}

\subsubsection{Physical Index}

\notes{This is what you would usually mean when talking about simple indexes. This is how dictionaries, encyclopedias work. Many datasets have built-in physical indices, even if not explicitly defined.}

\notes{In our example, we can see that some tables are sorted by an important column - eg. `models.csv` is sorted by `playerid`. We can use this to our advantage when searching through it.

Without abstracting away to library search functions, let's follow through on what it might look like to find who is player `188545`.}

\setupcode{import pandas as pd}

\code{models_df = pd.read_csv('football_data/models.csv')

start = time.time()
search_id = 188545
for i in range(len(models_df)):
    if models_df.iloc[i]['playerid'] == search_id:
        print(models_df.iloc[i]['playername'])
print(time.time()-start)}

\notes{Now, let's assume the table is sorted on `playerid`. This allows us to search through the data cleverly, only checking a couple values.}

\code{models_df = pd.read_csv('football_data/models.csv')
start = time.time()
search_id = 188545
left, right = 0, len(models_df) - 1
while left <= right:
    mid = (left + right) // 2
    val = models_df.iloc[mid]['playerid']
    if val == search_id:
        print(models_df.iloc[mid]['playername'])
        break
    elif val < search_id:
        left = mid + 1
    else:
        right = mid - 1
print(time.time() - start)}

\notes{The above is not *truly* an index, as many `playerids` are missing, so we can't just look up the 188545th row instantly - we still used `O(log(n))` lookups. Proper indexing will allow us to do that.}

\code{models_df_indexed = pd.read_csv('football_data/models.csv').set_index('playerid')
start = time.time()
search_id = 188545
print(models_df_indexed.loc[search_id]['playername'])
print(time.time() - start)}

\subsubsection{Logical index}

\notes{A logical index is an external structure that we build next to our database. Pandas doesn't really allow that (limit 1 index), but you can use as many as you want in SQL.}

\notes{Let's demonstrate a home-made logical index on the same dataframe, where we index the player names, for a quick `playername -> playerid` search.}

\code{name_to_index = {name: i for i, name in enumerate(models_df_indexed['playername'])}
start = time.time()
models_df_indexed.iloc[name_to_index['Robert Lewandowski']]
print(time.time() - start)}

\notes{Databases will do that under the hood for you, just use SQL like:

```
CREATE INDEX index_name
ON table_name (column1, column2, ...);
```}

\subsubsection{Practical example}

\notes{Let's load in the `players`, `teams`, and `teamplayerlinks` tables we have, to a new database.}

\code{db_path = "football.db"
players_csv = "football_data/players.csv"
teams_csv = "football_data/teams.csv"
teamlinks_csv = "football_data/teamplayerlinks.csv"

conn = sqlite3.connect(db_path)

players_df = pd.read_csv(players_csv)
teams_df = pd.read_csv(teams_csv)
teamlinks_df = pd.read_csv(teamlinks_csv)

players_df.to_sql("players", conn, if_exists="replace", index=False)
teams_df.to_sql("teams", conn, if_exists="replace", index=False)
teamlinks_df.to_sql("teamplayerlinks", conn, if_exists="replace", index=False)

cur = conn.cursor()}

\code{query = """
SELECT p.overallrating
FROM players p
JOIN teamplayerlinks tpl ON p.playerid = tpl.playerid
JOIN teams t ON tpl.teamid = t.teamid
WHERE t.teamname = "Sheffield Utd";
"""

start = time.time()
cur.execute(query)
results = [row[0] for row in cur.fetchall()]
print(time.time() - start)

print(results)}

\notes{Now, let's make indices on `teamid` and `playerid` (others optional).}

\code{queries = [
    "CREATE INDEX IF NOT EXISTS idx_teams_teamname ON teams(teamname);",
    "CREATE INDEX IF NOT EXISTS idx_tpl_teamid ON teamplayerlinks(teamid);",
    "CREATE INDEX IF NOT EXISTS idx_tpl_playerid ON teamplayerlinks(playerid);",
    "CREATE INDEX IF NOT EXISTS idx_players_playerid ON players(playerid);"
]

for q in queries:
    cur.execute(q)}

\notes{And now, let's call the same query we did before. This should be massively faster.}

\code{query = """
SELECT p.overallrating
FROM players p
JOIN teamplayerlinks tpl ON p.playerid = tpl.playerid
JOIN teams t ON tpl.teamid = t.teamid
WHERE t.teamname = "Sheffield Utd";
"""

start = time.time()
cur.execute(query)
results = [row[0] for row in cur.fetchall()]
print(time.time() - start)

print(results)}

\endif

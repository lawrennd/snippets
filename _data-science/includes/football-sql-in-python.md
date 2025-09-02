\ifndef{footballSqlInPython}
\define{footballSqlInPython}


\editme

\subsection{SQL in Python}

\notes{Just a reminder, you can use SQL inside Python very neatly. It's the recommended practice, and leaves you compatible with other systems using your database.}

\setupcode{import sqlite3
import pandas as pd}

\code{df = pd.read_csv("football_data/players.csv")
conn = sqlite3.connect("example.db")
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS players")
df.to_sql("players", conn, if_exists="replace", index=False)

for row in cur.execute("SELECT playerid FROM players WHERE potential > 92"):
    print(row)

cur.close()
conn.close()}

\subsubsection{Credential Storage}

\notes{Many times when working with APIs and non-public data, you will use passwords, usernames, keys. It's commonplace to just leave them in the notebook, but that's a horrible idea, for obvious reasons.

Better way is to set the values as environment variables. Ideally you would set them in your system, like:

```
set API_KEY=your_api_key_here
set DB_PASSWORD=your_db_password
```

Or in Python:}

\code{os.environ["API_KEY"] = "my_secret_key"
os.environ["DB_PASSWORD"] = "super_secret"
# remember to remove this from anything someone else might have access to,
# including autosave and version control!

print(os.getenv("API_KEY"))
print(os.getenv("DB_PASSWORD"))}

\notes{The above might be very annoying when working in a notebook where we keep resetting runtime, with you having to re-type the environment variables again and again.

A middle-ground between security and usability.}

\code{import json}

\code{secrets = {
    "API_KEY": "my_secret_key", # remember to remove, or ideally edit in file only
    "DB_PASSWORD": "super_secret" # remember to remove, or ideally edit in file only
}
with open("secrets.json", "w") as f:
    json.dump(secrets, f, indent=4)}

\code{with open("secrets.json") as f:
    loaded = json.load(f)

print("API_KEY:", loaded["API_KEY"])
print("DB_PASSWORD:", loaded["DB_PASSWORD"])
# remember to not have outputs like this in anything visible to others}

\notes{`.env` files and the `dotenv` library is also a less intuitive but more professional way to do it.}

\notes{You can also use `input`
```
api_key = input("Enter API key: ")
db_password = input("Enter DB password: ")
```
or IPython interact
```
import ipywidgets as w
from IPython.display import display

api_key = w.Text(description="API Key")
db_password = w.Password(description="Password")

display(api_key, db_password)
# api_key.value
# db_password.value
```
as other means of not leaving passwords in your notebook.}

\endif

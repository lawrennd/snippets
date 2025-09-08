\ifndef{recommenderData}
\define{recommenderData}
\editme

\subsection{Collecting the Data}

\notes{This functionality involves some prewritten code which connects to a central write server, where you can rate movies that you’ve seen. }

\notes{Once you have placed your ratings, we can download the data to a file. We will build an algorithm on these ratings and use them to make predictions for the rest of the class. Firstly, here’s the code for which movies we will be rating. Remember to change your name.}

\code{import pandas as pd
import os
movies_list = [
    # Kenyan films
    "Nairobi Half Life",
    "Rafiki",
    "Sincerely Daisy",
    "Supa Modo",
    "Kati Kati",
    "Mvera",
    "NAWI: Dear Future Me",
    "BOBO",
    "The First Grader",
    "Mother Mother",
    "The Wall Street Boy",
    "40 Sticks",
    "TeraStorm",

    # Global all-time blockbuster hits
    "Avatar",
    "Avengers: Endgame",
    "Titanic",
    "The Lion King",
    "Frozen",
    "Spider-Man: No Way Home",
    "Black Panther",
    "Top Gun: Maverick",
    "The Dark Knight",
    "Inception",
    "Jurassic World",
    "Minions: The Rise of Gru",
    "The Fate of the Furious",
    "Doctor Strange in the Multiverse of Madness",
    "Furious 7",
    "Star Wars: The Force Awakens",
    "The Avengers",
    "Beauty and the Beast",
    "Harry Potter and the Deathly Hallows – Part 2",
    "Joker",
    "Aladdin",
    "Aquaman"
]

name = 'todo' # TODO: your name here - this will be somewhat public so you might not want to use full real names, nickname is fine
assert name!='todo'}

\notes{The below code starts an interactive Python Widget, which will submit your responses. There's also code for reading the ratings after they've been submitted.}

\code{import random, requests, ipywidgets as W
from ipywidgets import Widget
from IPython.display import display, clear_output
import json

# Config
topic, target = "mlfc_movie_ratings", 25
url = f"https://ntfy.sh/{topic}"
cache = "rated_movies_cache.txt"

def responses(topic=topic, sep="|||", since="all", n=None):
    url = f"https://ntfy.sh/{topic}/json?poll=1&since={since}"
    rows = []
    with requests.get(url, stream=True) as r:
        for line in r.iter_lines():
            if not line: continue
            e = json.loads(line)
            if e.get("event") != "message": continue
            p = (e.get("message") or "").split(sep)
            rows.append({"user": p[0], "film": p[1], "rating": pd.to_numeric(p[2], errors="coerce")} if len(p)==3 else {"raw": e.get("message")})
            if n and len(rows) >= n: break
    return pd.DataFrame(rows)

def start_movie_rater(movies_list=movies_list, topic=topic, name=name, target=25):
    import random, requests
    import ipywidgets as W
    from IPython.display import display

    url = f"https://ntfy.sh/{topic}"
    movies = list(dict.fromkeys(map(str, movies_list)))
    seen = set()  # in-memory only
    rated, cur, running = 0, None, True

    def rem(): return [m for m in movies if m not in seen]
    def mark_seen(m):
        if m not in seen:
            seen.add(m)
    def send(m, r):
        try:
            requests.post(url, data=f"{name}|||{m}|||{r}".encode("utf-8"), timeout=3)
        except Exception:
            pass

    status = W.HTML()
    btns = [W.Button(description=str(i)) for i in range(1, 11)]
    skip = W.Button(description="Skip", button_style="warning")
    finish = W.Button(description="Finish", button_style="success")
    box = W.VBox([status, W.HBox(btns + [skip, finish])])

    def end(msg):
        nonlocal running
        running = False
        for w in btns + [skip, finish]:
            w.disabled = True
        status.value = msg

    def pick_next():
        nonlocal cur
        r = rem()
        cur = random.choice(r) if r else None
        status.value = f"<b>Rate ({rated}/{target}):</b> {cur}" if cur else ""

    def on_rate(b):
        nonlocal rated
        if not running or cur is None:
            return
        send(cur, int(b.description))
        mark_seen(cur)
        rated += 1
        if rated >= target:
            end(f"Done. Rated {rated}.")
            return
        pick_next()
        if cur is None:
            end(f"No unseen movies left. Rated {rated}.")

    def on_skip(_):
        if not running or cur is None:
            return
        mark_seen(cur)
        pick_next()
        if cur is None:
            end(f"No unseen movies left. Rated {rated}.")

    def on_finish(_):
        end(f"Finished. Rated {rated}.")

    for b in btns:
        b.on_click(on_rate)
    skip.on_click(on_skip)
    finish.on_click(on_finish)

    display(box)
    pick_next()
    if cur is None:
        end("No unseen movies to rate.")}

\code{# run this cell to provide your ratings
Widget.close_all()
start_movie_rater(target=5)}

\code{# run this cell to collect everyone's responses
Y = responses()
Y}

\subsection{Processing the Data}

\writeassignment{What is a pivot table? What does the `pandas` command `pd.pivot_table` do? Subsequently, what does `pd.melt` do?}{5}


\codeassignment{Convert the above DataFrame `Y` to a pivot table, and then back again to its current form.}{}{10}

\endif

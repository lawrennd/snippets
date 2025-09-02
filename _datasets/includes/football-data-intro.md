\ifndef{footballDataIntro}
\define{footballDataIntro}

\editme

\subsubsection{The Data}

\notes{We'll be using a partial EA FC 25 database for this workshop.}

\figure{\includepng{\diagramsDir/datasets/football-database}}{60%}{}

\notes{Find it in this GitHub repo: `radzim/football_data`}

\setupcode{import os, subprocess}

\code{repo_url = "https://github.com/radzim/football_data.git"
repo_dir = "football_data"

if not os.path.exists(repo_dir):
    subprocess.run(["git", "clone", repo_url], check=True)}

\notes{What we have:}

\code{os.listdir('football_data')}

\code{with open('football_data/models.csv') as f:
    print(f.read()[:394])}

\endif

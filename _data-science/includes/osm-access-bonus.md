\ifndef{osmAccessBonus}
\define{osmAccessBonus}

\editme

\subsection{Bonus}

\notes{If you made changes to the repository after pulling it, you might have issues getting the changes to take effect in the workbook without restarting runtime. Use the workaround below:

```
import os, subprocess, importlib, sys

def load_repo(repo):
    local = repo.split("/")[-1]
    if not os.path.exists(local):
        subprocess.run(["git", "clone", f"https://github.com/{repo}.git"], check=True)
    else:
        subprocess.run(["git", "-C", local, "pull"], check=True)
    if local not in sys.path:
        sys.path.insert(0, local)
    mod = importlib.import_module(local)
    importlib.reload(mod)
    return mod

# Use after making changes
fynesse = load_repo("TODO/fynesse_TODO")

```}
\endif

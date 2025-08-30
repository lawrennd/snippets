\ifndef{accessAssessAddress}
\define{accessAssessAddress}

\editme

\subsection{Access, Assess, Address Framework}

\notes{Over the course of this module we will end up reusing a lot of the code we create. This is on purpose, and a very important aspect of creating data science pipelines. The goal of this section is to put this idea in practice.

Have a *skim* through Neil Lawrence's article on the Access Assess Address data science framework [here](https://inverseprobability.com/talks/notes/access-assess-address-a-pipeline-for-automated-data-science.html).}

\notes{The Access-Assess-Address framework provides a systematic approach to data science projects:

- **Access**: How do we get the data? This includes APIs, web scraping, database queries, file formats, etc.
- **Assess**: How do we evaluate data quality, understand its structure, and validate our assumptions?
- **Address**: How do we answer the specific question or solve the problem at hand?}

\subsection{Applying the Framework}

\codeassignment{Using the lessons from the article, have a look at the functionality you created, and identify generalisable Access, Assess and Address functionality that could come in useful in the future.

Use git to fork this repository: https://github.com/lawrennd/fynesse_template and include your code in the `access.py`, `assess.py`, and `address.py` files.

Demonstrate this by importing your repository below and calling a couple example functions.

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

## Library

Consider creating a reusable library structure:

```python
# access.py

# assess.py  
def plot_city_map(place_name, latitude, longitude, box_size_km=2, poi_tags=None):
    # Access and visualize geographic data
    pass

def get_osm_features(latitude, longitude, box_size_km=2, tags=None):
    # Access raw OSM data
    pass

def get_feature_vector(latitude, longitude, box_size_km=2, features=None):
    # Assess and quantify geographic features
    pass

def visualize_feature_space(X, y, method='PCA'):
    # Assess data distribution and separability
    pass

# address.py
def train_location_classifier(X_train, y_train, model_type='logistic'):
    # Address classification problem
    pass

def evaluate_classifier(model, X_test, y_test):
    # Address evaluation of performance
    pass
```

This modular approach makes code reusable across different projects and enables systematic data science workflows. Each module has a clear responsibility within the overall pipeline.}{!git clone https://github.com/YOURGITHUBNAME/fynesse_mlfc.git}{30}

\setupcode{import sys
sys.path.append("/content/fynesse_mlfc")}

\notes{Once you have implemented your functions you should be able to call them to plot the city map.}

\setupcode{import fynesse}

\code{fynesse.assess.plot_city_map('Cambridge, England',  52.2053, 0.1218, 2)}


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

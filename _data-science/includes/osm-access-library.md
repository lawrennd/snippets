\ifndef{osmAccessLibrary}
\define{osmAccessLibrary}

\editme

\subsection{Library}


\notes{Consider for example, this reusable library structure:}

```python
# access.py

def get_osm_datapoints(latitude, longitude, box_size_km=2, poi_tags=None):
    # Example function for getting OSM data
    pass

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

\codeassignment{Over the course of this module we will end up reusing a lot of the code we create. This is on purpose, and a very important aspect of creating data science pipelines. The goal of this section is to put this idea in practice.

Have a *skim* through Neil Lawrence's article on the Access Assess Address data science framework [here](https://inverseprobability.com/talks/notes/access-assess-address-a-pipeline-for-automated-data-science.html).

Using the lessons from the article, have a look at the functionality you created, and identify generalisable Access, Assess and Address functionality that could come in useful in the future.

Use git to fork this repository: https://github.com/lawrennd/fynesse_template and include your code in the `access.py`, `assess.py`, and `address.py` files.

Demonstrate this by importing your repository below and calling a couple example functions.

This modular approach makes code reusable across different projects and enables systematic data science workflows. Each module has a clear responsibility within the overall pipeline.}{!git clone https://github.com/YOURGITHUBNAME/fynesse_mlfc.git #Replace YOURGITHUBNAME
import sys
sys.path.append("/content/fynesse_mlfc")}{15}

\notes{Once you have implemented your functions you should be able to call them to plot the city map.}

\setupcode{import fynesse}

\code{fynesse.assess.plot_city_map('Cambridge, England',  52.2053, 0.1218, 2)}


\endif

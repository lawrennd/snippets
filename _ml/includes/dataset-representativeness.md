\ifndef{datasetRepresentativeness}
\define{datasetRepresentativeness}

\editme

\subsection{Dataset Representativeness}

\notes{But are we sure that we're seperating for the right reasons? A brief look at the data above shows us that the England cities have a lot more OSM features in general, and that will probably be the line along which our algorithm will end up separating the data. Let's validate on a very different set of English towns.

Make sure your code in Exercise 3 handles the case when no features are found!}

\code{cities_england_3 = {
    "Corbridge, England": {"latitude": 54.9740, "longitude": -2.0180},
    "Hexworthy, England": {"latitude": 50.5400, "longitude": -3.8950},
    "Ruckland, England": {"latitude": 53.3000, "longitude": 0.0000},
    "Malmesbury, England": {"latitude": 51.5850, "longitude": -2.0980}
}

df_test_3 = build_feature_dataframe(city_dicts=[ ("England", cities_england_3)], features=features, box_size_km=1)

X_test_3 = df_test_3.drop(columns="country").fillna(0)
y_test_3 = df_test_3["country"]
y_pred_3 = clf.predict(X_test_3)
pd.Series(y_pred_3, index=X_test_3.index)}

\notes{What happens when we test on small English towns? This reveals an important issue in machine learning: **dataset representativeness**. Our model may be learning to distinguish between large, well-documented cities in Kenya versus large, well-documented cities in England, rather than learning the true cultural and geographic differences between the countries.}

\subsection{Improving the Dataset}

\notes{Based on what you found above, discuss what makes a dataset representative. What other aspects of the analysis could we improve on? Come up with a better set of English and Kenyan places to include in your training data, and improve on the analysis above to find real differences between these places as seen through openstreetmaps.}

\exercise{Consider the following questions:

1. **Sampling bias**: Are we comparing like with like? Large cities vs. small towns?
2. **Feature selection**: Are we using features that reflect genuine cultural/geographic differences?
3. **Data availability**: Does OpenStreetMap have equal coverage in both countries?
4. **Urban vs. rural**: Should we control for population size or urban development level?
5. **Economic factors**: Are we inadvertently learning to distinguish economic development levels?}

\code{# TODO: Implement improved dataset and feature selection
cities_england_new = {} # More representative sample
cities_kenya_new = {} # More representative sample  
features_new = [] # Better feature selection

# Example of more thoughtful approach:
# df_new = build_feature_dataframe(city_dicts=[("Kenya", cities_kenya_new), ("England", cities_england_new)], features=features_new, box_size_km=1)
# X_new = df_new.drop(columns="country").fillna(0)
# y_new = df_new["country"]}

\notes{A representative dataset requires careful consideration of sampling strategy, ensuring that we capture the true diversity within each class while controlling for confounding variables that might lead to spurious correlations.}

\endif

\endif

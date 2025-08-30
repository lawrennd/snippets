\ifndef{osmCityClassification}
\define{osmCityClassification}

\editme

\subsection{Dimensionality Reduction and Visualization}

\notes{Dimensionality reduction is a technique used to take data with many features and compress it into a smaller set of new features that still capture most of the important patterns. It is not covered in this practical, but it is very useful for visualising complex datasets in two or three dimensions, making it easier to spot structure, clusters, or similarities between observations. We will use it to quickly visualise the feature vectors we have.}

\setupcode{from sklearn.decomposition import PCA}

\code{pca = PCA(n_components=2)
X_proj = pca.fit_transform(X)
plt.figure(figsize=(8,6))
for country, color in [("Kenya", "green"), ("England", "blue")]:
    mask = (y == country)
    plt.scatter(X_proj[mask, 0], X_proj[mask, 1],
                label=country, color=color, s=100, alpha=0.7)

for i, city in enumerate(df.index):
    plt.text(X_proj[i,0]+0.02, X_proj[i,1], city, fontsize=8)
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.title("2D projection of feature vectors")
plt.legend()
plt.show()}

\notes{The visual separation between Kenyan and English cities makes it clear that a machine learning approach should be successful in classifying areas as either Kenya or England based on features in the area.

Try a simple classification method of your choosing (eg. linear model) below, and report the results on the test set below:}


\setupcode{from sklearn.linear_model import LogisticRegression}

\code{clf = LogisticRegression(max_iter=1000)
clf.fit(X, y)}

\subsection{Testing on New Cities}

\code{cities_kenya_2 = {
    "Nakuru, Kenya": {"latitude": -0.3031, "longitude": 36.0800},
    "Eldoret, Kenya": {"latitude": 0.5143, "longitude": 35.2698},
    "Meru, Kenya": {"latitude": 0.0463,"longitude": 37.6559},
    "Kakamega, Kenya": {"latitude": 0.2827,"longitude": 34.7519}
}
cities_england_2 = {
    "Birmingham, England": {"latitude": 52.4862, "longitude": -1.8904},
    "Manchester, England": {"latitude": 53.4808, "longitude": -2.2426},
    "Leeds, England": {"latitude": 53.8008, "longitude": -1.5491},
    "Liverpool, England": {"latitude": 53.4084, "longitude": -2.9916}
}

df_test = build_feature_dataframe(city_dicts=[("Kenya", cities_kenya_2), ("England", cities_england_2)], features=features, box_size_km=1)

X_test = df_test.drop(columns="country").fillna(0)
y_test = df_test["country"]}

\code{# TODO: Classify your test set and report results
y_pred = clf.predict(X_test)
pd.Series(y_pred, index=X_test.index)}

\notes{That probably worked!}

\endif

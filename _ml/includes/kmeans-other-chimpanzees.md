\ifndef{kmeansOtherChimpanzees}
\define{kmeansOtherChimpanzees}

\editme

\subsection{Other datasets}

\notes{Another bigger dataset of labeled chimpanzee images was published here: [paper](https://pub.inf-cv.uni-jena.de/pdf/freytag2016chimpanzee.pdf), [github](https://github.com/cvjena/chimpanzee_faces?tab=readme-ov-file).

*Alexander Freytag and Erik Rodner and Marcel Simon and Alexander Loos and Hjalmar Kühl and Joachim Denzler: "Chimpanzee Faces in the Wild: Log-Euclidean CNNs for Predicting Identities and Attributes of Primates", German Conference on Pattern Recognition (GCPR), 2016 .*}

\code{!git clone https://github.com/cvjena/chimpanzee_faces.git}

\notes{The below text file contains a description of the dataset. We're selecting only the Filename and Name, but you might use more data in other analyses. The below code converts it into a handy dataframe.}

\setupcode{import pandas as pd}

\code{ann = "chimpanzee_faces/datasets_cropped_chimpanzee_faces/data_CTai/annotations_ctai.txt" # you can also use data_CZoo
with open(ann) as f:
  recs = [{line.strip().split()[i]: line.strip().split()[i+1] for i in [0, 2]} for line in f]
df_freytag = pd.DataFrame(recs)
df_freytag}

\codeassignment{*Assess* the data, and modify it as necessary}{# TODO assess the data and modify it as necessary}{}

\notes{Let's select a subset of this, to use in our clusterings.}

\setupcode{import random
import shutil}

\code{def sample_subset(df, n, min_, max_=None, seed=42):
    if max_ is None:
      max_ = min_
    rng = random.Random(seed)
    valid = [n for n, c in df["Name"].value_counts().items() if c >= min_]
    names = rng.sample(valid, n)
    dfs = []
    for name in names:
        sub = df[df["Name"] == name]
        n = rng.randint(min_, min(max_, len(sub)))
        dfs.append(sub.sample(n, random_state=seed))
    out = pd.concat(dfs)
    return out

df_freytag_small = sample_subset(df_freytag, 10, 10) # 10 photos each for 10 chimps

gallery_freytag = "ChimpUFE/assets/gallery_freytag"
os.makedirs(gallery_freytag, exist_ok=True)
base = "chimpanzee_faces/datasets_cropped_chimpanzee_faces/data_CTai"

for _, row in df_freytag_small.iterrows():
    identity = row["Name"]
    src = os.path.join(base, row["Filename"])
    os.makedirs(os.path.join(gallery_freytag, identity), exist_ok=True)
    dst = os.path.join(gallery_freytag, identity, os.path.basename(row["Filename"]))
    shutil.copy(src, dst)

paths_freytag = [os.path.join(gallery_freytag, f, img)
         for f in sorted(os.listdir(gallery_freytag))
         for img in sorted(os.listdir(os.path.join(gallery_freytag, f)))]

df_freytag_small}

\notes{Finally, we can run the same embedding code on the new dataset.}

\code{embeddings_freytag = make_embeddings('./assets/gallery_freytag')}

\code{embeddings_freytag_2d = PCA(n_components=2).fit_transform(embeddings_freytag)}

\code{X2, history_freytag_e2d = iterative_kmeans_widget(embeddings_freytag_2d, paths_freytag, n_clusters=10, random_state=42)}

\code{classes_freytag = df_freytag_small['Name'].values
performance_stats(history_freytag_e2d, classes_freytag)}

\notes{The adjusted Rand index tells us that our approach worked on the new dataset!}

\endif

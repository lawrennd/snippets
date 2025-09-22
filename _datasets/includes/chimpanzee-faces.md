\ifndef{chimpanzeeFaces}
\define{chimpanzeeFaces}

\editme

\subsection{Chimpanzee Faces}

\notes{We know that human faces are unique to each of us. But did you know that chimpanzees also have unique faces?

We will be checking if different images of the same chimpanzee would naturally cluster together. Using a sample set of 25 photos of 5 chimpanzees from [Iashin et al., 2025](https://arxiv.org/abs/2507.10552), let's see if we are able to cluster the dataset.

Let's download the photos (and other code we will need later). The [ChimpUFE](https://github.com/v-iashin/ChimpUFE) repo was created by Iashin et al. We will also be using their pre-trained neural networks for creating embeddings of the chimp's faces.

*Iashin, Vladimir, et al. "Self-supervised Learning on Camera Trap Footage Yields a Strong Universal Face Embedder." arXiv preprint arXiv:2507.10552 (2025).*}

\setupcode{#these files are quite large and take a couple minutes to download
!git clone https://github.com/v-iashin/ChimpUFE.git
!cd ChimpUFE && pip install -r requirements.txt
!wget -P ./ChimpUFE/assets/weights https://github.com/v-iashin/ChimpUFE/releases/download/v1.0/25-06-06T20-51-36_330k.pth}

\notes{This is what the chimps look like:}

\setupplotcode{import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg}

\plotcode{gallery = "./ChimpUFE/assets/gallery"
folders = sorted(os.listdir(gallery))

fig, axes = plt.subplots(len(folders), 5, figsize=(10, 2*len(folders)))
for i, f in enumerate(folders):
    imgs = sorted(os.listdir(os.path.join(gallery, f)))[:5]
    for j, img in enumerate(imgs):
        ax = axes[i, j]
        ax.imshow(mpimg.imread(os.path.join(gallery, f, img)))
        ax.axis("off")
        if j == 0:
            ax.text(-0.02, 0.5, f, transform=ax.transAxes, ha="right", va="center", fontsize=10)

plt.subplots_adjust(left=0.18, wspace=0.3, hspace=0.05)}



\endif

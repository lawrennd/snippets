\ifndef{highDimensionalData}
\define{highDimensionalData}

\editme

\subsection{High Dimensional Data}

\slides{* USPS Data Set Handwritten Digit
* 3648 dimensions (64 rows, 57 columns)
* Space contains much more than just this digit.}

\notes{To introduce how to think about high dimensional data, we will first of all introduce a hand written digit from the U.S. Postal Service handwritten digit data set (originally collected from scanning enveolopes) and used in the first convolutional neural network paper [@LeCun:zip89].}

\notes{@LeCun:zip89 downscaled the images to $16 \times 16$, here we use an image at the original scale, containing 64 rows and 57 columns. Since the pixels are binary, and the number of dimensions is 3,648, this space contains $2^{3,648}$ possible images. So this space contains a lot more than just one digit.}


\subsection{USPS Samples}

\notes{If we sample from this space, taking each pixel independently from a probability which is given by the number of pixels which are 'on' in the original image, over the total number of pixels, we see images that look nothing like the original digit.}


\setupplotcode{import matplotlib.pyplot as plt
import numpy as np
import mlai
import pods}
\plotcode{fig, ax = plt.subplots(figsize=(5,5))

pods.access.download_url("https://github.com/lawrennd/slides/raw/gh-pages/diagrams/ml/br1561_6.3.pgm",
                         store_directory="\writeDiagramsDir/ml")
six_image = mlai.load_pgm("br1561_6.3.pgm", directory ="\writeDiagramsDir/ml")
rows = six_image.shape[0]
cols = six_image.shape[1]
      
ax.imshow(six_image,interpolation='none').set_cmap('gray')
mlai.write_figure("dem_six000.png", directory="\writeDiagramsDir/dimred/")
for i in range(3):
    rand_image = np.random.rand(rows, cols)<((six_image>0).sum()/float(rows*cols))
    ax.imshow(rand_image,interpolation='none').set_cmap('gray')
    mlai.write_figure('dem_six{i:0>3}.png'.format(i=i+1), directory="\writeDiagramsDir/dimred/")}

\setupdisplaycode{from ipywidgets import IntSlider
import notutils as nu}
\displaycode{nu.display_plots('dem_six{counter:0>3}.png', directory='\writeDiagramsDir/dimred', counter=IntSlider(0, 0, 3, 1))}


\slides{\define{width}{50%}
\startanimation{dem-six-sample}{0}{4}{Six Samples}
\newframe{\includepng{\diagramsDir/dimred/dem_six000}{\width}}{dem-six-sample}
\newframe{\includepng{\diagramsDir/dimred/dem_six001}{\width}}{dem-six-sample}
\newframe{\includepng{\diagramsDir/dimred/dem_six002}{\width}}{dem-six-sample}
\newframe{\includepng{\diagramsDir/dimred/dem_six003}{\width}}{dem-six-sample}
\endanimation}

\notes{\figure{\threeColumns{\includepng{\diagramsDir/dimred/dem_six000}{100%}}{\includepng{\diagramsDir/dimred/dem_six001}{100%}}{\includepng{\diagramsDir/dimred/dem_six002}{100%}}{30%}{30%}{30%}}{Even if we sample every nano second from now until the end of the universe we won't see the original six again.}{dem-six-sample}}


\subsection{Simple Model of Digit}

\notes{An independent pixel model for this digit doesn't seem sensible. The total space is enormous, and yet the space occupied by the type of data we're interested in is relatively small.}

\subsection{Probability of Random Image Generation}

\notes{Let's consider a simple model for handwritten 6s. We model each pixel independently with a binomial distribution. Each pixel is the result of a single binomial trial, known as a Bernoulli distribution.
$$
p(\dataVector) = \prod_{j=1}^\dataDim \binomProb^{\dataScalar_j}
(1-\binomProb)^{(1-\dataScalar_j)},
$$
where the probability across pixels are taken to be independent and
are governed by the same probability of being on, $\binomProb$. The
maximum likelihood solution for this parameter is given by the number
of pixels that are on in the data point divided by the total number
of pixels
$$
\binomProb = \frac{849}{3,648}.
$$
The probability of recovering the original six in any given sample is
then given by
$$
p(\dataVector=\text{given\,image}) = \binomProb^{849}(1-\binomProb)^{3,648 - 849
}=2.67\times10^{-860}.
$$}

\slides{
* Independent pixel model
  * Each pixel modeled as independent binomial trial
  * Probability of pixel being "on"$$\binomProb = \frac{849}{3,648} \approx 0.233$$
* Probability of original image
  $$p(\text{original six}) = \binomProb^{849}(1-\binomProb)^{2799} = 2.67 \times 10^{-860}
  $$
}
  
\newslide{Probability of Random Image Generation}
\slides{
* This is astronomically small!
* Even sampling every nanosecond until end of universe won't find it}

\notes{This demonstrates why independent pixel models are inadequate for high-dimensional data. The probability of generating the original image by random sampling is so small ($2.67 \times 10^{-860}$) that it's effectively impossible. This highlights the need for more sophisticated models that capture the underlying structure and dependencies in the data.}

\notes{Consider a different type of model. One where we take a prototype six and we rotate it left and right to create new data.}

\installcode{scikit-image}
\setupcode{from skimage.transform import rotate
import numpy as np
import mlai}

\code{# Load in the six
six_image = mlai.load_pgm('br1561_6.3.pgm', directory ='\writeDiagramsDir/ml')/255.0

# Pad out to 64 columns
rows = six_image.shape[0]
six_image = np.hstack([np.ones((rows, 3)), six_image, np.ones((rows, 4))])
dim_one = np.asarray(six_image.shape)
angles = range(360)
Y = np.zeros((len(angles), np.prod(dim_one)))
for i, angle in enumerate(angles):
    rot_image = rotate(six_image, angle, cval=1.0)
    dim_two = np.asarray(rot_image.shape)
    start = [int(round((dim_two[0] - dim_one[0])/2)), int(round((dim_two[1] - dim_one[1])/2))]
    crop_image = rot_image[start[0]+np.array(range(dim_one[0])), :][:, start[1]+np.array(range(dim_one[1]))]
    Y[i, :] = crop_image.flatten()
}
\plotcode{fig, ax = plt.subplots(figsize=plot.big_figsize)

show_angles = [31, 11, 350, 330, 310, 290]
for i, angle in enumerate(show_angles):
    ax.imshow(np.reshape(Y[angle, :], dim_one),interpolation='none').set_cmap('gray')
	ax.set_xticks(range(dim_one[1]), minor=True)  # Every column
	ax.set_yticks(range(dim_one[0]), minor=True)  # Every row
	ax.grid(True, which='minor', alpha=0.5, linewidth=0.1)
    ax.tick_params(which='minor', size=0)  
    ax.tick_params(which='major', size=0)  
	ax.tick_params(labelbottom=False, labelleft=False)	
	
    mlai.write_figure(f"six_rotate{i:0>3}.svg", directory="\writeDiagramsDir/dimred/")}

\newslide{Rotate a Prototype}

\setupdisplaycode{import notutils as nu}
\displaycode{nu.display_plots('six_rotate{counter:0>3}.svg', directory='\writeDiagramsDir/dimred', counter=(0, 5))}

\slides{\define{width}{50%}
\startanimation{six-rotate}{1}{5}{Rotate Prototype}
\newframe{\includediagram{\diagramsDir/dimred/six_rotate000}{\width}}{six-rotate}
\newframe{\includediagram{\diagramsDir/dimred/six_rotate001}{\width}}{six-rotate}
\newframe{\includediagram{\diagramsDir/dimred/six_rotate002}{\width}}{six-rotate}
\newframe{\includediagram{\diagramsDir/dimred/six_rotate003}{\width}}{six-rotate}
\newframe{\includediagram{\diagramsDir/dimred/six_rotate004}{\width}}{six-rotate}
\newframe{\includediagram{\diagramsDir/dimred/six_rotate005}{\width}}{six-rotate}
\endanimation}

\notes{\figure{\threeColumns{\includediagram{\diagramsDir/dimred/six_rotate001}{100%}}{\includediagram{\diagramsDir/dimred/six_rotate003}{100%}}{\includepng{\diagramsDir/dimred/six_rotate005}{100%}}{30%}{30%}{30%}}{Rotate a prototype six to form a set of plausible sixes.}{six-rotate-summary}}


\subsection{PCA of Rotated Sixes}

\notes{Now let's perform PCA on the rotated sixes to see how the data projects into a lower dimensional space. The rotated data should lie approximately on a one-dimensional manifold corresponding to the rotation angle.}

\setupcode{import numpy as np}
\code{# Center the data
Y_centered = Y - np.mean(Y, axis=0)

# SVD of the centered data matrix (360 x 3648)
U, s, Vt = np.linalg.svd(Y_centered, full_matrices=False)

# Eigenvalues are s^2 / n 
eigenvalues = s**2 / Y.shape[0]

# Project data onto principal components
# Standard approach: X = U @ diag(s) gives the projections
X = U @ np.diag(s)}

\code{def plot_pca_manifold(X, Y, dims, filename, show_every=20, angle_ranges=None, colors=None):
    """Plot PCA manifold with optional angle range filtering"""
    fig, ax = plt.subplots(figsize=plot.big_figsize)
    h_points = ax.plot(X[:, 0], X[:, 1], 'rx', linewidth=2, alpha=0.7)[0]
    show_indices = range(0, len(X), show_every)  # Every 20 degrees
    if angle_ranges is None:
        # Plot all points
        show_indices = range(0, len(X), show_every)  # Every 20 degrees
    else:
        # Plot specific angle ranges
        h_points.set_data([], [])
        for i, (start, end, color) in enumerate(zip(angle_ranges['starts'], 
                                                   angle_ranges['ends'], 
                                                   colors or ['r', 'b'])):
            mask = (np.arange(len(X)) >= start) & (np.arange(len(X)) < end)
            ax.plot(X[mask, 0], X[mask, 1], f'{color}x', linewidth=2, alpha=0.7)
        
        # Show images only in specified ranges
        orig_show = show_indices
        show_indices = []
        for start, end in zip(angle_ranges['starts'], angle_ranges['ends']):
            for ind in orig_show:
                if ind >= start and ind <= end:
                    show_indices.append(ind)
    
    # Add small image insets
    for i in show_indices:
        if i < len(X):
            ax.scatter(X[i, 0], X[i, 1], s=50)
            
            # Calculate position for small image
            x_pos, y_pos = X[i, 0], X[i, 1]
            
            # Get plot limits and convert to figure coordinates
            x_min, x_max = ax.get_xlim()
            y_min, y_max = ax.get_ylim()
            
            x_fig = 0.1 + 0.8 * (x_pos - x_min) / (x_max - x_min)
            y_fig = 0.1 + 0.8 * (y_pos - y_min) / (y_max - y_min)
            
            inset_ax = fig.add_axes([x_fig, y_fig, 0.05, 0.05])
            rotated_img = Y[i, :].reshape(dims)
            inset_ax.imshow(rotated_img, cmap='gray')
            inset_ax.axis('off')
    
    ax.grid(True, alpha=0.3)
    
    mlai.write_figure(filename, directory='\writeDiagramsDir/dimred/')
    return fig, ax}

\plotcode{fig, ax = plot_pca_manifold(X, Y, dim_one, 'six_manifold_001.svg')}

\figure{\includediagram{\diagramsDir/dimred/six_manifold_001}{60%}}{The rotated sixes projected onto the first two principal components. The data lives on a one-dimensional manifold in the high-dimensional space, forming approximately a circle in the 2D projection.}{six-manifold-001}

\newslide{}

\plotcode{fig, ax = plot_pca_manifold(X, Y, dim_one, 'six_manifold_002.svg',
                                    angle_ranges={'starts': [0, 135, 315], 'ends': [45, 225, 360]},
                                    colors=['r', 'b', 'r'])}

\figure{\includediagram{\diagramsDir/dimred/six_manifold_002}{60%}}{The rotated sixes projected onto the first two principal components as sixes and nines. The six and nine data live on two separate one-dimensional manifolds in the high-dimensional space, forming two arcs from a  circle in the 2D projection.}{six-manifold-002}

\subsection{Interpoint Distances for Rotated Sixes}

\notes{In this section we take all 360 examples of the rotated digits and analyze their interpoint distances. The data set is inherently one dimensional, with the dimension associated with the rotation transformation. A pure rotation would lead to a pure circle in the projected space. In practice, rotation of images requires some interpolation and this leads to small corruptions of the latent projections away from the circle.}

\setupplotcode{import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import mlai
import mlai.plot as plot}

\code{# Calculate variance of each dimension
varY = np.var(Y, axis=0)
# Sort by variance in descending order
sorted_indices = np.argsort(varY)[::-1]
# Take top q dimensions (e.g., q=50 for dimensionality reduction)
q = 50
order = sorted_indices[:q]

# Calculate interpoint distances for selected dimensions
Y_selected = Y[:, order]
# Compute squared distances between all pairs
distMat = np.zeros((Y.shape[0], Y.shape[0]))
for i in range(Y.shape[0]):
    for j in range(Y.shape[0]):
        distMat[i, j] = np.sum((Y_selected[i, :] - Y_selected[j, :])**2) / q

# Calculate error term
e = 2 * np.sum(varY[sorted_indices[q:]]) / Y.shape[1]}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_figsize)

# Create heatmap of interpoint distances
im = ax.imshow(distMat, cmap='RdBu_r', aspect='equal', origin='upper', 
               extent=[0, 360, 360, 0])  # extent: [left, right, bottom, top]
ax.set_xticks([0, 90, 180, 270, 360])
ax.set_yticks([0, 90, 180, 270, 360])
ax.set_xlabel('Rotation Angle (degrees)')
ax.set_ylabel('Rotation Angle (degrees)')

# Add colorbar
cbar = plt.colorbar(im, ax=ax)
cbar.set_label('Squared Distance')

mlai.write_figure('dem-six-distances-360.svg', directory='\writeDiagramsDir/dimred/')}

\figure{\includediagram{\diagramsDir/dimred/dem-six-distances-360}{60%}}{Inter-point squared distances for the rotated digits data. Much of the data structure can be seen in the matrix. All points are ordered by angle of rotation. We can see that the distance between two points with similar angle of rotation is small (note in the upper right and lower left corners the low distances associated with 6s rotated by roughly 360 degrees and unrotated 6s).}{six-distances-360}


\setupplotcode{import mlai.plot}
\plotcode{plot.squared_distances(Y, 'rotated-sixes', 'Rotated sixes', directory='\writeDiagramsDir/dimred')}

\figure{\includediagram{\diagramsDir/dimred/rotated-sixes_squared-distances}{60%}}{Hisgogram of squared distances vs theory for the rotated sixes.}{rotated-sixes-squared-distances}

\subsection{Low Dimensional Manifolds}

\slides{* Pure rotation is too simple
  * In practice data may undergo several distortions.
* For high dimensional data with *structure*:
  * We expect fewer distortions than dimensions;
  * Therefore we expect the data to live on a lower dimensional manifold.
  * Conclusion: Deal with high dimensional data by looking for a lower dimensional non-linear embedding.}
  
\notes{Of course, in practice pure rotation of the image is too simple a model. Digits can undergo several distortions and retain their nature. For example, they can be scaled, they can go through translation, they can udnergo 'thinning'. But, for data with 'structure' we expect fewer of these distortions than the dimension of the data. This means we expect data to live on a lower dimensonal manifold. This implies that we should deal with high dimensional data by looking for a lower dimensional (non-linear) embedding.}

\endif

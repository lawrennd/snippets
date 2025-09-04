\ifndef{mnistDigitsPlot}
\define{mnistDigitsPlot}

\editme

\subsection{MNIST Digit Examples}

\setupplotcode{import mlai
import mlai.plot as plot
import matplotlib.pyplot as plt}

\plotcode{# Visualize examples of each digit
fig, axes = plt.subplots(5, 5, figsize=plot.big_figsize)

for digit in digits:
    # Get indices for this digit
    digit_indices = np.where(labels == digit)[0]
    
    # Show first 5 examples of this digit
    for i in range(5):
        row = int(digit)
        col = i
        
        # Reshape 784-dim vector back to 28x28 image
        image = Y[digit_indices[i]].reshape(28, 28)
        
        axes[row, col].imshow(image, cmap='gray')
        axes[row, col].axis('off')

plt.tight_layout()
mlai.write_figure("mnist-digits-subsample-examples.svg", directory="\writeDiagramsDir/datasets")}

\newslide{MNIST Digits}

\figure{\includediagram{\diagramsDir/datasets/mnist-digits-subsample-examples}{60%}}{Examples of MNIST digits 0-4 from our subsampled dataset, showing 5 examples of each digit.}{mnist-digits-subsample-examples}

\notes{The visualization shows the variety in handwritten digits even within the same class. Each row represents a different digit (0 through 4), and each column shows a different example of that digit. }

\endif

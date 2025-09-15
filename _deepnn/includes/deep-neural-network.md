\ifndef{deepNeuralNetwork}
\define{deepNeuralNetwork}

\editme

\subsection{Deep Neural Network}

\installcode{daft}

\setupplotcode{import matplotlib
# Comment for google colab (no latex available)
matplotlib.rc('text', usetex=True)
matplotlib.rcParams['text.latex.preamble']=[r"\usepackage{amsmath}"]}

\setupplotcode{import mlai.plot as plot}
\plotcode{def deep_nn(diagrams='../diagrams'):
    """Draw a deep neural network."""
    model = plot.network()
    model.add_layer(layer(width=6, label='\inputScalar_{index}',
                    observed=True, text=r'given $\inputVector$'))
    model.add_layer(layer(width=8, label='\hiddenScalar_{{1, {index}}}',
                    text=r'$\hiddenScalarVector_1=\basisVector\left(\mappingMatrix_1\inputVector\right)$'.replace('\', '\\')))
    model.add_layer(layer(width=6, label='\hiddenScalar_{{2, {index}}}',
                    text=r'$\hiddenScalarVector_2=\basisVector\left(\mappingMatrix_2\hiddenScalarVector_1\right)$'.replace('\', '\\')))
    model.add_layer(layer(width=4, label='\hiddenScalar_{{3, {index}}}',
                    text=r'$\hiddenScalarVector_3=\basisVector\left(\mappingMatrix_3\hiddenScalarVector_2\right)$'.replace('\', '\\')))
    model.add_layer(layer(width=1, label='\dataScalar',
                    text=r'$\dataScalar=\mappingVector_4^\top\hiddenScalarVector_3$'.repalce('\', '\\'),
                    observed=True))
    fig, ax = model.draw()
    ma.write_figure('deep-neural-network.svg',
                      directory=diagrams,
                      figure=fig,
                      transparent=True)

    new_text = ['', '', '', '', '']
    for i, text in enumerate(new_text):
        model.layers[i].text=text
    fig, ax = model.draw()
    ma.write_figure('deep-neural-network.svg',
                      directory="\writeDiagramsDir/deepnn',
                      figure=fig,
                      transparent=True)}

\slides{\includediagram{\diagramsDir/deepnn/deep-neural-network}{50%}}

\newslide{Deep Neural Network}

\slides{\includediagram{\diagramsDir/deepgp/deep-nn2}{50%}}

\notes{\figure{\includediagram{\diagramsDir/deepgp/deep-nn2}{70%}}{A deep neural network. Input nodes are shown at the bottom. Each hidden layer is the result of applying an affine transformation to the previous layer and placing through an activation function.}{deep-neural-network}}

\newslide{Mathematically}

\notes{Mathematically, each layer of a neural network is given through computing the activation function, $\basisFunction(\cdot)$, contingent on the previous layer, or the inputs. In this way the activation functions, are composed to generate more complex interactions than would be possible with any single layer.}
$$
\begin{align*}
    \hiddenVector_{1} &= \basisFunction\left(\mappingMatrix_1 \inputVector\right)\\
    \hiddenVector_{2} &=  \basisFunction\left(\mappingMatrix_2\hiddenVector_{1}\right)\\
    \hiddenVector_{3} &= \basisFunction\left(\mappingMatrix_3 \hiddenVector_{2}\right)\\
    \mappingFunction &= \mappingVector_4 ^\top\hiddenVector_{3}
\end{align*}
$$

\endif

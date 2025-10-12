\ifndef{chainRuleCnnLayered}
\define{chainRuleCnnLayered}

\editme

\subsection{Chain Rule for Layered CNN Architecture}

\newslide{CNN Chain Rule Overview}

\slides{* **Layered Architecture**: Each layer implements `forward()`, `backward()`, `parameters`
* **Spatial Operations**: Convolution, pooling, flattening require specialized gradients
* **Composition**: CNN built by composing `ConvolutionalLayer`, `MaxPoolingLayer`, `FlattenLayer`
* **Gradient Flow**: Each layer computes its own gradients independently
* **Verification**: Finite difference testing ensures mathematical correctness}

\notes{Our layered CNN architecture provides a clean separation of concerns where each layer type has its own gradient computation. This makes the chain rule more modular and easier to understand than traditional CNN implementations.}

\newslide{CNN Layer Types and Their Gradients}

\slides{* **ConvolutionalLayer**: $\frac{\partial \lossFunction}{\partial \inputMatrix}$, $\frac{\partial \lossFunction}{\partial \filters}$, $\frac{\partial \lossFunction}{\partial \biases}$
* **MaxPoolingLayer**: $\frac{\partial \lossFunction}{\partial \inputMatrix}$ (no parameters)
* **FlattenLayer**: $\frac{\partial \lossFunction}{\partial \inputMatrix}$ (no parameters)
* **FullyConnectedLayer**: Standard neural network gradients
* **LinearLayer**: Linear transformation gradients}

\notes{Each layer type in our CNN architecture has specific gradient computations. The convolutional layer is the most complex, requiring gradients for filters, biases, and input. Pooling and flattening layers are simpler but still require careful handling of spatial dimensions.}

\newslide{Convolutional Layer Forward Pass}

\slides{* **Input**: $\inputMatrix$ of shape $(B, C_{in}, H, W)$
* **Filters**: $\filters$ of shape $(C_{out}, C_{in}, K_h, K_w)$
* **Output**: $\outputMatrix$ of shape $(B, C_{out}, H_{out}, W_{out})$
* **Operation**: $\outputMatrix[b,c,h,w] = \sum_{i,j,k} \inputMatrix[b,k,h+i,w+j] \cdot \filters[c,k,i,j] + \biases[c]$}

\notes{The convolutional forward pass applies filters across the input image, computing dot products between filter weights and local image regions. This creates feature maps that detect specific patterns in the input.}

\newslide{Convolutional Layer Backward Pass}

\slides{* **Output gradient**: $\frac{\partial \lossFunction}{\partial \outputMatrix}$ from next layer
* **Filter gradient**: $\frac{\partial \lossFunction}{\partial \filters[c,k,i,j]} = \sum_{b,h,w} \frac{\partial \lossFunction}{\partial \outputMatrix[b,c,h,w]} \cdot \inputMatrix[b,k,h+i,w+j]$
* **Bias gradient**: $\frac{\partial \lossFunction}{\partial \biases[c]} = \sum_{b,h,w} \frac{\partial \lossFunction}{\partial \outputMatrix[b,c,h,w]}$
* **Input gradient**: $\frac{\partial \lossFunction}{\partial \inputMatrix[b,k,h,w]} = \sum_{c,i,j} \frac{\partial \lossFunction}{\partial \outputMatrix[b,c,h-i,w-j]} \cdot \filters[c,k,i,j]$}

\notes{The convolutional backward pass requires careful indexing to ensure gradients flow correctly through the spatial dimensions. The filter gradient accumulates contributions from all spatial locations where the filter was applied.}

\newslide{Max Pooling Layer Gradients}

\slides{* **Forward**: $\outputMatrix[b,c,h,w] = \max_{i,j \in \poolRegion} \inputMatrix[b,c,h \cdot \stride + i, w \cdot \stride + j]$
* **Backward**: $\frac{\partial \lossFunction}{\partial \inputMatrix[b,c,h,w]} = \begin{cases} 
\frac{\partial \lossFunction}{\partial \outputMatrix[b,c,h_{out},w_{out}]} & \text{if } (h,w) \text{ was the max in pool region} \\
0 & \text{otherwise}
\end{cases}$}

\notes{Max pooling gradients are sparse - only the maximum positions in each pooling region receive gradients. This creates a natural form of attention where only the most important features contribute to the gradient flow.}

\newslide{Flatten Layer Gradients}

\slides{* **Forward**: $\outputMatrix = \inputMatrix.reshape(B, -1)$
* **Backward**: $\frac{\partial \lossFunction}{\partial \inputMatrix} = \frac{\partial \lossFunction}{\partial \outputMatrix}.reshape(\inputShape)$}

\notes{The flatten layer simply reshapes the gradient to match the input shape. This is a straightforward operation but crucial for connecting convolutional layers to fully connected layers.}

\newslide{CNN Chain Rule Implementation}

\slides{* **Layer-wise**: Each layer computes its own gradients independently
* **Composition**: `LayeredNeuralNetwork` coordinates gradient flow between layers
* **Spatial awareness**: Gradients preserve spatial structure through convolution
* **Parameter updates**: Each layer manages its own parameter gradients}

\notes{Our implementation uses a layered approach where each layer is responsible for its own gradient computation. The `LayeredNeuralNetwork` coordinates the flow of gradients between layers, ensuring that spatial information is preserved correctly.}

\newslide{Multi-Path Gradient Flow in CNNs}

\slides{* **Convolutional path**: $\inputMatrix \rightarrow \convOutput \rightarrow \poolOutput \rightarrow \flattenOutput$
* **Parameter paths**: $\filters \rightarrow \convOutput$, $\biases \rightarrow \convOutput$
* **Spatial paths**: Each spatial location has independent gradient flow
* **Channel paths**: Each output channel has independent gradient computation}

\notes{CNNs have more complex gradient flow than standard neural networks because of the spatial structure. Each spatial location and channel can have independent gradients, creating a rich gradient landscape.}

\newslide{Activation Function Integration}

\slides{* **ReLU in convolution**: $\frac{\partial \lossFunction}{\partial \convOutput} = \frac{\partial \lossFunction}{\partial \activationOutput} \odot \frac{\partial \activationFunction}{\partial \convOutput}$
* **ReLU gradient**: $\frac{\partial \reluFunction}{\partial x} = \begin{cases} 1 & \text{if } x > 0 \\ 0 & \text{if } x \leq 0 \end{cases}$
* **Spatial activation**: Applied element-wise across all spatial locations}

\notes{Activation functions in CNNs are applied element-wise across all spatial locations and channels. The ReLU activation creates sparse gradients where only positive activations contribute to the gradient flow.}

\newslide{CNN Gradient Verification}

\slides{* **Finite differences**: Compare analytical vs numerical gradients
* **Spatial testing**: Verify gradients at different spatial locations
* **Channel testing**: Verify gradients for different output channels
* **End-to-end testing**: Verify complete CNN gradient flow}

\notes{Our implementation includes comprehensive gradient testing using finite differences. This ensures that the complex spatial gradient computations are mathematically correct.}

\newslide{Layered CNN Architecture Benefits}

\slides{* **Modularity**: Each layer type has clear gradient responsibilities
* **Testability**: Each layer can be tested independently
* **Composability**: Layers can be combined in any order
* **Educational**: Clear separation makes learning easier
* **Maintainability**: Easy to add new layer types}

\notes{The layered architecture makes CNN gradients much more manageable. Students can understand each component in isolation before seeing how they compose together. This is a significant advantage over monolithic CNN implementations.}

\newslide{Complete CNN Gradient Flow}

\slides{* **Input**: $\inputMatrix$ (batch of images)
* **Convolution**: $\convOutput = \reluFunction(\convolution(\inputMatrix, \filters) + \biases)$
* **Pooling**: $\poolOutput = \maxPool(\convOutput)$
* **Flatten**: $\flattenOutput = \flatten(\poolOutput)$
* **Dense**: $\denseOutput = \reluFunction(\denseOutput \cdot \denseWeights + \denseBiases)$
* **Output**: $\outputMatrix = \denseOutput \cdot \outputWeights + \outputBiases$}

\notes{The complete CNN forward pass shows how different layer types compose together. Each layer transforms the data in a specific way, and the gradients must flow back through each transformation correctly.}

\newslide{CNN Gradient Chain Rule}

\slides{* **Output to dense**: $\frac{\partial \lossFunction}{\partial \denseOutput} = \frac{\partial \lossFunction}{\partial \outputMatrix} \cdot \outputWeights^\top$
* **Dense to flatten**: $\frac{\partial \lossFunction}{\partial \flattenOutput} = \frac{\partial \lossFunction}{\partial \denseOutput} \cdot \denseWeights^\top$
* **Flatten to pool**: $\frac{\partial \lossFunction}{\partial \poolOutput} = \frac{\partial \lossFunction}{\partial \flattenOutput}.reshape(\poolShape)$
* **Pool to conv**: $\frac{\partial \lossFunction}{\partial \convOutput} = \maxPoolGradient(\frac{\partial \lossFunction}{\partial \poolOutput})$
* **Conv to input**: $\frac{\partial \lossFunction}{\partial \inputMatrix} = \convolutionGradient(\frac{\partial \lossFunction}{\partial \convOutput}, \filters)$}

\notes{The CNN chain rule shows how gradients flow back through each layer type. Each layer implements its own gradient computation, and the `LayeredNeuralNetwork` coordinates the flow between layers.}

\newslide{Parameter Gradients in CNNs}

\slides{* **Filter gradients**: $\frac{\partial \lossFunction}{\partial \filters} = \sum_{b,h,w} \frac{\partial \lossFunction}{\partial \convOutput[b,c,h,w]} \cdot \inputMatrix[b,k,h+i,w+j]$
* **Bias gradients**: $\frac{\partial \lossFunction}{\partial \biases} = \sum_{b,h,w} \frac{\partial \lossFunction}{\partial \convOutput[b,c,h,w]}$
* **Dense gradients**: Standard neural network parameter gradients
* **Output gradients**: Final layer parameter gradients}

\notes{Parameter gradients in CNNs include the specialized convolutional gradients for filters and biases, plus the standard gradients for fully connected layers. The convolutional gradients require spatial accumulation across all locations where each filter was applied.}

\newslide{Implementation Verification}

\slides{* **Layer testing**: Each layer tested independently with finite differences
* **Composition testing**: Complete CNN tested end-to-end
* **Spatial testing**: Gradients verified at different spatial locations
* **Channel testing**: Gradients verified for different output channels
* **Parameter testing**: All parameter gradients verified numerically}

\notes{Our implementation includes comprehensive testing that verifies the mathematical correctness of all gradient computations. This ensures that the complex spatial gradient flow is implemented correctly.}

\newslide{Educational Benefits}

\slides{* **Clear separation**: Each layer type has distinct gradient responsibilities
* **Modular learning**: Students can understand each component independently
* **Visual debugging**: Easy to see where gradients flow and where they don't
* **Mathematical rigor**: All gradients verified with finite differences
* **Practical implementation**: Code directly maps to mathematical theory}

\notes{The layered CNN architecture makes the chain rule much more accessible to students. They can see exactly how each layer type contributes to the overall gradient computation, and the modular design makes it easy to understand the complete system.}

\newslide{Summary}

\slides{* **Layered design**: Each CNN layer type has specialized gradient computation
* **Spatial awareness**: Gradients preserve spatial structure through convolution
* **Modular testing**: Each layer can be verified independently
* **Educational clarity**: Clear separation of concerns makes learning easier
* **Mathematical rigor**: All gradients verified with finite differences
* **Practical implementation**: Code directly implements the mathematical theory}

\notes{The layered CNN architecture provides a clean, educational approach to understanding convolutional neural network gradients. Each layer type has clear responsibilities, and the modular design makes it easy to understand how the complete system works. The comprehensive testing ensures mathematical correctness while the clear separation of concerns makes the learning process much more accessible.}

\newslide{Code Mapping}

\slides{* **ConvolutionalLayer**: Implements spatial convolution with filter and bias gradients
* **MaxPoolingLayer**: Implements max pooling with sparse gradient distribution
* **FlattenLayer**: Implements spatial-to-vector conversion with shape preservation
* **LayeredNeuralNetwork**: Coordinates gradient flow between all layer types
* **Gradient testing**: Comprehensive finite difference verification}

\notes{Students can directly map the mathematical theory to our implementation. Each layer class implements the specific gradient computations described in the chain rule, and the `LayeredNeuralNetwork` coordinates the flow between layers. The comprehensive testing ensures that the implementation matches the mathematical theory exactly.}

\newslide{Verification with Our Implementation}

\slides{* **Gradient testing**: Use `finite_difference_gradient` to verify analytical gradients
* **Spatial verification**: Check gradients at different spatial locations
* **Channel verification**: Verify gradients for different output channels
* **End-to-end testing**: Complete CNN gradient flow verification
* **Parameter testing**: All parameter gradients verified numerically}

\notes{Students can verify the chain rule implementation using our comprehensive gradient testing framework. The tests in `test_convolutional_layers.py` and `test_neural_networks.py` demonstrate how to use finite differences to verify that our analytical gradients match the mathematical theory for CNNs.}

\endif

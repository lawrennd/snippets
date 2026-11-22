\ifndef{chainRuleCnnLayered}
\define{chainRuleCnnLayered}

\editme

\subsection{Chain Rule for Layered CNN Architecture}

\newslide{Why Convolution?}

\slides{* **Locality**: each output depends on a small $K_h \times K_w$ patch of the input
* **Weight sharing**: the same filter is applied at every position
* **Equivariance**: shifting the input shifts the feature map
* **Parameters**: $C_{out} C_{in} K_h K_w$, independent of image size}

\notes{A fully connected layer applied to an image treats every pixel as unrelated to its neighbours and needs a separate weight for every input-output pair. Convolutional layers build in two assumptions about images. The first is *locality*: useful features, such as edges, depend on small neighbourhoods of pixels. The second is *weight sharing*: a feature detector that is useful in one part of the image is useful everywhere. Applying the same small filter at every position gives a layer whose number of parameters does not depend on the image size, and whose output shifts when the input shifts (translation equivariance). Pooling then adds some invariance to small shifts.}

\newslide{CNN Chain Rule Overview}

\slides{* **Layered architecture**: each layer implements `forward()`, `backward()`, `parameters`, `gradients`
* **Spatial operations**: convolution, pooling and flattening need their own gradients
* **Composition**: `ConvolutionalLayer`, `MaxPoolingLayer`, `FlattenLayer`, `FullyConnectedLayer`, `LinearLayer`
* **Chain rule**: each layer maps $\frac{\partial \lossFunction}{\partial \text{output}}$ to $\frac{\partial \lossFunction}{\partial \text{input}}$ and its parameter gradients}

\notes{In the layered implementation each layer is responsible for two things in its backward pass. It converts the gradient of the loss with respect to its output into the gradient with respect to its input, which is passed to the previous layer. And it computes the gradient of the loss with respect to its own parameters. `LayeredNeuralNetwork` calls the layers' backward passes in reverse order and collects the parameter gradients.}

\newslide{Convolutional Layer Forward Pass}

\slides{* **Input**: $\inputMatrix$ of shape $(B, C_{in}, H, W)$
* **Filters**: $\mathbf{F}$ of shape $(C_{out}, C_{in}, K_h, K_w)$, biases $\mathbf{b}$ of shape $(C_{out})$
* **Output**: $\mathbf{Z}$ of shape $(B, C_{out}, H_{out}, W_{out})$}

$$
z_{b,c,h,w} = \sum_{k=1}^{C_{in}}\sum_{i=1}^{K_h}\sum_{j=1}^{K_w} x_{b,k,h+i,w+j}\, f_{c,k,i,j} + b_c
$$

\notes{This is written for stride 1 and no padding. Strictly it is a cross-correlation rather than a convolution (a convolution would flip the filter), but since the filters are learned the distinction does not matter, and deep learning libraries all use this form. With padding $P$ and stride $S$ the output size is
$$
H_{out} = \left\lfloor \frac{H + 2P - K_h}{S} \right\rfloor + 1,
$$
and similarly for $W_{out}$, and the input index becomes $hS + i$ in the padded input.}

\newslide{Convolutional Layer Backward Pass}

$$
\frac{\partial \lossFunction}{\partial f_{c,k,i,j}} = \sum_{b,h,w} \frac{\partial \lossFunction}{\partial z_{b,c,h,w}}\, x_{b,k,h+i,w+j},
\qquad
\frac{\partial \lossFunction}{\partial b_c} = \sum_{b,h,w} \frac{\partial \lossFunction}{\partial z_{b,c,h,w}}
$$

$$
\frac{\partial \lossFunction}{\partial x_{b,k,h,w}} = \sum_{c,i,j} \frac{\partial \lossFunction}{\partial z_{b,c,h-i,w-j}}\, f_{c,k,i,j}
$$

\notes{Because the same filter is used at every position, its gradient is a *sum* over every position (and every example in the batch) at which it was applied. This is the multiple-paths rule from the chain rule again: each filter weight affects the output through $B \times H_{out} \times W_{out}$ paths. The input gradient sums over every output whose receptive field contains the pixel $(h, w)$. Terms where $h-i$ or $w-j$ falls outside the output are zero. This sum is itself a convolution of the output gradient with the flipped filter. With padding, the filter gradient must be computed from the *padded* input, exactly as used in the forward pass, and the input gradient is cropped back to the unpadded size.}

\newslide{Max Pooling Layer Gradients}

$$
y_{b,c,h,w} = \max_{(i,j) \in \mathcal{R}_{h,w}} x_{b,c,hS+i,\,wS+j}
$$

\slides{* Gradient goes only to the position that achieved the maximum
* All other positions in the pooling region get zero gradient
* No parameters}

\notes{The max function passes its input through unchanged at the position of the maximum and ignores all others, so in the backward pass the gradient $\frac{\partial \lossFunction}{\partial y_{b,c,h,w}}$ is routed to the position in the pooling region $\mathcal{R}_{h,w}$ that achieved the maximum, and every other position receives zero. If pooling regions overlap (stride smaller than the pool size), one input can be the maximum of several regions, and its gradients are summed. When there is a tie the implementation picks one of the maximal positions (the max is not differentiable there).}

\newslide{Flatten Layer Gradients}

\slides{* **Forward**: reshape $(B, C, H, W) \to (B, CHW)$
* **Backward**: reshape the gradient $(B, CHW) \to (B, C, H, W)$}

\notes{The flatten layer only rearranges values, so its gradient is the incoming gradient reshaped back to the input shape. It connects the convolutional layers to the fully connected layers.}

\newslide{Activation Functions}

$$
\frac{\partial \lossFunction}{\partial \mathbf{Z}} = \frac{\partial \lossFunction}{\partial \mathbf{H}} \odot \activationFunction'(\mathbf{Z}),
\qquad \mathbf{H} = \activationFunction(\mathbf{Z})
$$

\notes{Activation functions are applied element-wise at every spatial location and channel, so their gradient is an element-wise product. For the ReLU, $\activationFunction'(z) = 1$ for $z > 0$ and $0$ otherwise, so only positions with positive pre-activations pass gradient back.}

\newslide{Complete CNN}

\slides{* **Convolution**: $\mathbf{H}_1 = \text{ReLU}(\text{conv}(\inputMatrix, \mathbf{F}) + \mathbf{b})$
* **Pooling**: $\mathbf{P} = \text{maxpool}(\mathbf{H}_1)$
* **Flatten**: $\mathbf{p} = \text{flatten}(\mathbf{P})$
* **Dense**: $\mathbf{h}_2 = \text{ReLU}(\mathbf{p}\mathbf{W}_2 + \mathbf{b}_2)$
* **Output**: $\mathbf{y} = \mathbf{h}_2\mathbf{W}_3 + \mathbf{b}_3$}

\notes{A complete CNN composes these layers. Each one transforms its input in a specific way, and the gradients flow back through each transformation in reverse order.}

\newslide{CNN Gradient Chain Rule}

\slides{* **Output to dense**: $\frac{\partial \lossFunction}{\partial \mathbf{h}_2} = \frac{\partial \lossFunction}{\partial \mathbf{y}}\mathbf{W}_3^\top$
* **Dense to flatten**: $\frac{\partial \lossFunction}{\partial \mathbf{p}} = \left(\frac{\partial \lossFunction}{\partial \mathbf{h}_2} \odot \text{ReLU}'\right)\mathbf{W}_2^\top$
* **Flatten to pool**: reshape $\frac{\partial \lossFunction}{\partial \mathbf{p}}$ to the shape of $\mathbf{P}$
* **Pool to conv**: route each gradient to its maximum position
* **Conv to input**: $\odot\,\text{ReLU}'$, then the convolution input gradient}

\notes{Working backwards from the output, each layer applies its own backward rule. Note that the gradient through each dense layer must include the derivative of its activation function before multiplying by the transposed weights. Along the way each layer with parameters computes its own parameter gradients: $\frac{\partial \lossFunction}{\partial \mathbf{W}_3} = \mathbf{h}_2^\top \frac{\partial \lossFunction}{\partial \mathbf{y}}$ for the output layer, the corresponding expression for the dense layer, and the summed filter and bias gradients above for the convolution.}

\newslide{Verification and Code Mapping}

\slides{* `ConvolutionalLayer`, `MaxPoolingLayer`, `FlattenLayer` implement the rules above
* `LayeredNeuralNetwork.gradients` collects every layer's parameter gradients
* Every gradient is checked against finite differences, layer by layer and end to end}

\notes{Each layer class implements the gradient computations described above, and `LayeredNeuralNetwork` coordinates the flow between layers. The tests in `test_layer_parameter_gradients.py` in the `mlai` package check the input and parameter gradients of every layer type, with and without padding and stride, and the gradients of a complete CNN, against central finite differences.}

\newslide{Summary}

\slides{* **Weight sharing**: filter gradients sum over all positions and the batch
* **Pooling**: routes gradient to the maximum; no parameters
* **Flatten**: reshapes the gradient
* **Modularity**: each layer's backward pass can be checked independently}

\notes{Convolutional networks use the same chain rule as other neural networks. What is new is the spatial structure: because filters are shared across positions, their gradients accumulate contributions from every position where they are applied.}

\endif

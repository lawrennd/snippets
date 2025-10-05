\ifndef{chainRuleTransformerAttention}
\define{chainRuleTransformerAttention}

\editme

\subsection{Chain Rule for Transformer Attention}

\newslide{Transformer Attention Structure}

\slides{* *Input*: $\inputMatrix$ appears in three roles
* *Query*: $\queryMatrix = \inputMatrix \queryWeightMatrix$
* *Key*: $\keyMatrix = \inputMatrix \keyWeightMatrix$  
* *Value*: $\valueMatrix = \inputMatrix \valueWeightMatrix$}

\notes{The transformer attention mechanism is more complex than standard neural networks because the same input matrix $\inputMatrix$ appears in three different linear transformations. This creates a more intricate chain rule when computing gradients.}

\notes{This multiple appearance is what allows the transformer to include variable length sequences. But it make sthe chain rule computation a little more complex than for a standard neural network.}

\newslide{Attention Computation}

\slides{$$\attentionMatrix = \softmax\left(\frac{\queryMatrix \keyMatrix^\top}{\sqrt{d_k}}\right)$$}

\slides{$$\outputMatrix = \attentionMatrix \valueMatrix$$}

\notes{The attention mechanism computes a weighted combination of values, where the weights are determined by the similarity between queries and keys. The softmax ensures the weights sum to one.}

\newslide{The Chain Rule Challenge}

\slides{* *Standard NN*: $\frac{\partial \lossFunction}{\partial \inputMatrix} = \frac{\partial \lossFunction}{\partial \outputMatrix} \frac{\partial \outputMatrix}{\partial \inputMatrix}$
* *Transformer*: $\frac{\partial \lossFunction}{\partial \inputMatrix} = \frac{\partial \lossFunction}{\partial \queryMatrix} \frac{\partial \queryMatrix}{\partial \inputMatrix} + \frac{\partial \lossFunction}{\partial \keyMatrix} \frac{\partial \keyMatrix}{\partial \inputMatrix} + \frac{\partial \lossFunction}{\partial \valueMatrix} \frac{\partial \valueMatrix}{\partial \inputMatrix}$}

\notes{In a standard neural network, we have a single path from input to output. In transformer attention, we have three parallel paths through the same input, making the chain rule more complex.}

\newslide{Gradient Flow Through Attention}

\slides{* **Step 1**: $\frac{\partial \lossFunction}{\partial \outputMatrix}$ (from next layer)
* **Step 2**: $\frac{\partial \lossFunction}{\partial \valueMatrix} = \frac{\partial \lossFunction}{\partial \outputMatrix} \attentionMatrix^\top$
* **Step 3**: $\frac{\partial \lossFunction}{\partial \attentionMatrix} = \frac{\partial \lossFunction}{\partial \outputMatrix} \valueMatrix^\top$}

\notes{The gradient flow through attention involves computing how the loss changes with respect to the attention weights and the value matrix.}

\newslide{Attention Weights Gradient}

\slides{$$\frac{\partial \lossFunction}{\partial \attentionMatrix} = \frac{\partial \lossFunction}{\partial \outputMatrix} \valueMatrix^\top$$}

\notes{The gradient with respect to the attention matrix comes from the product with the value matrix. This tells us how much each attention weight should change.}

\newslide{Query-Key Interaction Gradient}

\slides{* **Attention logits**: $\logitsMatrix = \frac{\queryMatrix \keyMatrix^\top}{\sqrt{d_k}}$
* **Gradient**: $\frac{\partial \lossFunction}{\partial \logitsMatrix} = \attentionMatrix \odot \left(\frac{\partial \lossFunction}{\partial \attentionMatrix} - \sum_{j} \frac{\partial \lossFunction}{\partial \attentionMatrix_{:,j}} \odot \attentionMatrix_{:,j}\right)$}

\notes{The gradient through the softmax requires the standard softmax gradient formula, accounting for the fact that attention weights sum to one.}

\newslide{Query and Key Gradients}

\slides{$$\frac{\partial \lossFunction}{\partial \queryMatrix} = \frac{\partial \lossFunction}{\partial \logitsMatrix} \keyMatrix$$}

\slides{$$\frac{\partial \lossFunction}{\partial \keyMatrix} = \frac{\partial \lossFunction}{\partial \logitsMatrix}^\top \queryMatrix$$}

\notes{The gradients for queries and keys come from their interaction in the attention logits. Each query interacts with all keys, and each key interacts with all queries.}

\newslide{Input Matrix Gradient}

\slides{$$\frac{\partial \lossFunction}{\partial \inputMatrix} = \frac{\partial \lossFunction}{\partial \queryMatrix} \queryWeightMatrix^\top + \frac{\partial \lossFunction}{\partial \keyMatrix} \keyWeightMatrix^\top + \frac{\partial \lossFunction}{\partial \valueMatrix} \valueWeightMatrix^\top$$}

\notes{Finally, we combine all three gradient paths to get the gradient with respect to the input matrix. This is the key insight: the same input appears in three different transformations.}

\newslide{Weight Matrix Gradients}

\slides{* **Query weights**: $\frac{\partial \lossFunction}{\partial \queryWeightMatrix} = \inputMatrix^\top \frac{\partial \lossFunction}{\partial \queryMatrix}$
* **Key weights**: $\frac{\partial \lossFunction}{\partial \keyWeightMatrix} = \inputMatrix^\top \frac{\partial \lossFunction}{\partial \keyMatrix}$
* **Value weights**: $\frac{\partial \lossFunction}{\partial \valueWeightMatrix} = \inputMatrix^\top \frac{\partial \lossFunction}{\partial \valueMatrix}$}

\notes{The gradients for the weight matrices follow the standard pattern: input matrix transposed times the gradient of the output.}

\newslide{Multi-Head Attention}

\slides{* **Multiple heads**: $\attentionHead_i = \attentionFunction(\queryMatrix_i, \keyMatrix_i, \valueMatrix_i)$
* **Concatenation**: $\multiHeadOutput = \concat(\attentionHead_1, \ldots, \attentionHead_h) \outputWeightMatrix$
* **Gradient complexity**: Each head has its own $Q$, $K$, $V$ gradients}

\notes{Multi-head attention adds another layer of complexity. Each head computes its own attention, and the gradients must be computed for each head separately before being combined.}

\newslide{Implementation Considerations}

\slides{* **Memory efficiency**: Store intermediate computations
* **Numerical stability**: Scale attention weights appropriately  
* **Parallel computation**: Each head can be computed independently
* **Gradient accumulation**: Sum gradients across heads}

\notes{Implementing transformer gradients efficiently requires careful attention to memory usage and numerical stability. The softmax operation can be numerically unstable for large attention scores.}

\newslide{Summary}

\slides{* **Three-path chain rule**: Input appears in $Q$, $K$, $V$ transformations
* **Softmax gradient**: Standard formula with attention weight constraints
* **Multi-head complexity**: Each head has independent gradients
* **Efficient implementation**: Careful memory and numerical considerations}

\notes{The transformer attention mechanism requires a more sophisticated understanding of the chain rule because the same input participates in multiple parallel computations.}

\endif

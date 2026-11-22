\ifndef{chainRuleTransformerAttention}
\define{chainRuleTransformerAttention}

\editme

\subsection{Chain Rule for Transformer Attention}

\newslide{Transformer Attention Structure}

\slides{* *Input*: $\inputMatrix \in \Re^{T \times d}$ appears in three roles
* *Query*: $\mathbf{Q} = \inputMatrix \mathbf{W}_q$
* *Key*: $\mathbf{K} = \inputMatrix \mathbf{W}_k$
* *Value*: $\mathbf{V} = \inputMatrix \mathbf{W}_v$}

\notes{In self-attention the input matrix $\inputMatrix$, whose $T$ rows are the token representations, is used three times: to form the queries $\mathbf{Q} = \inputMatrix \mathbf{W}_q$, the keys $\mathbf{K} = \inputMatrix \mathbf{W}_k$ and the values $\mathbf{V} = \inputMatrix \mathbf{W}_v$.}

\notes{Because the same weight matrices are applied to every row (every position), the number of parameters does not depend on the sequence length $T$. This weight sharing across positions is what lets the same layer process sequences of different lengths. The fact that $\inputMatrix$ is used three times is what makes the chain rule more interesting than for a standard layer.}

\newslide{Attention Computation}

$$
\mathbf{S} = \frac{\mathbf{Q}\mathbf{K}^\top}{\sqrt{d_k}}, \qquad
\mathbf{A} = \text{softmax}(\mathbf{S}), \qquad
\mathbf{O} = \mathbf{A}\mathbf{V}
$$

\notes{The scores $\mathbf{S}$ measure the similarity between each query and each key. The softmax is applied to each row of $\mathbf{S}$, so each row of the attention matrix $\mathbf{A}$ is a set of positive weights that sum to one. The output for each position is the corresponding weighted combination of the values. The scaling by $1/\sqrt{d_k}$ stops the scores growing with the key dimension $d_k$, which would otherwise push the softmax into a regime with very small gradients.}

\newslide{The Chain Rule Challenge}

\slides{* *Standard layer*: one path from $\inputMatrix$ to the output
* *Self-attention*: three paths, through $\mathbf{Q}$, $\mathbf{K}$ and $\mathbf{V}$}

$$
\frac{\partial \lossFunction}{\partial \inputMatrix}
= \underbrace{\frac{\partial \lossFunction}{\partial \mathbf{Q}} \mathbf{W}_q^\top}_{\text{query path}}
+ \underbrace{\frac{\partial \lossFunction}{\partial \mathbf{K}} \mathbf{W}_k^\top}_{\text{key path}}
+ \underbrace{\frac{\partial \lossFunction}{\partial \mathbf{V}} \mathbf{W}_v^\top}_{\text{value path}}
$$

\notes{When a variable feeds into several computations, the multivariate chain rule tells us to *sum* the contributions from each path. In a standard layer there is a single path from the input to the output. In self-attention there are three, so the gradient with respect to $\inputMatrix$ is the sum of the gradients arriving through the queries, the keys and the values. We now work backwards to find each of $\frac{\partial \lossFunction}{\partial \mathbf{Q}}$, $\frac{\partial \lossFunction}{\partial \mathbf{K}}$ and $\frac{\partial \lossFunction}{\partial \mathbf{V}}$.}

\newslide{Gradient Flow Through Attention}

\slides{* **Step 1**: $\frac{\partial \lossFunction}{\partial \mathbf{O}}$ arrives from the next layer
* **Step 2**: since $\mathbf{O} = \mathbf{A}\mathbf{V}$,}

$$
\frac{\partial \lossFunction}{\partial \mathbf{V}} = \mathbf{A}^\top \frac{\partial \lossFunction}{\partial \mathbf{O}},
\qquad
\frac{\partial \lossFunction}{\partial \mathbf{A}} = \frac{\partial \lossFunction}{\partial \mathbf{O}} \mathbf{V}^\top
$$

\notes{These follow from the rule for a matrix product $\mathbf{O} = \mathbf{A}\mathbf{V}$: the gradient with respect to the right-hand factor is pre-multiplied by $\mathbf{A}^\top$, and the gradient with respect to the left-hand factor is post-multiplied by $\mathbf{V}^\top$. Checking shapes is a useful guard against mistakes. $\mathbf{A}$ is $T \times T$ and $\frac{\partial \lossFunction}{\partial \mathbf{O}}$ is $T \times d_v$, so $\mathbf{A}^\top \frac{\partial \lossFunction}{\partial \mathbf{O}}$ is $T \times d_v$, the shape of $\mathbf{V}$. Note that the order matters: $\frac{\partial \lossFunction}{\partial \mathbf{O}}\mathbf{A}^\top$ is not even defined unless $d_v = T$, and is wrong when it is.}

\newslide{Gradient Through the Softmax}

\slides{* Softmax is applied row by row: $a_{ij} = \frac{\exp(s_{ij})}{\sum_k \exp(s_{ik})}$
* Jacobian of each row: $\frac{\partial a_{ij}}{\partial s_{ik}} = a_{ij}(\delta_{jk} - a_{ik})$}

$$
\frac{\partial \lossFunction}{\partial s_{ik}} = a_{ik}\left(\frac{\partial \lossFunction}{\partial a_{ik}} - \sum_{j} \frac{\partial \lossFunction}{\partial a_{ij}} a_{ij}\right)
$$

\notes{Each row of $\mathbf{A}$ depends only on the same row of $\mathbf{S}$, so we can treat the rows independently. Using the softmax Jacobian $\frac{\partial a_{ij}}{\partial s_{ik}} = a_{ij}(\delta_{jk} - a_{ik})$ and summing over $j$ gives the expression above. In matrix form, $\frac{\partial \lossFunction}{\partial \mathbf{S}} = \mathbf{A} \odot \left(\frac{\partial \lossFunction}{\partial \mathbf{A}} - \mathbf{r}\mathbf{1}^\top\right)$, where $\mathbf{r}$ is the vector of row sums of $\frac{\partial \lossFunction}{\partial \mathbf{A}} \odot \mathbf{A}$. The subtracted term appears because the weights in each row must sum to one. Increasing one of them necessarily decreases the others.}

\newslide{Query and Key Gradients}

$$
\frac{\partial \lossFunction}{\partial \mathbf{Q}} = \frac{1}{\sqrt{d_k}} \frac{\partial \lossFunction}{\partial \mathbf{S}} \mathbf{K},
\qquad
\frac{\partial \lossFunction}{\partial \mathbf{K}} = \frac{1}{\sqrt{d_k}} \left(\frac{\partial \lossFunction}{\partial \mathbf{S}}\right)^\top \mathbf{Q}
$$

\notes{Since $\mathbf{S} = \mathbf{Q}\mathbf{K}^\top/\sqrt{d_k}$, the same matrix-product rule applies, and the scale factor $1/\sqrt{d_k}$ carries through to both gradients. Each query interacts with every key, and each key with every query, so every row of $\frac{\partial \lossFunction}{\partial \mathbf{Q}}$ depends on all the keys and vice versa.}

\newslide{Input and Weight Gradients}

\slides{* Combine the three paths (see above) for $\frac{\partial \lossFunction}{\partial \inputMatrix}$
* Weight gradients follow the standard pattern:}

$$
\frac{\partial \lossFunction}{\partial \mathbf{W}_q} = \inputMatrix^\top \frac{\partial \lossFunction}{\partial \mathbf{Q}}, \qquad
\frac{\partial \lossFunction}{\partial \mathbf{W}_k} = \inputMatrix^\top \frac{\partial \lossFunction}{\partial \mathbf{K}}, \qquad
\frac{\partial \lossFunction}{\partial \mathbf{W}_v} = \inputMatrix^\top \frac{\partial \lossFunction}{\partial \mathbf{V}}
$$

\notes{The gradients for the weight matrices follow the same pattern as for a linear layer: the input matrix transposed times the gradient of the layer's output. With a batch of sequences these are summed over the batch. If the layer has an output projection $\mathbf{Y} = \mathbf{O}\mathbf{W}_o$, the first step backwards is $\frac{\partial \lossFunction}{\partial \mathbf{O}} = \frac{\partial \lossFunction}{\partial \mathbf{Y}}\mathbf{W}_o^\top$, with $\frac{\partial \lossFunction}{\partial \mathbf{W}_o} = \mathbf{O}^\top\frac{\partial \lossFunction}{\partial \mathbf{Y}}$.}

\newslide{Causal Masking}

\slides{* For next-token prediction, position $t$ must not see positions $t' > t$
* Set $s_{tt'} = -\infty$ for $t' > t$ before the softmax, so $a_{tt'} = 0$
* Masked entries receive zero gradient}

\notes{When a transformer is trained to predict the next token, the output at position $t$ must not depend on the tokens it is trying to predict. A causal mask sets the scores $s_{tt'}$ to $-\infty$ for all $t' > t$ before the softmax, so the corresponding attention weights are exactly zero. Because $\frac{\partial \lossFunction}{\partial s_{tt'}}$ is proportional to $a_{tt'}$, the masked entries also receive zero gradient, and the backward pass needs no special treatment.}

\newslide{Multi-Head Attention}

\slides{* Head $i$ has its own $\mathbf{W}_q^{(i)}, \mathbf{W}_k^{(i)}, \mathbf{W}_v^{(i)} \in \Re^{d \times d_k}$, $d_k = d/h$
* Every head sees the full input $\inputMatrix$
* Output: $\text{concat}(\mathbf{O}^{(1)}, \ldots, \mathbf{O}^{(h)}) \mathbf{W}_o$
* $\frac{\partial \lossFunction}{\partial \inputMatrix}$ is the *sum* of the gradients from each head}

\notes{In multi-head attention each head has its own projections from the full $d$-dimensional input down to $d_k = d/h$ dimensions, so different heads can learn to attend to different kinds of relationship. The head outputs are concatenated and combined by an output projection $\mathbf{W}_o$. Since $\inputMatrix$ feeds every head, this is another case of multiple paths: the gradient with respect to $\inputMatrix$ is the sum of the gradients from all the heads. In the implementation `MultiHeadAttentionLayer` composes $h$ `AttentionLayer` heads (without their own output projections) and a shared $\mathbf{W}_o$.}

\newslide{Cross-Attention}

\slides{* **Cross-attention**: $\mathbf{Q} = \mathbf{X}_q \mathbf{W}_q$, $\mathbf{K} = \mathbf{X}_{kv} \mathbf{W}_k$, $\mathbf{V} = \mathbf{X}_{kv} \mathbf{W}_v$
* Queries from one sequence, keys and values from another
* $\mathbf{X}_q$ receives gradient through one path; $\mathbf{X}_{kv}$ through two}

\notes{In cross-attention, used for example in encoder-decoder models, the queries come from one sequence and the keys and values from another. The gradient with respect to the query input now has a single path, through $\mathbf{Q}$, while the gradient with respect to the key-value input is the sum of two paths, through $\mathbf{K}$ and $\mathbf{V}$.}

\newslide{Implementation Considerations}

\slides{* **Memory**: store $\mathbf{Q}, \mathbf{K}, \mathbf{V}, \mathbf{A}$ from the forward pass; $\mathbf{A}$ is $T \times T$
* **Numerical stability**: subtract the row maximum before the softmax
* **Dropout**: store the dropout mask for the backward pass
* **Parallelism**: heads are independent and can be computed in parallel}

\notes{The attention matrix has $T^2$ entries per head, so memory grows quadratically with sequence length. This is the motivation for the efficient attention variants. The softmax is computed stably by subtracting the row maximum before exponentiating. If dropout is applied to the attention weights, the same mask must be used in the backward pass.}

\newslide{Summary}

\slides{* **Three-path chain rule**: $\inputMatrix$ appears in $\mathbf{Q}$, $\mathbf{K}$ and $\mathbf{V}$, so gradients are summed
* **Softmax gradient**: row-wise, with a correction because weights sum to one
* **Multi-head**: each head sees the full input; input gradient sums over heads
* **Causal mask**: masked weights are zero and receive zero gradient}

\notes{The transformer attention mechanism requires careful use of the chain rule because the same input participates in several parallel computations. Each time a variable is used more than once, the gradients from each use are summed.}

\newslide{Verification}

\slides{* Compare analytical gradients against finite differences
* Check input gradients *and* parameter gradients ($\mathbf{W}_q, \mathbf{W}_k, \mathbf{W}_v, \mathbf{W}_o$)
* Test self-, cross- and causal attention and multi-head attention}

\notes{Whenever we derive gradients by hand we should check them numerically. The tests in `test_layer_parameter_gradients.py` in the `mlai` package compare the analytical input and parameter gradients of the attention layers with central finite differences.}

\endif

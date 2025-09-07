\ifndef{attentionIntroduction}
\define{attentionIntroduction}

\editme

\subsection{Traditional Sequence Modelling}
\slides{* Encoder compresses inputs into a state vector (context)
* Decoder generates outputs from context
* Bottlenecks: fixed-length context; gradient stability}
\notes{Seq2seq compresses an entire sequence into a single context vector, limiting capacity for long/complex inputs.}
\figure{\includesvg{}{70%}}{Traditional encoder–decoder with fixed context.}{seq2seq-context}

\subsection{The Innovation: Attention}
\slides{* Replace fixed context with per-step, input-dependent context
* Learn attention weights over encoder states; softmax normalisation}
\notes{Each output step computes a context as a weighted sum over encoder states, with weights learned from the decoder state and encoder states.}
\figure{\includesvg{}{70%}}{Attention mechanism with learned alignment.}{attention-mechanism}

\subsection{First Use of Attention}

\slides{* Bahdanau et al., 2015 (soft-)search the source sentence for segments that are rlevant to predicting a target word.}
* The Method
  * **Encoder**: bi-directional RNN; 
  * **Decoder**: gated RNN
  * **Innovation**: each time-step gets its own separate set of weights used to generate its part of the context vector

  \begin{aligned} \alpha_{t, j} & =\frac{\exp \left(e_{t, j}\right)}{\sum_{k=1}^T \exp\left(e_{t, k}\right) \\ e_{t, j} & =f\left(s_{t-1}, h_j\right)\end{aligned}


\notes{A small MLP computes unnormalised scores from decoder and encoder states; softmax yields alignment.}

\figure{\includediagram{\diagramsDir/ml/attention-diagram}{50%}}{Alignment-based attention in encoder–decoder RNNs.}{attention-diagram}
\figure{\includesvg{}{70%}}{Attention heatmap for translation (alignment matrix).}{attention-heatmap}

\endif

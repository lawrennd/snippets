\ifndef{attentionVariants}
\define{attentionVariants}

\editme

\subsection{Vision Transformers (ViT)}
\slides{* Split image into patches; embed + positions
* Transformer encoder over patch sequence
* Strong vision results}
\notes{Patch tokenisation with positional encodings enables global interactions without convolutions.}
\figure{\includesvg{}{70%}}{ViT architecture.}{vit-architecture}
\figure{\includesvg{}{70%}}{ViT attention visualisations.}{vit-attn}

\subsection{Transformer in Transformer (TNT)}
\slides{* Nested tokens: inner (patch) + outer (image)
* Attention at multiple granularities}
\notes{TNT improves fine-grained modelling within patches while maintaining global context.}
\figure{\includesvg{}{70%}}{TNT nested token structure.}{tnt-architecture}

\subsection{AlphaFold 2}
\slides{* Attention-centric modules for structure prediction
* Transformers superseded CNNs in later versions}
\notes{Attention enables modelling of long-range residue interactions; key to breakthrough accuracy.}
\figure{\includesvg{}{70%}}{Attention modules in AlphaFold-style models.}{alphafold}

\endif

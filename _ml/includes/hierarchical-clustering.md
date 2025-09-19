\ifndef{hierarchicalClustering}
\define{hierarchicalCLustering}

\editme

\subsection{Hierarchical Clustering}

\slides{
* Form taxonomies of the cluster centers
* Like humans apply to animals, to form *phylogenies*
* Builds a tree structure showing relationships between data points
* Two main approaches:
    * Agglomerative (bottom-up): Start with individual points and merge
    * Divisive (top-down): Start with one cluster and split
}

\notes{Other approaches to clustering involve forming taxonomies of the cluster centers, like humans apply to animals, to form trees. Hierarchical clustering builds a tree structure showing the relationships between data points. We'll demonstrate agglomerative clustering on the oil flow data set, which contains measurements from a multiphase flow facility.}

\include{_datasets/includes/oil-flow-data.md}
\include{_ml/includes/oil-flow-hierarchical-clustering.md}

\subsection{Phylogenetic Trees}
\slides{
* Hierarchical clustering of genetic sequence data
* Creates evolutionary trees showing species relationships
* Estimates common ancestors and mutation timelines
* Critical for tracking viral evolution and outbreaks
}
\notes{A powerful application of hierarchical clustering is in constructing phylogenetic trees from genetic sequence data. By comparing DNA/RNA sequences across species, we can reconstruct their evolutionary relationships and estimate when species diverged from common ancestors. The resulting tree structure, called a phylogeny, maps out the evolutionary history and relationships between organisms.

Modern phylogenetic methods go beyond simple clustering - they incorporate sophisticated models of genetic mutation and molecular evolution. These models can estimate not just the structure of relationships, but also the timing of evolutionary divergence events based on mutation rates. This has important applications in tracking the origins and spread of rapidly evolving pathogens like HIV and influenza viruses. Understanding viral phylogenies helps epidemiologists trace outbreak sources, track transmission patterns, and develop targeted containment strategies.

[^commonancestor]: Phylogenetic models incorporate molecular clock models that estimate mutation rates over time. By calibrating these with known divergence events from the fossil record, the timing of common ancestors can be estimated.}

\subsection{Product Clustering}
\slides{
* Hierarchical clustering for e-commerce products
* Creates product taxonomy trees
* Splits into nested categories (e.g. Electronics → Phones → Smartphones)
}
\notes{An e-commerce company could apply hierarchical clustering to organize their product catalog into a taxonomy tree. Products would be grouped into increasingly specific categories - for example, Electronics might split into Phones, Computers, etc., with Phones further dividing into Smartphones, Feature Phones, and so on. This creates an intuitive hierarchical organization. However, many products naturally belong in multiple categories - for instance, running shoes could reasonably be classified as both sporting equipment and footwear. The strict tree structure of hierarchical clustering doesn't allow for this kind of multiple categorization, which is a key limitation for product organization.}

\subsection{Hierarchical Clustering Challenge}
\slides{
* Many products belong in multiple clusters (e.g. running shoes are both 'sporting goods' and 'clothing')
* Tree structures are too rigid for natural categorization
* Human concept learning is more flexible:
    * Forms overlapping categories
    * Learns abstract rules
    * Builds causal theories}
\notes{Our psychological ability to form categories is far more sophisticated than hierarchical trees. Research in cognitive science has revealed that humans naturally form overlapping categories and learn abstract principles that guide classification. Josh Tenenbaum's influential work demonstrates how human concept learning combines multiple forms of inference through hierarchical Bayesian models that integrate similarity-based clustering with theory-based reasoning. This computational approach aligns with foundational work by Eleanor Rosch on prototype theory and Susan Carey's research on conceptual change, showing how categorization adapts to context and goals. While these cognitively-inspired models better capture human-like categorization, their computational complexity currently limits practical applications to smaller datasets. Nevertheless, they provide important insights into more flexible clustering approaches that could eventually enhance machine learning systems.}

\endif

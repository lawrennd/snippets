\ifndef{clusteringIntro}
\define{clusteringIntro}


\editme

\subsection{Clustering}

\slides{* Common approach for grouping data points
* Assigns data points to discrete groups
* Examples include:
  * Animal classification
  * Political affiliation grouping}

\notes{Clustering is a common approach to data analysis, though we will not cover it in great depth in this course. The fundamental idea is to associate each data point $\dataVector_{i, :}$ with one of $k$ different discrete groups. This approach raises interesting questions - for instance, when clustering animals into groups, we might ask whether animal traits are truly discrete or continuous in nature. Similar questions arise when clustering political affiliations.

Humans seem to have a natural affinity for discrete clustering approaches. This makes clustering particularly useful when collaborating with biologists, who often think in terms of discrete categories. However, we should be mindful that this preference for discrete categories may sometimes oversimplify continuous variations in data.}

\newslide{Clustering vs Vector Quantisation}

\slides{* Clustering expects gaps between groups in data density
* Vector quantization may not require density gaps
* For practical purposes, both involve:
  * Allocating points to groups
  * Determining optimal number of groups
}

\notes{There is a subtle but important distinction between clustering and vector quantisation. In true clustering, we typically expect to see reductions in data density between natural groups - essentially, gaps in the data that separate different clusters. This definition isn't universally applied though, and vector quantization may partition data without requiring such density gaps. For our current discussion, we'll treat them similarly, focusing on the common challenges they share: how to allocate points to groups and, more challengingly, how to determine the optimal number of groups.}


\newslide{Task}

\slides{* *Task*: associate data points with different labels.
* Labels are *not* provided by humans.
* Process is intuitive for humans - we do it naturally.}

\notes{Clustering methods associate data points with different labels that are allocated by the computer rather than provided by human annotators. This process is quite intuitive for humans - we naturally cluster our observations of the real world. For example, we cluster animals into groups like birds, mammals, and insects. While these labels can be provided by humans, they were originally invented through a clustering process. With computational clustering, we want to recreate that process of label invention.}

\newslide{Platonic Ideals}
\slides{
* Greek philosopher Plato considered the concept of ideals
* The Platonic ideal bird is the most bird-like bird
* In clustering, we find these ideals as cluster centers
* Data points are allocated to their nearest center}

\notes{When thinking about ideas, the Greek philosopher Plato considered the concept of Platonic ideals - the most quintessential version of a thing, like the most bird-like bird or chair-like chair. In clustering, we aim to define different categories by finding their Platonic ideals (cluster centers) and allocating each data point to its nearest center. This allows computers to form categorizations of data at scales too large for human processing.}

\endif

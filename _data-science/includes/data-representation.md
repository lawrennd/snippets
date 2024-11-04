\ifndef{dataRepresentation}
\define{dataRepresentation}

\editme

\subsection{Data Representation}

\notes{Before we can reduce dimensionality, we need to understand the distinction between how data is represented and its intrinsic structure. This distinction is fundamental to dimensionality reduction.}

\subsection{Parametrization vs Canonical Representation}

\notes{We can think about data representation in two important ways:}

\slides{
* Two key views of data:
    * How it's given (parametrization)
    * How it varies (canonical form)
}

\subsubsection{Parametrization of Representation}

\notes{The parametrization of data is often determined by how we measure or collect it. For example:
* A color image might be represented as RGB values (3 dimensions)
* A time series might be represented as measurements at fixed intervals
* A document might be represented as word counts
This representation is often chosen for convenience or due to measurement constraints rather than being natural to the underlying phenomenon.}

\slides{
* Determined by measuring device
* Often higher dimensional than necessary
* Example: RGB values for color
* Example: Time series measurements}

\subsubsection{Canonical Representation}

\notes{The canonical representation captures how the data actually varies - the true degrees of freedom in the system. This is often lower dimensional than the parametrization:
* Colors might vary primarily along brightness and saturation
* A time series might follow simple periodic patterns
* Documents might cluster around a few main topics}

\slides{
* How variations in data can be parametrized
* True degrees of freedom
* Often lower dimensional
* Captures intrinsic structure}

\subsection{The Gap Between Representations}

\notes{The difference between these representations creates both challenges and opportunities:}

\slides{
* Challenge: Data given in one form
* Need: Understanding in another
* Goal: Bridge the gap}

\includediagram{\diagramsDir/dimred/representation-gap}

\notes{Consider plotting points that lie on a circle. While each point might be represented using two coordinates (x,y), there's really only one degree of freedom - the angle around the circle. This is a simple example where the parametric dimension (2) is higher than the intrinsic dimension (1).}

\subsection{Implications for Visualization}

\notes{This understanding has important implications for visualization:
1. We shouldn't necessarily trust the original data dimensions
2. We should look for simpler representations that capture the true variation
3. The goal of dimensionality reduction is to move from the parametric to the canonical representation}

\slides{
* Don't trust original dimensions
* Look for simpler structure
* Bridge parametric and canonical forms
* Preserve important variations}

\subsection{Connection to Statistical Learning}

\notes{The distinction between parametric and canonical representations connects directly to statistical learning theory:
* The parametric representation often includes noise and redundancy
* The canonical representation relates to the true underlying variables
* Finding the canonical representation can help prevent overfitting}

\slides{
* Parametric includes noise
* Canonical captures signal
* Key to avoiding overfitting}

\notes{This framework provides the motivation for the mathematical tools we'll develop. Whether we use MDS, PCA, or non-linear methods, we're always trying to find a simpler representation that captures the true structure of our data.}

\endif

\ifndef{manifoldDefinition}
\define{manifoldDefinition}

\editme


\subsection{Manifolds}

\notes{The concept of a manifold provides a mathematical framework for understanding how high-dimensional data might be organized on a lower-dimensional structure.}

\subsection{Definition}

\notes{A manifold has a precise mathematical definition:}

\slides{
Definition (Manifold):
"A manifold is a topological space that near each point resembles Euclidean space"}

\notes{This formal definition has important practical implications:
1. Locally, the manifold looks like flat Euclidean space
2. Globally, it might have complex curvature
3. The dimensionality of the local Euclidean space defines the intrinsic dimension}

\subsection{Visual Examples}

\includediagram{\diagramsDir/dimred/swiss-roll}

\slides{
* Swiss roll: 2D surface curved in 3D
* Points nearby on manifold might be far in ambient space
* Local structure ≠ Global structure
}

\notes{The Swiss roll is a canonical example that illustrates key manifold concepts:
* The data lies on a 2D surface embedded in 3D
* Euclidean distance in 3D can be misleading
* Points that are close in the ambient space might be far along the manifold
* The manifold can be "unrolled" to reveal its true structure}

\subsection{Sequence of Examples}

\notes{We can understand manifolds through a progression of increasingly complex examples:}

\slides{
1. Line in 2D
2. Circle in 2D
3. Swiss roll in 3D
4. Complex manifolds in high dimensions
}

\includediagram{\diagramsDir/dimred/manifold-sequence}

\notes{Each example illustrates different aspects of manifold structure:
* A line shows the simplest case where intrinsic and ambient dimensions differ
* A circle introduces the concept of periodic structure
* The Swiss roll shows how global structure can differ from local
* More complex examples prepare us for real-world data}

\subsection{Local vs Global Structure}

\notes{The key insight from manifold theory is the relationship between local and global structure:}

\slides{
* Locally: Euclidean geometry works
* Globally: Need to respect manifold structure
* Challenge: Build global from local
}

\notes{This relationship provides the foundation for many dimensionality reduction algorithms:
1. We can trust local distances/relationships
2. Global structure must be built by carefully combining local information
3. Different algorithms make different choices about how to combine local information}

\subsection{Implications for Data Analysis}

\notes{Understanding manifolds changes how we approach data analysis:}

\slides{
* Data might appear higher dimensional than it is
* Local relationships more trustworthy than global
* Need methods that respect manifold structure
}

\notes{When working with real data:
* We should expect it to lie on or near a lower-dimensional manifold
* We should trust local relationships more than global distances
* We need algorithms that can discover and respect manifold structure
* The manifold perspective helps explain why some methods work better than others}

\endif

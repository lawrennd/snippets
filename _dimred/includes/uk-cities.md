\ifndef{ukCities}
\define{ukCities}

\editme

\subsection{UK Cities}

\notes{To make the ideas of MDS concrete, let's look at a practical example using distances between UK cities. This example is particularly instructive because we can compare the MDS reconstruction with our geographic knowledge.}

\subsection{Distance Matrix}

\notes{We start with a matrix of distances (in miles) between six UK cities:}

\slides{
|     | Man | Ox  | Lon | Bri | Liv | Birm |
|-----|-----|-----|-----|-----|-----|------|
| Man | 0   | 203 | 262 | 224 | 46  | 114  |
| Ox  | 203 | 0   | 83  | 95  | 217 | 91   |
| Lon | 262 | 83  | 0   | 170 | 285 | 161  |
| Bri | 224 | 95  | 170 | 0   | 217 | 122  |
| Liv | 46  | 217 | 285 | 217 | 0   | 126  |
| Birm| 114 | 91  | 161 | 122 | 126 | 0    |
}

\notes{The cities are:
* Manchester (Man)
* Oxford (Ox)
* London (Lon)
* Brighton (Bri)
* Liverpool (Liv)
* Birmingham (Birm)}

\subsection{Converting to Gram Matrix}

\notes{Following our earlier derivation, we can convert this distance matrix into a Gram matrix that encodes the relative positions of the cities. The key steps are:
1. Center the distance matrix
2. Apply the conversion formula
3. Ensure the result is positive semi-definite}

\slides{
* Convert distances to inner products
* Center the data
* Check eigenvalues
}

\subsection{MDS Solution}

\includeCode{cities_example}{mlai}

\notes{When we apply MDS to this distance matrix, we get a two-dimensional representation that looks remarkably like a map of England:}

\includediagram{\diagramsDir/dimred/uk-cities-mds}

\slides{
* Two dominant eigenvalues
* North-South dimension strongest
* East-West dimension second
* Recovers approximate geography
}

\notes{The reconstruction shows several interesting features:
* The first dimension roughly corresponds to North-South position
* The second dimension captures East-West variation
* The relative positions of cities are well-preserved
* Some distortion occurs but overall geography is maintained}

\subsection{Understanding the Result}

\notes{This example illustrates several key points about MDS:}

\slides{
* MDS recovers underlying structure
* Works from only pairwise distances
* Result is rotation invariant
* Preserves relative positions
}

\notes{1. MDS can recover meaningful geometric structure from just pairwise distances
2. The result is unique up to rotation and reflection
3. The method naturally finds the important dimensions (here, North-South and East-West)
4. The eigenvalues tell us how important each dimension is
5. Two dimensions capture most of the variance because UK geography is essentially 2D}

\subsection{Connection to Geography}

\notes{The success of this example isn't coincidental:
* UK geography is inherently low-dimensional (mostly 2D)
* Road distances approximate Euclidean distances
* The cities are well-distributed across England
* There are no major geographical barriers between these cities}

\slides{
* Geography naturally 2D
* Road distances ≈ Euclidean
* Well-distributed sample
* No major barriers}

\subsection{Lessons for General Use}

\notes{This example teaches us several lessons for using MDS in practice:}

\slides{
* Check eigenvalue spectrum
* Compare with known structure
* Consider underlying geometry
* Verify assumptions}

\notes{When applying MDS to new problems:
1. Look at the eigenvalue spectrum to determine dimensionality
2. If possible, compare results with known structure
3. Consider whether Euclidean distance is appropriate
4. Think about what structure you expect to find
5. Verify whether your assumptions about the data are reasonable}

\endif

\ifndef{inducingIntroduction}
\define{inducingIntroduction}
\editme

\newslide{Introducing $\inducingVector$}

Take an extra $\numInducing$ points on the function,
$\inducingVector = \mappingFunction(\inducingInputMatrix)$.
$$p(\dataVector,\mappingFunctionVector,\inducingVector) = p(\dataVector\given \mappingFunctionVector) p(\mappingFunctionVector\given \inducingVector) p(\inducingVector)$$

\setupplotcode{import mlai.plot as plot}
\plotcode{plot.nystrom_covariance_inducing(diagrams='\writeDiagramsDir')}

\newslide{Introducing $\inducingVector$}

\figure{\includediagram{\diagramsDir/cov_inducing_withX}{60%}}{Joint covariance of $\mappingFunctionVector$ and $\inducingVector$: blocks $\Kff$, $\Kfu$, $\Kuf$, $\Kuu$.}{cov-inducing-withX}

\newslide{Introducing $\inducingVector$}

Take an extra $M$ points on the function,
$\inducingVector = \mappingFunction(\inducingInputMatrix)$.
$$p(\dataVector,\mappingFunctionVector,\inducingVector) = p(\dataVector\given \mappingFunctionVector) p(\mappingFunctionVector\given \inducingVector) p(\inducingVector)$$
$$\begin{aligned}
    p(\dataVector\given\mappingFunctionVector) &= \gaussianDist{\dataVector}{\mappingFunctionVector}{\dataStd^2 \eye}\\
    p(\mappingFunctionVector\given\inducingVector) &= \gaussianDist{\mappingFunctionVector}{ \Kfu\Kuu^{-1}\inducingVector}{ \tilde{\kernelMatrix}}\\
    p(\inducingVector) &= \gaussianDist{\inducingVector}{ \zerosVector}{\Kuu}
  \end{aligned}$$


\newslide{}

\columns{
$$\inputMatrix,\,\dataVector$$ $$\mappingFunction(\inputVector) \sim {\mathcal GP}$$ $$p(\mappingFunctionVector) = \gaussianSamp{\zerosVector}{\Kff}$$ $$p(\mappingFunctionVector\given \dataVector,\inputMatrix)$$
}{
\includediagram{\diagramsDir/nomenclature4}{90%}
}{30%}{70%}
$$
\begin{align}
                           &\qquad\inducingInputMatrix, \inducingVector\\                      &p({\color{red} \inducingVector})  = \gaussianSamp{\zerosVector}{\Kuu}\end{align}
$$

\newslide{}

\columns{
$$\inputMatrix,\,\dataVector$$ $$\mappingFunction(\inputVector) \sim {\mathcal GP}$$ $$p(\mappingFunctionVector) = \gaussianSamp{\zerosVector}{\Kff}$$ $$p(\mappingFunctionVector\given \dataVector,\inputMatrix)$$ $$p(\inducingVector)  = \gaussianSamp{\zerosVector}{\Kuu}$$ $$\widetilde p({\color{red}\inducingVector}\given \dataVector,\inputMatrix)$$
}{
\includediagram{\diagramsDir/nomenclature5}{90%}
}{30%}{70%}

\endif

\ifndef{inducingNotation}
\define{inducingNotation}
\editme

\setupplotcode{import mlai.plot as plot}
\plotcode{plot.inducing_nomenclature(diagrams='\writeDiagramsDir')}

\newslide{}

\columns{$$\inputMatrix,\,\dataVector$$}{\includediagram{\diagramsDir/nomenclature1}{90%}}{30%}{70%}


\newslide{}

\columns{$$\inputMatrix,\,\dataVector$$  $${\color{\blueColor} \mappingFunction(\inputVector)} \sim {\mathcal GP}$$}{\includediagram{\diagramsDir/nomenclature2}{90%}}{30%}{70%}

\newslide{}

\columns{$$\inputMatrix,\,\dataVector$$ $$\mappingFunction(\inputVector) \sim {\mathcal GP}$$$$p({\color{\blueColor} \mappingFunctionVector}) = \gaussianSamp{\zerosVector}{\Kff}$$}{\includediagram{\diagramsDir/nomenclature3}{90%}
}{30%}{70%}

\newslide{}

\columns{
$$
\inputMatrix,\,\dataVector$$ $$\mappingFunction(\inputVector) \sim {\mathcal GP}
$$ 
$$
p(\mappingFunctionVector) = \gaussianSamp{\zerosVector}{\Kff}
$$
$$p( \mappingFunctionVector \given \dataVector,\inputMatrix)
$$}{\includediagram{\diagramsDir/nomenclature3a}{90%}}{30%}{70%}

\endif

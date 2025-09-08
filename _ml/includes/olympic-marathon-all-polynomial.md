\ifndef{olympicMarathonAllPolynomial}
\define{olympicMarathonAllPolynomial}

\include{_datasets/includes/olympic-marathon-data.md}

\editme

\subsection{Polynomial Fits to Olympic Data}

\setupcode{import mlai}

\code{data_limits=xlim
basis=mlai.Basis(mlai.polynomial, number=1, data_limits=xlim)}

\setupplotcode{import matplotlib.pyplot as plt
import mlai.plot as plot
import mlai}

\plotcode{plot.rmse_fit(x, y, param_name='number', param_range=(1, 30), 
              model=mlai.LM, 
			  basis=basis,
              xlim=xlim, objective_ylim=[0, 0.8],
              diagrams='\writeDiagramsDir/ml')}

\setupdisplaycode{from ipywidgets import IntSlider}
\setupdisplaycode{import notutils as nu}
\displaycode{nu.display_plots('olympic_LM_polynomial_number{num_basis:0>3}.svg',
                            directory='\writeDiagramsDir/ml', 
                            num_basis=IntSlider(1,1,29,1))}

                            

\slides{
\define{width}{80%}
\define{animationName}{olympic_LM_polynomial_number}
\startanimation{\animationName}{1}{29}
\newframe{\includediagram{\diagramsDir/ml/olympic_LM_polynomial_number001}{\width}}{\animationName}
\newframe{\includediagram{\diagramsDir/ml/olympic_LM_polynomial_number002}{\width}}{\animationName}
\newframe{\includediagram{\diagramsDir/ml/olympic_LM_polynomial_number003}{\width}}{\animationName}
\newframe{\includediagram{\diagramsDir/ml/olympic_LM_polynomial_number004}{\width}}{\animationName}
\newframe{\includediagram{\diagramsDir/ml/olympic_LM_polynomial_number005}{\width}}{\animationName}
\newframe{\includediagram{\diagramsDir/ml/olympic_LM_polynomial_number006}{\width}}{\animationName}
\newframe{\includediagram{\diagramsDir/ml/olympic_LM_polynomial_number007}{\width}}{\animationName}
\newframe{\includediagram{\diagramsDir/ml/olympic_LM_polynomial_number008}{\width}}{\animationName}
\newframe{\includediagram{\diagramsDir/ml/olympic_LM_polynomial_number009}{\width}}{\animationName}
\newframe{\includediagram{\diagramsDir/ml/olympic_LM_polynomial_number010}{\width}}{\animationName}
\newframe{\includediagram{\diagramsDir/ml/olympic_LM_polynomial_number011}{\width}}{\animationName}
\newframe{\includediagram{\diagramsDir/ml/olympic_LM_polynomial_number012}{\width}}{\animationName}
\newframe{\includediagram{\diagramsDir/ml/olympic_LM_polynomial_number013}{\width}}{\animationName}
\newframe{\includediagram{\diagramsDir/ml/olympic_LM_polynomial_number014}{\width}}{\animationName}
\newframe{\includediagram{\diagramsDir/ml/olympic_LM_polynomial_number015}{\width}}{\animationName}
\newframe{\includediagram{\diagramsDir/ml/olympic_LM_polynomial_number016}{\width}}{\animationName}
\newframe{\includediagram{\diagramsDir/ml/olympic_LM_polynomial_number017}{\width}}{\animationName}
\newframe{\includediagram{\diagramsDir/ml/olympic_LM_polynomial_number018}{\width}}{\animationName}
\newframe{\includediagram{\diagramsDir/ml/olympic_LM_polynomial_number019}{\width}}{\animationName}
\newframe{\includediagram{\diagramsDir/ml/olympic_LM_polynomial_number020}{\width}}{\animationName}
\newframe{\includediagram{\diagramsDir/ml/olympic_LM_polynomial_number021}{\width}}{\animationName}
\newframe{\includediagram{\diagramsDir/ml/olympic_LM_polynomial_number022}{\width}}{\animationName}
\newframe{\includediagram{\diagramsDir/ml/olympic_LM_polynomial_number023}{\width}}{\animationName}
\newframe{\includediagram{\diagramsDir/ml/olympic_LM_polynomial_number024}{\width}}{\animationName}
\newframe{\includediagram{\diagramsDir/ml/olympic_LM_polynomial_number025}{\width}}{\animationName}
\newframe{\includediagram{\diagramsDir/ml/olympic_LM_polynomial_number026}{\width}}{\animationName}
\newframe{\includediagram{\diagramsDir/ml/olympic_LM_polynomial_number027}{\width}}{\animationName}
\newframe{\includediagram{\diagramsDir/ml/olympic_LM_polynomial_number028}{\width}}{\animationName}
\newframe{\includediagram{\diagramsDir/ml/olympic_LM_polynomial_number029}{\width}}{\animationName}
\endanimation
}

\notes{\figure{\includediagram{\diagramsDir/ml/olympic_LM_polynomial_number002}{80%}}{Fit of a 1 degree polynomial to the olympic marathon data.}{olympic-lm-polynomial-num-basis-02}}

\notes{\figure{\includediagram{\diagramsDir/ml/olympic_LM_polynomial_number003}{80%}}{Fit of a 2 degree polynomial to the olympic marathon data.}{olympic-lm-polynomial-num-basis-03}}



                            
\endif

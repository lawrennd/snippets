\ifndef{resolveDeployInnovate}
\define{resolveDeployInnovate}
\setupcode{import mlai.plot as plot}

\plotcode{plot.three_pillars_innovation(diagrams='\writeDiagramsDir/ai')}

\notesfigure{\includediagram{\diagramsDir/ai/three_pillars_innovation003}}

\setupdisplaycode{import notutils as nu}
\displaycode{nu.display_plots('three-pillars-innovation{sample:0>3}.svg', 
                            '\writeDiagramsDir/ai', sample=(1,3))}

\slides{
### Three Pillars of Disruption {.slide: data-transition="none"}

\includediagram{\diagramsDir/ai/three-pillars-innovation001}

### Three Pillars of Disruption {.slide: data-transition="none"}

\includediagram{\diagramsDir/ai/three-pillars-innovation002}

### Three Pillars of Disruption {.slide: data-transition="none"}

\includediagram{\diagramsDir/ai/three-pillars-innovation003}
}


\endif

\ifndef{dataOrientedArchitecturesIntro}
\define{dataOrientedArchitecturesIntro}

\editme

\subsection{Data Oriented Architectures}


\slides{
* View data to a *first-class citizen*.
* Prioritise decentralisation.
* Openness
}
\notes{In a streaming architecture we shift from management of services, to management of data streams. Instead of worrying about availability of the services we shift to worrying about the quality of the data those services are producing.}

\newslide{Data Orientated Architectures}

\slides{
* Historically we've been *software first*
    * A necessary but not sufficient condition for *data first*
* Move from
    1. service oriented architectures
	2. *data oriented architectures*
}
\notes{Historically we've been *software first*, this is a necessary but insufficient condition for *data first*. We need to move from software-as-a-service to data-as-a-service, from service oriented architectures to *data oriented architectures*.}


\subsection{Data Oriented Principles}

\figure{\includediagramclass{\diagramsDir/software/data-oriented-principles}{80%}}{For an overview of data oriented principles see @Cabrera-realworld23.}{data-oriented-principles}

\notes{Our work comes from surveying machine learning case studies [@Paleyes-challenges22] identifying the challenges and then surveying papers that focus on deployment [@Cabrera-realworld23] and identifying the principles they use.}

\notes{The philosphy of DOA is also possible with more standard data infrastructures, such as SQL data bases, but more work has to be put into place to ensure that book-keeping around data provenance and origin is stored, as well as approaches for snapshotting the data ecosystem. Our studies [@Paleyes-flow22] have made a lot of use of flow based programming [@Paleyes-flow22].}

\endif

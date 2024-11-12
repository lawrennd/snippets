\ifndef{doaCaseStudy}
\define{doaCaseStudy}
\define{claudeSonnet35Content}

\editme

\subsection{Case Study: Water Level Monitoring}

\notes{A practical example of DOA principles being applied can be seen in the water level monitoring project at Dedan Kimathi University of Technology (DeKUT) in Kenya, monitoring the Ewaso Nyiro River. This real-world implementation demonstrates both the benefits and challenges of applying DOA principles.}

\slides{
* Water level monitoring project at DeKUT
* Monitors Ewaso Nyiro River in Kenya
* Demonstrates practical DOA implementation
}

\newslide{System Architecture}

\figure{\includediagram{\diagramsDir/data-science/water-monitoring-arch}{80%}}{Architecture of the water level monitoring system showing key components and data flows}{water-monitoring-arch}

\slides{
Key Components:
* Data Collection (sensor nodes)
* Listener Component 
* Anomaly Detection
* Visualization
}

\newslide{DOA Principles in Practice}

\notes{The system demonstrates the three core DOA principles, though with some practical limitations. The data-first approach is evident in the centralized data collection, while openness is implemented through MQTT-based communication. However, the heavy reliance on cloud resources presents opportunities for more decentralization.}

\slides{
Implementation of principles:
* Data-First: Centralized collection and storage
* Openness: MQTT publish-subscribe
* Decentralization: Potential for edge processing
}

\undef{claudeSonnet35Content}
\endif

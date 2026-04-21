\ifndef{informationFlowStructures}
\define{informationFlowStructures}

\editme

\subsection{How Information Flows in Organisations}

\notes{The information topography of an organisation is how information flows through the organisaiton. At one level this will involve a hierarchy of information propagation: the  chart of reporting lines. But alongside this there are other mechanisms to share information.}

\notes{This dictates the organisations "absorbtive capacity which in turn dictates how it will make decisions. The nature of decisio of decisions depend on how well the information that feeds them can travel.}

\notes{Classically information propagates through two principle patterns. Hub-and-spoke networks, and peer-to-peer meshes. The hub-and-spoke becomes a hierarchy as it scales. The different mechanisms have different  implications for bandwidth, latency, and resilience.}

\figure{\includediagram{\diagramsDir/business/corporate-hierarchy-information-flow}{90%}}{In a classical corporate hierarchy, information travels vertically. Strategic decisions flow downward from the CEO through the C-suite (CFO, CIO, COO) to functional departments. Data and reports flow upward. External signals from customers and markets enter at the top. Each layer introduces delay and compression.}{corporate-hierarchy-information-flow}

\newslide{Hub-and-Spoke}

\notes{The hub-and-spoke model centralises information processing. All communication between departments routes through a central function. This works well for "command and control" but the central node tends to become overloaded. In practive that's why we obtain a hierarchy so each spoke is itself a hub for the next level. }

\figure{\includediagram{\diagramsDir/business/hub-and-spoke-information-flow}{90%}}{In a hub-and-spoke model, all information routes through a central node. This can result in low latency (good command and control) but the central hub can become overloaded.}{hub-and-spoke-information-flow}

\newslide{Peer-to-Peer}

\notes{Peer-to-peer structures allow direct communication between teams without a central intermediary. This maximises bandwidth and reduces latency, but requires more communication interfaces than are managed with hub-and-spoke. Amazon's API mandate — requiring all teams to expose their capabilities through programmatic interfaces — is an example of deliberately engineering a peer-to-peer information structure within a large organisation. The challenge is coordination: without a hub, norms and protocols must emerge from the network itself. This is where culture becomes important}

\figure{\includediagram{\diagramsDir/business/peer-to-peer-information-flow}{90%}}{In a peer-to-peer network, teams communicate directly with each other through adjacent and cross-cutting channels, without routing through a central authority. This structure is resilient and high-bandwidth, but requires shared protocols and trust. It mirrors how open-source software communities and federated data ecosystems operate.}{peer-to-peer-information-flow}

\endif

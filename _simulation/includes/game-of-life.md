\ifndef{gameOfLife}
\define{gameOfLife}

\editme


\subsection{Game of Life}

\notes{[John Horton Conway](https://en.wikipedia.org/wiki/John_Horton_Conway) was a mathematician who developed a game known as the Game of Life. He died in April 2020, but since he invented the game, he was in effect 'god' for this game. But as we will see, just inventing the rules doesn't give you omniscience in the game.}

\notes{The Game of Life is played on a grid of squares, or pixels. Each pixel is either on or off. The game has no players, but a set of simple rules that are followed at each turn the rules are.}

\include{_simulation/includes/life-rules.md}
\include{_simulation/includes/life-implementation.md}
\include{_simulation/includes/life-glider-loafer-conway.md}

\notes{Once these patterns are discovered, they are combined (or engineered) to create new Life patterns that do some remarkable things. For example, there's a life pattern that runs a Turing machine, or more remarkably there's a Life pattern that runs Life itself.}

\newslide{}

\figure{\includegif{\diagramsDir/simulation/life-in-life}{80%}}{The Game of Life running in Life. The video is drawing out recursively showing pixels that are being formed by filling cells with moving spaceships. Each individual pixel in this game of life is made up of $2048 \times 2048$ pixels called an [OTCA metapixel](https://www.conwaylife.com/wiki/OTCA_metapixel).}{life-in-life}

\notes{To find out more about the Game of Life you can watch this video by Alan Zucconi or read his [associated blog post](https://www.alanzucconi.com/2020/10/13/conways-game-of-life/).}

\newslide{}

\figure{\includeyoutube{Kk2MH9O4pXY}{600}{450}}{An introduction to the Game of Life by Alan Zucconi.}{intro-to-life}


\notes{Contrast this with our situation where in 'real life' we don't know the simple rules of the game, the state space is larger, and emergent behaviors (hurricanes, earthquakes, volcanos, climate change) have direct consequences for our daily lives, and we understand why the process of 'understanding' the physical world is so difficult. We also see immediately how much easier we might expect the physical sciences to be than the social sciences, where the emergent behaviors are contingent on highly complex human interactions.}

\endif

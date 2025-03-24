\ifndef{validGames}
\define{validGames}

\editme

\subsection{Valid Games}

\notes{The histogram game allows us to explore the notion of valid games.}

\notes{Our thought experiment suggested that all games should appear to start from an *origin*, a very entropy point. We define a game to be valid if it is reachable by steepest ascent from an origin.} 

\notes{Conceptually we can check whether a game configuration is valid in the following manner. Starting with the configuration, we descend the entropy gradient in the steepest direction until we reach the origin. We then attempt to return to our original configuration through steepest ascent. If the original configuration cannot be recovered in this way we say that that configuration is invalid.}

\include{_information-game/includes/jaynes-world-histogram-valid-games-example.md}

\endif
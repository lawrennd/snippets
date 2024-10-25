\ifndef{causalitySection}
\define{causalitySection}

\editme

\subsection{Causality}

\figure{\includeyoutube{yksduYxEusQ}{600}{450}}{Judea Pearl and Elias Bareinboim giving a Tutorial on Causality at NeurIPS in 2013. Again, the slides aren't synchronised, but you can find them separately [here](http://media.nips.cc/Conferences/2013/nips-dec2013-pearl-bareinboim-tutorial-full.pdf).}{judea-pearl-causality}

\notes{All these approaches offer a lot of promise for developing machine learning at the interface with science but covering each in detail would require four separate modules. We've chosen to focus on the emulation approach, for two principal reasons. Firstly, it's conceptual simplicity. Our aim is to replace all or part of our simulation with a machine learning model. Typically, we're going to want uncertainties as part of that representation. That explains our focus on Gaussian process models. Secondly, the emulator method is flexible. Probabilistic programming requires that the simulator has been built in a particular way, otherwise we can't compile the program. Finally, the emulation approach can be combined with any of the existing simulation approaches. For example, we might want to write our emulators as probabilistic programs. Or we might do causal analysis on our emulators, or we could speed up the simulation in ABC through emulation.}

\endif
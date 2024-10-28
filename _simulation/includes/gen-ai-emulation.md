\ifndef{genAiEmulation}
\define{genAiEmulation}

\editme

\subsection{Generative AI for Emulation}

\slides{* Modern ML models can learn from simulation histories
* Example: [GraphCast for weather prediction](https://deepmind.google/discover/blog/graphcast-ai-model-for-faster-and-more-accurate-global-weather-forecasting/)
  * Trained on archived weather forecasts
  * Faster than traditional numerical simulation
  * Maintains high accuracy
* Key requirement: Large archive of simulation runs
  * <https://github.com/google-deepmind/graphcast>}

\notes{While Gaussian processes provide an excellent framework for emulation when we have relatively few simulation runs, modern generative AI approaches become powerful when we have extensive archives of previous simulations. Google DeepMind's GraphCast system provides an excellent example of this approach in weather forecasting.}

\notes{Traditional numerical weather prediction requires solving complex partial differential equations on supercomputers, taking hours to complete. [GraphCast](https://deepmind.google/discover/blog/graphcast-ai-model-for-faster-and-more-accurate-global-weather-forecasting/) was trained on archived weather forecasts from the European Centre for Medium-Range Weather Forecasts (ECMWF) [@Lam-graphcast23]. This ECMWF dataset - containing millions of previous forecasts and their outcomes - allowed the model to learn the complex patterns and physics underlying weather systems.}

\figure{\includeyoutube{Q6fOlW-Y_Ss}{800}{600}}{YouTube video of results from the GraphCast algorithm.}{graphcast-results}

\notes{As a result GraphCast can produce forecasts of similar accuracy to traditional numerical methods in seconds rather than hours. This is possible because:
1. The model has seen millions of examples of how weather patterns evolve
2. The underlying physics, while complex, has regularities that can be learned
3. The training data comes from a consistent, high-quality source of simulations

In many domains, we don't have access to such a vast archive and must rely on more data-efficient approaches like Gaussian processes.}

\endif

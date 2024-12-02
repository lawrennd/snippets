\ifndef{stochasticProcessComposition}
\define{stochasticProcessComposition}

\editme

\subsection{Stochastic Process Composition}

\notes{In deep learning we compose functions together to form more complex functions. In the same way, we can compose stochastic processes to form more complex stochastic processes.}
$$\dataVector = \mappingFunctionVector_4\left(\mappingFunctionVector_3\left(\mappingFunctionVector_2\left(\mappingFunctionVector_1\left(\inputVector\right)\right)\right)\right)$$

\slides{* Compose functions together to form more complex functions
* Compose stochastic processes to form more complex stochastic processes}

\notes{This means that not only is the composed function more complex, but the composed stochastic process has more complex characteristics, for example composing two Gaussian processes together results in a non-Gaussian process.}

\newslide{Composing Gaussian Processes}

\slides{* Compose two Gaussian processes together
* Resulting process is non-Gaussian}

\endif

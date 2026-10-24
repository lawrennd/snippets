\ifndef{embodimentFactorsCelsius}
\define{embodimentFactorsCelsius}

\editme

\subsection{Information and Embodiment}

\figure{\aligncenter{\includejpg{\diagramsDir/ClaudeShannon_MFO3807}{40%}}\aligncenter{*Claude Shannon*}}{Claude Shannon (1916-2001)}{claude-shannon}

\speakernotes{Just as we measure temperature. Just as Celsius gave us the scale for temperature, so entropy measures ignorance. Formalised most famously by Claude Shannon}


\newslide{Embodiment Factors}

\figure{\include{_ai/includes/embodiment-factors-computer-human-table.html}}{Embodiment factors are the ratio between our ability to compute and our ability to communicate. Relative to the machine we are also locked in. In the table we represent embodiment as the length of time it would take to communicate one second's worth of computation. For computers it is a matter of minutes, but for a human, it is a matter of thousands of millions of years.}{embodiment-factors-table}

\notes{I am using voice, sound, to communicate with you. Those communications propagate at about 300 metres per second. The speed of light is about $3\times 10^{8}$ metres per second --- a million times larger than 300. If I had stood here and given this lecture by sending light waves instead of speaking, I would have gone a million times faster, even using the same mode of communication.

Now look at bits per minute. I am probably speaking at 150 words a minute. Shannon's later paper on printed English estimated $11.82$ bits per word from word frequencies (Zipf's law, no context) [@Shannon-prediction51]. That is the "$\sim 12$ bits per word" figure; it is not from the 1948 paper. With context his estimates fall to around one bit per letter, so true word entropy is much lower. Using the crude $12$ bits/word figure I am speaking to you at about $2{,}000$ bits per minute, or about $30$ bits per second. The "$10$--$60$ bits/s" band is that same crude estimate at typical speaking rates [@Reed-information98,@Lawrence-embodiment17,@Lawrence-atomic24], not Shannon's context-conditioned entropy. Two machines on a gigabit link are not merely a million times faster than that. The difference in their communication rates, relative to us, is the difference between walking --- one metre per second --- and the speed of light.

Computationally our brain is very fast. The best estimates we have suggest you would need a very large computer to simulate it. If one computer wants to tell another computer everything it computed in one second, my estimate is that it would take about 20 minutes. For a human the ratio is far larger. At $2{,}000$ bits per minute, a billion calculations per second would take about a year to talk out. The slogan in the table --- around a billion years --- needs around $10^{18}$ calculations per second, a "billion billion". That is an order-of-magnitude claim with those two assumptions stated, not a measured brain flop rate. I cannot access one second of neuron firings, and the computer cannot access it either.

We can talk about embodiment physically, in terms of what it means to touch something, and in terms of what it means to sense the world. This difference in our context, in what we are doing in our relationship with the world, is what defines our intelligence.}

\endif
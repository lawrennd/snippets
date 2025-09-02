\ifndef{footballSpatialTemoralLocality}
\define{footballSpatialTemoralLocality}

\editme

\subsection{Spatial (and Temporal) locality}

\figure{\includepng{\diagramsDir/datasets/storage-pyramid}}{60%}{}

\notes{Spatial locality means a program is likely to access nearby memory addresses soon after accessing one (e.g., iterating through an array). CPUs exploit both by loading data from RAM based on expected patterns of use.

Temporal locality benefits from keeping recently used data in cache, while spatial locality benefits from prefetching adjacent data to speed up sequential access.}

\notes{Let's test it out using a toy example - summing over 1m numbers, first in order, then randomly.}

\setupcode{import time}
\code{arr = [1]*10000000
indices = list(range(10000000))
start_time = time.time()
s = 0
for i in indices:
    s += arr[i]
print(s, time.time()-start_time)}

\setupcode{import random}
\code{arr = [1]*10000000
indices = list(range(10000000))
random.shuffle(indices)
start_time = time.time()
s = 0
for i in indices:
    s += arr[i]
print(s, time.time()-start_time)}

\notes{Mathematically speaking, these two operations are the same. Yet one takes about 5-10 times longer. This is exactly due to locality - it's much faster to read data that's right next to each other in memory.

Python's huge representations of data, and overused pointers, limit the capabilities of caching.}

\notes{It is a little bit silly to be optimising Python code, given how much inefficiency our choice of language brings on, but the considerations are still important, and translate to other systems you may build.}

\code{# temporal locality would be this - difference is quite small
# import time
# arr = [1]*10000000
# indices = [1]*10000000
# start_time = time.time()
# s = 0
# for i in indices:
#     s += arr[i]
# print(s, time.time()-start_time)}

\endif

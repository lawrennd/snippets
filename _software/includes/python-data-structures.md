\ifndef{pythonDataStructures}
\define{pythonDataStructures}

\editme

\subsubsection{Data Structures}

\notes{Hardware acceleration and memory layouts can only take us so far, usually some constant multiplier faster. For real step-changes in performance, we need to be mathematically clever about how we arrange our data.}

\subsubsection{Basic data structures}

\notes{```
list
tuple
set
dict
```}

\notes{By default, you would use a list for data. But other data types have their advantages too - set has very quick lookups, dict has quick lookups and stores values, and tuple is mutable and hashable (more on that later).}

\notes{Example where set massively outperforms a list:}

\setupcode{import time
import random}

\code{data_list = list(range(1000000))
queries = [random.randint(0, 2000000) for _ in range(1000)]

start_time = time.time()
hits = sum(1 for q in queries if q in data_list)
print(hits, time.time() - start_time)}

\code{data_set = set(range(1000000))

start_time = time.time()
hits = sum(1 for q in queries if q in data_set)
print(hits, time.time() - start_time)}

\subsubsection{Other useful data structures}

\subsubsection{Counter}

\setupcode{from collections import Counter}

\code{with open('football_data/leagueteamlinks.csv') as f:
  leagues = ([x.split(',')[12] for x in f.read().split('\n')[1:-1]]) # 13th column is leagueid
c = Counter(leagues)
print(c)}

\notes{*To be expanded as I get reminded of cool things.*}

\endif

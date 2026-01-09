\ifndef{footballPythonMemoryManagement}
\define{footballPythonMemoryManagement}

\editme

\subsubsection{Memory}

\notes{
Something not many people think about, is what these actually are, under the hood.}

\code{True, '1', 1, 1.0}

\notes{Someone coming from a C++ background, would call the above `primitives` - expecting them to just be raw data in memory.}

\code{type(True), type('1'), type(1), type(1.0)}

\notes{Let's check this assumption - we would expect a bool to take `1 bit` or `1 byte`, int `1-4 bytes`, string `1-2 bytes`, and float `4 bytes`}

\setupcode{import sys}
\code{sys.getsizeof(True), sys.getsizeof('1'), sys.getsizeof(1), sys.getsizeof(1.0)}

\notes{The above numbers look nothing like our predictions - why is that?

Turns out, in Python, everything is actually an object. The simple `1` we saw above is represented in memory as:

```
ob_refcnt: 8 bytes
ob_type: 8 bytes
ob_size: 8 bytes (Py_ssize_t)
ob_digit: 4 bytes per 30 bits of int
```

The four types above are somewhat special in Python too, with a slightly different implementation than other objects. Other types and structures are built up in similar ways, but don't store actual values inside, but rather pointers to "primitives" objects.}

\notes{In the example above we needed 28 bytes to encode one bit of information. Native Python is insanely inefficient for operations on large data. This memory design also impacts other ways in which we accelerate data operations, namely caching.}

\endif

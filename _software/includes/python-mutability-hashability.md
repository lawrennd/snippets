\ifndef{pythonMutabilityHashability}
\define{pythonMutabilityHashability}

\editme

\subsubsection{Mutability}

\code{l1, l2, l3 = ['apple'], ['banana'], ['cherry']
list_of_lists = [l1, l2, l3]
s1, s2, s3 = 'apple', 'banana', 'cherry'
list_of_strings = [s1, s2, s3]
print(list_of_lists, list_of_strings)}

\code{l3[0] = 'cranberry'
s3 = 'cranberry'
print(l3, s3)
print(list_of_lists)
print(list_of_strings)}

\notes{This will be particularly important when working with Pandas, when operations on rows will sometimes be in-place, and sometimes return new objects. You will get serious silent bugs if you're not careful.}

\subsubsection{Hashability}

\notes{
Python property, means roughly "can convert this to a number for lookups".}

\code{try:
    s = {'a', 'b', 'c', ['d', 'e']}
    print(s)
except TypeError as e:
    print(e)}

\code{{'a', 'b', 'c', ('d', 'e')}}

\code{dict_ = {1: 'one', 2: 'two', (3, 4): 'three or four'}
dict_[(3, 4)]}

\endif

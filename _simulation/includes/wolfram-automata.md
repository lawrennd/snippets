\ifndef{wolframAutomata}
\define{wolframAutomata}


\editme


\subsection{Wolfram Automata}

\notes{Cellular automata are systems with simple rules that lead to complex behaviours. A simple cellular automata can be defined over one dimension of cells binary cells, and a discrete time evolution. At each time step a cell's state is dependent on its state in a previous time step and that of its neighbours.}

\notes{Stephen Wolfram noticed that such systems could be represented by a binary number that described the nature of these rules. Each cell ($x$) has a state at time $t$, and the state of two neighbours ($x+1$ and $x-1$ at time $t$. The cellular automata dictates what the value of that cell will be at time $t+1$. The possible values of the cell are $1$ or $0$.}

\notes{This simple system has eight different input states (three bits associated with the cell and its two neighbours). And two possible output states (one bit associated with the cell's output state). so the rules of the cellular automata can be expressed by exhaustively running through the eight different input states giving the output state. To do this requires a string of eight bits (or a byte) long: one output per different input. That means there are 256 different possible cellular automata.}

\notes{Wolfram numbered the different cellular automata according to the output states in an 8 bit binary number, each bit indexed by the three bits of the input states (most significant bit first). So Rule 0 would give zero output regardless of the input state. Rule 1 will give an output of 1 for the input state of three zeros etc and Rule 255 will give an output of 1 regardless of the input state.}


\endif

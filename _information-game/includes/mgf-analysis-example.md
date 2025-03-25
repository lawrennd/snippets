\ifndef{mgfAnalysisExample}
\define{mgfAnalysisExample}

\editme

\subsection{Detecting Transitions with Moment Generating Functions}

\notes{The moment generating function (MGF) provides a powerful tool for analyzing variable transitions and detecting quantum-like vs. classical behavior.}

\slides{
* MGF: $M_Z(t) = \mathbb{E}[e^{tZ}] = \exp(A(\theta+t) - A(\theta))$
* Cumulant generating function: $K_Z(t) = \log M_Z(t)$
* Quantum-like variables: Oscillatory MGF behavior
* Classical variables: Monotonic MGF growth
* MGF reveals channel properties without needing state information
}

\notes{
For each variable in our system, we can compute its moment generating function (MGF):

$$M_{Z_i}(t) = \mathbb{E}[e^{tZ_i}] = \exp(A(\theta + te_i) - A(\theta))$$

where $e_i$ is the standard basis vector for the $i$-th coordinate.

The behavior of this MGF reveals whether a variable is functioning in a quantum-like or classical regime:

1. **Quantum-like variables** show oscillatory MGF behavior, with complex analytic structure
2. **Classical variables** show monotonic MGF growth, with simple analytic structure

This provides a diagnostic tool to identify which variables are functioning as quantum-like information reservoirs versus classical processing components.
}

\setupcode{import numpy as np}


\helpercode{
# Visualizing MGF differences between quantum-like and classical variables

# Define example MGF functions
def quantum_like_mgf(t):
    """MGF with oscillatory behavior (quantum-like)"""
    return np.exp(t**2/2) * np.cos(2*t)

def classical_mgf(t):
    """MGF with monotonic growth (classical)"""
    return np.exp(t**2/2)
}

\code{
# Create a range of t values
t = np.linspace(-3, 3, 1000)

# Compute MGFs
qm_mgf = quantum_like_mgf(t)
cl_mgf = classical_mgf(t)
}

\setupplotcode{import matplotlib.pyplot as plt
import mlai.plot as plot
import mlai}

\plotcode{# Create figure
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Plot MGFs
ax1.plot(t, qm_mgf, 'b-', label='Quantum-like variable')
ax1.plot(t, cl_mgf, 'r-', label='Classical variable')
ax1.set_xlabel('t')
ax1.set_ylabel('M(t)')
ax1.set_title('Moment (Cummulant) Generating Functions')
ax1.legend()
ax1.grid(True, linestyle='--', alpha=0.7)

# Plot log derivatives (oscillation index)
d_qm_log_mgf = np.gradient(np.log(np.abs(qm_mgf)), t)
d_cl_log_mgf = np.gradient(np.log(cl_mgf), t)

ax2.plot(t, d_qm_log_mgf, 'b-', label='Quantum-like variable')
ax2.plot(t, d_cl_log_mgf, 'r-', label='Classical variable')
ax2.set_xlabel('t')
ax2.set_ylabel('$\\frac{\\text{d} \\log M(t)}{\\text{d}t}')
ax2.set_title('Log-Derivative of MGF')
ax2.legend()
ax2.grid(True, linestyle='--', alpha=0.7)

mlai.write_figure(filename='oscillation-in-cummulant-generating-function.svg', 
                  directory = '\writeDiagramsDir/information-game')
}

\notes{The oscillation in the derivative of the log-MGF provides a clear signature of quantum-like behavior. This "oscillation index" can be used to quantify how much a variable displays quantum versus classical characteristics.

This analysis offers a practical method to detect the quantum-classical transition in our information reservoirs without needing to directly observe the system's internal state. It connects directly to information-theoretic channel properties and provides a bridge between our abstract model and experimentally observable quantities.
} 

\endif

\ifndef{landauerShannonConnection}
\define{landauerShannonConnection}

\editme

\subsection{Is Landauer's Limit Related to Shannon's Gaussian Channel Capacity?}

\notes{Digital memory can be viewed as a communication channel through time - storing a bit is equivalent to transmitting information to a future moment. This perspective immediately suggests that we look for a connection between Landauer's erasure principle and Shannon's channel capacity. The connection might arise because both these systems are about maintaining reliable information against thermal noise.}

\notes{The Landauer limit [@Landauer-irreversibility61] is the minimum amount of heat energy that is dissapated when a bit of information is erased. Conceptually it's the potential energy associated with holding a bit to an identifiable single value that is differentiable from the background thermal noise (representated by temperature).}

\notes{The Gaussian channel capacity [@Shannon-info48] represents how identifiable a signal $S$, is relative to the background noise, $N$. Here we trigger a small exploration of potential relationship between these two values.}

\slides{
* Memory $\equiv$ Communication through time
* Storage is transmission to future
* Both limited by thermal noise
}

\notes{When we store a bit in memory, we maintain a signal that can be reliably distinguished from thermal noise, just as in a communication channel. This suggests that Landauer's limit for erasure of one bit of information, $E_{min} = k_BT$, and Shannon's Gaussian channel capacity,
$$
C = \log_2\left(1 + \frac{S}{N}\right),
$$ 
might be different views of the same limit.}

\notes{Landauer's limit states that erasing one bit of information requires a minimum energy of $E_{\text{min}} = k_BT$. For a communication channel operating over time $1/B$, the signal power $S = EB$ and noise power $N = k_BTB$. This gives us:
$$
C = \frac{1}{2}\log_2\left(1 + \frac{S}{N}\right) = \frac{1}{2}\log_2\left(1 + \frac{E}{k_BT}\right)
$$
where the bandwidth B cancels out in the ratio.}

\notes{When we operate at Landauer's limit, setting $E = k_BT$, we get a signal-to-noise ratio of exactly 1:
$$
\frac{S}{N} = \frac{E}{k_BT} = 1
$$
This yields a channel capacity of exactly half a bit per second,
$$
C = \frac{1}{2}\log_2(2) = \frac{1}{2} \text{ bit/s}
$$}

\notes{The factor of 1/2 appears in Shannon's formula because of Nyquist's theorem - we need two samples per cycle at bandwidth B to represent a signal. The bandwidth $B$ appears in both signal and noise power but cancels in their ratio, showing how Landauer's energy-per-bit limit connects to Shannon's bits-per-second capacity.}

\slides{
* At Landauer's limit: $E = k_BT$
* Gives $\frac{S}{N} = 1$
* Results in capacity of $\frac{1}{2}$ bit/s
* Fundamental connection between energy and information
}

\notes{This connection suggests that Landauer's limit may correspond to the energy needed to establish a signal-to-noise ratio sufficient to transmit one bit of information per second. The temperature $T$ may set both the minimum energy scale for information erasure and the noise floor for information transmission.}

\subsection{Implications for Information Engines}

\notes{This connection suggests that the fundamental limits on information processing may arise from the need to maintain signals above the thermal noise floor. Whether we're erasing information (Landauer) or transmitting it (Shannon), we need to overcome the same fundamental noise threshold set by temperature.}

\slides{
* Information engines must overcome thermal noise
* Related threshold for:
    * Information erasure
    * Information transmission
* Temperature sets fundamental noise floor
}
\notes{This perspective suggests that both memory operations (erasure) and communication operations (transmission) are limited by the same physical principles. The temperature $T$ emerges as a fundamental parameter that sets the scale for both energy requirements and information capacity.}

\notes{The connection between Landauer's limit and Shannon's channel capacity is intriguing but still remains speculative. For Landauer's original work see @Landauer-irreversibility61, Bennett's review and developments see @Bennett-thermodynamics82, and for a more recent overview and connection to developments in non-equilibrium thermodynamics @Parrondo-thermodynamics15.}

\endif 

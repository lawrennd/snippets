\ifndef{maxentReferenceMeasureDensityOfStates}
\define{maxentReferenceMeasureDensityOfStates}

\editme

\subsection{Minimise KL to a Measure}

\slides{Equivalently minimise $\KL{f}{m}$ under a kinetic constraint. The answer depends on $m$.}

\slidesincremental{
* Same constraint: $\langle\tfrac12 m_{\mathrm{mass}}v^2\rangle$ fixed
* Minimise $\KL{f}{m}$ (or maximise $-D(f\|m)$)
* $m$ Lebesgue on component $v_x$ $\Rightarrow$ Gaussian
* $m$ Lebesgue on 3D velocity ($m(v)\propto v^2$ in speed) $\Rightarrow$ Maxwell--Boltzmann
}

\speakernotes{Continuous MaxEnt example after the discrete die. Relative entropy to $m$ is the KL we named earlier. The $v^2$ that looked like a Jacobian is the density of states — the reference measure in the speed coordinate. Same principle; declared prior.}

\notes{Write continuous MaxEnt as minimising KL (relative entropy) to a reference measure $m$,
\begin{align}
\KL{f}{m}=\int f\log\frac{f}{m}\,dx = D(f\|m),
\end{align}
or equivalently maximising $h_m(f)=-D(f\|m)$, subject to mean kinetic energy $\langle E\rangle=\langle\tfrac12 m_{\mathrm{mass}}|\mathbf{v}|^2\rangle$. The solution is
\begin{align}
f(\mathbf{v})\propto m(\mathbf{v})\,e^{-\beta E(\mathbf{v})}.
\end{align}
If $m$ is Lebesgue on a Cartesian component $v_x$, the MaxEnt density is Gaussian. If $m$ is Lebesgue on three-dimensional velocity space, then in the speed coordinate the reference density is proportional to the shell volume $v^2$, and MaxEnt recovers the Maxwell--Boltzmann speed distribution. The $v^2$ factor is the density of states. Declaring $m$ makes the choice of "equally likely a priori" explicit instead of hiding it in the coordinate chart.}

\newslide{Same Principle, Declared Prior}

\slidesmall{
$$
f\propto m(\cdot)\,e^{-\beta E}
\qquad
\begin{cases}
m\sim\mathrm{Lebesgue}(v_x) & \Rightarrow\text{Gaussian component}\\
m\sim v^2\,dv & \Rightarrow\text{Maxwell--Boltzmann}
\end{cases}
$$
}

\slidesincremental{
* Exponential family always carries a base measure
* For the ideal gas, that base measure is the density of states
* Coordinate dependence of $h$ was a symptom; $\KL{f}{m}$ is the cure
}

\endif

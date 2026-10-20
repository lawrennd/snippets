\ifndef{maxentReferenceMeasureDensityOfStates}
\define{maxentReferenceMeasureDensityOfStates}

\editme

\subsection{MaxEnt Needs a Reference Measure}

\slides{Maximise $-D(f\|m)$ at fixed mean energy. The answer depends on $m$.}

\slidesincremental{
* Same constraint: $\langle\tfrac12 m_{\mathrm{mass}}v^2\rangle$ fixed
* $m$ uniform in component $v_x$ $\Rightarrow$ Gaussian
* $m$ uniform in 3D velocity ($m(v)\propto v^2$ in speed) $\Rightarrow$ Maxwell speed law
}

\speakernotes{Callback to week 3: $h=-D(f\|m)$. The $v^2$ that looked like a Jacobian is the density of states — the reference measure written in the speed coordinate. Same MaxEnt principle; different undeclared prior.}

\notes{Write continuous MaxEnt as minimising relative entropy to a reference measure $m$, or equivalently maximising $h_m(f)=-D(f\|m)$, subject to mean energy $\langle E\rangle=\langle\tfrac12 m_{\mathrm{mass}}|\mathbf{v}|^2\rangle$. The solution is
\begin{align}
f(\mathbf{v})\propto m(\mathbf{v})\,e^{-\beta E(\mathbf{v})}.
\end{align}
If $m$ is Lebesgue on a Cartesian component $v_x$, the MaxEnt density is Gaussian. If $m$ is Lebesgue on three-dimensional velocity space, then in the speed coordinate the reference density is proportional to the shell volume $v^2$, and MaxEnt recovers the Maxwell speed distribution. The $v^2$ factor is the density of states. Relative entropy makes the choice of ``equally likely a priori'' explicit instead of hiding it in the coordinate chart.}

\newslide{Same Principle, Declared Prior}

\slidesmall{
$$
f\propto m(\cdot)\,e^{-\beta E}
\qquad
\begin{cases}
m\sim\mathrm{Lebesgue}(v_x) & \Rightarrow\text{Gaussian component}\\
m\sim v^2\,dv & \Rightarrow\text{Maxwell speed}
\end{cases}
$$
}

\slidesincremental{
* Exponential family always carries a base measure
* For the ideal gas, that base measure is the density of states
* Coordinate dependence of $h$ was a symptom; $D(f\|m)$ is the cure
}

\endif

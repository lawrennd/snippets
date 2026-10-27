\ifndef{maxwellBoltzmannComponentsVsSpeed}
\define{maxwellBoltzmannComponentsVsSpeed}

\editme

\subsection{Maxwell--Boltzmann: Components Versus Speed}

\slides{Each Cartesian velocity component is Gaussian. Speed $v=|\mathbf{v}|$ is not.}

\slidesincremental{
* Component: $f(v_x)=\sqrt{m/(2\pi kT)}\,e^{-mv_x^2/2kT}$
* Speed: integrate the isotropic 3D Gaussian over angles
* Jacobian $d^3v = v^2\,dv\,d\Omega$ supplies the $v^2$ factor
}

\speakernotes{First look, as taught: Maxwell--Boltzmann is a Gaussian in the velocities. Then: the histogram of one component is Gaussian; the histogram of speed peaks away from zero. Board the spherical shell volume briefly. Both statements are Maxwell--Boltzmann.}

\notes{Write the joint density on Cartesian velocities as isotropic,
\begin{align}
f(\mathbf{v})
  = \left(\frac{m}{2\pi kT}\right)^{3/2}
    \exp\Bigl(-\frac{m|\mathbf{v}|^2}{2kT}\Bigr).
\end{align}
Each marginal $f(v_x)$ is Gaussian. Change to spherical coordinates with $v=|\mathbf{v}|$ and solid angle $\Omega$. Probability conservation uses the volume element $d^3v = v^2\,dv\,d\Omega$. Integrating over angles ($\int d\Omega = 4\pi$) gives the Maxwell speed distribution
\begin{align}
f(v)
  = 4\pi\left(\frac{m}{2\pi kT}\right)^{3/2}
    v^2\,e^{-mv^2/2kT},
    \qquad v\ge 0.
\end{align}
The factor $v^2$ is the Jacobian of the change of variables — the density of states of spherical shells in velocity space. Calling ``Maxwell--Boltzmann'' Gaussian is correct for a component and wrong for speed.}

\newslide{Same Physics, Different Variable}

\slidesmall{
$$
f(v_x)=\sqrt{\tfrac{m}{2\pi kT}}\,e^{-mv_x^2/2kT}
\qquad\text{versus}\qquad
f(v)\propto v^2\,e^{-mv^2/2kT}
$$
}

\slidesincremental{
* The $v^2$ is not an energy correction — it is geometry
* Each component is the quadratic $E=mv_x^2/2$ whose expectation we split next
}

\endif

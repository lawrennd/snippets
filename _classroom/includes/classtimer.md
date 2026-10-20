\ifndef{classtimer}
\define{classtimer}

\editme

\subsection{Class test timer}

\notes{For an in-class test or timed exercise, insert a full-bleed
countdown slide with the lamd macro `classtimer`, passing the duration
as its argument. Examples: ten minutes as `10:00`, fifteen minutes as
`900` seconds, or one and a half hours as `1:30:00`.}

\notes{On HTML slides the timer fills the viewport with Start,
Pause/Resume and Reset controls, and flashes when time is up. Other
output formats omit the interactive clock; notes keep a short
placeholder naming the duration. The page is served from
`scriptsDir/timer/` in the talks repository.}

\slides{
* Full-bleed countdown for class tests
* Pass duration to the `classtimer` macro (`MM:SS` or seconds)
* Start / Pause / Reset; flashes when finished
}

\endif

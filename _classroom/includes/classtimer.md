\ifndef{classtimer}
\define{classtimer}

\editme

\subsection{Class test timer}

\notes{For an in-class test or timed exercise, insert a full-bleed
countdown slide with the lamd macro `classtimer`, passing the duration
as its argument. Examples: ten minutes as `10:00`, fifteen minutes as
`900` seconds, or one and a half hours as `1:30:00`. An optional second
argument sets the on-timer label (for example `Quiz 2`) so the heading
stays readable on the dark background.}

\notes{On HTML slides the timer fills the viewport with Start,
Pause/Resume and Reset controls, and flashes when time is up. Arrow keys
still advance the parent Reveal deck; Space starts or pauses the clock.
Other output formats omit the interactive clock; notes keep a short
placeholder naming the duration. The page is served from
`scriptsDir/timer/` in the talks repository.}

\slides{
* Full-bleed countdown for class tests
* `\classtimer{10:00}` or `\classtimer{10:00}{Quiz 2}`
* Space starts/pauses; arrows still move the deck
}

\endif

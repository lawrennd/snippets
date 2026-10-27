\ifndef{josephBlackCalorimeter}
\define{josephBlackCalorimeter}

\editme

\subsection{Joseph Black and Heat as a Quantity}

\notes{Before heat was understood as a property, it was understood as a quantity. For Clausius, entropy was not yet a measure of uncertainty, but to try and understand what he was measuring we need to go back to heat. For our purposes the intellectual thread starts with Joseph Black (1728--1799) who is responsible for making heat a quantity you can measure, mix and even hide. This notion of *heat* as a measurable is different from the notion of *temperature* as a measurable.}

\newslide{Joseph Black}

\figure{\includejpg{\diagramsDir/physics/joseph-black}{40%}}{Joseph Black (1728--1799). Black was a physician and chemist at Glasgow, then Edinburgh. Stipple engraving by James Heath after Henry Raeburn, 1800 (Wellcome Collection / Wikimedia Commons, public domain).}{joseph-black}

\notes{Black lectured in medicine and chemistry, in the mid eighteenth century he was based in Glasgow, where he was a contemporary of James Watt. His work on heat was done while he was still a physician. It was published posthumously by John Robison as *Lectures on the Elements of Chemistry* (Edinburgh, 1803) [@Black-lectures03].}

\speakernotes{This is the Worksheet 1 follow-up. Clausius was not doing uncertainty. He was doing heat. We start with the person who made heat measurable. Do not yet write $\mathrm{d}Q/T$. Portrait, dates, Glasgow then Edinburgh, Watt as a colleague. Then the stuck thermometer.}

\newslide{The Problem}

\slides{Ice melts. The thermometer does not move.}

\slidesincremental{
* Heat is entering the mixture
* Temperature stays at the melting point until the ice is gone
* If heat *were* temperature, that would be a contradiction
}

\notes{Thermometers had existed since about the 17th century. This leads to a mystery, ice melts, but the temperature doesn't change. The same thing happens at the other end: water boils, steam is produced, and the thermometer sits at the boiling point. If you heat an equal mass of water equally as a mass of mercury, they do not change temperture equally. The important step that Joseph Black made was to realise that temperature and heat are separate quantities. Temperature is a reading, but heat is a 'quantity' that can enter that body without changing the reading.}

\newslide{Heat Is Not Temperature}

\slides{Temperature is the reading. Heat is a quantity you can add, mix, and hide.}

\slidesincremental{
* *Mixing*: known masses, known starting temperatures, one final temperature
* *Capacity*: when a substance absorbs heat at different rates
* *Latent* heat: when a substance 'swallows heat'
}

\notes{Black's mixing calorimetry is the mechanism. You account for heat as you would account for a fluid: what leaves one body arrives in the other. The maths is an additive ledger, not a kinetic theory. Mercury, he says, has less *capacity for the matter of heat* than water: the same heat produces a larger change of temperature. That is specific heat, named as a capacity. The heat that melts ice, or that turns water into steam, does not raise the temperature at all. Black calls it *latent*: combined with the particles, hidden from the thermometer, recovered when the change of state is reversed.}

\speakernotes{Keep mechanism and maths apart. Mechanism: mix, or melt ice, or time a kettle. Maths: heat as an additive quantity independent of the thermometer. Capacity first, then latent. Students often still hear ``heat'' as ``how hot''.}

\newslide{The Ice Calorimeter}

\figure{\includejpg{\diagramsDir/physics/ice-calorimeter}{45%}}{The calorimeter of Lavoisier and Laplace. Heat delivered is read as the mass of ice melted; the conversion factor is Black's latent heat of fusion. Plate XI from *Encyclopaedia Londinensis* (1801--02), after H. Lascelles (Wikimedia Commons / Science History Institute, public domain).}{ice-calorimeter}

\notes{Black did not build this box. He measured by mixing, and by timing how long a steady fire takes to melt ice or to boil a pan dry. The ice calorimeter is Lavoisier and Laplace in the winter of 1782--83: a sample in the inner chamber, a jacket of ice, an outer ice shield against the room. Heat that leaves the sample melts ice in the middle jacket; you weigh the meltwater. The conversion factor is Black's latent heat of fusion, about $143$--$144^\circ\mathrm{F}$ of heat per unit mass of ice. This is close to the modern figure of $80^\circ\mathrm{C}$, or $334\,\mathrm{kJ\,kg}^{-1}$. The instrument makes his accounting automatic: the thermometer is no longer the meter. The meltwater is.}

\speakernotes{Be precise if someone asks who invented the calorimeter. Black made heat measurable. This apparatus is Lavoisier and Laplace, using Black's latent heat of fusion as the scale. The picture is the mechanism: weigh what melted.}

\newslide{Latent Heat of Steam}

\slides{Black: about $810^\circ\mathrm{F}$ of latent heat --- the heat that would raise the same water by $810^\circ\mathrm{F}$.}

\slidesincremental{
* Ice to steam on his scale is $180^\circ\mathrm{F}$, so vaporisation is about four and a half times that interval
* The method is a kettle on a steady fire: time to the boil versus time to boil dry
* Heat losses make the figure low. Watt, by condensation: nearer $950^\circ\mathrm{F}$. Modern: about $967^\circ\mathrm{F}$, or $2256\,\mathrm{kJ\,kg}^{-1}$
}

\notes{Black's unit is the heat that raises an equal mass of water by one degree Fahrenheit. On that scale the interval from melting ice to boiling water is $180$ units. The extra heat to turn the boiling water into steam he estimates at about $810$ units: the pan sits on the fire four and a half times longer boiling dry than it did coming up to the boil. He knows the timing method is rough because the the fire is not a closed system. His contemporary, James Watt, condensing steam and measuring the water it warms, gets nearer $950$. The modern figure is about $967^\circ\mathrm{F}$ on the same scale, $540\,\mathrm{cal\,g}^{-1}$, or $2256\,\mathrm{kJ\,kg}^{-1}$: a little more than five times the heat that takes water from $0$ to $100^\circ\mathrm{C}$. The number is already important industrially. James Watt is famous for improving the efficiency of the steam engine. Until his time, a Newcomen engine would condense steam by spraying cold water onto the engine cylinder. That condensation occuring on the cylinder becomes latent heat that the engine has to re-pay on every stroke. Watt's invention of the separate condenser can be motivated by Black's latent heat.}

\speakernotes{Put Black's $810$ on the slide; the modern comparison lives in the notes. Do not fight over calories versus kilojoules. The point is the size: making steam swallows several times the heat that brought the water to the boil, and none of it shows on the thermometer.}

\endif

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

\notes{Thermometers had existed since about the 17th century. This leads to a mystery: ice melts, but the temperature doesn't change. The same thing happens at the other end: water boils, steam is produced, and the thermometer sits at the boiling point. If you heat an equal mass of water equally as a mass of mercury, they do not change temperature equally. The important step that Joseph Black made was to realise that temperature and heat are separate quantities. That is quite a big leap. Most children, and most of us at first, think heat and temperature are the same. Temperature is a reading, but heat is a quantity that can enter a body without changing the reading.}

\newslide{Heat Is Not Temperature}

\slides{Temperature is the reading. Heat is what you add.}

\slidesincremental{
* Mix two bodies of known mass and starting temperature; one final reading
* Equal heat, equal mass: mercury rises more than water --- different *capacity*
* Ice melts with the thermometer stuck --- heat can be hidden
}

\notes{Black's notion is that heat is a quantity you can add, mix, and hide. Take known masses, mix them, and they come up to a final temperature: the heat has mixed. Capacity is when something absorbs heat at a different rate. Mercury, he says, has less *capacity for the matter of heat* than water: the same heat produces a larger change of temperature. That is specific heat. The ice can start below zero, but once you get it to zero it stops absorbing heat --- it is swallowing heat, latent heat. The heat that turns water into steam does not raise the thermometer either. Recovered when the change of state is reversed.}

\speakernotes{Keep mechanism and maths apart. Mechanism: mix, or melt ice, or time a kettle. Maths: heat as an additive quantity independent of the thermometer. Capacity first, then latent. Students often still hear ``heat'' as ``how hot''.}

\newslide{The Ice Calorimeter}

\slides{Black mixed and timed. This box weighs meltwater.}

\figure{\includejpg{\diagramsDir/physics/ice-calorimeter}{45%}}{The calorimeter of Lavoisier and Laplace. Heat delivered is read as the mass of ice melted; the conversion factor is Black's latent heat of fusion. Plate XI from *Encyclopaedia Londinensis* (1801--02), after H. Lascelles (Wikimedia Commons / Science History Institute, public domain).}{ice-calorimeter}

\slidesincremental{
* Heat leaving the sample melts ice in the jacket
* You weigh what melted --- that *is* the heat
* The conversion is Black's latent heat of fusion
}

\notes{Black did not build this box. His own apparatus was an open fire and a pan. He tried to keep the fire steady --- bellows, not a closed system --- and timed how long it takes to melt ice or to boil a pan dry. The ice calorimeter is Lavoisier and Laplace in the winter of 1782--83: a sample in the inner chamber, a jacket of ice, an outer ice shield against the room. Heat that leaves the sample melts ice in the middle jacket; you weigh the meltwater. The conversion factor is Black's latent heat of fusion: the heat that would raise an equal mass of water by about $143$--$144$ Fahrenheit *degrees*. That is a quantity of heat, not a temperature on the thermometer. It is close to the modern figure of $80^\circ\mathrm{C}$, or $334\,\mathrm{kJ\,kg}^{-1}$. The thermometer is no longer the meter. The meltwater is.}

\notes{One of the striking things in this period, even though Britain and France are at war half the time, is how much scientific traffic there is between them, including people travelling. Laplace is famous in England. Lavoisier, with Laplace, forms an early table of chemical elements; Lavoisier is killed in the Revolution; Laplace survives it and later becomes a count under the Bourbon restoration. Their calorimeter is inspired by Black.}

\speakernotes{Be precise if someone asks who invented the calorimeter. Black made heat measurable. This apparatus is Lavoisier and Laplace, using Black's latent heat of fusion as the scale. The picture is the mechanism: weigh what melted.}

\newslide{Latent Heat of Steam}

\slides{A kettle on a steady fire. Time is the meter.}

\slidesincremental{
* Clock the water from ice-cold to the boil; then clock it boiling dry
* Boiling dry takes about four and a half times as long
* That extra heat does not move the thermometer. Black calls it *latent*
}

\notes{Black's unit of heat is not a temperature. It is the heat that raises an equal mass of water by one degree on Fahrenheit's thermometer. On that scale the interval from melting ice to boiling water is $180$ units. The extra heat to turn the boiling water into steam he estimates at about $810$ of those units: the pan sits on the fire four and a half times longer boiling dry than it did coming up to the boil --- say fifteen minutes to the boil, then about an hour and a quarter to evaporate. He knows the timing method is rough because the fire is not a closed system. His contemporary, James Watt, condensing steam and measuring the water it warms, gets nearer $950$, within a few percent of the modern figure. The modern figure is about $967^\circ\mathrm{F}$ on the same scale, $540\,\mathrm{cal\,g}^{-1}$, or $2256\,\mathrm{kJ\,kg}^{-1}$: a little more than five times the heat that takes water from $0$ to $100^\circ\mathrm{C}$.}

\notes{The number is already important industrially. Until Watt, a Newcomen engine condensed steam by spraying cold water onto the cylinder. That makes a vacuum and the piston comes down; then you heat the cylinder again and it goes up. The condensation on the cylinder is latent heat the engine has to repay on every stroke. Watt's question is: how much energy is that spray? His answer is the separate condenser --- take the steam out of the cylinder and cool it somewhere that is always cold. That is why the engine becomes more efficient. Manufacturing it takes him twenty-five to thirty years. Glasgow does not yet have the machinery; he has to come to Boulton in Birmingham. You do not see these engines in industrial use until about twenty years after the 1760s work. The Lap engine in the Science Museum in London is late 1770s, early 1780s.}

\speakernotes{Do not put $810^\circ\mathrm{F}$ on the slide. That number is a *quantity of heat* in Black's unit --- the heat that would raise the same water by one Fahrenheit degree --- not a temperature. The experiment is the kettle: time to the boil versus time to boil dry. Four and a half times as long, thermometer stuck. Watt and the modern figure live in the notes.}

\endif

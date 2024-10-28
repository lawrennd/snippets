\ifndef{pythonSimulationResources}
\define{pythonSimulationResources}

\editme

\subsection{Examples in Python}

\slides{* Wide range of Python simulation tools:
    * SimPy - Discrete event simulation
    * OpenAI Gym - Control problems
    * Fluid dynamics and FEA examples 
    * Domain-specific examples (F1, supply chain)}

\notes{There are many Python resources available for different types of simulation:

* General Purpose:
    * `simpy` provides [examples](https://simpy.readthedocs.io/en/latest/examples/) of machine shops, gas stations, car washes
    * The news vendor problem for [NFL jersey orders](https://github.com/fabryandrea/newsvendor)
    * [Amazon's supply chain simulation](https://github.com/amzn/supply-chain-simulation-environment)

* Control Systems:
    * [N-link pendulum](https://www.moorepants.info/blog/npendulum.html) using symbolic Python
    * [Mountain Car](https://github.com/openai/gym/blob/master/gym/envs/classic_control/mountain_car.py) in OpenAI Gym

* Scientific Computing:
    * [Hodgkin-Huxley neuron models](https://mark-kramer.github.io/Case-Studies-Python/HH.html)
    * [Formula One race simulation](https://github.com/rothnic/formulapy)
    * [Computational fluid dynamics](https://github.com/barbagroup/CFDPython)
    * [Finite element analysis](https://solidspy.readthedocs.io/en/latest/readme.html)}
	

\notes{There are a number of different simulations available in python, and tools specifically design for simulation. For example `simpy` has a [list of example simulations](https://simpy.readthedocs.io/en/latest/examples/) around machine shops, gas stations, car washes.}
\slides{
* [Simpy](https://simpy.readthedocs.io/en/latest/examples/gas_station_refuel.html)}

\notes{Operations research ideas like the newsvendor problem, can also be solved, Andrea Fabry provides an example of the newsvendor problem in python for order of [NFL replica jerseys here](https://github.com/fabryandrea/newsvendor).}
\slides{
* [News Vendor Problem](https://github.com/fabryandrea/newsvendor) in python (for ordering NFL Replica Jerseys.}

\notes{The news vendor problem is also a component in the Amazon supply chain. The Amazon supply chain makes predictions about supply and demand, combines them with a cost basis and computes optimal stock. Inventory orders are based on the difference between this optimal stock and current stock. The [MiniSCOT simulation](https://github.com/amzn/supply-chain-simulation-environment) provides code that illustrates this.}
\slides{
* [Amazon Supply Chain](https://github.com/amzn/supply-chain-simulation-environment)}

\notes{Control problems are also systems that aim to achieve objectives given a set of parameters. A classic control problem is the inverted pendulum. This [python code](https://www.moorepants.info/blog/npendulum.html) generalises the standard inverted pendulum using one with $n$-links using symbolic python code.}
\slides{
* [Trolley & Pendulum](https://www.moorepants.info/blog/npendulum.html) using sympy (symbolic python)}

\newslide{Examples in Python}

\notes{In reinforcement learning similar control problems are studied, a classic reinforcement learning problem is known as the [Mountain Car](https://github.com/openai/gym/blob/master/gym/envs/classic_control/mountain_car.py). You can work with this problem using an environment known as [OpenAI gym](https://github.com/openai/gym) that includes many different reinforcement learning scenarios.}
\slides{
* [Mountain Car](https://github.com/openai/gym/blob/master/gym/envs/classic_control/mountain_car.py) in the OpenAI Gym.
}

\notes{In neuroscience Hodgkin and Huxley studied the giant axon in squid to work out a set of differential equations that are still used today to model spiking neurons. Mark Kramer explains how to [simulate them in python here](https://mark-kramer.github.io/Case-Studies-Python/HH.html).}
\slides{
* [Hodgkin Huxley](https://mark-kramer.github.io/Case-Studies-Python/HH.html) by Mark Kramer.}

\notes{All Formula One race teams simulate the race to determine their strategy (tyres, pit stops etc). While those simulations are proprietary, there is sufficient interest in the wider community that race simulations have been developed in python. Here is [one that Nick Roth has made available](https://github.com/rothnic/formulapy).}
\slides{
* [Formula One Race Simulation in Python](https://github.com/rothnic/formulapy) by Nick Roth.}

\notes{Formula one teams also make use of simulation to design car parts. There are at least two components to this, simulations that allow the modelling of fluid flow across the car, and simulations that analyze the capabilities of materials under stress. You can find computational [fluild dynamics simulations in python here](https://github.com/barbagroup/CFDPython) and [finite element analysis methods for computing stress in materials here](https://solidspy.readthedocs.io/en/latest/readme.html).}
\slides{* [Fluid Dynamics](https://github.com/barbagroup/CFDPython) Discretisation of PDEs
* [Stress in a connecting rod](https://solidspy.readthedocs.io/en/latest/readme.html) Discretisation of PDEs
}

\notes{Alongside continuous system simulation through partial differential equations, another form of simulation that arises is known as *discrete event simulation*. This comes up in c[omputer networks](https://github.com/mkalewski/sim2net) and also in chemical systems where the approach to simulating is kown as the [Gillespie algorithm](https://github.com/karinsasaki/gillespie-algorithm-python/).}

\slides{
* [Network simulation](https://github.com/mkalewski/sim2net) Discrete Event simulation.
* [Gillespie Algorithm](https://github.com/karinsasaki/gillespie-algorithm-python/) notebook (in Python 2.7).}



\endif

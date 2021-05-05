from main import *

sim = Simulation()
pop = Population(sim)

pop.initial_infection(sim)
pop.display_statistics(sim)


pop.graphics()


input("\nPress enter to begin the simulation")


for x in range(1, sim.sim_days):
    pop.spread_infection(sim)
    pop.update(sim)
    pop.display_statistics(sim)
    pop.graphics()

    if x != sim.sim_days - 1:
        input("\nPress enter to advance to the next day.")

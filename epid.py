import random
import math


class Simulation():
    """Controlls the simulation of the Infection"""

    def __init__(self):

        self.day_number = 1
        print("To simulate an epidemic outbreak, we must know the population size.")
        self.pop_size = int(input("---Enter the Population size: "))

        root = math.sqrt(self.pop_size)

        if int(root + 0.5)**2 != self.pop_size:
            root = round(root, 0)
            self.grid_size = int(root)
            self.pop_size = self.grid_size**2
            print(
                f"Rounding population size to {self.pop_size} for visual purposes.")
        else:
            self.grid_size = int(math.sqrt(self.pop_size))

        print("\nWe must first start by infecting a portion of the population.")
        self.inf_percentage = float(
            input("---Enter the Percentage(0 - 100) of the population to initially infect: "))
        self.inf_percentage /= 100
        print("\nWe must know th risk a person has to contract the disease when exposed.")
        self.inf_pro = float(input(
            "---Enter the Probability(0 - 100) that a person gets infected when exposed to the disease: "))

        print("\nWe must know how long the infection will last when exposed.")
        self.inf_duration = int(
            input("---Enter the duration (in days) of the infection: "))

        print("\nWe must know th mortality rate of those infected.")
        self.mor_rate = float(input("---Enter the mortality rate: "))

        print("\nWe must know how long to run the simulation.")
        self.sim_days = int(input("---Enter the days to simulate: "))


class Person():
    """A class to model an individual person in a population"""

    def __init__(self):
        self.is_infected = False
        self.is_dead = False
        self.days_infected = 0

    def infect(self, sim):
        if random.randint(0, 100) < sim.inf_pro:
            self.is_infected = True

    def heal(self):
        self.is_infected = False
        self.days_infected = 0

    def die(self):
        self.is_dead = True

    def update(self, sim):
        if self.is_infected:
            self.days_infected += 1
            if random.randint(0, 100) < sim.mor_rate:
                self.die()
            elif self.days_infected == sim.inf_duration:
                self.heal()


class Population():
    """A class to model a whole population of Person Objects"""
    def __init__():
        pass

    def initial_infection():
        pass

    def spread_infection():
        pass

    def update():
        pass

    def display_statistics():
        pass


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

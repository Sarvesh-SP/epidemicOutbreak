import random


class Simulation():
    """Controlls the simulation of the Infection"""

    def __init__(self):
        self.day_number = 1

        self.pop_size = int(input("---Enter the Population size: "))

        self.inf_percentage = float(
            input("---Enter the Infection Percentage: "))

        self.inf_pro = float(input("---Enter the Infection Probability: "))

        self.mor_rate = float(input("---Enter the mortality rate: "))

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
            elif self.days_infected == sim.sim_days:
                self.heal()

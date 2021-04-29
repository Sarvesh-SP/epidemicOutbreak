import random


class Simulation():
    """Controlls the simulation of the Infection"""

    def __init__(self):
        self.days = 1

        self.pop_size = int(input("---Enter the Population size: "))

        self.inf_percentage = float(
            input("---Enter the Infection Percentage: "))

        self.inf_pro = float(input("---Enter the Infection Probability: "))

        self.mor_rate = float(input("---Enter the mortality rate: "))

        self.sim = int(input("---Enter the days to simulate: "))


class Person():
    """A class to model an individual person in a population"""

    def __init__(self):
        self.is_infected = False
        self.is_dead = False
        self.days_infected = 0

    def infect(self, sim):
        if ran

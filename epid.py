import random


class Simulation():
    """Controlls the simulation of the Infection"""

    def __init__(self):

        self.day_number = 1

        self.pop_size = int(input("---Enter the Population size: "))

        self.inf_percentage = float(
            input("---Enter the Infection Percentage: "))
        self.inf_percentage /= 100
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


class Population():
    """Models a whole Population"""

    def __init__(self, sim):
        self.population = []

        for _ in range(sim.pop_size):
            person = Person()
            self.population.append(person)

    def initial_infection(self, sim):
        infected_count = int(round(sim.inf_percentage * sim.pop_size), 0)

        for x in range(infected_count):
            self.population[x].is_infected = True
            self.population[x].days_infected = True
        random.shuffle(self.population)

    def spread_infection(self, sim):

        for x in range(len(self.population)):
            if x == 0:
                if self.population[x+1].is_infected:
                    self.population[x].infect(sim)
            elif x < len(self.population) - 1:
                if self.population[x+1].is_infected or self.population[x-1].is_infected:
                    self.population[x].infect(sim)
            elif x == len(self.population) - 1:
                if self.population[x-1].is_infected:
                    self.population[x].infect(sim)

    def update(self, sim):
        sim.day_number += 1

        for x in self.population:
            x.update(sim)

    def display_statistics(self, sim):
        total_infC = 0
        total_dedC = 0

        for x in self.population:
            if x.is_infected:
                total_infC += 1
                if x.is_dead:
                    total_dedC += 1

        inf_percentage = round((total_infC / sim.pop_size) * 100, 4)
        ded_percentage = round((total_dedC / sim.pop_size) * 100, 4)

        print(f"\n----Day #{sim.day_number}----")
        print(f"----Percentage of Population Infected: {inf_percentage}")
        print(f"----Percentage of Population Death: {ded_percentage} %")
        print(f"----Total People Infected: {total_infC} / {sim.pop_size}")
        print(f"----Total Deaths: {total_dedC} / {sim.pop_size}")

    def graphics():
        pass

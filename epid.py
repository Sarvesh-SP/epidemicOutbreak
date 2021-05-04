import random
import math


class Simulation():
    """Controlls the simulation of the Infection"""

    def __init__(self):

        self.day_number = 1
        print("To simulate an epidemic outbreak, we must know the population size.")
        self.pop_size = int(input("---Enter the Population size: "))

        root = math.sqrt(self.pop_size)

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
    """Models a whole Population"""

    def __init__(self, sim):
        self.population = []

        for _ in range(sim.pop_size):
            person = Person()
            self.population.append(person)

    def initial_infection(self, sim):
        infected_count = int(round(sim.inf_percentage*sim.pop_size, 0))

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
        print(f"----Percentage of Population Infected: {inf_percentage}%")
        print(f"----Percentage of Population Death: {ded_percentage}%")
        print(f"----Total People Infected: {total_infC} / {sim.pop_size}")
        print(f"----Total Deaths: {total_dedC} / {sim.pop_size}")

    def graphics(self):
        """A Graphical representation for a population. O is healthy, I is Infected, X is dead."""

        status = []
        for person in self.population:
            if person.is_dead:
                char = 'X'
            elif person.is_infected:
                char = 'I'
            else:
                char = 'O'
            status.append(char)

        for x in status:
            print(x, end="-")


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

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

    def __init__(self, simulation):
        """Initialize attributes"""
        self.population = []

        for i in range(simulation.grid_size):
            row = []
            for j in range(simulation.grid_size):
                person = Person()
                row.append(person)
            self.population.append(row)

    def initial_infection(self, simulation):
        """Infect an initial portion of the population based on initial conditions of the sim"""
        infected_count = int(
            round(simulation.inf_percentage*simulation.pop_size, 0))

        infections = 0
        while infections < infected_count:
            x = random.randint(0, simulation.grid_size - 1)
            y = random.randint(0, simulation.grid_size - 1)

            if not self.population[x][y]:
                self.population[x][y].is_infected = True
                self.population[x][y].days_infected = 1
                infections += 1

    def spread_infection(self, sim):
        """Spread the infection in a 2D array to all adjacent people to a given person"""
        for i in range(sim.grid_size):
            for j in range(sim.grid_size):
                if not self.population[i][j].is_dead:
                    if i == 0:
                        if j == 0:
                            if self.population[i][j + 1].is_infected or self.population[i+1][j].is_infected:
                                self.population[i][j].infect(sim)
                        elif j == sim.grid_size - 1:
                            if self.population[i][j - 1].is_infected or self.population[i+1][j].is_infected:
                                self.population[i][j].infect(sim)
                        else:
                            if self.population[i][j - 1].is_infected or self.population[i][j + 1].is_infected or self.population[i+1][j].is_infected:
                                self.population[i][j].infect(sim)
                    elif i == sim.grid_size - 1:
                        if j == 0:
                            if self.population[i][j + 1].is_infected or self.population[i-1][j].is_infected:
                                self.population[i][j].infect(sim)
                        elif j == sim.grid_size - 1:
                            if self.population[i][j - 1].is_infected or self.population[i-1][j].is_infected:
                                self.population[i][j].infect(sim)
                        else:
                            if self.population[i][j - 1].is_infected or self.population[i][j + 1].is_infected or self.population[i-1][j].is_infected:
                    else:
                        if j == 0:
                            if self.population[i][j + 1].is_infected or self.population[i+1][j].is_infected or self.population[i - 1][j]:
                                self.population[i][j].infect(sim)
                        elif j == sim.grid_size - 1:
                            if self.population[i][j - 1].is_infected or self.population[i+1][j].is_infected or self.population[i - 1][j]:
                                self.population[i][j].infect(sim)
                        else:
                            if self.population[i][j - 1].is_infected or self.population[i][j + 1].is_infected or self.population[i+1][j].is_infected or self.population[i - 1][j]:

    def update(self, simulation):
        """Update the whole population by updating each individual Person"""
        simulation.day_number += 1

        for row in self.population:
            for person in row:
                person.update(simulation)

    def display_statistics(self, sim):
        """Display the statistics of the population"""
        total_inf_count = 0
        total_ded_count = 0

        for row in self.population:
            for person in row:
                if person.is_infected:
                    total_inf_count += 1
                    if person.is_dead:
                        total_ded_count += 1

        infected_percent = round(100*(total_inf_count/sim.pop_size), 4)
        death_percent = round(100*(total_ded_count/sim.pop_size), 4)

        print(f"\n----Day # {sim.day_number}----")
        print(f"Percentage of Population Infected: {infected_percent}%")
        print(f"Percentage of Population Dead: {death_percent}%")
        print(f"Total People Infected: {total_inf_count} / {sim.pop_size}")
        print(f"Total Deaths: {total_ded_count} / {sim.pop_size}")

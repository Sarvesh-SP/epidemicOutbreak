import tkinter
from main import *


def graphics(sim, population, canvas):
    """A helper function to update a tkinter display."""
  sq_dm = 600//sim.grid_size

  for i in range(sim.grid_size):
    y = i*sq_dm
    for j in range(sim.grid_size):
      x = j*sq_dm

      if population.population[i][j].is_dead:
        canvas.create_rectangle(x, y, x+sq_dm, y+sq_dm, fill='red')
      else:
        if population.population[i][j].is_infected:
          canvas.create_rectangle(x, y, x+sq_dm, y+sq_dm, fill='yellow')
        else:
          canvas.create_rectangle(x, y, x+sq_dm, y+sq_dm, fill='green')


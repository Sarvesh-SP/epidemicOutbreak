from main import *
from graphics import graphics
import tkinter

sim = Simulation()


WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600

sim_window = tkinter.Tk()
sim_window.title("Epidemic Outbreak")
sim_canvas = tkinter.Canvas(
    sim_window, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, bg='lightblue')
sim_canvas.pack(side=tkinter.LEFT)

pop = Population(sim)

pop.initial_infection(sim)
pop.display_statistics(sim)
input("Press enter to begin simulation.")


for i in range(1, sim.sim_days):
    pop.spread_infection(sim)
    pop.update(sim)

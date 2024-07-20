from tkinter import *

# Constants
GRID_HEIGHT = 20
GRID_WIDTH = 10
CANVAS_HEIGHT = 1000
CANVAS_WIDTH = 1000

# Create window and set dimensions
pt = Tk()
pt.title("Python Tetris")
pt.geometry(str(CANVAS_WIDTH) + "x" + str(CANVAS_HEIGHT))

# Run main loop
while True:
    pt.update_idletasks()
    pt.update()
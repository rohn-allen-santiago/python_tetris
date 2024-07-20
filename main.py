from time import sleep
from tkinter import *
from block import *

# Constants
GRID_HEIGHT = 20
GRID_WIDTH = 10
WINDOW_HEIGHT = 1000
WINDOW_WIDTH = 1000
CANVAS_HEIGHT = 1000
CANVAS_WIDTH = 500

# Create window and set dimensions
pt = Tk()
pt.title("Python Tetris")
pt.geometry(str(WINDOW_WIDTH) + "x" + str(WINDOW_HEIGHT))

# Create Frame and set dimensions
f = Frame(pt, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, bg="white")
f.pack()

# Create canvas and set dimensions
canvas = Canvas(f, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="gray")
canvas.pack()

# Draw grid lines on the canvas
# Vertical lines
for i in range(11):
    canvas.create_line(i * BLOCK_WIDTH, 0, i * BLOCK_WIDTH, 1000)
# Horizontal lines
for i in range(21):
    canvas.create_line(0, i * BLOCK_WIDTH, 1000, i * BLOCK_WIDTH)

# Testing
testBlock = Block(canvas, 1, 3, "red")
testBlock.draw()

# Run main loop
while True:
    pt.update_idletasks()
    pt.update()
    sleep(1)
    testBlock.fall()
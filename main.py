from time import sleep
from mttkinter import *
from piece import *
from pynput.keyboard import Listener
from math import *

# Constants
WINDOW_HEIGHT = 1000
WINDOW_WIDTH = 1000
CANVAS_HEIGHT = 1000
CANVAS_WIDTH = 500

# Globals
level = 1

# Create window and set dimensions
pt = mtTkinter.Tk()
pt.title("Python Tetris")
pt.geometry(str(WINDOW_WIDTH) + "x" + str(WINDOW_HEIGHT))

# Create Frame and set dimensions
f = mtTkinter.Frame(pt, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, bg="white")
f.pack()

# Create canvas and set dimensions
canvas = mtTkinter.Canvas(f, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="gray")
canvas.pack()

# Draw grid lines on the canvas
# Vertical lines
for i in range(11):
    canvas.create_line(i * BLOCK_WIDTH, 0, i * BLOCK_WIDTH, 1000)
# Horizontal lines
for i in range(21):
    canvas.create_line(0, i * BLOCK_WIDTH, 1000, i * BLOCK_WIDTH)

# Select action based on key press
def input(key):
    global currentPiece

    # Move left
    if key.char == 'a':
        currentPiece.move_left()
    # Move right
    if key.char == 'd':
        currentPiece.move_right()
    # Rotate counterclockwise
    if key.char == 'q':
        currentPiece.rotate_ccw()
    # Rotate clockwise
    if key.char == 'e':
        currentPiece.rotate_cw()
    # Rotate 180 degrees
    if key.char == 'w':
        currentPiece.rotate_180()
    # hard drop
    if key.char == 'j':
        currentPiece.hard_drop()
    # Soft drop
    # if key == key.from_char('s'):

# Set up listener for registering key presses
listener = Listener(on_press=input)
listener.start()

# Testing
testPiece = Piece(canvas, L_PIECE)
testPiece.draw()
currentPiece = testPiece

# Run main loop
while True:
    pt.update_idletasks()
    pt.update()
    currentPiece.check_update(level)
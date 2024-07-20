"""
A class for individual blocks.
Blocks should hbe able to fall until they reach the bottom of the grid or another block.
Blocks can change the speed they are falling at
"""

# Constants
BLOCK_WIDTH = 50

class Block:

    # Initialize the ball object
    def __init__(self, canvas, x, y, color):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.color = color
        self.speed = 1


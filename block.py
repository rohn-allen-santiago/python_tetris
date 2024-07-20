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

    # Draw the block on teh canvas
    def draw(self):
        x1 = self.x * BLOCK_WIDTH
        y1 = self.y * BLOCK_WIDTH
        x2 = x1 + BLOCK_WIDTH
        y2 = y1 + BLOCK_WIDTH
        self.canvas.create_rectangle(x1, y1, x2, y2, fill=self.color)
        return None
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
        self.block = ""

    # Draw the block on teh canvas
    def draw(self):
        x1 = self.x * BLOCK_WIDTH
        y1 = self.y * BLOCK_WIDTH
        x2 = x1 + BLOCK_WIDTH
        y2 = y1 + BLOCK_WIDTH
        self.block = self.canvas.create_rectangle(x1, y1, x2, y2, fill=self.color)
        return None

    # Moves block down a position on the grid
    def fall(self):
        if self.y < 19:
            self.canvas.move(self.block, 0, BLOCK_WIDTH)
            self.y += 1
            print(self.y)
        return None

"""
A class for individual blocks.
Blocks should hbe able to fall until they reach the bottom of the grid or another block.
Blocks can change the speed they are falling at
"""

# Constants
BLOCK_WIDTH = 50
GRID_HEIGHT = 20
GRID_WIDTH = 10

class Block:

    # Initialize a block
    def __init__(self, canvas, x, y, color):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.color = color
        self.block = ""

    # Draw the block on the canvas
    def draw(self):
        x1 = self.x * BLOCK_WIDTH
        y1 = self.y * BLOCK_WIDTH
        x2 = x1 + BLOCK_WIDTH
        y2 = y1 + BLOCK_WIDTH
        self.block = self.canvas.create_rectangle(x1, y1, x2, y2, fill=self.color)
        return None

    # Moves block down a position on the grid
    def move_down(self):
        if self.y >= GRID_HEIGHT - 1:
            return False
        self.canvas.move(self.block, 0, BLOCK_WIDTH)
        self.y += 1
        return True

    # Checks if a block can move down
    def can_move_down(self):
        if self.y >= GRID_HEIGHT - 1:
            return False
        return True

    # Moves block left one position if possible
    def move_left(self):
        if self.x <= 0:
            return False
        self.canvas.move(self.block, -1 * BLOCK_WIDTH, 0)
        self.x -= 1
        return True

    # Checks if a block can move left
    def can_move_left(self):
        if self.x <= 0:
            return False
        return True

    # Moves block right one position if possible
    def move_right(self):
        if self.x >= GRID_WIDTH - 1:
            return False
        self.canvas.move(self.block, BLOCK_WIDTH, 00)
        self.x += 1
        return True

    # Checks if a block cna move right
    def can_move_right(self):
        if self.x >= GRID_WIDTH - 1:
            return False
        return True

    # Delete the block from teh canvas
    def delete(self):
        self.canvas.delete(self.block)
        return None
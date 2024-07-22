"""
A class for each piece.
A piece consists of exactly 4 blocks.
Pieces can behave differently in certain situations so they will be differentiated by a switch case.
"""
from block import *

# Constants
O_PIECE = (0, "yellow")
I_PIECE = (1, "deep sky blue")
T_PIECE = (2, "magenta")
L_PIECE = (3, "dark orange")
J_PIECE = (4, "blue")
S_PIECE = (5, "chartreuse")
Z_PIECE = (6, "red")
START_X = 4
START_Y = 2

# Table for piece orientation lookup.
# Orientation numbers represent different positions moving clockwise
# Rows contain position delta of each block relative to the pivot block
# Row number = (Piece number * 4) +  Orientation number
OT = [
    # O Piece
    [(1, 0), (0, 1), (1, 1)],
    [(1, 0), (0, 1), (1, 1)],
    [(1, 0), (0, 1), (1, 1)],
    [(1, 0), (0, 1), (1, 1)],
    # I Piece
    [(-1, 0), (1, 0), (2, 0)],
    [(0, -1), (0, 1), (0, 2)],
    [(-1, 0), (1, 0), (-2, 0)],
    [(0, -1), (0, 1), (0, -2)],
    # T Piece
    [(-1, 0), (0, -1), (1, 0)],
    [(0, 1), (0, -1), (1, 0)],
    [(0, 1), (-1, 0), (1, 0)],
    [(0, 1), (-1, 0), (0, -1)],
    # L Piece
    [(0, -1), (0, -2), (1, 0)],
    [(1, 0), (0, 1), (2, 0)],
    [(0, 1), (0, 2), (-1, 0)],
    [(-1, 0), (0, -1), (-2, 0)],
    # J Piece
    [(0, -1), (0, -2), (-1, 0)],
    [(1, 0), (0, -1), (2, 0)],
    [(0, 1), (0, 2), (1, 0)],
    [(-1, 0), (0, 1), (-2, 0)],
    # S Piece
    [(-1, 0), (0, -1), (1, -1)],
    [(1, 0), (0, -1), (1, 1)],
    [(-1, 0), (0, -1), (1, -1)],
    [(1, 0), (0, -1), (1, 1)],
    # Z Piece
    [(1, 0), (0, -1), (-1, -1)],
    [(-1, 0), (0, -1), (-1, 1)],
    [(1, 0), (0, -1), (-1, -1)],
    [(-1, 0), (0, -1), (-1, 1)],
]

class Piece:

    # Initialize a piece
    def __init__(self, canvas, type):
        self.canvas = canvas
        self.x = START_X
        self.y = START_Y
        self.type = type[0]
        self.color = type[1]
        self.orientation = 0
        self.blocks = []

    # Draw the piece on the canvas
    def draw(self):
        block = Block(self.canvas, self.x, self.y, self.color)
        self.blocks.append(block)
        for i in range(3):
            otIndex = (self.type * 4) + (self.orientation % 4)
            x = self.x + OT[otIndex][i][0]
            y = self.y + OT[otIndex][i][1]
            block = Block(self.canvas, x, y, self.color)
            self.blocks.append(block)
        for block in self.blocks:
            block.draw()
        return None

    # Moves the piece down a position if possible
    def move_down(self):
        for block in self.blocks:
            if not block.can_move_down():
                return False
        for block in self.blocks:
            block.move_down()
        self.x += 1
        return True

    # Moves the piece left a position if possible
    def move_left(self):
        for block in self.blocks:
            if not block.can_move_left():
                return False
        for block in self.blocks:
            block.move_left()
        self.y -= 1
        return True

    # Moves the piece right a position if possible
    def move_right(self):
        for block in self.blocks:
            if not block.can_move_right():
                return False
        for block in self.blocks:
            block.move_right()
        self.y += 1
        return True

    # Deletes a piece
    def delete(self):
        for block in self.blocks:
            block.delete()
        self.blocks.clear()
        return None
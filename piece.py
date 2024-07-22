"""
A class for each piece.
A piece consists of exactly 4 blocks.
Pieces can behave differently in certain situations so they will be differentiated by a switch case.
"""

# Constants
O_PIECE = (0, "yellow")
I_PIECE = (1, "deep sky blue")
T_PIECE = (2, "purple")
L_PIECE = (3, "orange red")
J_PIECE = (4, "blue")
S_PIECE = (5, "green")
Z_PIECE = (6, "red")

class Piece:

    # Initialize a piece
    def __init__(self, canvas, x, y, type):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.type = type[0]
        self.color = type[1]
        self.blocks = []

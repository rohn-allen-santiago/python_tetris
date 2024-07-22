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
START_X = 4
START_Y = 1

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

from enum import Enum


class BoardLocation(Enum):
    """The symbolic locations of each possible position on the game board"""
    TL = 0 # top-left
    TM = 1 # top-middle
    TR = 2 # top-right
    ML = 3 # middle-left
    M = 4  # middle
    MR = 5 # middle-right
    BL = 6 # bottom-left
    BM = 7 # bottom-middle
    BR = 8 # bottom-right

from enum import Enum


class BoardLocation(Enum):
    """The symbolic locations of each possible position on the game board"""
    TL = 0
    TM = 1
    TR = 2
    ML = 3
    M = 4
    MR = 5
    BL = 6
    BM = 7
    BR = 8

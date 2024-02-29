# WARNING: IntEnum requires python 3.11 or higher
from enum import IntEnum


class BoardLocation(IntEnum):
    """The symbolic locations of each possible position on the game board"""
    TL = 0  # top-left
    TM = 1  # top-middle
    TR = 2  # top-right
    ML = 3  # middle-left
    M = 4  # middle
    MR = 5  # middle-right
    BL = 6  # bottom-left
    BM = 7  # bottom-middle
    BR = 8  # bottom-right

    def __str__(self):
        match self.name:
            case 'TL':
                return 'Top-Left'
            case 'TM':
                return 'Top-Middle'
            case 'TR':
                return 'Top-Right'
            case 'ML':
                return 'Middle-Left'
            case 'M':
                return 'Middle'
            case 'MR':
                return 'Middle-Right'
            case 'BL':
                return 'Bottom-Left'
            case 'BM':
                return 'Bottom-Middle'
            case 'BR':
                return 'Bottom-Right'
            case other:
                return self.name

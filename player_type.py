# WARNING: StrEnum requires python 3.11 or higher
from enum import StrEnum


class PlayerType(StrEnum):
    """The type of player, X or O"""
    X: str = 'X'
    O: str = 'O'
    NONE: str = ' '

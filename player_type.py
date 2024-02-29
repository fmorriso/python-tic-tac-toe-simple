from enum import Enum


class PlayerType(Enum):
    """The type of player, X or O"""
    X: str = 'X'
    O: str = 'O'
    NONE: str = ' '

    def __str__(self):
        return str(self.value)

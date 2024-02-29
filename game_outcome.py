from enum import Enum


class GameOutcome(Enum):
    """The game outcome"""
    IN_PROGRESS = 'in progress'
    TIE = 'tie'
    X_winner = 'X wins'
    O_winner = 'O wins'

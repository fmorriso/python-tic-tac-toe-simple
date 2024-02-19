from enum import StrEnum


class GameOutcome(StrEnum):
    """The game outcome"""
    IN_PROGRESS = 'in progress'
    TIE = 'tie'
    X_winner = 'X wins'
    O_winner = 'O wins'

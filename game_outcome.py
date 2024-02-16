from enum import StrEnum


class GameOutcome(StrEnum):
    """The game outcome"""
    UNKNOWN = 'unknown'
    TIE = 'tie'
    X_winner = 'X wins'
    O_winner = 'O wins'

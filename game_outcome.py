from enum import StrEnum


class GameOutcome(StrEnum):
    """The game outcome"""
    unknown = 'unknown'
    tie = 'tie'
    x_winner = 'X wins'
    o_winner = 'O wins'

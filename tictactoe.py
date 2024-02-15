import random

from game_outcome import GameOutcome
from player_type import PlayerType


class TicTacToe:
    def __init__(self):
        self.board = None
        self.x_choices = None
        self.o_choices = None
        self.game_outcome = None
        self.start_new_game()

    def start_new_game(self) -> None:
        # blank out the board
        self.board = [" " in range(9)]
        # erase any previous X choices
        self.x_choices = [" " in range(9)]
        # erase any previous O choices
        self.o_choices = [" " in range(9)]
        # the game outcome is now unkown
        self.game_outcome = GameOutcome.unknown

    def get_starting_player(self) -> str:
        n = random.randint(0, 1)
        if n == 0:
            return PlayerType.X
        else:
            return PlayerType.O

    def play(self) -> None:
        """Plays one game of Tic-Tac-Toe"""
        # 1. determine which player, X or O will go first
        player = self.get_starting_player()
        print(f'starting player = {player}')

        # 2. keep playing until either 
        #    (a) there is a winner or
        #    (b) it is a tie
        while self.game_outcome == GameOutcome.unknown:
            # temporary exit logic
            self.game_outcome = GameOutcome.tie

    def get_play_again_decision(self) -> bool:
        """Returns True if the player wants to play again; otherwise returns False"""
        resp: str = input('Do you want to play again? (y/n)?>')
        # treat Enter key same as entering y
        return resp is None or len(resp) == 0 or resp[:1].lower() == 'y'

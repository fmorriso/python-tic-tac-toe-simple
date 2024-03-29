import random

from board_location import BoardLocation
from game_outcome import GameOutcome
from player_type import PlayerType


class TicTacToe:
    def __init__(self):
        self.board: list[PlayerType] = []
        # initialize the board so that no player occupies any of the squares
        for i in range(9):
            self.board.append(PlayerType.NONE)
        self.game_outcome = None
        self.player = PlayerType.X
        self.start_new_game()

    def start_new_game(self) -> None:
        # blank out the board
        self.board.clear()
        for i in range(9):
            self.board.append(PlayerType.NONE)
        # the game outcome is now unknown
        self.game_outcome = GameOutcome.IN_PROGRESS

    @staticmethod
    def get_starting_player() -> PlayerType:
        n = random.randint(0, 1)
        if n == 0:
            return PlayerType.X
        else:
            return PlayerType.O

    def play(self) -> None:
        """Plays one game of Tic-Tac-Toe"""
        # 1. determine which player, X or O will go first
        self.player = self.get_starting_player()
        print(f'starting player = {self.player}')

        # 2. keep playing until either 
        #    (a) there is a winner or
        #    (b) it is a tie
        while self.game_outcome == GameOutcome.IN_PROGRESS:
            self.next_player_selection()
            self.game_outcome = self.check_for_winner()
            if self.game_outcome != GameOutcome.IN_PROGRESS:
                self.display_game_board()
                print(f'The game has ended. Outcome: {self.game_outcome}')
                break
            else:
                self.switch_player()

    def next_player_selection(self):
        """Ask the current player to pick a square"""
        self.display_game_board()
        location_description: str = ''
        while True:
            selection: str = input(
                f"{self.player}: which square do you want? (TL, TM, TR, ML, M, MR, BL, BM, BR)>").upper()
            try:
                location = BoardLocation[selection]
                location_description = location.__str__()
            except KeyError:
                print(f'{selection} is not valid. Try again.')
                continue
            who_has_this_location: PlayerType = PlayerType(self.board[location])
            if who_has_this_location != PlayerType.NONE:
                print(f'Position {location_description} is already occupied. Try a different location.')
            else:
                break

        if location is not None:
            print(f'Player {self.player} chose {location_description}')
            self.board[location] = self.player

    def display_game_board(self) -> None:
        """Displays the current game board"""
        print('-' * 13)
        for i in [BoardLocation.TL, BoardLocation.ML, BoardLocation.BL]:
            print(f'| {self.board[i]} | {self.board[i + 1]} | {self.board[i + 2]} |')
            print('-' * 13)

    def switch_player(self) -> None:
        """alternate between player X and player O"""
        if self.player == PlayerType.X:
            self.player = PlayerType.O
        else:
            self.player = PlayerType.X

    @staticmethod
    def get_play_again_decision() -> bool:
        """Returns True if the player wants to play again; otherwise returns False"""
        resp: str = input('Do you want to play again? (y/n)?>')
        # treat Enter key same as entering y
        return resp is None or len(resp) == 0 or resp[:1].lower() == 'y'

    def check_for_winner(self) -> GameOutcome:
        # 1. check for vertical three-in-a-row for either player
        result = self.check_for_consecutive(BoardLocation.TL, BoardLocation.ML, BoardLocation.BL)
        if result != GameOutcome.IN_PROGRESS:
            return result

        result = self.check_for_consecutive(BoardLocation.TM, BoardLocation.M, BoardLocation.MR)
        if result != GameOutcome.IN_PROGRESS:
            return result

        result = self.check_for_consecutive(BoardLocation.TR, BoardLocation.MR, BoardLocation.BR)
        if result != GameOutcome.IN_PROGRESS:
            return result

        # 2. check for horizontal three-in-a-row for either player
        result = self.check_for_consecutive(BoardLocation.TL, BoardLocation.TM, BoardLocation.TR)
        if result != GameOutcome.IN_PROGRESS:
            return result

        result = self.check_for_consecutive(BoardLocation.ML, BoardLocation.M, BoardLocation.MR)
        if result != GameOutcome.IN_PROGRESS:
            return result

        result = self.check_for_consecutive(BoardLocation.BL, BoardLocation.BM, BoardLocation.BR)
        if result != GameOutcome.IN_PROGRESS:
            return result

        # 3. check for Upper-Left to Bottom-Right three-in-a-row for either player
        result = self.check_for_consecutive(BoardLocation.TL, BoardLocation.M, BoardLocation.BR)
        if result != GameOutcome.IN_PROGRESS:
            return result

        # 4. check for Bottom-Left to Upper-Right three-in-a-row for either player
        result = self.check_for_consecutive(BoardLocation.BL, BoardLocation.M, BoardLocation.TR)
        if result != GameOutcome.IN_PROGRESS:
            return result

        # 5. check for Tie
        if self.is_hopeless_tie_game():
            return GameOutcome.TIE

        # 6. if nobody has won and it's not a hopeless tie, the game is still in progress
        return GameOutcome.IN_PROGRESS

    def check_for_consecutive(self, first: BoardLocation, second: BoardLocation,
                              third: BoardLocation) -> GameOutcome:
        if self.board[first] == PlayerType.X and \
                self.board[second] == PlayerType.X and self.board[third] == PlayerType.X:
            return GameOutcome.X_winner

        if self.board[first] == PlayerType.O and \
                self.board[second] == PlayerType.O and self.board[third] == PlayerType.O:
            return GameOutcome.O_winner

        # if there are any unused areas in the board, the game is not over yet
        for i in range(len(self.board)):
            if self.board[i] == PlayerType.NONE:
                return GameOutcome.IN_PROGRESS

        return GameOutcome.TIE

    def is_hopeless_tie_game(self) -> bool:
        """ determine if the game is a hopeless tie, even if there are unused squares"""

        # Check for PlayerType.NONE as the only remaining choice for any
        # of the following where there are already two values OTHER than
        # PlayerType.NONE in:
        #       1. any of the three verticals
        #       2. any of the three horizontals
        #       3. either of the two diagonals
        #       4. the total number of unused squares is two or less
        num_tie_areas = 0

        # verticals (left, middle, right)
        if self.is_tie_triple([BoardLocation.TL, BoardLocation.ML, BoardLocation.BL]):
            num_tie_areas += 1

        if self.is_tie_triple([BoardLocation.TM, BoardLocation.M, BoardLocation.BM]):
            num_tie_areas += 1

        if self.is_tie_triple([BoardLocation.TR, BoardLocation.MR, BoardLocation.BR]):
            num_tie_areas += 1

        # horizontals (top, middle, bottom)
        if self.is_tie_triple([BoardLocation.TL, BoardLocation.TM, BoardLocation.TR]):
            num_tie_areas += 1

        if self.is_tie_triple([BoardLocation.ML, BoardLocation.M, BoardLocation.MR]):
            num_tie_areas += 1

        if self.is_tie_triple([BoardLocation.BL, BoardLocation.BM, BoardLocation.BR]):
            num_tie_areas += 1

        # diagonals (Top-left to bottom-right, top-right to bottom left)
        if self.is_tie_triple([BoardLocation.TL, BoardLocation.M, BoardLocation.BR]):
            num_tie_areas += 1

        if self.is_tie_triple([BoardLocation.TR, BoardLocation.M, BoardLocation.BL]):
            num_tie_areas += 1

        num_unused: int = 0
        for location in BoardLocation:
            if self.board[location] == PlayerType.NONE:
                num_unused += 1

        # if all eight areas where a triple can occur have at least one open square,
        # or there are two or less unused squares,
        # the game is hopelessly tied
        return num_tie_areas == 8 or num_unused <= 1

    def is_tie_triple(self, triple=list[int]) -> bool:
        """Return true if it is impossible for either player to complete a triple
        within the three consecutive squares; otherwise return false"""
        if len(triple) != 3:
            raise ValueError(f"Expected 3 items, but got {len(triple)} instead")

        n: int = 0
        num_x: int = 0
        num_o: int = 0
        num_blank: int = 0
        for i in triple:
            if self.board[i] == PlayerType.X:
                num_x += 1
            elif self.board[i] == PlayerType.O:
                num_o += 1
            else:
                num_blank += 1

        n = num_x + num_o
        # return true if more than one square is occupied by a player, but not by the same player
        return n > 1 and num_x < 2 and num_o < 2

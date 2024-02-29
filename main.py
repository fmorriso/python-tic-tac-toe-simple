import sys

from tictactoe import TicTacToe


def get_python_version() -> str:
    return f'{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}'


if __name__ == '__main__':
    print(f'Tic-Tac-Toe game using Python version {get_python_version()}')
    # call the constructor on class TicTacToe
    game = TicTacToe()

    # allow the game to be played multiple times if desired
    keep_playing: bool = True
    while keep_playing:
        game.play()
        keep_playing = game.get_play_again_decision()
        if keep_playing:
            game.start_new_game()
        else:
            print('Thanks for playing')
            break

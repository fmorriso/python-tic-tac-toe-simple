import sys

from tictactoe import TicTacToe


def get_python_version() -> str:
    return f'{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}'


if __name__ == '__main__':
    print(f'Python version {get_python_version()}')

    game = TicTacToe()
    # allow the game to be played multiple times if desired
    while True:
        game.play()

        if game.get_play_again_decision():
            game.start_new_game()
        else:
            print('Thanks for playing')
            break

import sys

from tictactoe import TicTacToe


def get_python_version() -> str:
    return f'{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}'


def get_play_again_decision() -> bool:
    """Returns True if the player wants to play again; otherwise returns False"""
    resp: str = input('Do you want to play again? (y/n)?>')
    # treat Enter key same as entering y
    return resp is None or len(resp) == 0 or resp[:1].lower() == 'y'
    

if __name__ == '__main__':
    print(f'Python version {get_python_version()}')

    # allow the game to be played multiple times if desired
    while True:
        game = TicTacToe()

        game.play()

        if get_play_again_decision():
            game.start_new_game()
        else:
            print('Thanks for playing')
            break

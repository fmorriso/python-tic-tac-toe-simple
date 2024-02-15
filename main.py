import sys

from tictactoe import TicTacToe


def get_python_version() -> str:
    return f'{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}'


def get_play_again_decision() -> bool:
    resp = input('Do you want to play again? (y/n)?> ')
    play_again = False
    if resp is None or len(resp) == 0:
        play_again = True
    else:
        resp = resp[:1].lower()
        play_again = resp == 'y'
    return play_again


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(f'Python version {get_python_version()}')

    while True:
        game = TicTacToe()

        game.play()

        if get_play_again_decision():
            game.start_new_game()
        else:
            print('Thanks for playing')
            break

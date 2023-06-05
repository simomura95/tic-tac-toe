import os
from gameboard import Gameboard


def cls():
    """Function to clear the console output. Works on terminal, but not in pycharm"""
    os.system('cls' if os.name == 'nt' else 'clear')


print('''
  _____   _                  _                            _                  
 |_   _| (_)   ___          | |_    __ _    ___          | |_    ___     ___ 
   | |   | |  / __|  _____  | __|  / _` |  / __|  _____  | __|  / _ \   / _ \ 
   | |   | | | (__  |_____| | |_  | (_| | | (__  |_____| | |_  | (_) | |  __/
   |_|   |_|  \___|          \__|  \__,_|  \___|          \__|  \___/   \___|
                                                                             
''')  # titolo

t = Gameboard()

game_is_on = True
while game_is_on and t.turn <= 9:
    t.print_board()
    print(t.board)
    print(f'Player {t.player} turn.')
    t.new_sign()
    if t.is_game_over():
        game_is_on = False
    else:
        t.pass_turn()
        cls()

t.print_board()
if t.turn < 9:
    print(f'Player {t.player} wins!')
else:
    print('It\'s a tie!')

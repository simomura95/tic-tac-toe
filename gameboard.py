class Gameboard:
    def __init__(self):
        self.board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.player = 'X'
        self.turn = 1

    def print_board(self):
        print(f'''
         {self.board[0]} | {self.board[1]} | {self.board[2]} 
        ---|---|---
         {self.board[3]} | {self.board[4]} | {self.board[5]} 
        ---|---|---
         {self.board[6]} | {self.board[7]} | {self.board[8]} 
        ''')

    def new_sign(self):
        try:
            pos = int(input('Which cell do you want? '))
            if pos < 1 or pos > 9 or self.board[pos - 1] in ['X', 'O']:
                raise ValueError
        except ValueError:
            print('Invalid input!')
            return self.new_sign()
        else:
            self.board[pos - 1] = self.player
            return pos

    def pass_turn(self):
        if self.player == 'X':
            self.player = 'O'
        else:
            self.player = 'X'

    def is_game_over(self):
        for line in [
            self.board[0:3], self.board[3:6], self.board[6:9],  # righe
            self.board[0:7:3], self.board[1:8:3], self.board[2:9:3],  # colonne
            self.board[0:9:4], self.board[2:7:2],  # diagonali
        ]:
            # print(line)
            if line == [self.player, self.player, self.player]:
                return True
        return False

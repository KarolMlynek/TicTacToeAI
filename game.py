from board import Board
from random import randint

class Game:
    def __init__(self, board):
        self.board = board
        self.round_counter = 0
    def player_move(self):
        is_move_valid = False
        while is_move_valid == False:
            coordinate_x = int(input('Choose your coordinate X: '))
            coordinate_y = int(input('Choose your coordinate Y: '))
            if self.board[coordinate_x][coordinate_y] == "   ":
                is_move_valid = True
            else:
                print("This move is invalid")

        if self.round_counter % 2 == 0:
            self.board[coordinate_x][coordinate_y] = " X "
            self.round_counter += 1
        else:
            self.board[coordinate_x][coordinate_y] = " O "
            self.round_counter += 1

    def get_winner(self):
        pass
    def starting_player(self):
        self.round_counter = randint(0, 1)
        if self.round_counter == 0:
            print("Player1 is starting")
        else:
            print("Player2 is starting")

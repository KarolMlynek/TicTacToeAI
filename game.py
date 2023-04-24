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
        player1 = [0] * 6
        player2 = [0] * 6
        diagonal1 = 0
        diagonal2 = 0
        for row in range(3):
            for element in range(3):
                if self.board[row][element] == " X ":
                    player1[element] += 1
                    player1[row + 3] += 1
                if self.board[row][element] == " O ":
                    player2[element] += 1
                    player2[row + 3] += 1
                element += 1
            row += 1
        for i in range(len(player1)):
            if player1[i] != 1:
                if player1[i] == 3:
                    print("Player1 won!")
                    exit()
            else:
                diagonal1 +=1
                if diagonal1 == 6 and self.board[1][1] == " X ":
                    print("Player1 won!")
                    exit()
            if player2[i] != 1:
                if player2[i] == 3:
                    print("Player2 won!")
                    exit()
            else:
                diagonal2 += 1
                if diagonal2 == 6 and self.board[1][1] == " O ":
                    print("Player2 won!")
                    exit()
        print(player1)
        print(player2)




    def starting_player(self):
        self.round_counter = randint(0, 1)
        if self.round_counter == 0:
            print("Player1 is starting")
        else:
            print("Player2 is starting")

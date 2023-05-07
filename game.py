import math
from random import randint


class Game:

    def __init__(self, board, is_full):
        self.board = board
        self.round_counter = 0
        self.player_win = False
        self.computer_win = False
        self.is_full = is_full

    def player_move(self):
        is_move_valid = False
        if self.round_counter % 2 == 0:
            while is_move_valid == False:
                coordinate_x = int(input('Choose your coordinate X: '))
                coordinate_y = int(input('Choose your coordinate Y: '))
                if self.board[coordinate_x][coordinate_y] == "   ":
                    is_move_valid = True
                else:
                    print("This move is invalid")
            self.board[coordinate_x][coordinate_y] = " X "
            self.round_counter += 1
        else:
            move = self.get_best_move()
            self.board[move[0]][move[1]] = " O "
            self.round_counter += 1

    def get_winner(self):
        player1 = [0] * 6
        computer = [0] * 6
        for row in range(3):
            for element in range(3):
                if self.board[row][element] == " X ":
                    player1[element] += 1
                    player1[row + 3] += 1
                if self.board[row][element] == " O ":
                    computer[element] += 1
                    computer[row + 3] += 1
                element += 1
            row += 1
        for i in range(len(player1)):
            if player1[i] == 3:
                self.player_win = True
                print("Player1 won!")
                exit()
            else:
                if all(el >= 1 for el in player1) and self.board[1][1] == " X ":
                    self.player_win = True
                    print("Player1 won!")
                    exit()
            if computer[i] == 3:
                self.computer_win = True
                print("Player2 won!")
                exit()
            else:
                if all(el >= 1 for el in computer) and self.board[1][1] == " O ":
                    self.computer_win = True
                    print("Player2 won!")
                    exit()

    def starting_player(self):
        self.round_counter = randint(0, 1)
        if self.round_counter == 0:
            print("You go first!")
        else:
            print("Computer goes first!")

    def minimax(self, depth, is_maximizing):
        if self.player_win:
            return -10
        elif self.computer_win:
            return 10
        elif self.is_full:
            return 0

        if is_maximizing:
            best_score = -math.inf
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == '   ':
                        self.board[i][j] = ' O '
                        score = self.minimax(depth+1, False)
                        self.board[i][j] = '   '
                        best_score = max(score, best_score)
            return best_score
        else:
            best_score = math.inf
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == '   ':
                        self.board[i][j] = ' X '
                        score = self.minimax(depth+1, True)
                        self.board[i][j] = '   '
                        best_score = min(score, best_score)
            return best_score

    def get_best_move(self):
        best_score = -math.inf
        best_move = []
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == '   ':
                    self.board[i][j] = ' O '
                    score = self.minimax(0, False)
                    self.board[i][j] = '   '
                    if score > best_score:
                        best_score = score
                        best_move = [i, j]
        return best_move

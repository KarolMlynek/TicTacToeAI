import math
from random import randint


class Game:

    def __init__(self, board):
        self.board = board
        self.round_counter = 0
        self.player_win = False
        self.computer_win = False

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
    def end_game(self):
        if self.get_winner(" X "):
            print("You win!")
            exit()
        elif self.get_winner(" O "):
            print("Computer win!")
            exit()
        elif self.check_draw():
            print("It is a draw!")
            exit()

    def get_winner(self, player):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] == player:
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] == player:
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == player:
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] == player:
            return True
        return False

    def check_draw(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == "   ":
                    return False
        return True

    def starting_player(self):
        self.round_counter = randint(0, 1)
        if self.round_counter == 0:
            print("You go first!")
        else:
            print("Computer goes first!")

    def minimax(self, depth, is_maximizing):
        if self.get_winner(" X "):
            return -10
        elif self.get_winner(" O "):
            return 10
        elif self.check_draw():
            return 0
        if is_maximizing:
            best_score = -math.inf
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == "   ":
                        self.board[i][j] = " O "
                        score = self.minimax(depth+1, False)
                        self.board[i][j] = "   "
                        best_score = max(score, best_score)
            return best_score
        else:
            best_score = math.inf
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == "   ":
                        self.board[i][j] = " X "
                        score = self.minimax(depth+1, True)
                        self.board[i][j] = "   "
                        best_score = min(score, best_score)
            return best_score

    def get_best_move(self):
        best_score = -math.inf
        best_move = []
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == "   ":
                    self.board[i][j] = " O "
                    score = self.minimax(0, False)
                    self.board[i][j] = "   "
                    if score > best_score:
                        best_score = score
                        best_move = [i, j]
        return best_move


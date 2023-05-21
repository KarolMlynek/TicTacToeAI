from os import system, name

class Board:
    def __init__(self):
        self.board = [["   ", "   ", "   "], ["   ", "   ", "   "], ["   ", "   ", "   "]]
        self.is_full = False

    def show_board(self):
        print(self.board[0][0] +"|"+ self.board[0][1]+"|"+self.board[0][2])
        print("------------")
        print(self.board[1][0] + "|" + self.board[1][1] + "|" + self.board[1][2])
        print("------------")
        print(self.board[2][0] + "|" + self.board[2][1] + "|" + self.board[2][2])

    def clear_screen(self):
        if name == "nt":
            _ = system("cls")
        else:
            _ = system('printf \'\\33c\\e[3J\'')
    def is_board_full(self):
        counter = 0
        for row in self.board:
            for element in row:
                if element == "   ":
                    counter += 1
                else:
                    continue
        if counter == 0:
            return True


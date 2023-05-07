class Board:
    def __init__(self):
        self.board = [["   ", "   ", "   "], ["   ", "   ", "   "], ["   ", "   ", "   "]]
        self.is_full = False

    def show_board(self):
        for row in self.board:
            for element in row:
                print(element, end='|')
            print()

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


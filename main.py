from board import Board
from game import Game


def main():
    tic_tac_board = Board()
    tic_tac_game = Game(tic_tac_board.board)
    tic_tac_board.show_board()
    tic_tac_game.starting_player()
    for i in range(4):
        tic_tac_game.player_move()
        tic_tac_board.show_board()


main()





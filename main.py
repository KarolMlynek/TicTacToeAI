from board import Board
from game import Game


def main():
    tic_tac_board = Board()
    tic_tac_game = Game(tic_tac_board.board)
    tic_tac_board.show_board()
    tic_tac_game.starting_player()
    tic_tac_game.minimax(0, True)
    for i in range(9):
        tic_tac_board.clear_screen()
        if tic_tac_game.round_counter % 2 == 0:
            tic_tac_board.is_board_full()
            tic_tac_board.show_board()
            tic_tac_game.player_move()
            tic_tac_game.get_winner(" X ")
            if tic_tac_game.get_winner(" X ") or tic_tac_game.check_draw():
                tic_tac_board.show_board()
                print("\n")
            tic_tac_game.end_game()

        else:
            tic_tac_board.is_board_full()
            tic_tac_game.get_best_move()
            tic_tac_game.player_move()
            tic_tac_game.get_winner(" O ")
            if tic_tac_game.get_winner(" O ") or tic_tac_game.check_draw():
                tic_tac_board.show_board()
                print("\n")
            tic_tac_game.end_game()


main()

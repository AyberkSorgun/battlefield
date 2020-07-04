from base import Board, GamePlay



if __name__ == "__main__":

    game_board = Board().get_instance()

    game_board.shoot("A4")

    print(game_board.get_instance())


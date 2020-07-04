from base import Board


def main():

    print("Welcome to the game of Battlefield! Please choose your difficulty: ")

    difficulty_level = ""

    while difficulty_level not  in ["1", "2", "3"]:
        difficulty_level = input("Press 1 for Easy, 2 for Medium and 3 for Hard \n")

    game_board = Board().get_instance()

    game_board.initialize_board(size=int(difficulty_level) * 8)


if __name__ == "__main__":
    main()



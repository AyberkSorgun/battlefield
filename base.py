from random import random

class Board:

    instance = None

    def get_instance(self):
        if Board.instance is None:
            Board()
        return Board.instance

    def __init__(self):
        if Board.instance is not None:
            raise Exception("There can only be one Board. This class is a singleton!")
        else:
            Board.instance = self

    def setup_board(self, size):
        """
        :param size: length of one side of the game board
        :return: a game board with size of (size x size)
        """

        print([["O" for i in range(size)] for j in range(size)])

    def add_ship(self,Ship: ship):



        return True

    def update_board(self, coordinate_x, coordinate_y):

        #missing the target
        if Board.get_instance()[coordinate_x][coordinate_y] == "O":
            Board.get_instance()[coordinate_x][coordinate_y] = "o"
            print("It's a miss")

        #hitting the target
        elif Board.get_instance()[coordinate_x][coordinate_y] == "X":
            Board.get_instance()[coordinate_x][coordinate_y] = "x"
            print("It's a hit!")


    def print_board(self,board):
        """
        :param board:
        :return: prints the game board to console
        """
        for rows in board:
            print(rows)


class GamePlay:

    def shoot(self, coordinate: str):

        # decomposing the coordinate into integers
        x_axis = coordinate[0]
        y_axis = int(coordinate[1])

        Board.update_board(x_axis, y_axis)


class Ship:



    def is_down(self):
        1


class Player:

    is_lost = False
    number_of_ships: int

    if number_of_ships == 0:
        is_lost = True



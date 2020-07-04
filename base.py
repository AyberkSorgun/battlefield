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

    def initialize_board(self, size):
        """
        :param size: length of one side of the game board
        :return: a game board with size of (size x size)
        """

        print([["O" for i in range(size)] for j in range(size)])

    def update_board(self, board, coordinate_x, coordinate_y):

        #missing the target
        if board[coordinate_x][coordinate_y] == "O":
            board[coordinate_x][coordinate_y] = "o"

        #hitting the target
        elif board[coordinate_x][coordinate_y] == "X":
            board[coordinate_x][coordinate_y] = "x"

        return board

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






class Ship:



    def is_down(self):
        1

    def create_ship(self):

        direction = random.randint(1, 2)


    def add_ship(self,ship,board: Board):
        #board.

        1





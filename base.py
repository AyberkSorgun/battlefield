from random import random


class Board:

    def initialize_board(self, size):
        """
        :param size: length of one side of the game board
        :return: a game board with size of (size x size)
        """
        return [["O" for i in range(size)] for j in range(size)]

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

    def shoot(self, coordinate):

        # decomposing the coordinate into integers
        x_axis = coordinate[0]
        y_axis = int(coordinate[1])






class Ships:

    def create_ship(self):

        direction = random.ranint(1,2)





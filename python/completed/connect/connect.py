from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Point:
    """
    Represents a point in two-dimensional space.

    Attributes:
        row (int): The row of the point.
        col (int): The column of the point.

    Methods:
        __add__(self, other: Point) -> Point: Adds the coordinates of two points.

    """

    row: int
    col: int

    def __add__(self, other: Point) -> Point:
        """
        Adds the coordinates of two points.

        Args:
            other (Point): The point to add to this point.

        Returns:
            Point: The result of adding the coordinates of this point and the other point.

        """
        return Point(self.row + other.row, self.col + other.col)


class ConnectGame:
    """
    A game of connect.

    Attributes:
        board (str): A string representing the game board.

    Methods:
        get_winner(self) -> str: Returns the winner of the game.
        check(self, player: str) -> bool: Checks if a player has won the game.

    """

    NEIGHBORS = ((1, 0), (0, -1), (0, 1), (1, -1), (-1, 0), (-1, 1))

    def __init__(self, board: str) -> None:
        """
        Initializes a new ConnectGame.

        Args:
            board (str): A string representing the game board.
        """
        self.board = board.replace(" ", "").splitlines()

    def get_winner(self) -> str:
        """
        Returns the winner of the game.

        Returns:
            str: The winner of the game, or an empty string if there is no winner.

        """
        for p in ["O", "X"]:
            if self.check(p):
                return p
        return ""

    def check(self, player: str) -> bool:
        """
        Checks if a player has won the game.

        Args:
            player (str): The player to check for a win.

        Returns:
            bool: True if the player has won the game, False otherwise.

        """
        board = self.board if player == "O" else list(zip(*self.board))
        points = [
            Point(r, c)
            for r, row in enumerate(board)
            for c, col in enumerate(row)
            if col == player
        ]
        if not points:
            return False

        length = len(points.copy())
        curr = points.pop(0)

        if curr.row != 0:
            return False

        for _ in range(length):
            for neighbor in self.NEIGHBORS:
                next = curr + Point(*neighbor)
                if next in points:
                    points.remove(next)
                    curr = next
                    break

        return curr.row == len(board) - 1

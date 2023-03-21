from typing import Any


class Matrix:
    """A Class represents a Matrix object."""

    def __init__(self, matrix_string: str) -> None:
        """Constructs a matrix object from a string representation of the matrix.

        The matrix string must consist of one or more rows of integers separated by whitespace
        and newlines. For example: "1 2 3\n4 5 6\n7 8 9".

        Args:
            matrix_string (str): A string representing the matrix.

        Returns:
            None
        """
        self.matrix = list()

        for row in matrix_string.splitlines():
            self.matrix.append([int(r) for r in row.split()])

    def row(self, index: int) -> list[Any]:
        """Returns the specified row of the matrix.

        Args:
            index (int): The index of the row to retrieve, where the first row has index 1.

        Returns:
            list[Any]: A list containing the specified row.
        """
        return self.matrix[index - 1]

    def column(self, index: int) -> list[Any]:
        """Returns the specified column of the matrix.

        Args:
            index (int): The index of the column to retrieve, where the first column has index 1.

        Returns:
            list[Any]: A list containing the specified column.
        """
        return [row[index - 1] for row in self.matrix]

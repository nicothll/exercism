from __future__ import annotations


class Queen:
    """Represents a Queen object."""

    def __init__(self, row: int, column: int):
        """Initializes Queen object.

        Args:
            row (int): Queen position on the row.
            column (int): Queen position on the column.

        Raises:
            ValueError: row or column are not positive.
            ValueError: row or column are not on the board.

        """
        self._row = row
        self._column = column

        if self._row < 0:
            raise ValueError("row not positive")
        if self._row > 7:
            raise ValueError("row not on board")
        if self._column < 0:
            raise ValueError("column not positive")
        if self._column > 7:
            raise ValueError("column not on board")

    def can_attack(self, another_queen: Queen) -> bool:
        """Checks if the Queen object can attack another Queen object.

        Args:
            another_queen (Queen): An given another Queen object.

        Returns:
            bool: Can it attack?
        """
        if (self._row, self._column) == (another_queen._row, another_queen._column):
            raise ValueError("Invalid queen position: both queens in the same square")
        if self._row == another_queen._row or self._column == another_queen._column:
            return True
        if abs(self._row - another_queen._row) == abs(
            self._column - another_queen._column
        ):
            return True
        return False

import itertools
import re

MINE = "*"
NEIGHBORS = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))


def is_valid(board: list[str]) -> bool:
    """Checks if the minefield board is valid.

    Args:
        board (list[str]): The minefield board represented as a list of strings.

    Returns:
        bool: True if the board is valid, False otherwise.

    Raises:
        ValueError: If the board is invalid with the current input.
    """
    length = len(board[0])
    for row in board:
        if length != len(row) or not re.match(r"[\s\*]*$", row):
            return False
    return True


def annotate(minefield: list[str]) -> list[str]:
    """Annotates the minefield with the number of adjacent mines.

    Args:
        minefield (list[str]): The minefield represented as a list of strings.

    Returns:
        list[str]: The annotated minefield with numbers indicating the number of adjacent mines.

    Raises:
        ValueError: If the board is invalid with the current input.

    Note:
        The minefield should consist of the characters '*', ' ', and newline.
        '*' represents a mine, ' ' represents an empty cell, and newline separates rows.
        The returned annotated minefield will have numbers indicating the number of adjacent mines for each empty cell.
        The original minefield will remain unchanged.
    """
    if not minefield:
        return minefield
    if not is_valid(minefield):
        raise ValueError("The board is invalid with current input.")

    nb_rows, nb_cols = len(minefield), len(minefield[0])
    board = [[0] * nb_cols for _ in range(nb_rows)]

    for idx_row, row in enumerate(minefield):
        for idx_col, item in enumerate(row):
            if item == MINE:
                board[idx_row][idx_col] = MINE
                for n_row, n_col in NEIGHBORS:
                    r = idx_row + n_row
                    c = idx_col + n_col
                    if r >= 0 and c >= 0:
                        try:
                            board[r][c] += 1
                        except (TypeError, IndexError):
                            continue
    return ["".join(map(lambda x: str(x) if x != 0 else " ", r)) for r in board]

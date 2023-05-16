import re

MINE = "*"
NEIGHBORS = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))


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

    nb_rows, nb_cols = len(minefield), len(minefield[0])

    # Create matrix fill of zeros
    board = [[0] * nb_cols for _ in range(nb_rows)]

    for idx_row, row in enumerate(minefield):
        if nb_cols != len(row) or not re.match(r"[\s\*]*$", row):
            raise ValueError("The board is invalid with current input.")
        for idx_col, cell in enumerate(row):
            if cell == MINE:
                board[idx_row][idx_col] = MINE
                for n_row, n_col in NEIGHBORS:
                    r = idx_row + n_row
                    c = idx_col + n_col
                    if (
                        r < 0
                        or r > nb_rows - 1
                        or c < 0
                        or c > nb_cols - 1
                        or board[r][c] == MINE
                    ):
                        continue
                    board[r][c] += 1

    annotated_field = []
    for row in board:
        annotated_field.append("".join(map(lambda x: str(x) if x != 0 else " ", row)))
    return annotated_field

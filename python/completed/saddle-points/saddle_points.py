def saddle_points(matrix: list[list[int]]) -> list[dict[str:int]]:
    """Find saddle points in a matrix.

    A saddle point is an element that is greater than or equal to all elements in its row
    and less than or equal to all elements in its column.

    Args:
        matrix (list[list[int]]): A matrix represented as a list of lists of integers.

    Returns:
        list[dict[str,int]]: A list of dictionaries containing the row and column indices
        of each saddle point found. If no saddle points are found, an empty list is returned.

    Raises:
        ValueError: If the matrix is not rectangular (i.e., it has rows of different lengths).

    """

    if len({len(r) for r in matrix}) > 1:
        raise ValueError("irregular matrix")

    check_col = lambda mx, idx: all(map(lambda n: mx <= n, list(zip(*matrix))[idx]))

    saddle = list()
    for idx_row, row in enumerate(matrix):
        _max = max(row)
        for idx_col, nb in enumerate(row):
            if nb == _max and check_col(_max, idx_col):
                saddle.append({"row": idx_row + 1, "column": idx_col + 1})
    return saddle

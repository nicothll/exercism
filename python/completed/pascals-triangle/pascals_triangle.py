def rows(row_count):
    if row_count < 0:
        raise ValueError("number of rows is negative")
    elif row_count == 0:
        return []
    elif row_count == 1:
        return [[1]]

    triangle: list = rows(row_count - 1)
    last = triangle[-1]
    new = [1] + [last[i] + last[i + 1] for i in range(len(last) - 1)] + [1]
    triangle.append(new)
    return triangle

import itertools


def transpose(lines: str) -> str:
    """
    Transposes the given lines by swapping rows and columns.

    Args:
        lines (str): A string containing one or more lines of text to be transposed.

    Returns:
        str: The transposed lines, with rows and columns swapped.
    """
    # Transpose the lines using itertools.zip_longest()
    # and fill any empty cells with the character '*'.

    T = itertools.zip_longest(*lines.splitlines(), fillvalue="*")

    # Join the transposed cells into rows and remove any trailing '*' characters.
    # Replace any remaining '*' characters with spaces.
    transposed_lines = ["".join(l).rstrip("*").replace("*", " ") for l in list(T)]

    return "\n".join(transposed_lines)

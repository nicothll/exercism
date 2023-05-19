from typing import Generator


def formatting(
    input: list[tuple[str]],
    filename_only: bool,
    show_numbers: bool,
    add_filenames: bool,
) -> str:
    """Formats the input based on specified flags.

    Args:
        input (list[tuple[str]]): The input to be formatted, which is a list of tuples.
        filename_only (bool): Indicates whether to display only the filenames.
        show_numbers (bool): Indicates whether to display line numbers.
        add_filenames (bool): Indicates whether to include filenames in the formatted output.

    Returns:
        str: The formatted output as a string.

    """
    formatted = []

    for file, n_line, line in input:
        if filename_only:
            if file not in formatted:
                formatted.append(file)
            continue

        output = []
        if add_filenames:
            output.append(file)
        if show_numbers:
            output.append(n_line)
        output.append(line)
        formatted.append(":".join(output))

    return "\n".join(formatted) + "\n" if formatted else ""


def search(text: str, flags: str, pattern: str) -> Generator[str, None, None]:
    """Yields each matching line in the text.
    Args:
        text (str): The text that is searched.
        flags (str): The flags that determine how the search is performed.
        pattern (str): The pattern to search for.

    Yields:
        str: The matching line in the text.

    """
    if "-i" in flags:
        pattern = pattern.lower()

    for i, line in enumerate(text.splitlines(), start=1):
        original = line
        if "-i" in flags:
            line = line.lower()

        if "-x" in flags:
            match = pattern == line
        else:
            match = pattern in line
        if "-v" in flags:
            match = not match
        if match:
            yield str(i), original


def grep(pattern: str, flags: str, files: list[str]) -> str:
    """Searches for a pattern in one or more files, taking into account flags.

    Args:
        pattern (str): The pattern to search for.
        flags (str): The flags that determine how the search is performed.
        files (list[str]): The list of files to search in.

    Returns:
        str: The results of the search as a string.

    """
    results = []
    for file in files:
        with open(file) as f:
            text = f.read()

        results += [
            (file, n_line, line) for n_line, line in search(text, flags, pattern)
        ]

    return formatting(
        results,
        filename_only="-l" in flags,
        show_numbers="-n" in flags,
        add_filenames=len(files) > 1,
    )

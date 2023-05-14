from typing import Generator


def formatting(text: list[str], sep: str = "\n") -> str:
    return f"{sep}".join(text)


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
            yield formatting([str(i), original], sep=":") if "-n" in flags else original


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

        lines = search(text, flags, pattern)

        if len(files) > 1:
            lines = (formatting([file, line], sep=":") for line in lines)

        if lines := list(lines):
            results.append(file if "-l" in flags else formatting(lines))

    return formatting(results) + "\n" if results else ""

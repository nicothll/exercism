from typing import Generator

FLAGS = ("-n", "-l", "-i", "-v", "-x")


def search(text: str, flags: str, pattern: str) -> Generator:
    """Yields each matching line in the text.

    Yields:
        str: The matching line in the text.

    """
    for i, line in enumerate(text.splitlines(), start=1):
        original = line
        if "-i" in flags:
            pattern, line = pattern.lower(), line.lower()

        if "-x" in flags:
            match = pattern == line
        else:
            match = pattern in line
        if "-v" in flags:
            match = not match
        if match:
            yield f"{i}:{original}" if "-n" in flags else original


def grep(pattern: str, flags: str, files: list[str]) -> str:
    """Searches for a pattern in one or more files, taking into account flags.

    Args:
        pattern (str): The pattern to search for.
        flags (str): The flags that determine how the search is performed.
        files (list[str]): The list of files to search in.

    Returns:
        str: The results of the search as a string.

    """
    results = ""
    for file in files:
        with open(file) as f:
            text = f.read()

        lines = search(text, flags, pattern)

        lines_list = (
            [f"{file}:{line}" for line in lines] if len(files) > 1 else list(lines)
        )

        if lines_list:
            results += (file if "-l" in flags else "\n".join(lines_list)) + "\n"
    return results

from typing import Iterator


class Search:
    """Searches for a pattern in a given text, taking into account flags.

    Attributes:
        original_txt (str): The original text that was searched.
        flags (str): The flags that determine how the search is performed.
        pattern (str): The pattern that is searched for.
        txt (str): The text that is searched, possibly in lowercase.

    Methods:
        _checking(line: str) -> bool:
            Returns whether the line matches the pattern.
        _checking_lines() -> Iterator[bool]:
            Yields a Boolean value for each line indicating whether it matches the pattern.
        lines() -> Iterator[str]:
            Yields each matching line in the original text.

    """

    def __init__(self, text: str, flags: str, pattern: str) -> None:
        """Initializes a new instance of the Search class.

        Args:
            text (str): The text to be searched.
            flags (str): The flags that determine how the search is performed.
            pattern (str): The pattern that is searched for.

        """
        self.original_txt = text
        self.flags = flags

        if "-i" in flags:
            self.pattern, self.txt = pattern.lower(), text.lower()
        else:
            self.pattern, self.txt = pattern, text

    def _checking(self, line: str) -> bool:
        """Checks if the given line matches the pattern, taking into account the flags.

        Args:
            line (str): The line to be checked.

        Returns:
            bool: True if the line matches the pattern; otherwise, False.

        """
        return self.pattern == line if "-x" in self.flags else self.pattern in line

    def _checking_lines(self) -> Iterator[bool]:
        """Yields a Boolean value for each line indicating whether it matches the pattern.

        Yields:
            bool: True if the line matches the pattern; otherwise, False.

        """
        for line in self.txt.splitlines():
            response = self._checking(line)
            yield not response if "-v" in self.flags else response

    def lines(self) -> Iterator[str]:
        """Yields each matching line in the original text.

        Yields:
            str: The matching line in the original text.

        """
        for (i, line), in_line in zip(
            enumerate(self.original_txt.splitlines()), self._checking_lines()
        ):
            if in_line:
                yield f"{i+1}:{line}" if "-n" in self.flags else line


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
            search = Search(f.read(), flags, pattern)
            lines = search.lines()

            lines_list = (
                [f"{file}:{line}" for line in lines] if len(files) > 1 else list(lines)
            )

            if lines_list:
                results += (file if "-l" in flags else "\n".join(lines_list)) + "\n"
    return results

from typing import Iterator

FLAGS = ("-n", "-l", "-i", "-v", "-x")


class Search:
    """Searches for a pattern in a given text, taking into account flags.

    Attributes:
        original_txt (str): The original text that was searched.
        flags (str): The flags that determine how the search is performed.
        pattern (str): The pattern that is searched for.
        txt (str): The text that is searched, possibly in lowercase.

    Methods:
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
        self.n, _, i, self.v, self.x = [flag in flags for flag in FLAGS]

        if i:
            self.pattern, self.txt = pattern.lower(), text.lower()
        else:
            self.pattern, self.txt = pattern, text

    def lines(self) -> Iterator[str]:
        """Yields each matching line in the original text.

        Yields:
            str: The matching line in the original text.

        """
        for (i, original), line in zip(
            enumerate(self.original_txt.splitlines()), self.txt.splitlines()
        ):
            response = self.pattern == line if self.x else self.pattern in line

            if not response if self.v else response:
                yield f"{i+1}:{original}" if self.n else original


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

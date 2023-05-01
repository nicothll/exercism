class OCRNumbers:
    """A class that converts OCR representations of numbers to their actual numerical value.

    Attributes:
        DIGITS (tuple): A tuple of integers representing the digits 0-9.
        ROWS (list): A list of dictionaries representing the rows of the OCR representation and their
                     corresponding digit mappings.

    Args:
        sequence (list[str]): A list of strings representing the OCR representation of a number.

    Raises:
        ValueError: If the number of input lines is not a multiple of four or the number of input
                    columns is not a multiple of three.

    Methods:
        get_digit: Returns the numerical value of a single digit in the OCR representation.
        digits: Returns the numerical value of the entire OCR representation.

    """

    DIGITS = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
    ROWS = [
        {"...": (1, 4), "._.": (2, 3, 5, 6, 7, 8, 9, 0)},
        {"..|": (1, 7), "._|": (2, 3), "|_|": (4, 8, 9), "|_.": (5, 6), "|.|": (0,)},
        {"..|": (1, 4, 7), "._|": (3, 5, 9), "|_|": (6, 8, 0), "|_.": (2,)},
        {"...": DIGITS},
    ]

    def __init__(self, sequence: list[str]) -> None:
        """Initializes a new instance of the OCRNumbers class.

        Args:
            sequence (list[str]): A list of strings representing the OCR representation of a number.

        Raises:
            ValueError: If the number of input lines is not a multiple of four or the number of input
                        columns is not a multiple of three.

        """

        self.sequence = sequence

        if len(self.sequence) % 4 != 0:
            raise ValueError("Number of input lines is not a multiple of four")
        elif tuple({len(r) for r in self.sequence})[0] % 3 != 0:
            raise ValueError("Number of input columns is not a multiple of three")

    def get_digit(self, value: str) -> str:
        """Returns the numerical value of a single digit in the OCR representation.

        Args:
            value (str): A string representing the OCR representation of a single digit.

        Returns:
            str: The numerical value of the digit.

        """
        digits = set(self.DIGITS)
        for r, item in enumerate(value):
            row = self.ROWS[r].get(item.replace(" ", "."), "?")
            digits = digits & set(row)
        return str(digits.pop()) if digits else "?"

    @property
    def digits(self) -> str:
        """Returns the numerical value of the entire OCR representation.

        Returns:
            str: The numerical value of the OCR representation.

        """
        ocr_digits = {}
        for row in self.sequence:
            for i, idx in enumerate(range(0, len(row), 3)):
                d = ocr_digits.get(i, [])
                d.append(row[idx : idx + 3])
                ocr_digits[i] = d
        return "".join(self.get_digit(v) for v in ocr_digits.values())


def convert(input_grid: list[str]) -> str:
    """Converts a list of OCR input grid strings into a string of digit characters.

    Args:
        input_grid (list[str]): A list of OCR input grid strings.

    Returns:
        str: A string of digit characters.

    Raises:
        ValueError: If the number of input lines is not a multiple of four or
            the number of input columns is not a multiple of three
    """
    if len(input_grid) > 4:
        rows = [input_grid[i : i + 4] for i in range(0, len(input_grid), 4)]
        return ",".join(OCRNumbers(row).digits for row in rows)
    return OCRNumbers(input_grid).digits

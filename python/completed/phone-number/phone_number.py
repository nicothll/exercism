import re


class PhoneNumber:
    """A class representing a phone number.

    The phone number is stored as a string and may contain digits, parentheses,
    hyphens, and spaces. The class provides methods for checking and cleaning
    the phone number.

    Args:
        number (str): The phone number.

    Attributes:
        number (str): The phone number without spaces.
        area_code (str): The area code extracted from the phone number.

    Raises:
        ValueError: If the phone number is not in a valid format.
    """

    def __init__(self, number: str) -> None:
        """Initializes a PhoneNumber object

        Args:
            number (str): The phone number
        """
        self._number = number.replace(" ", "")

        self._checking()

        self._cleaning()

    def _checking(self):
        """Checks the phone number format.

        Raises:
            ValueError: The letters are not permitted.
            ValueError: The punctuations are not permitted.
            ValueError: If the number has 11 digits, it must start with +1 or 1.
        """

        if re.search(r"[A-Za-z]", self._number):
            raise ValueError("letters not permitted")

        if re.search(r"[!@#$%&:]", self._number):
            raise ValueError("punctuations not permitted")

        if len(self._number) == 11 and self._number[0] not in ["+1", "1"]:
            raise ValueError("11 digits must start with 1")

    def _cleaning(self):
        """Cleans and verifies the phone number format.

        Raises:
            ValueError: The area code cannot start with 0 or 1.
            ValueError: The exchange code cannot start with 0 or 1.
            ValueError: The phone number must contain 10 or 11 digits.
        """

        nb_phone = re.sub(r"^\+?1", "", self._number)
        self._number = re.sub(r"[().-]", "", nb_phone).strip()

        if self._number[0] == "0":
            raise ValueError("area code cannot start with zero")

        if self._number[0] == "1":
            raise ValueError("area code cannot start with one")

        if self._number[3] == "0":
            raise ValueError("exchange code cannot start with zero")

        if self._number[3] == "1":
            raise ValueError("exchange code cannot start with one")

        if len(self._number) < 10:
            raise ValueError("must not be fewer than 10 digits")

        if len(self._number) > 10:
            raise ValueError("must not be greater than 11 digits")

    def pretty(self) -> str:
        """Pretties the phone number with parentheses and hyphens.

        Returns:
            str: The formatted phone number.
        """

        number = list(self._number[1:] if len(self._number) > 10 else self._number)
        number.insert(0, "(")
        number.insert(4, ")-")
        number.insert(8, "-")

        return "".join(number)

    @property
    def area_code(self) -> str:
        """Returns the area code of the phone number.

        Returns:
            str: The area code.
        """
        return self._number[:3]

    @property
    def number(self) -> str:
        """Returns the cleaned phone number (only digits)

        Returns:
            str: The cleaned phone number.
        """
        return self._number

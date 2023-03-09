import re


class Luhn:
    """
    A class represents Luhn object.

    The Luhn algorithm is a simple checksum formula used to validate a variety of identification numbers,
    such as credit card numbers and Canadian Social Insurance Numbers.
    """

    def __init__(self, card_num: str):
        """Initializes Luhn class

        Args:
            card_num (str): A given card number
        """
        self._card_num = card_num

    def valid(self) -> bool:
        """
        Given a number determine whether or not it is valid per the Luhn formula.

        Returns:
            bool: Is it pass the Luhn test?
        """
        card_num = self._card_num.replace(" ", "")
        if re.search(r"\D", card_num) or len(card_num) < 2:
            return False

        card_num = list(card_num)
        doubled = map(lambda x: self.__doubling(x), card_num[-2::-2])
        others = map(lambda x: int(x), card_num[::-2])

        return sum([*doubled, *others]) % 10 == 0

    @staticmethod
    def __doubling(_number: str | int) -> int:
        """Doubled the number, if it's superior at 9 remove from it.

        Args:
            _number (str | int): A given number can be a string or integer.

        Returns:
            int: number transformed.
        """
        number = int(_number) * 2
        return number if number < 9 else number - 9

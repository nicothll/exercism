import itertools
import string
import random
from typing import Optional


class Cipher:
    """A class representing a simple Cipher.

    Attributes:
        (class) ALPHABET (str): The alphabet in lowercase.
        key (str, optional): The cipher key, generates randomly if None.

    Methods:
        caesar_alphabet(): Returns the caesar alphabet according to normal alphabet index.
        encode(text): Returns the given text encoded.
        decode(text): Returns the given text decoded.
        (private) encoder(text, mode): Returns the text encoded or decoded according the mode.
    """

    ALPHABET = string.ascii_lowercase

    def __init__(self, key: Optional[str] = None) -> None:
        """Initializes the Cipher object.

        Args:
            key (str, optional): The Cipher key. Defaults to None, generate a truly random key of at least 100 lowercase characters in length.
        """
        self.key = key if key else "".join(random.choices(list(self.ALPHABET), k=100))

    def caesar_alphabet(self, idx: int) -> str:
        """Generates the Caesar Alphabet.

            If the idx greater than the alphabet length returns the normal alphabet

        Args:
            idx (int): A given index represents the position in alphabet.

        Returns:
            str: The Caesar Alphabet, or Normal Alphabet if idx is greater than alphabet length.
        """
        return (
            self.ALPHABET[idx:] + self.ALPHABET[:idx]
            if idx < len(self.ALPHABET) + 1
            else self.ALPHABET
        )

    def encode(self, text: str) -> str:
        """Encodes the given text.

        Args:
            text (str): The given text to encode.

        Returns:
            str: The text encoded.
        """
        return self.__encoder(text)

    def decode(self, text: str) -> str:
        """Decodes the given text.

        Args:
            text (str): A given text to decode.

        Returns:
            str: The text decoded.
        """
        return self.__encoder(text, "decode")

    def __encoder(
        self,
        text: str,
        mode: str = None,
    ) -> str:
        """Encodes or decodes the given text according to the mode.

        Args:
            text (str): The text to encode or decode
            mode (str, optional): Given mode. Defaults to None is encode mode

        Returns:
            str: The text encoded or decoded.
        """

        result = str()
        for k, ch in zip(itertools.cycle(self.key), text):
            idx = self.ALPHABET.index(k)
            if mode == "decode":
                result += self.ALPHABET[self.caesar_alphabet(idx).index(ch)]
            else:
                result += self.caesar_alphabet(idx)[self.ALPHABET.index(ch)]
        return result

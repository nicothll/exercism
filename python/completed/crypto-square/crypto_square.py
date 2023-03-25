import re
import itertools
import math


def cipher_text(plain_text: str) -> str:
    """Encodes the classic method for composing secret messages called a square code.

    Args:
        plain_text (str): The given an English text.

    Returns:
        str: The encoded version of the text.
    """
    text = re.sub(r"[,.!?\s@%-]+", "", plain_text).lower()
    if len(text) < 2:
        return text

    col = math.ceil(len(text) ** 0.5)

    chunks = [text[idx - col : idx] for idx in range(col, len(text) + col, col)]
    T = itertools.zip_longest(*chunks, fillvalue="$")

    return " ".join("".join(ch).replace("$", " ") for ch in T)

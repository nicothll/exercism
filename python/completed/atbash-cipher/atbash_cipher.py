import string

ALPHABET = string.ascii_lowercase
SECRET = str.maketrans(ALPHABET, ALPHABET[::-1])


def _clean(text: str) -> str:
    """Returns text with only alpha or digit character.

    :param text: str - The text to clean.
    :return: str - The text cleaned.
    """
    return "".join(ch.lower() for ch in text if ch.isalnum())


def _split(text: str) -> str:
    """Returns the text with whitespace every 5 character.

    :param text: str - The text to split up.
    :return: str - The text chunked.
    """
    if len(text) <= 5:
        return text
    return text[:5] + " " + _split(text[5:])


def encode(plain_text: str) -> str:
    """Encode a text into an atbash cipher.

    :param plain_text: str - Given text.
    :return: str - Encrypted text.
    """
    return _split(_clean(plain_text).translate(SECRET))


def decode(ciphered_text: str) -> str:
    """Dencode an atbash cipher text.

    :param ciphered_text: str - Given encrypted text.
    :return: str - Decrypted text.
    """
    return _clean(ciphered_text.translate(SECRET))

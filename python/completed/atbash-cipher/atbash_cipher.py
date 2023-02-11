import string

ALPHABET = string.ascii_lowercase
CIPHER = ALPHABET[::-1]


def encode(plain_text: str) -> str:
    """Encode a text into an atbash cipher.

    :param plain_text: str - Given text.
    :return: str - Encrypted text.
    """
    result = []
    count = 0
    for letter in plain_text.lower():
        if letter in ALPHABET:
            result.append(CIPHER[ALPHABET.index(letter)])
        elif letter.isdigit():
            result.append(letter)
        else:
            continue
        count += 1
        if count == 5:
            result.append(" ")
            count = 0
    return "".join(result).rstrip()


def decode(ciphered_text: str) -> str:
    """Dencode an atbash cipher text

    :param ciphered_text: str - Given encrypted text
    :return: str - Decrypted text
    """
    result = []
    for letter in ciphered_text:
        if letter in CIPHER:
            result.append(ALPHABET[CIPHER.index(letter)])
        elif letter.isdigit():
            result.append(letter)
    return "".join(result)

ALPHA = "abcdefghijklmnopqrstuvwxyz"


def rotate(text: str, key: int) -> str:
    """Given text and key create a Rotational Cipher

    :param text:  str - Given text
    :param key:  int - Given key
    :return: str - A Rotational Cipher
    """

    if key == 0:
        return text

    cipher = ALPHA[key:] + ALPHA[:key]

    response = []
    for ch in text:
        if ch not in ALPHA and ch not in ALPHA.upper():
            response.append(ch)
        elif ch.isupper():
            response.append(cipher[ALPHA.index(ch.lower())].upper())
        else:
            response.append(cipher[ALPHA.index(ch)])

    return "".join(response)

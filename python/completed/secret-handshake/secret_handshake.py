COMMANDS = ("jump", "close your eyes", "double blink", "wink")


def commands(binary_str: str) -> list[str]:
    """Convert binary number to the appropriate sequence of events for a secret handshake.

    :param binary_str: str - Binary number in string format.
    :return: list[str] - list of sequence with: wink, double blink, close your eyes or jump.
    """

    handshake = []
    for idx, b in enumerate(binary_str[1:]):
        if b == "1":
            handshake.append(COMMANDS[idx])
    if binary_str[0] == "0":
        handshake.reverse()
    return handshake

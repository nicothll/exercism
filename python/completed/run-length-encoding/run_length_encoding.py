def decode(string: str) -> str:
    """Decodes a given Run-length encoding (RLE).

    Args:
        string (str): A given encoded string.

    Returns:
        str: The string decoded.
    """

    _decode, digits = str(), str()

    for ch in string:
        if ch.isdigit():
            digits += ch
        else:
            _decode += ch * int(digits) if digits else ch
            digits = str()
    return _decode


def encode(string: str) -> str:
    """Encodes a given string to Run-length encoding (RLE).

    Args:
        string (str): A given string to encode.

    Returns:
        str: The string encoded.
    """

    if len(string) < 1:
        return ""

    code, memo = str(), dict()

    for idx, ch in enumerate(string):
        memo[ch] = memo.get(ch, 0) + 1
        if idx < len(string) - 1 and ch != string[idx + 1]:
            code += str(memo[ch]) + ch if memo[ch] > 1 else ch
            del memo[ch]
    code += str(memo[ch]) + ch if memo[ch] > 1 else ch
    return code

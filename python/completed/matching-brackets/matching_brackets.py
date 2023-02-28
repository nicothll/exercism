OPENED, CLOSED = tuple("[{("), tuple("]})")


def is_paired(input_string: str) -> bool:
    """Verify that any and all pairs are matched and nested correctly.

    Args:
        input_string (str): Given a string containing brackets [], braces {}, parentheses ().

    Returns:
        bool: Is it paired?
    """
    _map = dict(zip(OPENED, CLOSED))
    _memo = list()
    for ch in input_string:
        if ch in OPENED:
            _memo.append(_map[ch])
        elif ch in CLOSED:
            if not _memo or ch != _memo.pop():
                return False
    return len(_memo) == 0

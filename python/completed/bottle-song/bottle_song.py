NUMBERS = (
    "no",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
    "ten",
)


plural = lambda word, nb: word if nb == 1 else word + "s"


def recite(start: int, take: int = 1) -> list[str]:
    """Recites the lyrics to that popular children's repetitive song: Ten Green Bottles.

    Args:
        start (int): Number of bottles at the start
        take (int, optional): How many verses? Defaults to 1.

    Returns:
        list[str]: The list of the verses of the song.
    """
    song = list()

    for nb in range(start, start - take, -1):
        song += [
            f"{NUMBERS[nb].capitalize()} green {plural('bottle', nb)} hanging on the wall,",
            f"{NUMBERS[nb].capitalize()} green {plural('bottle', nb)} hanging on the wall,",
            "And if one green bottle should accidentally fall,",
            f"There'll be {NUMBERS[nb - 1]} green {plural('bottle', nb -1)} hanging on the wall.",
            "",
        ]

    return song[:-1]

LYRICS = [
    ("first", "and a Partridge in a Pear Tree."),
    ("second", "two Turtle Doves,"),
    ("third", "three French Hens,"),
    ("fourth", "four Calling Birds,"),
    ("fifth", "five Gold Rings,"),
    ("sixth", "six Geese-a-Laying,"),
    ("seventh", "seven Swans-a-Swimming,"),
    ("eighth", "eight Maids-a-Milking,"),
    ("ninth", "nine Ladies Dancing,"),
    ("tenth", "ten Lords-a-Leaping,"),
    ("eleventh", "eleven Pipers Piping,"),
    ("twelfth", "twelve Drummers Drumming,"),
]


def recite(start_verse: int, end_verse: int) -> list[str]:
    """Function that returns the lyrics of the song: "The Twelve Days of Christmas".

    :param start_verse: int - given verse
    :param end_verse: int - given verse
    :return: list[str] - list of lyrics of the song
    """
    lyrics = []
    for idx in range(start_verse - 1, end_verse):
        if idx == 0:
            lyrics.append(
                f"On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree."
            )

        else:
            lyrics.append(
                f"On the {LYRICS[idx][0]} day of Christmas my true love gave to me: {' '.join(LYRICS[i - 1][1] for i in range(idx + 1, 0, -1))}"
            )
    return lyrics

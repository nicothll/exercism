RHYME = (
    "This is the horse and the hound and the horn",
    "that belonged to the farmer sowing his corn",
    "that kept the rooster that crowed in the morn",
    "that woke the priest all shaven and shorn",
    "that married the man all tattered and torn",
    "that kissed the maiden all forlorn",
    "that milked the cow with the crumpled horn",
    "that tossed the dog",
    "that worried the cat",
    "that killed the rat",
    "that ate the malt",
    "that lay in the house that Jack built.",
)


def recite(start_verse: int, end_verse: int) -> list[str]:
    """Returns a list of verses between the specified start and end verse.

    :param start_verse: int - The starting verse
    :param end_verse: int - The ending verse
    :return: list[str] - A list of strings representing the verses
    """

    result = []
    while start_verse <= end_verse:
        verse = list(RHYME[-abs(start_verse) :])

        # Replace the beginning of the first element
        verse[0] = "This is the" + verse[0].split("the", 1)[1]
        result.append(" ".join(verse))
        start_verse += 1

    return result

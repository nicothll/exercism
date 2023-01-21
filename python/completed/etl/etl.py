def transform(legacy_data: dict[int : list[str]]) -> dict[str:int]:
    """Function that transform Scrabble legacy data into a new shiny data

    :param legacy_data: dict[int:list[str]] - Legacy data of Scrabble
    :return: dict[str:int] - Shiny data
    """
    shiny_data = {}
    for score, letters in legacy_data.items():
        for letter in letters:
            shiny_data[letter.lower()] = score
    return shiny_data

def is_pangram(sentence: str) -> bool:
    """Function verifies if the sentence is a pangram.
    A pangram is a sentence using every letter of the alphabet at least once

    :param sentence: str - given sentence
    :return: bool - Is it pangram?
    """

    return len({ch for ch in sentence.lower() if ch.isalpha()}) == 26
    
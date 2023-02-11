import re


def count_words(sentence: str) -> dict[str:int]:
    """Counts the occurrences of each word in that phrase.

    :param sentence: str - The given phrase.
    :return: dict[str: int] - The number of occurrences for each word.
    """
    word_counter = {}

    sentence = re.sub(r"[?.,:_!&@$%\^&\t\n\"]", " ", sentence)
    for word in sentence.split():
        word = word.lower()
        if word := re.sub(r"^\'+|\'+$", "", word):
            word_counter[word] = word_counter.get(word, 0) + 1
    return word_counter

def find_anagrams(word: str, candidates: list[str]) -> list[str]:
    """Find anagrams in a list of words according to a target word.

    :param word: str - The target word.
    :param candidates: list[str] - A list of words to check for anagrams.
    :return: list[str] - A list of anagrams found in the candidates.
                        If no anagrams are found, an empty list is returned.
    """
    return [
        candidate
        for candidate in candidates
        if sorted(candidate.lower()) == sorted(word.lower())
        and candidate.lower() != word.lower()
    ]

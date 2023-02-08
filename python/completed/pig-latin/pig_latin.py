import re


def translate(text: str) -> str:
    """Translate from English to Pig Latin.

    Pig Latin is a made-up children's language.

    :param text: str - english text to translate.
    :return: str - text translated in Pig Latin.
    """
    translation = []
    for word in text.split():
        if re.search(r"^(xr|yt|[aeiou])", word):
            translation.append(word + "ay")
        elif match := re.search(r"^.*(qu)", word):
            idx = len(match.group())
            translation.append(word[idx:] + word[:idx] + "ay")
        elif len(word) > 1 and re.search(r"^[^aeiou]y", word):
            translation.append(word[1:] + word[0] + "ay")
        else:
            vowels = "aeiou"
            for i, letter in enumerate(word):
                if letter in vowels or (
                    i > 0 and word[i - 1] not in vowels and letter == "y"
                ):
                    translation.append(word[i:] + word[:i] + "ay")
                    break

    return " ".join(translation)

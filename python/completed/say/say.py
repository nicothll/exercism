ONES = ("", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine")
TEENS = (
    "ten",
    "eleven",
    "twelve",
    "thirteen",
    "fourteen",
    "fifteen",
    "sixteen",
    "seventeen",
    "eighteen",
    "nineteen",
)
TENS = (
    "",
    "",
    "twenty",
    "thirty",
    "forty",
    "fifty",
    "sixty",
    "seventy",
    "eighty",
    "ninety",
)
MORE = ("", "thousand", "million", "billion")


def say(number: int) -> str:
    """Spells out that number in English.

    Args:
        number (int): An integer number.

    Returns:
        str: The number writes in English.
    """

    if not -1 < number < 999_999_999_999:
        raise ValueError("input out of range")
    if number == 0:
        return "zero"

    digits = [int(d) for d in str(number)][::-1]
    words = list()

    for idx in range(0, len(digits), 3):
        word_group = list()
        group = digits[idx : idx + 3]

        # Single digit group
        if len(group) == 1:
            word_group.append(ONES[group[0]])

        # Two digits group
        elif len(group) == 2:
            if group[1] == 1:
                word_group.append(TEENS[group[0]])
            else:
                word_group.append(
                    TENS[group[1]] + "-" + ONES[group[0]]
                    if group[0] != 0
                    else TENS[group[1]]
                )

        # Three digits group
        else:
            if group[2] != 0:
                word_group.append(ONES[group[2]] + " hundred")
            if group[1] == 1:
                word_group.append(TEENS[group[0]])
            else:
                if group[0] and group[1] != 0:
                    word_group.append(TENS[group[1]] + "-" + ONES[group[0]])
                elif group[0] != 0:
                    word_group.append(ONES[group[0]])
                else:
                    word_group.append(TENS[group[1]])

        # Add suffix when more than hundred
        if idx > 0 and sum(group) != 0:
            word_group.append(MORE[idx // 3])

        words.append(" ".join(word_group))

    return " ".join(words[::-1]).strip()

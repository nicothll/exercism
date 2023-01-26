import operator
import re

OPS = {
    "plus": operator.add,
    "minus": operator.sub,
    "multiplied": operator.mul,
    "divided": operator.floordiv,
}


def answer(question: str) -> int:
    """Evaluate simple math word problems returning the answer as an integer.

    :param question: int - given question.
    :return: int - answer.
    """

    if question == "What is?":
        raise ValueError("syntax error")
    if re.match(r"What is (-?\d+)\?", question):
        return int(question.split()[-1][:-1])

    # Extracting
    # for match in re.finditer(r'-?[0-9]+|\b(plus|minus|multiplied|divided)\b', string):
    #     print(match.group())
    words = [
        word
        for word in question.replace("?", "").split()
        if word.lstrip("-").isnumeric() or word in OPS.keys()
    ]

    numbers = words[::2]
    operators = words[1::2]

    # Checking
    if not numbers or not operators:
        raise ValueError("unknown operation")
    if len(numbers) - len(operators) != 1:
        raise ValueError("syntax error")
    # Evaluating
    try:
        result = int(numbers[0])
        for nb, op in zip(numbers[1:], operators):
            result = OPS[op](result, int(nb))

        return result
    except (ValueError, KeyError):
        raise ValueError("syntax error")

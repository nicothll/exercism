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

    question = question.removeprefix("What is").removesuffix("?").strip()
    if not question:
        raise ValueError("syntax error")
    if question.isdigit():
        return int(question)

    # Extracting
    words = [
        match.group()
        for match in re.finditer(
            r"-?[0-9]+|\b(plus|minus|multiplied|divided)\b", question
        )
    ]

    numbers, operators = words[::2], words[1::2]

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

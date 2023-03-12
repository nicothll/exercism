import random
import math


class Character:
    """
    A class representing a character in a role-playing game.

    Attributes:
        abilities (tuple): A list of the character's ability names.
        strength (int): The character's strength score.
        dexterity (int): The character's dexterity score.
        constitution (int): The character's constitution score.
        intelligence (int): The character's intelligence score.
        wisdom (int): The character's wisdom score.
        charisma (int): The character's charisma score.
        hitpoints (int): The character's hit points, based on their constitution score.

    Methods:
        ability(): Returns a random ability score for the character.
    """

    def __init__(self):
        """
        Initializes a new Character object with random ability scores and hit points.
        """

        self.abilities = (
            "strength",
            "dexterity",
            "constitution",
            "intelligence",
            "wisdom",
            "charisma",
        )

        for ab in self.abilities:
            self.__setattr__(ab, self.ability())

        self.hitpoints = 10 + modifier(self.constitution)

    @staticmethod
    def ability() -> int:
        """
        Generates a random ability score for a character by rolling four six-sided dice and
        dropping the lowest roll.

        Returns:
            int: The total score of the three highest dice rolls.
        """
        dices = [random.randint(1, 6) for _ in range(4)]
        dices.remove(min(dices))
        return sum(dices)


def modifier(value: int) -> int:
    """
    Calculates the ability modifier for a given ability score.

    Args:
        value (int): The ability score to calculate the modifier for.

    Returns:
        int: The ability modifier.
    """
    return math.floor((value - 10) / 2)

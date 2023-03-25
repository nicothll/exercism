class Allergies:
    """
    A class representing a person's allergies.

    Attributes:
        (class) ITEMS (tuple[str:int]): The allergens with their scores.
        score (int): The allergy score.
        lst (list): A list of allergens that the person is allergic to.

    Methods:
        allergic_to(item): Returns whether the object is allergic to a given item or not.
    """

    ITEMS = (
        ("eggs", 1),
        ("peanuts", 2),
        ("shellfish", 4),
        ("strawberries", 8),
        ("tomatoes", 16),
        ("chocolate", 32),
        ("pollen", 64),
        ("cats", 128),
    )
    # Other allergens are double the value of the previous one and ignored for this exercise.

    def __init__(self, score: int) -> None:
        """Initializes an Allergies object with the given score.

        Args:
            score (int): The allergy score.
        """
        self.score = score
        self.__allergens = [
            item for item, value in self.ITEMS if self.score & value == value
        ]

    def allergic_to(self, item: str) -> bool:
        """Returns whether the object is allergic to a given item or not.

        Args:
            item (str): The item to check.

        Returns:
            bool: True if the object is allergic to the given item, False otherwise.
        """

        return item in self.__allergens

    @property
    def lst(self) -> list[str]:
        """Returns a list of allergens that the object is allergic to.

        Returns:
            List[str]: A list of allergens.
        """

        return self.__allergens

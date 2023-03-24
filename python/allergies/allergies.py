class Allergies:
    """
    A class representing a person's allergies.

    Attributes:
        (class) ITEMS (dict[str:int]): The allergens with their scores.
        score (int): The allergy score.
        lst (list): A list of allergens that the person is allergic to.

    Methods:
        allergic_to(item): Returns whether the object is allergic to a given item or not.
    """

    ITEMS = {
        "eggs": 1,
        "peanuts": 2,
        "shellfish": 4,
        "strawberries": 8,
        "tomatoes": 16,
        "chocolate": 32,
        "pollen": 64,
        "cats": 128,
    }
    # Other allergens are double the value of the previous one and ignored for this exercise.

    def __init__(self, score: int) -> None:
        """Initializes an Allergies object with the given score.

        Args:
            score (int): The allergy score.
        """

        self.score = score if score < 256 else score - 256
        self.__allergens = list()

    def allergic_to(self, item: str) -> bool:
        """Returns whether the object is allergic to a given item or not.

        Args:
            item (str): The item to check.

        Returns:
            bool: True if the object is allergic to the given item, False otherwise.
        """
        if self.score == 0:
            return False
        if self.score == 255:
            self.__allergens = list(self.ITEMS.keys())
            return True

        score = self.score
        for itm, value in list(self.ITEMS.items())[::-1]:
            if value <= score:
                self.__allergens.append(itm)
                score -= value
            if score < 1:
                break

        return item in self.__allergens

    @property
    def lst(self) -> list[str]:
        """Returns a list of allergens that the object is allergic to.

        Returns:
            List[str]: A list of allergens.
        """
        self.allergic_to("")
        return self.__allergens[::-1]

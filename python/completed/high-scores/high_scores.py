class HighScores:
    """A class representing a list of high scores.

    Attributes:
        scores (list): A list of high scores.

    Methods:
        latest(): Returns the most recent high score.
        personal_best(): Returns the personal best high score.
        personal_top_three(): Returns a list of the top three high scores.
    """

    def __init__(self, scores: list[int]):
        """Initializes a HighScores object with the given list of scores.

        Args:
            scores (list[int]): A list of high scores.
        """
        self.__scores = scores

    def latest(self) -> int:
        """Returns the most recent high score.

        Returns:
            int: The most recent high score.
        """
        return self.__scores[-1]

    def personal_best(self) -> int:
        """Returns the personal best high score.

        Returns:
            int: The personal best high score.
        """
        return max(self.__scores)

    def personal_top_three(self):
        """Returns a list of the top three high scores.

        Returns:
            List[int]: A list of the top three high scores.
        """
        return sorted(self.__scores, reverse=True)[:3]

    @property
    def scores(self) -> list[int]:
        """Returns the list of high scores.

        Returns:
            list[int]: A list of high scores.
        """
        return self.__scores

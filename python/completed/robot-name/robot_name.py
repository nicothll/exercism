import string
import random


class Robot:
    """
    A class representing a robot
    """

    def __init__(self) -> None:
        """
        Initializes a new instance of the Robot class.
        Automatically generates a pseudo-random name for the robot.
        """

        self._name = ""
        self._reset = 0
        self._generate_name()

    def _generate_name(self) -> str:
        """
        Generates a pseudo-random name for the robot. The name consists of
        2 uppercase letters and 3 digits.

        :return: str - The random name
        """
        letters = random.choices(string.ascii_uppercase, k=2)
        digits = random.choices(string.digits, k=3)
        self._name = "".join([*letters, *digits])

    def reset(self) -> None:
        """
        Resets the robot's name by generating a new pseudo-random name.
        """

        random.seed(self._reset)
        self._reset += 1
        self._generate_name()

    @property
    def name(self) -> str:
        """
        Returns the name of the robot.

        :return: str - Robot's name.
        """
        return self._name

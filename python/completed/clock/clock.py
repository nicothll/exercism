from __future__ import annotations


class Clock:
    """A class representing a clock.

    Attributes:
        hour (int): The current hour.
        minute (int): The current minute.

    Methods:
        __init__(hour, minute): Initializes the clock object.
        __repr__(): Returns a string representation of the clock object.
        __str__(): Returns a formatted string representing the current time.
        __eq__(other): Returns whether two clock objects have the same time.
        __add__(minutes): Adds a given number of minutes to the clock time and returns a formatted string.
        __sub__(minutes): Subtracts a given number of minutes from the clock time and returns a formatted string.
    """

    def __init__(self, hour: int, minute: int):
        """Initializes the clock object.

        Args:
            hour (int): The given hours.
            minute (int): The given minutes.
        """
        self.hour = hour
        self.minute = minute

        clockwise = self.minute > 0

        while self.minute >= 60 or self.minute < 0:
            if clockwise:
                self.minute -= 60
                self.hour += 1
            else:
                self.minute += 60
                self.hour -= 1

        self.hour = self.hour % 24

    def __repr__(self):
        """Returns a string representation of the clock object."""
        return f"{self.__class__.__name__}{self.hour, self.minute}"

    def __str__(self):
        """Returns a formatted string representing the current time."""
        return f"{self.hour:02d}:{self.minute:02d}"

    def __eq__(self, other: Clock) -> bool:
        """Returns whether two clock objects have the same time."""
        return self.hour == other.hour and self.minute == other.minute

    def __add__(self, minutes: int) -> str:
        """Adds a given number of minutes to the clock time and returns a formatted string.

        Args:
            minutes (int): The number of minutes to add.

        Returns:
            str: A formatted string representing the new time.
        """
        return str(Clock(self.hour, self.minute + minutes))

    def __sub__(self, minutes) -> str:
        """Subtracts a given number of minutes from the clock time and returns a formatted string.

        Args:
            minutes (int): The number of minutes to subtract.

        Returns:
            str: A formatted string representing the new time.
        """
        return str(Clock(self.hour, self.minute - minutes))

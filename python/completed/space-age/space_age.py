import functools


def rounding(digits: int):
    """Decorator function to round the return value of a function.

    Args:
        digits (int): The number of decimal places to round the return value to.

    Returns:
        A decorator function that can be applied to other functions to round their return values.
    """

    def _rounding(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return round(result, digits)

        return wrapper

    return _rounding


class SpaceAge:
    """Create an SpaceAge object with seconds.

    Attributes:
    - seconds (int): The given age in seconds.
    - age_earth (float): age on Earth according to seconds parameter.

    Methods:
    - on_mercury(): Return the age in seconds on Mercury.
    - on_venus(): Return the age in seconds on Venus.
    - on_earth(): Return the age in seconds on Earth.
    - on_mars(): Return the age in seconds on Mars.
    - on_jupiter(): Return the age in seconds on Jupiter.
    - on_saturn(): Return the age in seconds on Saturn.
    - on_uranus(): Return the age in seconds on Uranus.
    - on_neptune(): Return the age in seconds on Neptune.

    """

    def __init__(self, seconds: int) -> None:
        self.seconds = seconds
        self.age_earth = self.seconds / 31557600

    @rounding(2)
    def on_mercury(self) -> float:
        """
        Return the age in seconds on Mercury
        :return: float
        """
        return self.age_earth / 0.2408467

    @rounding(2)
    def on_venus(self) -> float:
        """
        Return the age in seconds on Venus
        :return: float
        """
        return self.age_earth / 0.61519726

    @rounding(2)
    def on_earth(self) -> float:
        """
        Return the age in seconds on Earth
        :return: float
        """
        return self.age_earth

    @rounding(2)
    def on_mars(self) -> float:
        """
        Return the age in seconds on Mars
        :return: float
        """
        return self.age_earth / 1.8808158

    @rounding(2)
    def on_jupiter(self) -> float:
        """
        Return the age in seconds on Jupiter
        :return: float
        """
        return self.age_earth / 11.862615

    @rounding(2)
    def on_saturn(self) -> float:
        """
        Return the age in seconds on Saturn
        :return: float
        """
        return self.age_earth / 29.447498

    @rounding(2)
    def on_uranus(self) -> float:
        """
        Return the age in seconds on Uranus
        :return: float
        """
        return self.age_earth / 84.016846

    @rounding(2)
    def on_neptune(self) -> float:
        """
        Return the age in seconds on Neptune
        :return: float
        """
        return self.age_earth / 164.79132

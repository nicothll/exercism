class SpaceAge:
    """Create an SpaceAge object with seconds.

    Attributes:
    - (class) ONE_YEAR_IN_SECONDS (int): one year in seconds on Earth.
    - seconds (int): The given age in seconds.
    - age_on_earth (float): age on Earth according to seconds parameter without rounding.

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

    ONE_YEAR_IN_SECONDS = 31557600

    def __init__(self, seconds: int) -> None:
        self.seconds = seconds
        self.age_on_earth = self.seconds / self.ONE_YEAR_IN_SECONDS

    def on_mercury(self) -> float:
        """
        Return the age in seconds on Mercury
        :return: float
        """
        return round(self.age_on_earth / 0.2408467, 2)

    def on_venus(self) -> float:
        """
        Return the age in seconds on Venus
        :return: float
        """
        return round(self.age_on_earth / 0.61519726, 2)

    def on_earth(self) -> float:
        """
        Return the age in seconds on Earth
        :return: float
        """
        return round(self.age_on_earth, 2)

    def on_mars(self) -> float:
        """
        Return the age in seconds on Mars
        :return: float
        """
        return round(self.age_on_earth / 1.8808158, 2)

    def on_jupiter(self) -> float:
        """
        Return the age in seconds on Jupiter
        :return: float
        """
        return round(self.age_on_earth / 11.862615, 2)

    def on_saturn(self) -> float:
        """
        Return the age in seconds on Saturn
        :return: float
        """
        return round(self.age_on_earth / 29.447498, 2)

    def on_uranus(self) -> float:
        """
        Return the age in seconds on Uranus
        :return: float
        """
        return round(self.age_on_earth / 84.016846, 2)

    def on_neptune(self) -> float:
        """
        Return the age in seconds on Neptune
        :return: float
        """
        return round(self.age_on_earth / 164.79132, 2)

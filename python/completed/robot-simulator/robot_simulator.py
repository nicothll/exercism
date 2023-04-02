# Globals for the directions

NORTH = ("N", "E", "S", "W")
EAST = ("E", "S", "W", "N")
SOUTH = ("S", "W", "N", "E")
WEST = ("W", "N", "E", "S")


class Robot:
    """A class representing a robot.

    Attributes:
        MOVES (dict[tuple[str], int]): A dictionary representing the moves a robot can make.
    Args:
        direction (tuple[str], optional): A tuple representing the initial direction. Defaults to NORTH.
        x_pos (int, optional): An integer representing the initial x position of the robot. Defaults to 0.
        y_pos (int, optional): An integer representing the initial y position of the robot. Defaults to 0.

    Methods:
        change_direction(_mvt, _directions): Change the direction of the robot based on the movement.
        move(path): Move the robot based on the given path.

    Properties:
        coordinates: Return a tuple representing the current coordinates of the robot.
        direction: Return a tuple representing the current direction of the robot.
    """

    MOVES = {NORTH: 1, EAST: 1, SOUTH: -1, WEST: -1}

    def __init__(
        self, direction: tuple[str] = NORTH, x_pos: int = 0, y_pos: int = 0
    ) -> None:
        """Initializes the Robot class.

        Args:
            direction (tuple[str], optional): A tuple representing the initial direction. Defaults to NORTH.
            x_pos (int, optional): An integer representing the initial x position of the robot. Defaults to 0.
            y_pos (int, optional): An integer representing the initial y position of the robot. Defaults to 0.
        """
        self._direction = direction
        self._x = x_pos
        self._y = y_pos

    def move(self, path: str) -> None:
        """Move the robot based on the given path.

        Args:
            path (str): A string representing the path to move.
        """
        for m in path:
            if m in ("R", "L"):
                self._direction = self.change_direction(m, self._direction)
            if m == "A":
                # Advance towards the direction
                if self._direction in (NORTH, SOUTH):
                    self._y += self.MOVES[self._direction]
                else:
                    self._x += self.MOVES[self._direction]

    @staticmethod
    def change_direction(_mvt, _directions: tuple[str]) -> tuple[str]:
        """Change the direction of the robot based on the movement.

        Args:
            _mvt (str): A string representing the movement.
            _directions (tuple[str]): A tuple representing the directions.

        Returns:
            tuple[str]: A tuple representing the updated directions.
        """
        _direction = list(_directions)
        if _mvt == "L":
            _direction.insert(0, _direction.pop())
        elif _mvt == "R":
            _direction.append(_direction.pop(0))
        return tuple(_direction)

    @property
    def coordinates(self):
        """Return a tuple representing the current coordinates of the robot.

        Returns:
            tuple[int, int]: A tuple representing the current coordinates of the robot.
        """
        return self._x, self._y

    @property
    def direction(self):
        """Return a tuple representing the current direction of the robot.

        Returns:
            tuple[str]: A tuple representing the current direction of the robot.
        """
        return self._direction

class Garden:
    """A class representing a garden in a classroom.

    Attributes:
        (class) PLANTS (dict): A dictionary containing the abbreviations and corresponding full names of the plants.
        (class) STUDENTS (list[str]): A list of the students' names.

    Args:
        diagram (str): A string representing the garden's layout.
        students (list[str], optional): A list of the students' names. Defaults to DEFAULT_STUDENTS.

    Methods:
        plants(student: str) -> list[str]: Returns the list of plants in the garden that the given student is responsible for.
    """

    PLANTS_NAMES = {"G": "Grass", "C": "Clover", "R": "Radishes", "V": "Violets"}

    DEFAULT_STUDENTS = [
        "Alice",
        "Bob",
        "Charlie",
        "David",
        "Eve",
        "Fred",
        "Ginny",
        "Harriet",
        "Ileana",
        "Joseph",
        "Kincaid",
        "Larry",
    ]

    def __init__(self, diagram: str, students: list[str] = DEFAULT_STUDENTS) -> None:
        """Initializes the Garden class.

        Args:
            diagram (str): A string representation of the garden layout for the class.
            students (list[str], optional): A list of student names. Defaults to DEFAULT_STUDENTS.
        """
        self._diagram = diagram.splitlines()
        self._students = sorted(self.DEFAULT_STUDENTS if students is None else students)

        self._garden = dict()

        for row in self._diagram:
            for s, p1, p2 in zip(self._students, row[::2], row[1::2]):
                self._garden.setdefault(s, []).extend(
                    list(map(lambda p: self.PLANTS_NAMES.get(p), [p1, p2]))
                )

    def plants(self, student: str) -> list[str]:
        """Returns the list of plants a given student has in their row of the garden.

        Args:
            student (str): The name of the student to retrieve the plants for.

        Returns:
            list[str]: A list of strings representing the plants in the student's row of the garden.
        """
        return self._garden.get(student, [])

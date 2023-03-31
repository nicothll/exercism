class Garden:
    """A class representing a garden in a classroom.

    Attributes:
        (class) PLANTS (dict): A dictionary containing the abbreviations and corresponding full names of the plants.
        (class) STUDENTS (list[str]): A list of the students' names.

    Args:
        diagram (str): A string representing the garden's layout.
        students (list[str], optional): A list of the students' names. Defaults to STUDENTS.

    Methods:
        plants(student: str) -> list[str]: Returns the list of plants in the garden that the given student is responsible for.
    """

    PLANTS = {"G": "Grass", "C": "Clover", "R": "Radishes", "V": "Violets"}

    STUDENTS = [
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

    def __init__(self, diagram: str, students: list[str] = STUDENTS) -> None:
        """Initializes the Garden class.

        Args:
            diagram (str): A string representation of the garden layout for the class.
            students (list[str], optional): A list of student names. Defaults to STUDENTS.
        """
        self._diagram = diagram.split()
        self._students = sorted(students)

        self._garden = dict()

        for row in self._diagram:
            for idx, student in zip(range(0, len(row), 2), self._students):
                plants = list(map(lambda p: self.PLANTS[p], list(row[idx : idx + 2])))
                self._garden[student] = self._garden.get(student, []) + plants

    def plants(self, student: str) -> list[str]:
        """Returns the list of plants a given student has in their row of the garden.

        Args:
            student (str): The name of the student to retrieve the plants for.

        Returns:
            list[str]: A list of strings representing the plants in the student's row of the garden.
        """
        return self._garden.get(student, [])

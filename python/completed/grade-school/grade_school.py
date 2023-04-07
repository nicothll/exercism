class School:
    def __init__(self):
        """Initializes a new instance of the School class."""

        self._students = dict()
        self._added = list()

    def add_student(self, name: str, grade: int) -> None:
        """Adds a new student to the school.

        Args:
            name (str): The name of the student to add.
            grade (int): The grade level of the student.

        Returns:
            None
        """

        if name not in self._students:
            self._students[name] = grade
            self._added.append(True)
        else:
            self._added.append(False)

    def roster(self) -> list[str]:
        """Gets the list of all students in the school in grade and alphabetical order.

        Returns:
            list[str]: The list of all students in the school.
        """

        students = sorted(self._students.items(), key=lambda x: (x[1], x[0]))
        return [name for name, _ in students]

    def grade(self, grade_number) -> list[str]:
        """Gets the list of students in a specific grade.

        Args:
            grade_number (int): The grade level to filter by.

        Returns:
            list[str]: The list of students in the specified grade, in alphabetical order.
        """

        students = [st for st, g in self._students.items() if g == grade_number]
        return sorted(students)

    def added(self) -> list[bool]:
        """Gets a list indicating whether each student added was new or already existed.

        Returns:
            list[bool]: A list of Boolean values indicating whether each student added was new or already existed.
        """
        return self._added

"""Student Grade Management System.

This module provides a Student class to manage grades, calculate averages,
determine letter grades, pass/fail status and honor roll.
"""

GRADE_MIN = 0.0
GRADE_MAX = 100.0
PASS_THRESHOLD = 60.0
HONOR_THRESHOLD = 90.0

class Student:
    """Represents a student with an ID, name and a list of grades."""

    def __init__(self, student_id: str, name: str) -> None:
        if not student_id or not student_id.strip():
            raise ValueError("Student ID cannot be empty.")
        if not name or not name.strip():
            raise ValueError("Student name cannot be empty.")

        self.student_id = student_id.strip()
        self.name = name.strip()
        self.grades: list[float] = []
        self.is_passed = "Failed"
        self.honor_roll = False

    def add_grade(self, grade: float) -> None:

        """Add a grade to the student."""

        if not isinstance(grade, (int, float)) or isinstance(grade, bool):
            raise ValueError(f"Grade must be numeric, got: {grade!r}")
        if grade < GRADE_MIN or grade > GRADE_MAX:
            raise ValueError(
                f"Grade must be between {GRADE_MIN} and {GRADE_MAX}, got: {grade}"
            )
        self.grades.append(float(grade))
        self._update_status()

    def calculate_average(self) -> float:
        """Return the average of all grades, or 0 if there are none."""
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)

    def get_letter_grade(self) -> str:

        """Return the letter grade based on the current average."""

        average = self.calculate_average()
        if average >= 90:
            return "A"
        if average >= 80:
            return "B"
        if average >= 70:
            return "C"
        if average >= 60:
            return "D"
        return "F"

    def _update_status(self) -> None:

        """Update pass/fail and honor roll based on current average."""

        average = self.calculate_average()
        self.is_passed = "Passed" if average >= PASS_THRESHOLD else "Failed"
        self.honor_roll = average >= HONOR_THRESHOLD

    def remove_grade_by_value(self, value: float) -> bool:

        """Remove the first grade matching the value."""

        try:
            self.grades.remove(float(value))
            self._update_status()
            return True
        except ValueError:
            return False

    def remove_grade_by_index(self, index: int) -> bool:

        """Remove a grade at the specified index."""

        if index < 0 or index >= len(self.grades):
            return False
        del self.grades[index]
        self._update_status()
        return True

    def report(self) -> str:

        """Generate a formatted report of the student's information and grades."""

        return (
            f"\n===== Student Report =====\n"
            f"ID:            {self.student_id}\n"
            f"Name:          {self.name}\n"
            f"Grades count:  {len(self.grades)}\n"
            f"Grades:        {self.grades}\n"
            f"Average:       {self.calculate_average():.2f}\n"
            f"Letter grade:  {self.get_letter_grade()}\n"
            f"Status:        {self.is_passed}\n"
            f"Honor Roll:    {'Yes' if self.honor_roll else 'No'}\n"
            f"==========================\n"
        )



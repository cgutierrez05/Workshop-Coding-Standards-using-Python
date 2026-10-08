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


from __future__ import annotations

class IDError(Exception):
    pass

class GradeError(ValueError):
    pass


class Student:
    '''
    Code for the student class goes here:
    Student has:
    student_id
    name
    subject_name
    dict[subject name: grade]
    '''

    def __init__(self, student_id: str, name: str, subject_name: str, grade: dict[str, int | float]):
        self._student_id = student_id
        self._name = name
        self._subject_name = subject_name
        self.__grade = grade

    @staticmethod
    def validate_id(student_id) -> str:
        if not student_id:
            raise ValueError('Student ID is required')

        if student_id[:3].upper() != "D00":
            raise IDError("Student ID must start with D00")

        return student_id.upper()

    @staticmethod
    def validate_grade(grade) -> int | float:
        if grade is None:
            raise GradeError("Grade is required")

        if grade <= 0 or grade > 100:
            raise GradeError("Grade must be between 0 and 100")

        return grade

    def add_grade(self, subject_name: str, grade: int | float) -> bool:
        valid = Student.validate_grade(grade)
        subject = subject_name.strip()
        if subject in self.__grade:
            return False
        self.__grade[subject] = valid
        return True


    def __eq__(self, other) -> bool:
        if not isinstance(other, Student):
            return NotImplemented
        return self._student_id == other._student_id

    def __ne__(self, other) -> bool:
        if not isinstance(other, Student):
            return NotImplemented
        return self._student_id != other._student_id

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}{{_student_id={self._student_id}, name={self._name}, subject_name={self._subject_name}, _grade={self.__grade}}}"













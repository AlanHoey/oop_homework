class Student:
    '''
    Code for the student class goes here:
    Student has:
    student_id
    name
    subject_name
    dict[subject name: grade]
    '''

    def __init__(self, student_id: str, name: str, subject_name: str, grade: dict[str, int]):
        self._student_id = student_id
        self._name = name
        self._subject_name = subject_name
        self.__grade = grade

    def validate_id(self, student_id) -> str:
        if not student_id:
            raise ValueError('Student ID is required')

        if student_id[:3].upper() != "D00":
            raise ValueError("Student ID must start with D00")

        return student_id.upper()

    def validate_grade(self, grade) -> int:
        if grade == "":
            raise ValueError("Grade is required")

        if grade <= 0 or grade > 100:
            raise ValueError("Grade must be between 0 and 100")

        return grade









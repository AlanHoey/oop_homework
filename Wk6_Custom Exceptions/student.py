class Student:
    '''
    Code for the student class goes here:
    Student has:
    student_id
    name
    dict[subject name: grade]
    '''

    def __init__(self, student_id: str, name: str, grades: dict[str, float]):
        self._student_id = student_id
        self._name = name
        self._grades = grades

    def validate_id(self, student_id):
        if not student_id:
            raise ValueError('Student ID is required')

        if student_id[:3].upper() != "D00":
            raise ValueError("Student ID must start with D00")



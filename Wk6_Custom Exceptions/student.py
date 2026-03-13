class Student:
    '''
    Code for the student class goes here:
    Student has:
    student_id
    name
    dict[subject name: grade]
    '''

    def __init__(self, student_id: str, name: str, grades: dict[str, float]):
        self.student_id = student_id
        self.name = name
        self.grades = grades
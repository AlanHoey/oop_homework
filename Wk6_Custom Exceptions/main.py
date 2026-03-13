from student import Student, IDError, GradeError

grades_file = "grades.txt"

def read_grades(grades_file: str) -> dict[str, Student]:
    students: dict[str, Student] = {}

    try:
        with open(grades_file, "r") as grades_file:
            for line in grades_file:
                line = line.strip()
                components = line.split(",")
                student_id = components[0]
                name = components[1]
                grades_str = components[2].split(",")
                grades: dict[str, float] = {}
from classes.student import Student
from classes.staff import Staff

class School:
    def __init__(self, name) -> None:
        self.name = name
        self.staff = Student.all_students()
        self.students = Staff.all_staff()
        
from classes.student import Student
from classes.staff import Staff

class School:
    def __init__(self, name) -> None:
        self.name = name
        self.staff = Staff.all_staff()
        self.students = Student.all_students()
    
    def list_students(self):
        student_count = 1
        for student in self.students:
            print(f"{student_count}. {student.name} {student.school_id}")
            student_count += 1
            
    def find_student_by_id(self, student_id):
        for student in self.students:
            if student.school_id == student_id:
                print(student)
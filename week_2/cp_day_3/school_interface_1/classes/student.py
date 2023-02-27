from classes.person import Person
import csv

class Student(Person):
    def __init__(self, name, age, role, school_id, password) -> None:
        super().__init__(name, age, role, school_id, password) 

    def __str__(self) -> str:
        return f"\n{self.name}\n-------------\nage:{self.age}\nid: {self.school_id}"
    
    @classmethod
    def all_students(cls):
        array_students = []
        with open('/Users/joshparina/repos/cp_assignments/week_2/cp_day_3/school_interface_1/data/students.csv', mode='r') as student_file:
            student_data = csv.DictReader(student_file)
            for row in student_data:
                array_students.append(cls(**dict(row)))
        return array_students
            

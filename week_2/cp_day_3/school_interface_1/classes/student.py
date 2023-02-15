from classes.person import Person
import csv

class Student(Person):
    def __init__(self, name, age, role, school_id, password) -> None:
        super().__init__(name, age, role, school_id, password) 

    def all_students():
        array_students = []
        with open('/Users/joshparina/repos/cp_assignments/week_2/cp_day_3/school_interface_1/data/students.csv', mode='r') as student_file:
            student_data = csv.DictReader(student_file)
            for row in student_data:
                array_students.append(row)
        return array_students
            

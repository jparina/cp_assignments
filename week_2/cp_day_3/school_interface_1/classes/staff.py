from classes.person import Person
import csv

class Staff(Person):
    def __init__(self, name, age, role, school_id, password) -> None:
        super().__init__(name, age, role, school_id, password)
    
    def all_staff():
        array_staff = []
        array_staff = []
        with open('/Users/joshparina/repos/cp_assignments/week_2/cp_day_3/school_interface_1/data/staff.csv', mode='r') as staff_file:
            staff_data = csv.DictReader(staff_file)
            for row in staff_data:
                array_staff.append(row)
        return array_staff
    
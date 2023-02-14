import csv

def needs_a_home(animal=None):
    animal = input("Please choose a type of animal: ").lower()
    try:
        with open(f'/Users/joshparina/repos/cp_assignments/week_2/csv_reader/data/{animal}.csv', mode = 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            print('These animals need a home!')
            for row in csv_reader:
                print(f'{row["name"].capitalize()} is a {row["age"]} year old {row["breed"]}')
    except:
        print(f"We dont have any {animal} here")
    
needs_a_home()
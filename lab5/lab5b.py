#!/usr/bin/python3

from bus import Bus

def main():
    while True:
        try:
            students = int(input("Enter the number of students: "))
            age = int(input("Enter the age of the students: "))
            break
        except ValueError:
            print("Invalid input. Please enter integers for both the number of students and the age.")

    # Create a Bus object with user input
    my_bus = Bus(students, age)

    # Modify the number of students
    new_students = int(input("Enter the new number of students: "))
    my_bus.set_students(new_students)

    # Modify the age of students
    new_age = int(input("Enter the new age of students: "))
    my_bus.set_age(new_age)
    
if __name__ == "__main__":
    main()


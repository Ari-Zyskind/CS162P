#!/usr/bin/python3

from mymath import MyMath

def main():
    my_math = MyMath()

    # Prompt the user to enter a number for the absolute value calculation
    while True:
        try:
            number = float(input("Enter a number to find its absolute value: "))
            print(f"Absolute value of {number}: {my_math.absolute(number)}")
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    # Prompt the user to enter a list of numbers for the average calculation
    while True:
        numbers_input = input("Enter a list of numbers separated by spaces to find their average: ")
        try:
            numbers = [float(n) for n in numbers_input.split()]
            if not numbers:
                raise ValueError("No numbers entered.")
            print(f"Average of {numbers}: {my_math.average(numbers)}")
            break
        except ValueError:
            print("Invalid input. Please enter valid numbers separated by spaces.")

if __name__ == "__main__":
    main()


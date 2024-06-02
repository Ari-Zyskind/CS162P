#!/usr/bin/python3

from reversemath import ReverseFloat

def get_single_digit_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if 0 <= value <= 9:
                return value
            else:
                print("Please enter a single-digit integer (0-9).")
        except ValueError:
            print("Invalid input. Please enter a single-digit integer (0-9).")

def main():
    # Getting single-digit integer inputs from the user
    num1 = get_single_digit_integer("Enter the first single-digit integer: ")
    num2 = get_single_digit_integer("Enter the second single-digit integer: ")

    # Converting integers to floats
    float1 = float(num1)
    float2 = float(num2)

    # Creating ReverseFloat instances
    rf1 = ReverseFloat(float1)
    rf2 = ReverseFloat(float2)

    # Performing and displaying operations
    print(f"rf1: {rf1}")
    print(f"rf2: {rf2}")

    print(f"rf1 + rf2: {rf1 + rf2}")
    print(f"rf1 - rf2: {rf1 - rf2}")
    print(f"rf1 * rf2: {rf1 * rf2}")
    print(f"rf1 / rf2: {rf1 / rf2}")

if __name__ == "__main__":
    main()


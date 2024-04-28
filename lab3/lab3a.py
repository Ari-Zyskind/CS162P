#!/usr/bin/python3

import sys

def factorial1(num):
    total = 1
    for i in range(1, num + 1):
        total = total * i
    return total

def factorial2(num):
    if num == 0:
        return 1
    else:
        return num * factorial2(num - 1)

def determine_method():
    response = False
    while not response:
        in_method = input("What method would you like to use to calculate the factorial?\n"
                    "Type '1' for 'iterative\n"
                    "Type '2' for 'recursive'\n")
        if in_method == '1':
            print("You chose iterative!")
            response = True  # Exit the loop
        elif in_method == '2':
            print("You chose recursive!")
            response = True  # Exit the loop
        else:
            print("\nHmmm. That's not a choice. Try again\n\n")

def determine_number():
    response = False
    while not response:
        in_num = input("Type the integer greater than or equal to 0 and less than 1000 you would like to calculate the factorial for: ")
        if in_num.isdigit() and 0 <= int(in_num) < 1000:
            print(f"Awesome! You chose {in_num}!")
            response = True
            return int(in_num)  # Return the valid input
        else:
            print("Hmmm. It seems like that's not a valid integer.\nLet's try again.\n\n")

def main():
    # Determine the method input type
    in_method = determine_method()
    
    # Determine the integer input
    in_num = determine_number()
    
    # Calculate the factorial from the method and integer inputs
    if in_method == '1':
        out_num = factorial1(in_num)
    else:
        out_num = factorial2(in_num)
    
    # Display results
    print("\n%d! = %d\n" % (in_num, out_num))

if __name__ == "__main__":
    main()

#!/usr/bin/python3

import sys


def receive_input():
    # Receive a string input
    try:
        user_input = input("Enter a single argument consisting of a string of characters: ")
        return user_input
    except:
        print("An error occurred. Please make sure you entered a valid input.")


def convert_list(user_string):
    # Initiate a list
    char_list = []

    # for loop to add each character to a list
    for char in user_string:
        char_list.append(char)
    return char_list


def palindrome(lst):
    # Base case: if there are 1 or 0 characters left, it's a palindrome
    if len(lst) <= 1:
        return True
    # Check if the first and last characters are the same. If they are, call the function through recursion to check if we are in the Base case.
    elif lst[0] == lst[-1]:
        # Remove the first and last characters and recursively check the remaining sublist
        lst.pop(0)
        lst.pop(-1)
        return palindrome(lst)
    else:
        return False



def main():
    # Call the function to receive a string input
    user_input = receive_input()

    # Call the function to convert the string into a list
    char_list = convert_list(user_input)

    # Call the function to determine if the string is a Palindrome and to display the results
    palindrome_check = palindrome(char_list)

    if palindrome_check == True:
        print("Palindrome")
    else:
        print("Not Palindrome")

if __name__ == "__main__":
    main()

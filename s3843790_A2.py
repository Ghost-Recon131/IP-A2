# COSC1519 Introduction to Programming
# A2 Programming Project
# Student name: Jingxuan Feng
# Student number: s3843790

# Import modules
import math
import random


# This section is for Utility/ helper functions

# This function attempts to get integer input from user
def get_user_input_int():
    userin = None
    try:
        userin = int(input("Please enter an integer: "))
    except:
        print("")
    return userin


# This function attempts to get a String from the user
def get_user_input_string():
    return input("Please enter a string: ")


# This function helps to validate user input, takes the entered input & an array of allowed values to compare against
def validate_userinput(input, allowed_values_array):
    is_valid = False

    # Only checks against array once verified input is not None to save time
    if(input is not None):
        for value in allowed_values_array:
            if value == input:
                is_valid = True

    return is_valid


# Functions for scenes

# Prints the main menu / welcome text
def show_main_menu():
    print(
        "--------------------------------------------------------------- \n"
        "Welcome to GAME NAME, the text based game! \n"
        "--------------------------------------------------------------- \n"
    )


# TODO: Function for scene 1
def scene1():
    return None


# TODO: Function for scene 2
def scene2():
    return None


# TODO: Function for scene 3
def scene3():
    return None


# TODO: Function for scene 4
def scene4():
    return None


# TODO: Function for scene 5
def scene5():
    return None


# TODO: Function for scene 6
def scene6():
    return None


# Functions for


# Main Program
def main():
    show_main_menu()
    scene1()
    scene2()
    scene3()
    scene4()
    scene5()
    scene6()


# Start program
main()
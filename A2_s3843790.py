# COSC1519 Introduction to Programming
# A2 Programming Project
# Student name: Jingxuan Feng
# Student number: s3843790

# Private GitHub repo (email for access): https://github.com/Ghost-Recon131/IP-A2

# References in IEEE
"""
1.
2.
3.
"""


# Import modules
import math
import random

# These are global variables used in multiple scenes
user_char_name = None
user_char_height = None
user_char_weapon = "Chunchunmaru"


# This section is for Utility/ helper functions
# This function attempts to get integer input from user
def get_user_input_int():
    userin = None
    try:
        userin = int(input("Please enter your choice as an integer: "))
    except:
        print("You did not enter a valid integer! ")
    return userin


# This function attempts to get float input from user
def get_user_input_float(prompt):
    userin = None
    try:
        userin = float(input(prompt))
    except:
        print("You did not enter a valid float! ")
    return userin


# This function attempts to get a String from the user
def get_user_input_string(prompt):
    return input(prompt)


# This function helps to validate user input, takes the entered input & an array of allowed values to compare against
def validate_userinput(input, allowed_values_array):
    is_valid = False

    # Only checks against array once verified input is not None to save time
    if (input is not None):
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
    # List of alternative weapons user can choose
    alternative_weapons = ["Katana", "Long Sword", "Dagger"]

    # Get user to create name of their character
    name_entered = False
    while not name_entered:
        new_name = get_user_input_string("Please enter your character's name: ")
        global user_char_name
        if (new_name != None):
            user_char_name = new_name
            name_entered = True
        else:
            print("You did not enter a value")

    # Get user to enter height of their character
    height_entered = False
    while not height_entered:
        new_height = get_user_input_float("Please enter your character's height (can be int or float): ")
        global user_char_height
        if (new_height != None):
            user_char_height = new_height
            height_entered = True
        else:
            print("You did not enter a value")

    # Get user to choose a weapon
    global user_char_weapon
    print("Please enter the weapon you want to carry. Weapons: ")
    for weapon in alternative_weapons:
        print(weapon)

    choose_weapon = get_user_input_string("By default Chunchunmaru will be chosen if you do not enter a valid choice: ")
    valid_weapon_name = validate_userinput(choose_weapon, alternative_weapons)

    if(valid_weapon_name):
        user_char_weapon = choose_weapon
    # END OF scene1 FUNCTION


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

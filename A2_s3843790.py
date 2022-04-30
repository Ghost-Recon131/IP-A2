# COSC1519 Introduction to Programming
# A2 Programming Project
# Student name: Jingxuan Feng
# Student number: s3843790

# Private GitHub repo (email for access): https://github.com/Ghost-Recon131/IP-A2


"""
References in IEEE

About story: This storyline uses characters and terminology from anime show "Kono Subarashii Sekai ni Shukufuku wo!".
The storyline itself is original and based off the original anime.

1. Kono Subarashii Sekai ni Shukufuku wo! Wiki (no date). Available at: https://konosuba.fandom.com/wiki/Kono_Subarashii_Sekai_ni_Shukufuku_wo!_Wiki (Accessed: 1 May 2022).
2. Random Name Generator &mdash; Easy Random Name Picker (no date) Random Word Generator. Available at: https://randomwordgenerator.com/name.php (Accessed: 1 May 2022).
"""

# Import modules
import math
import random

# These are global variables used in multiple scenes, has pre-defined values if the user does not overwrite them
user_char_name = "Filarion Zylyarus"
user_char_height = 175
user_char_weapon = "Chunchunmaru"
daily_explosion_spell = True
quest_award = 2000000


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


# This function checks if the user's choice selection is valid
def validate_userinput_int(input, maxoption):
    is_valid = False

    if (input > 0 and input <= maxoption):
        is_valid = True

    return is_valid


# This function is used to end the game
def end_game(message):
    print(message)
    quit(0)


# Functions for scenes

# Prints the main menu / welcome text
def show_main_menu():
    print(
        "--------------------------------------------------------------- \n"
        "Welcome to KonoSuba side-story, the text based spinoff game! \n"
        "--------------------------------------------------------------- \n"
    )


# Function for scene 1, ask user to enter their character's name, height and pick a weapon
def scene1():
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
    # List of alternative weapons user can choose
    alternative_weapons = ["KATANA", "LONG SWORD", "DAGGER"]

    global user_char_weapon
    print("Please enter the weapon you want to carry (not case sensitive). Weapons: ")
    for weapon in alternative_weapons:
        print(weapon)

    choose_weapon = get_user_input_string(
        "By default Chunchunmaru will be chosen if you do not enter a valid choice: ").upper()
    valid_weapon_name = validate_userinput(choose_weapon, alternative_weapons)

    if (valid_weapon_name):
        user_char_weapon = choose_weapon
    print("Your chosen weapon is : " + choose_weapon + "\n \n")
    # END OF scene1 FUNCTION


# Function for scene 2 - Work scene, user needs to select option 3 to progress the story
def scene2():
    global user_char_name
    print(
        "Hi " + user_char_name + " , it is almost the end of the day and a customer wants to negotiate price for a potion. \n"
                                 "You need to sell this as it is part of your task to help clear the store inventory. \n")

    prompt = "What action will you take? \n" \
             "1. Attempt to not lower the price \n" \
             "2. Offer a free item along with the purchase \n" \
             "3. Offer a 15% discount"
    next_scene = False

    # Continuously prompt for input until user selects option 3
    while not next_scene:
        print(prompt)

        user_choice = get_user_input_int()
        if (validate_userinput_int(user_choice, 3)):  # is the number of options offered to user
            if (user_choice == 1):
                print("The buyer is not budging, perhaps offer something... \n")
            elif (user_choice == 2):
                print("The buyer is not interested in other items, perhaps offer a small discount... \n")
            elif (user_choice == 3):
                print("The buyer accepts your offer, after they paid for the potion, you close up shop and go home. \n")
                next_scene = True
        else:
            print("You did not enter a valid option! \n")

    # END OF scene2 FUNCTION


# Function for scene 3 - Gives user a quest and will continue the story if they accept
def scene3():
    print("""
    As you go home, Luna, the Adventurer Guild receptionist offers you a quest - \n 
    Luna: "One of the demon lord's generals have deployed a small recon force near Axel..." 
    Luna: "They will scout out the city and judge its defences then prepare for an invasion..." 
    Luna: "Take them out before the scout group can report back!" 
    Luna: "You will be working with Kazuma's party in this quest." 
    Luna: "This quest reward is 2 mithril coin (2000000 eris)" 
    """)

    prompt = "Will you accept the quest and defend the city? \n" \
             "1. Accept the quest \n" \
             "2. Accept but on condition of being paid 3 mithril coin  \n" \
             "3. Decline the quest \n" \
             "4. No reply"
    next_scene = False
    accept_message = "You go home and ready your gear, then you meet up with Kazuma's party to begin your quest"

    # Continuously prompt for input until user selects option 3
    while not next_scene:
        print(prompt)

        user_choice = get_user_input_int()
        if (validate_userinput_int(user_choice, 4)):  # is the number of options offered to user
            if (user_choice == 1):
                print(accept_message + "\n")
                next_scene = True
            elif (user_choice == 2):
                global quest_award
                quest_award = 3000000
                print("Luna accepts your request. " + accept_message + "\n")
                next_scene = True
            elif (user_choice == 3):
                early_end_message = "You declined the quest, believing it to be too risky, and decided to travel to Arcanletia instead."
                end_game(early_end_message)
            elif (user_choice == 4):
                print("""Luna: "Have you made up your mind? " \n""")
        else:
            print("You did not enter a valid option! \n")


# END OF scene3 FUNCTION


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

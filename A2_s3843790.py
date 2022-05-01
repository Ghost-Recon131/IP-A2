# COSC1519 Introduction to Programming
# A2 Programming Project
# Student name: Jingxuan Feng
# Student number: s3843790

# Private GitHub repo (email for access): https://github.com/Ghost-Recon131/IP-A2


"""
References in IEEE

About story: This storyline uses characters and terminology from anime show "Kono Subarashii Sekai ni Shukufuku wo!".
The storyline itself is original and based off the original anime.

[1]‘Kono Subarashii Sekai ni Shukufuku wo! Wiki’. https://konosuba.fandom.com/wiki/Kono_Subarashii_Sekai_ni_Shukufuku_wo!_Wiki (accessed May 01, 2022).
[2]‘Online Ascii Art Creator’. https://www.ascii-art-generator.org/ (accessed May 01, 2022).
[3]‘Random Name Generator &mdash; Easy Random Name Picker’, Random Word Generator. https://randomwordgenerator.com/name.php (accessed May 01, 2022).
[4] Aceblade10, ‘All Megumin’s anime translated explosion quotes.’, r/Konosuba, Mar. 17, 2017. www.reddit.com/r/Konosuba/comments/5zz3gw/all_megumins_anime_translated_explosion_quotes/ (accessed May 01, 2022).
"""

# Import modules
import random

# These are global variables used in multiple scenes, has pre-defined values if the user does not overwrite them
user_char_name = "Filarion Zylyarus"
user_char_height = 175
user_char_weapon = "CHUNCHUNMARU"
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

    if (input is not None):
        if (input > 0 and input <= maxoption):
            is_valid = True

    return is_valid


# This function is used to end the game
def end_game(message):
    print(message)
    quit(0)


# Functions for scenes

# Prints the main menu - ascii art generated using [3]
def show_main_menu():
    ascii_art = "    __ __      _   __     _____       ____                  _____ ________  ______   _______________  ______  __\n" \
                "   / //_/___  / | / /___ / ___/__  __/ __ )____ _   _      / ___//  _/ __ \/ ____/  / ___/_  __/ __ \/ __ \ \/ /\n" \
                "  / ,< / __ \/  |/ / __ \\__ \ / / / / __  / __ `/  (_)     \__ \ / // / / / __/     \__ \ / / / / / / /_/ /\  / \n" \
                " / /| / /_/ / /|  / /_/ /__/ / /_/ / /_/ / /_/ /  _       ___/ // // /_/ / /___    ___/ // / / /_/ / _, _/ / /  \n" \
                "/_/ |_\____/_/ |_/\____/____/\__,_/_____/\__,_/  (_)     /____/___/_____/_____/   /____//_/  \____/_/ |_| /_/   \n"

    print(ascii_art + "\n")


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
    alternative_weapons = ["KATANA", "LONG SWORD", "RAPIER"]

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
    # Introduces current scene and scenario to user
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
    # Introduces current scene and scenario to user
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

    # Continuously prompt for input until user selects option 1 or 2
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


# Utility functions for scene 4 and 5
# Randomly generate user's damage depending on their weapon
def user_attack_damage(user_weapon):
    damage = None

    if (user_weapon == "CHUNCHUNMARU"):
        damage = random.randint(2, 4)
    elif (user_weapon == "KATANA"):
        damage = random.randint(4, 6)
    elif (user_weapon == "LONG SWORD"):
        damage = random.randint(6, 10)
    else:  # only other possible value is RAPIER, thus don't have to use another else if
        damage = random.randint(4, 8)

    return damage


def longbow_attack_damage():
    longbow_damage = None
    random_values = random.sample(range(1, 10), 3)
    miss = validate_userinput(random.randint(1, 10), random_values)

    if (miss):
        longbow_damage = 0
    else:
        longbow_damage = random.randint(8, 15)

    return longbow_damage


# Uses random to see if user can land critical hit
# validate_userinput function can actually be reused here as it checks if a parameter is inside the supplied array
def critical_damage(blessing):
    critical_hit = False

    # Guaranteed critical hit with Aqua's blessing cast
    if (blessing):
        critical_hit = True
    else:
        # chance of critical hit (chance of number being inside loop)
        random_values = random.sample(range(1, 10), 4)
        critical_hit = validate_userinput(random.randint(1, 10), random_values)

    return critical_hit


# Function for scene 4 - Continuously fight enemy guard until his hp <= 0
def scene4():
    # Introduces current scene and scenario to user
    print("You get close to the camp of the recon force, and you notice a single guard guarding the only entry path. \n"
          "You're currently ahead of the party and will need to deal with the guard yourself. \n"
          "Aqua and Megumin have not yet caught up so their abilities will not be available here. \n")

    global user_char_weapon
    prompt_1 = "How will you proceed? \n" \
               "1. Try sneak around the guard \n" \
               "2. Prepare to attack"

    attack = False
    # Continuously prompt for input until user selects option 2
    while not attack:
        print(prompt_1)

        user_choice = get_user_input_int()
        if (validate_userinput_int(user_choice, 2)):  # is the number of options offered to user
            if (user_choice == 1):
                print("The guard does not give you an opening. It appears you will have to take him out... \n")
            elif (user_choice == 2):
                attack = True
                print("You step out of hiding, the guard draws his weapon and prepares to attack you \n")
        else:
            print("You did not enter a valid option! \n")

    # Continuously prompt until the user kills the guard
    enemy_hp = 25
    prompt_2 = "1. Attack with your weapon: " + user_char_weapon + " \n" \
                "2. Tell Kazuma longbow attack; has chance of missing \n" \
                "3. Tell Darkness to attack \n"

    while enemy_hp > 0:

        print("The guard has " + str(enemy_hp) + " hp remaining." + "\n" + prompt_2)
        user_choice = get_user_input_int()
        if (validate_userinput_int(user_choice, 3)):  # is the number of options offered to user
            if (user_choice == 1):
                damage = user_attack_damage(user_char_weapon)
                critical_hit = critical_damage(False)  # False since Aqua cannot cast Blessing in this scene

                # Deal 2x damage in critical hit or with damage buff
                if (critical_hit):
                    print("You've landed a critical hit!!!")
                    damage = damage * 2

                enemy_hp = enemy_hp - damage
                print("Your attack deals " + str(damage) + " damage")

            elif (user_choice == 2):
                damage = longbow_attack_damage()
                enemy_hp = enemy_hp - damage
                result = ""
                if (damage == 0):
                    result = "Kazuma has missed! Dealing 0 damage"
                else:
                    result = "Kazuma dealt " + str(damage) + " damage"
                print(result)

            elif (user_choice == 3):
                print("Darkness missed and deals 0 damage!")
        else:
            print("You did not enter a valid option! \n")
    # END OF scene4 FUNCTION


# Utility function for scene 5 - adds more immersion to story
# doesn't do much other than print one the few different ways Megumin casts her explosion spell, referenced [4]
def megumin_explosion_chant():
    chant1 = "Megumin: \"Darkness blacker than black and darker than dark, I beseech thee, combine with my deep crimson.\" \n" \
             "Megumin: \"The time of awakening cometh. Justice, fallen upon the infallible boundary, appear now as an intangible distortion!\" \n" \
             "Megumin: \"Dance, Dance, Dance! I desire for my torrent of power a destructive force: a destructive force without equal!\" \n" \
             "Megumin: \"Return all creation to cinders, and come from the abyss!\" \n" \
             "Megumin: \"EXPLOSION!!!\" \n"

    chant2 = "Megumin: \"By my efflux of deep crimson, topple this white world!\" \n" \
             "Megumin: \"EXPLOSION!!!\" \n"

    chant3 = "Megumin: \"Detonation... Detonation... Detonation... \" \n" \
             "Megumin: \"Wielder of the most glorious, powerful, and grand explosion magic, My name is Megumin\" \n" \
             "Megumin: \"The blow that I am given to strike turns a blind eye to the fate of my kindred, rendering all hope of rebirth and anguish, and the model by which all forces are judged!\" \n" \
             "Megumin: \"Pitiful creature... Synchronize yourself with the red smoke, and atone in a surge of blood!\" \n" \
             "Megumin: \"EXPLOSION!!!\" \n"

    chant4 = "Megumin: \"The tower of rebellion creeps upon man's world, \" \n" \
             "Megumin: \"The unspoken faith displayed before me, The time has come!\" \n" \
             "Megumin: \"Now, awaken from your slumber, and by my madness, be wrought!\" \n" \
             "Megumin: \"EXPLOSION!!!\" \n"

    list_of_chants = [chant1, chant2, chant3, chant4]
    return random.choice(list_of_chants)


# Function for scene 5 - Prompts user to fight multiple enemies
def scene5():
    global daily_explosion_spell
    global user_char_weapon

    # Introduces current scene and scenario to user
    print("\nYou've successfully taken out the guard and move on with the rest of the part... \n"
          "Your earlier attacks have caused quite a commotion, the scouts inside the camp is ready to face you! \n")

    prompt = "1. Attack with your weapon: " + user_char_weapon + " \n" \
             "2. Ask Aqua to cast \"Damage Buff\", increased damage in next attack \n" \
             "3. Have Aqua cast \"Blessing\", increase chance for critical hit \n" \
             "4. Tell Kazuma longbow attack; has chance of missing \n" \
             "5. Ask Megumin to cast explosion (Warning: can only be used once per day!) \n" \
             "6. Tell Darkness to attack \n"

    # Variables used for battling multiple enemies
    number_of_enemies = random.randint(3, 5)  # user could face anywhere from 3-5 enemies
    number_of_enemies_defeated = 0 # Keeps track on number of enemies killed
    damage_buff = False
    blessing = False

    # continue loop as long as user has not killed all enemies
    while (number_of_enemies_defeated != number_of_enemies):
        enemy_hp = random.randint(15, 30) # this time enemy hp varies
        enemy_remaining = number_of_enemies - number_of_enemies_defeated
        print("There are " + str(enemy_remaining) + " enemies left... \n")

        while enemy_hp > 0:
            print("The guard has " + str(enemy_hp) + " hp remaining." + "\n" + prompt)
            user_choice = get_user_input_int()
            if (validate_userinput_int(user_choice, 6)):  # is the number of options offered to user
                if (user_choice == 1):
                    damage = user_attack_damage(user_char_weapon)
                    critical_hit = critical_damage(blessing)  # Deal 2x damage in critical hit or with damage buff

                    # Small preventive step to stop meta gaming, critical hit and damage buff together will give 3x instead of 4x damage
                    if (critical_hit and damage_buff):
                        damage = damage * 3
                        print("You've landed a critical hit with damage buff!!!")
                    else:
                        if (critical_hit or damage_buff):
                            damage = damage * 2
                            print("You've dealt extra damage!")

                    enemy_hp = enemy_hp - damage
                    print("Your attack deals " + str(damage) + " damage")

                    # Reset buffs, only last 1 turn
                    damage_buff = False
                    blessing = False

                elif (user_choice == 2):
                    damage_buff = True
                    print("Aqua: \"Damage Buff!\" \n")

                elif (user_choice == 3):
                    blessing = True
                    print("Aqua: \"Blessing!\" \n")

                elif (user_choice == 4):
                    damage = longbow_attack_damage()
                    enemy_hp = enemy_hp - damage
                    result = ""
                    if (damage == 0):
                        result = "Kazuma has missed! Dealing 0 damage"
                    else:
                        result = "Kazuma dealt " + str(damage) + " damage"
                    print(result)

                elif (user_choice == 5):
                    if(daily_explosion_spell):
                        daily_explosion_spell = False
                        enemy_hp = 0
                        chant = megumin_explosion_chant()
                        print(chant)
                    else:
                        print("Megumin has already casted her explosion spell today and exhausted her mana... \n")

                elif (user_choice == 6):
                    print("Darkness missed and deals 0 damage! \n")

            else:
                print("You did not enter a valid option! \n")
        number_of_enemies_defeated = number_of_enemies_defeated + 1
    # END OF scene5 FUNCTION


# Function for scene 6 - 4 alternate endings depending on user's choice
def scene6():
    global daily_explosion_spell
    global user_char_weapon
    global quest_award

    # Introduces current scene and scenario to user
    print("\nYour party took out the remaining scouts, however their squad leader returns...\n"
          "Will you fight him or will you sneak away? \n")

    prompt = "1. Attack with your weapon: " + user_char_weapon + " \n" \
             "2. Sneak away and retreat back to Axel  \n" \
             "3. Ask Megumin to cast explosion \n" \
             "4. All out attack with your party \n"

    finish_game = False
    end_game_plot = None
    # Continuously prompt for valid input, has different endings depending on action chosen
    while not finish_game:
        print(prompt)
        user_choice = get_user_input_int()
        if (validate_userinput_int(user_choice, 4)):  # is the number of options offered to user
            if (user_choice == 1):
                actual_award = quest_award / 2
                end_game_plot = "You were quickly defeated by the squad leader. \n" \
                                "Aqua revives you and you travel back to Axel along with your party. \n" \
                                "You all make it back to Axel to celebrate your victory. \n" \
                                "You've stopped an invasion of Axel but didn't fully complete the quest. \n" \
                                "\nYou've earned " + str(actual_award) + " eris as the quest award instead."
                finish_game = True

            elif (user_choice == 2):
                actual_award = quest_award / 2
                end_game_plot = "Your party makes a quite getaway. \n" \
                                "You all make it back to Axel to celebrate your victory. \n" \
                                "You've stopped an invasion of Axel but didn't fully complete the quest. \n" \
                                "\nYou've earned " + str(actual_award) + " eris as the quest award instead."
                finish_game = True

            elif (user_choice == 3):
                if(daily_explosion_spell):
                    daily_explosion_spell = False
                chant = megumin_explosion_chant()
                print(chant)

                end_game_plot = "You've taken out the squad leader, successfully completing the quest. \n" \
                                "Back at Axel, you and your other party members gain a lot of attention, \n" \
                                "but the Demon Load have also taken an interest in this situation... \n" \
                                "\nYou've earned " + str(quest_award) + " eris as the quest award."
                finish_game = True

            elif (user_choice == 4):
                end_game_plot = "Your attacks were ineffective, the squad leader specialises in close quarters fighting and takes out your whole party...\n" \
                                "While your quest managed to stop an attack on Axel, your party did not get to tell the tale. \n"
                finish_game = True
        else:
            print("You did not enter a valid option! \n")
    print(end_game_plot + "\n" + "Thank you for playing KoNoSuBa: Side Story!")
    # END OF scene6 FUNCTION


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

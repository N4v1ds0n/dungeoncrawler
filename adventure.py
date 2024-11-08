def treasure_island_intro():
    print('''
    *******************************************************************************
              |                   |                  |                     |
     _________|________________.=""_;=.______________|_____________________|_______
    |                   |  ,-"_,=""     `"=.|                  |
    |___________________|__"=._o`"-._        `"=.______________|___________________
              |                `"=._o`"=._      _`"=._                     |
     _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
    |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
    |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
              |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
     _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
    |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
    |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
    ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
    /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
    ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
    /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
    ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
    /______/______/______/______/______/______/______/______/______/______/_____ /
    *******************************************************************************
    ''')
    print("Welcome to Treasure Island.")
    print("Your mission is to find the treasure.")
    first_choice()

def first_choice():
    choice1 = input("You're at a cross road.\nWhere do you want to go? Type \"left\" or \"right\"!\n")
    if choice1.lower() == 'right':
        print('You wander into a forest where you get lost and starve.\nGame over!')
        del choice1
        retry_prompt()
    elif choice1.lower() == 'left':
        print()
        second_choice()
    else:
         first_choice()
        
def second_choice():
    choice2 = input("You come to a lake. There is an island in the middle of the lake.\nType \"wait\" to wait for a boat, type \"swim\" to swim across.\n")
    if choice2.lower() == 'swim':
        print('You drown. Game over!')
        del choice2
        retry_prompt()
    elif choice2.lower() == 'wait':
        print("\nAfter some time a boat arrives out of the fog. A scrawny figure standing inside.\n\"Hello young adventurer, looking for a way across?\"\nYou climb aboard and soon arrive at the island unharmed")
        third_choice()
    else:
        print()
        second_choice()

def third_choice():
    choice3 = input("There is a house on the island, do you enter? Y/N\n" )
    if choice3.upper() == 'Y':
        print("\nYou enter a room with three doors. One red, one yellow and one blue.")
        del choice3
        fourth_choice()
    elif choice3.upper() == 'N':
        del choice3
        print("\nYou ponder on life and wait a while.\nAfter some time you realize:")
        third_choice()
    else:
        print()
        third_choice()

def fourth_choice():
    choice4 = input("Which colour do you choose?\n")
    if choice4.lower() == 'red':
        print('\nYou are sucked into the door and loose the feeling of space and time.\nAs you come to your senses you find yourself on an island.')
        del choice4
        third_choice()
    elif choice4.lower() == 'yellow':
        print('\nYou enter a room with a chest in the center. A sign at the wall reads:\"Do not open chest\"')
        del choice4
        fifth_choice()
    elif choice4.lower() == 'blue':
        print('\nYou enter a room full of beasts.\nGame over!')
        del choice4
        retry_prompt()
    else:
        fourth_choice()

def fifth_choice():
    choice5 = input('Do you open the chest? Y/N\n')
    if choice5.upper() == 'Y':
        print('\nA tentacle emerges from the chest and pulls you inside. You die.\nGame over.')
        del choice5
        retry_prompt()
    else:
        print('\nYou stare at the chest for a while not sure whether you should open it.\nSuddenly an old man with a long beard enters the room.\nHe takes a long look at you and says:\"Congratulations! You passed the test. Take your reward.\"\nHe conjures a bowl full of diamonds and gives it to you before he vanishes into thin air.\nWell done, you finished \"Treasure Island\"')
        del choice5
        retry_prompt()

def retry_prompt():
    retry = input('Do you want to try again? Y/N\n')
    if retry.upper() == 'N':
        quit()
    else:
        del retry
        treasure_island_intro()

treasure_island_intro()

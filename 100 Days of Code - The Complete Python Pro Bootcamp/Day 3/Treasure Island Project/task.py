print(r'''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
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
# direction=input("You're at a cross road. Where do you want to go? \nType left or right ")
# if direction=="right":
#     print("Fall into a hole...GAME OVER")
# else:
#     swim_wait=input("You've come to a lake. \nThere is an island in the middle of the lake.\nType wait to wait for a boat. Type swim to swim across.")
#     if swim_wait=="swim":
#         print("Attacked by trout...GAME OVER")
#     if swim_wait=="wait":
#         wait=input("You arrive at the island unharmed.\n There is a house with 3 doors.One red, one yellow and one blue. \nWhich colour do you choose?")
#         if wait=="red":
#             print("Its room full of fire ....GAME OVER")
#         elif wait=="blue":
#             print("Eaten by Beasts....GAME OVER")
#         elif wait=="yellow":
#             print("FOUND THE TREASURE.....\n YOU WIN")
#         else:
#             print("GAME OVER")


choice1=input('You\'re at a cross road. Where do you want to go? '
              '\nType "left" or "right"').lower()
if choice1=="left":
    choice2=input("You arrive at the island unharmed.\n There is a house with 3 doors.One red, one yellow and one blue."
          " \nWhich colour do you choose?").lower()
    if choice2=="red":
        print("Its room full of fire ....GAME OVER")
    elif choice2=="yellow":
        print("FOUND THE TREASURE.....\n YOU WIN")

    elif choice2=="blue":
        print("Eaten by Beasts....GAME OVER")
    else:
        print("You've chosen wrong door...try again")


else:
    print("Fall into a hole...GAME OVER")


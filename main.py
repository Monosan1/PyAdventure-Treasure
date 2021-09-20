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
choice1 = input("You're at a cross road. Where do you want to go? Type 'Left or 'Right' \n")
if choice1.lower() == "left":
  choice2 = input("You came to a lake. There is an Island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swin' to swin across \n ")
  if choice2.lower() =="wait":
    choice3 = input("You arrive athe the island unharmed. There is a house with 3 dorrs. One Red, One yellow and one blue. Which colour do you choose? \n")
    if choice3.lower() =="yellow":
      print("You chose wisely, and the treasure was in the Yellow  door \n YOU WIN")
    elif choice3.lower() =="red":
       print("Unfortunelly the Red room was full of fire traps, and you burned in seconds. \nGAME OVER")
    else:
      print("Unfortunelly the Blue room has 5 monstrous Beasts, and they eated you alive.\n GAME OVER")
  else:
    print("Unfortunelly you are attacked by a Trout and died. \nGAME OVER")  
else:
  print("Unfortunelly you fall into a Hole and DIE. GAME OVER")







#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload
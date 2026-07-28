""" Python program that allows a user to play the Snake, Water, Gun game against the computer. 

Game Rules:
Snake vs. Water: Snake drinks Water = Snake wins
Water vs. Gun: Water rusts/drowns Gun = Water wins
Gun vs. Snake: Gun shoots Snake= Gun wins
Same Choice: Player choices match = It's a Draw """


import random

options=["snake", "water", "gun"]

#User input

while True:
    user_input = input("Choose 'Snake', 'Water', or 'Gun': ").lower()
    
    if user_input in options:
        final_user_input = user_input[0]
        print(f"You selected: {final_user_input}")
        break
    else:
        print("Invalid choice! Please type 'Snake', 'Water', or 'Gun'.\n")

#Computer Input

bot_pick = random.choice(options).lower()[0]
print(f"Computer Selected: {bot_pick}")


#Processing
if final_user_input == "s" and bot_pick == "w":
    print("You won!")
elif final_user_input == "w" and bot_pick == "g":
    print("You won!")
elif final_user_input == "g" and bot_pick == "s":
    print("You won!")
elif final_user_input == bot_pick:
    print("It's a Draw!")
else:
    print("You lost!")  
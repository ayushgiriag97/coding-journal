""" Python program that allows a user to play the Snake, Water, Gun game against the computer. 

Game Rules:
Snake vs. Water: Snake drinks Water = Snake wins
Water vs. Gun: Water rusts/drowns Gun = Water wins
Gun vs. Snake: Gun shoots Snake= Gun wins
Same Choice: Player choices match = It's a Draw """


import random
import sys

# --- FEATURE 1: Validated Start Game Prompt ---
while True:
    start_choice = (
        input("🎮 Do you want to start the game? (yes/no): ").strip().lower()
    )

    if start_choice in ["yes", "y"]:
        break
    elif start_choice in ["no", "n"]:
        print("Game terminated. See you next time! 👋")
        sys.exit()
    else:
        print("Invalid input! Please type 'yes' or 'no'.\n")

# --- FEATURE 2: Select Best of N Rounds ---
print("\nSelect Game Format:")
print("1. Best of 1")
print("2. Best of 3 (First to 2 wins)")
print("3. Best of 5 (First to 3 wins)")

while True:
    format_input = input("Choose format (1, 3, or 5): ").strip()
    if format_input in ["1", "3", "5"]:
        total_rounds = int(format_input)
        break
    print("Invalid choice! Please select 1, 3, or 5.")

wins_needed = (total_rounds // 2) + 1

# --- FEATURE 3: Scoreboard Tracking ---
user_score = 0
bot_score = 0
round_number = 1

choice_to_num = {"s": 0, "w": 1, "g": 2}

# Outcomes matrix: outcomes[user_num][bot_num]
outcomes = [
    ["Draw", "You Won!", "You Lost!"],  # User: Snake (0) vs [S, W, G]
    ["You Lost!", "Draw", "You Won!"],  # User: Water (1) vs [S, W, G]
    ["You Won!", "You Lost!", "Draw"],  # User: Gun (2) vs [S, W, G]
]

print(
    f"\n🚀 Game Started! Best of {total_rounds} Series (First to {wins_needed} wins)!\n"
)

# Game Loop: Runs until someone reaches required wins
while user_score < wins_needed and bot_score < wins_needed:
    print(f"--- Round {round_number} ---")

    # User input loop
    while True:
        user_input = (
            input("Choose 'Snake', 'Water', or 'Gun': ").strip().lower()
        )
        if user_input in ["snake", "water", "gun"]:
            final_user_input = user_input[0]
            break
        else:
            print("Invalid choice! Please type 'Snake', 'Water', or 'Gun'.\n")

    # Immediate bot selection
    bot_pick = random.choice(list(choice_to_num.keys()))

    emoji_map = {"s": "🐍 Snake", "w": "💧 Water", "g": "🔫 Gun"}
    print(f" You selected:     {emoji_map[final_user_input]}")
    print(f"🤖 Computer chose:  {emoji_map[bot_pick]}")

    # Matrix lookup
    user_num = choice_to_num[final_user_input]
    bot_num = choice_to_num[bot_pick]
    result = outcomes[user_num][bot_num]

    # Update scores based on result
    if result == "You Won!":
        user_score += 1
        print(" Round Result: YOU WON THIS ROUND! 🎉")
    elif result == "You Lost!":
        bot_score += 1
        print(" Round Result: COMPUTER WON THIS ROUND! 🤖")
    else:
        print(" Round Result: IT'S A DRAW! 🤝")

    # Scoreboard Display
    print(f" SCORE: You [{user_score}] — Computer [{bot_score}]\n")
    round_number += 1

# --- Series Winner Announcement ---
print("=========================================")
if user_score > bot_score:
    print("🏆 CONGRATULATIONS! YOU WON THE SERIES! 🏆")
else:
    print("💻 GAME OVER! COMPUTER WON THE SERIES! 💻")
print(f"Final Score: You [{user_score}] — Computer [{bot_score}]")
print("=========================================")
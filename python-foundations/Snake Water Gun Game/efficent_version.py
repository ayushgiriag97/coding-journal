""" Python program that allows a user to play the Snake, Water, Gun game against the computer. 

Game Rules:
Snake vs. Water: Snake drinks Water = Snake wins
Water vs. Gun: Water rusts/drowns Gun = Water wins
Gun vs. Snake: Gun shoots Snake= Gun wins
Same Choice: Player choices match = It's a Draw """

import random
import sys

# --- Constants ---
CHOICES = {"snake": "s", "water": "w", "gun": "g"}
EMOJIS = {"s": "🐍 Snake", "w": "💧 Water", "g": "🔫 Gun"}
OUTCOMES = [
    ["Draw", "You Won!", "You Lost!"],   # Snake vs [S, W, G]
    ["You Lost!", "Draw", "You Won!"],   # Water vs [S, W, G]
    ["You Won!", "You Lost!", "Draw"],   # Gun vs [S, W, G]
]

# --- Functions ---
def get_user_choice():
    """Prompt user until valid choice is entered."""
    while True:
        choice = input("Choose 'Snake', 'Water', or 'Gun': ").strip().lower()
        if choice in CHOICES:
            return CHOICES[choice]
        print("❌ Invalid choice! Please type 'Snake', 'Water', or 'Gun'.\n")

def play_round(user_score, bot_score, round_number):
    """Play one round and return updated scores."""
    print(f"\n--- Round {round_number} ---")

    user_pick = get_user_choice()
    bot_pick = random.choice(list(CHOICES.values()))

    print(f" You selected:     {EMOJIS[user_pick]}")
    print(f"🤖 Computer chose: {EMOJIS[bot_pick]}")

    result = OUTCOMES[list(CHOICES.values()).index(user_pick)][list(CHOICES.values()).index(bot_pick)]

    if result == "You Won!":
        user_score += 1
        print(" 🎉 YOU WON THIS ROUND!")
    elif result == "You Lost!":
        bot_score += 1
        print(" 🤖 COMPUTER WON THIS ROUND!")
    else:
        print(" 🤝 IT'S A DRAW!")

    print(f" 📊 SCORE: You [{user_score}] — Computer [{bot_score}]")
    return user_score, bot_score

def select_format():
    """Ask user for game format (best of N)."""
    print("\nSelect Game Format:")
    print("1. Best of 1")
    print("3. Best of 3 (First to 2 wins)")
    print("5. Best of 5 (First to 3 wins)")

    while True:
        choice = input("Choose format (1, 3, or 5): ").strip()
        if choice in ["1", "3", "5"]:
            total_rounds = int(choice)
            return total_rounds, (total_rounds // 2) + 1
        print("❌ Invalid choice! Please select 1, 3, or 5.")

# --- Main Game ---
def main():
    # Start prompt
    while True:
        start_choice = input("🎮 Do you want to start the game? (yes/no): ").strip().lower()
        if start_choice in ["yes", "y"]:
            break
        elif start_choice in ["no", "n"]:
            print("Game terminated. See you next time! 👋")
            sys.exit()
        else:
            print("Invalid input! Please type 'yes' or 'no'.\n")

    total_rounds, wins_needed = select_format()
    print(f"\n🚀 Game Started! Best of {total_rounds} Series (First to {wins_needed} wins)!\n")

    user_score = bot_score = 0
    round_number = 1

    while user_score < wins_needed and bot_score < wins_needed:
        user_score, bot_score = play_round(user_score, bot_score, round_number)
        round_number += 1

    print("\n=========================================")
    if user_score > bot_score:
        print("🏆 CONGRATULATIONS! YOU WON THE SERIES! 🏆")
    else:
        print("💻 GAME OVER! COMPUTER WON THE SERIES! 💻")
    print(f"Final Score: You [{user_score}] — Computer [{bot_score}]")
    print("=========================================")

    # Replay option
    replay = input("\n🔄 Do you want to play again? (yes/no): ").strip().lower()
    if replay in ["yes", "y"]:
        main()
    else:
        print("Thanks for playing! 👋")

# Run game
if __name__ == "__main__":
    main()

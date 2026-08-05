import random

def get_int_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("⚠️ Invalid input! Please enter a valid integer.")

while True:
    lower_bound = get_int_input("Enter lower bound: ")
    higher_bound = get_int_input("Enter higher bound: ")

    if lower_bound >= higher_bound:
        print("⚠️ Lower bound must be less than higher bound. Try again.")
    else:
        break

number = random.randint(lower_bound, higher_bound)

print("\n🎯 You have only seven guesses to guess the number!\n")

for attempt in range(1, 8):
    guess = get_int_input(f"Guess {attempt}: ")

    if guess < lower_bound or guess > higher_bound:
        print(f"⚠️ Your guess is out of bounds! Please guess between {lower_bound} and {higher_bound}.")
        continue  # does not consume attempt, lets user retry

    if number < guess:
        print("Guess lower!")
    elif number > guess:
        print("Guess higher!")
    else:
        print(f"🎉 You guessed it right! The number was {number}")
        break
else:
    print(f"❌ Out of tries! Better luck next time. The number was {number}")

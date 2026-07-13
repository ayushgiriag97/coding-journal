import random

lower_bound=int(input("Enter lower bound: "))
higher_bound=int(input("Enter higher bound: "))

number=random.randint(lower_bound, higher_bound)

print("You have only seven guesses to guess the number! \n")

for attempt in range(1,8):
    guess=int(input(f"Guess {attempt}: "))
    
    if number < guess:
        print("Guess lower!")
    elif number > guess:
        print("Guess higher!")
    elif number == guess:
        print(f"You guessed it right! The number was {number}")
else:
    print(f"Out of tries! Better luck next time. The number was {number}")
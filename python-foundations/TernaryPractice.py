# ternary_practice.py

# EXERCISE 1: The Status Gatekeeper (Easy)
# Write a shorthand if-else statement that sets a variable named status to the string "Access Granted" if a variable named age is 18 or older
# , and "AccessDenied" if it is below 18.

age = 20  # Test input
access= "Accesse Granted" if age >= 18 else  "Access Denied"
print(f"Status: {access}")

# EXERCISE 2: Zero Out Noise (Medium)
# Write a one-liner shorthand if-else statement that sets a variable named cleaned_signal to 0 if a variable named signal_strength is less 
# than zero,otherwise sets it to retain the exact current value of signal_strength.

signal_strength = -4.5  # Test input

cleaned_signal= 0 if signal_strength < 0 else  signal_strength
print(f"Your signal strength is: {cleaned_signal}")

# EXERCISE 3: The Multi-Condition Chain (Harder)
# Write a chained shorthand if-else statement evaluating a variable named score. If score is greater than or equal to 50, return "Pass". 
# If score is less than 50 but greater than or equal to 40, return "Conditional Pass". For all other scores below 40, return "Fail".

score = 46  # Test input

checker = "Pass" if score >=50 else "Conditional Pass" if 50 > score >=40 else  "Fail"
print(f"Result status: {checker}")
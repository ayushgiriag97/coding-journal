# =====================================================================
# 🎯 DAY 35 PRACTICE: Mastery of the for...else Control Structure
# =====================================================================

# 🟢 CHALLENGE 1: The Username Validator
print("--- CHALLENGE 1 ---")
usernames = ["anil_pokhara", "sita_99", "admin$", "gita_kumar"]

# Write your loop and else block here:
for i in usernames:   
    for j in i:
        if j=="$":
            print(f"This is invalid username: {i}")
            break
    else:
        print(f"This is valid username: {i}")     
        
# 🟡 CHALLENGE 2: The Item Price Checker
print("\n--- CHALLENGE 2 ---")
prices = [120.50, 45.00, 99.99, 0.0, 250.00] # Try changing 0.0 to a positive number

# Write your loop and else block here:
for i in prices:
    if i <=0:
        print("Entry error found!")
        break
else:
    print("Inventory audit clear. All items priced correctly.")


# 🟡 CHALLENGE 3: Prime Number Checker
print("\n--- CHALLENGE 3 ---")
num = int(input("Enter a number to check if it is Prime: "))

# Write your loop and else block here:
for i in range(2, num):
    if num % i==0:
        print(f"{num} is not prime number!")
        break
else:
    print(f"{num} is prime number!")



# 🟠 CHALLENGE 4: The Multi-Tiered Database Search
print("\n--- CHALLENGE 4 ---")
databases = [
    ["user_id_1", "user_id_2"],
    ["transaction_33", "Target_Data", "transaction_34"],
    ["log_file_99"]
]
target = "Target_Data"

# Hint: You can use a helper variable or function structure, or attach else 
# directly to the inner loop. Try implementing it cleanly!
# Write your logic here:

for i in databases:
    for j in i:
        if j == target:
            print("Target data found!")
            print(f"target data found in this database: {i}")
            break
    else:
        print("Target data not found!")


# 🔴 CHALLENGE 5: The AI Stream Packet Decoder
print("\n--- CHALLENGE 5 ---")
# Variant A (Interrupted stream):
coord_stream = [[12, 4], [10, 10], [45, 12], [-1, -1], [8, 9]]
# Variant B (Clean stream): Change coord_stream to [[12, 4], [10, 10], [45, 12]] to test

# Write your loop and else block here:
for i in coord_stream:
    if i == [-1,-1]:
        print("Stream interrupted by terminal indicator.")
        break
    else:
        print("Stream works just fine!")


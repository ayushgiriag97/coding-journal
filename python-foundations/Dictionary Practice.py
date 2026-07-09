# # ==========================================
# # 🎯 TASK 1: Question 4 (Key Verification)
# # ==========================================
# sample_dict = {"ICP": "Pokhara", "LTMU": "London", "ING": "Kathmandu"}
# keychecker=input("Enter a key to check weather it exits or not.")

# if keychecker in sample_dict:
#     print("Key belongs to dictonary.")


# # =========================================================
# # 🎯 TASK 2: Question 12 (Remove a Key from a Dictionary)
# # =========================================================
# sample_dict1 = {"ICP": "Pokhara", "LTMU": "London", "ING": "Kathmandu"}

# sample_dict1.pop("ICP")
# print(sample_dict1)


# # ===============================================================
# # 🎯 TASK 3: Question 38 (Match Key Values in Two Dictionaries)
# # ===============================================================
# x = {'key1': 1, 'key2': 3, 'key3': 2}
# y = {'key1': 1, 'key2': 2}

# for match in x.items():
#     for matchs in y.items():
#         if match==matchs:
#             print(f"Match found the {match} is present in both x and y!")


# # ==========================================
# # 🎯 TASK 4: Question 36 (Create Dictionary from Two Lists Without Losing
# # Duplicates)
# # ==========================================
# a = [["Class-V","Class-VI","Class-VII","Class-VIII"], #Row 0
#     [1, 2, 2, 3]]                                     #Row 1

# dic={}
# for index in range(len(a[0])):
#     dic_key=a[0][index]
#     dic_value=a[1][index]
#     dic[dic_key] = dic_value

# print(dic)


# =====================================================================
# 🎯 PRACTICE: Sequential Loop Search vs. Direct Hash Lookup
# =====================================================================

monitored_ips = ["192.168.1.1", "10.0.0.5", "172.16.0.2", "192.168.1.50", "10.0.0.9"]
traffic_stream = ["192.168.1.25", "10.0.0.5", "192.168.1.1", "8.8.8.8", "172.16.0.2"]

for 
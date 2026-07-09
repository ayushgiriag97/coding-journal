menu=[["Dhal-Bhat","120","Khana","Yes","Yes"],
      ["Masala Chiya","30","Drink","Yes","Yes"],
      ["Dharane Kalo Bungur","400","Khana","No","Yes"],
      ["Sekuwa","200","Khana","No","Yes"]]


print("menu:")
for iteams in menu:
    print(f"{iteams}\n")

print("veg iteams only.")
for iteams in menu:
    if iteams[3]=="Yes":
        print(f"{iteams}\n")
        
print("non-veg iteams only with price more than 100 and which is available.")
for iteams in menu:
    if iteams[3]=="No" and int(iteams[1])>100 and iteams[4]=="Yes":
        print(f"{iteams}\n")
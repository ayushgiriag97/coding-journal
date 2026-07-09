details=[["Ayush Giri",80],
        ["Monika Giri",45],
        ["Manisha Giri",79],
        ["Tula Giri",91],
        ["Sabita Giri",100]]

Grade=""
marks=0
avg=0

for list in details:
    if list[1] >= 90:
        Grade = "A+"
    elif list[1] >= 80:
        Grade = "A"
    elif list[1] >= 70:
        Grade = "B+"
    elif list[1] >= 60:
        Grade = "B"
    elif list[1] >= 50:
        Grade = "C+"
    elif list[1] >= 40:
        Grade = "C"
    else:
        Grade = "NG"

    print(f"Name: {list[0]}")
    print(f"Marks: {list[1]}")
    if list[1]>=40:
        print(f"Status: Pass")
    else:
        print("Status: Fail")
    print(f"Grade: {Grade}\n")

    if marks < list[1]:
        marks=list[1]
        print(f"topper is {list[0]}")

    avg+=list[1]
    average=avg/len(details)

print(average)



    







    

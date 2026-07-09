#Create a program capable of displaying questions to the user like KBC.
#Use list data type to store the question and their correct answers.
#Display the final amount the person is taking home after playing the game.

list_qns = [
    "Q1: Which is the tallest mountain in the world?\n\nA:KanchanJunga   B:Macchapuchre\nC:Mt.Everest     D:Mt.K2\n",
    "Q2: Which is the largest country in the world?\n\nA:Nepal   B:India\nC:China   D:Russia\n",
    "Q3: Who is known as the father of computers?\n\nA:Charles Babbage   B:Alan Turing\nC:Bill Gates        D:Steve Jobs\n",
    "Q4: What is the capital city of Japan?\n\nA:Beijing   B:Seoul\nC:Tokyo     D:Kyoto\n",
    "Q5: Which planet is known as the Red Planet?\n\nA:Earth   B:Mars\nC:Jupiter D:Venus\n",
    "Q6: What is the chemical symbol for water?\n\nA:H2O   B:O2\nC:CO2   D:HO\n",
    "Q7: Which continent is the Sahara Desert located in?\n\nA:Asia   B:Africa\nC:Australia   D:South America\n",
    "Q8: Who wrote 'Romeo and Juliet'?\n\nA:William Shakespeare   B:Charles Dickens\nC:Leo Tolstoy           D:Mark Twain\n",
    "Q9: What is the national currency of Japan?\n\nA:Yuan   B:Yen\nC:Won    D:Rupee\n",
    "Q10: Which gas do humans need to breathe to survive?\n\nA:Carbon Dioxide   B:Oxygen\nC:Nitrogen        D:Hydrogen\n"
]

list_ans = ["C", "D", "A", "C", "B", "A", "B", "A", "B", "B"]
money=250
for index in range(len(list_qns)):
    print(list_qns[index])
    answer=input("Enter Answer (Eg.A,B,C,D) : ")
    
    if answer==list_ans[index]:
        money*=2
        print(f"Correct answer, You won {money}")
    else:
        print(f"You lost the amount you are taking home is {money}")
        break
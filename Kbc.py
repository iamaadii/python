question =  [   ["Which of the following countries is the world's largest producer of saffron?",'iran','spain','india','greece'],
                ["Which god is also known as 'Gauri Nandan' ?",'agini','ganesha','indra','hanuman'],
                ["Which city is known as the Pink City of India ?",'goa','mumbai','jaipur','delhi'],
                ["Who wrote India's National Anthem ?",'lal bahadur shashtri','rk narayan','chetan bhagat','rabindranath tagore']
            ]

money = [1000,2000,3000,4000]
total = 0

print("\n                      WELCOME TO KBC                         ")

for i in range(0,len(question)):
    print("\n\n",question[i][0])
    print(f"1. {question[i][1]}      2. {question[i][2]}\n3. {question[i][3]}      4. {question[i][4]}")
    ans = int(input("Enter your answer (1,2,3,4): "))
    if ans == i+1:
        print(f"Correct answer!!!...you have won Rs.{money[i]}")
        total += money[i]
    else:
        print("Wrong answer!!..try again")
        
print(f"You have won total amount of Rs.{total}")
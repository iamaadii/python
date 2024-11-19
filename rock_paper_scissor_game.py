import random as r
print("0 for rock.\n1 for scissor.\n2 for paper.")
rounds = input("Enter number of rounds:- ")
rounds = int(rounds)
cw, cl = 0,0
for i in range(0,rounds):
    choice = input("Enter your Choice:- ")
    choice = int(choice)
    n = r.randint(0,2)
    if choice is n:
        print("Draw.")
    elif (choice+1 is n) or (choice is 2 and n is 0):
        print("You win.")
        cw+=1
    else:
        print("You lose.")
        cl+=1
print(cw,cl)
if cw > cl:
    print("\nYou win the game.")
elif cl > cw:
    print("\nYou lose the game.")
elif cl is cw:
    print("\nDraw.")


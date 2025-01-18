import random as r
import string as s

print("Welcome to hangman game!!!")
size = int(input("Enter length of word which u want to guess : "))
life = 6

word_to_guess = ''.join(r.choices(s.ascii_lowercase, k=size))

print(word_to_guess)

display=[]
for i in word_to_guess:
    display+="_"

print(display)

# game_over = False
while(life>=1 or '_' in display):
    gussed_letter = input('Guess a letter : ').lower()
    
    for i in range(size):
        if(word_to_guess[i] == gussed_letter):
            print('correctly guessed')
            display[i] = gussed_letter
    print(display)
    
    if gussed_letter not in word_to_guess:
        print('wrong guess')
        life-=1
        print('life : ',life)
        if(life == 0):
            print("you lost") 
            
    if '_' not in display:
        print("You Won!!!")
import random as r
import logo

print(logo.guess_number)

print('Let me think of a number between 1 to 50')
rand_num = r.randrange(2,50)
easy = 10
hard = 5

level = input("Choose level of difficulty..Type 'easy' or 'hard' : ")

match level:
    case 'easy':
        while easy>=1:
            print(f'You have {easy} attempts remaining to guess the number!!')
            guess_num = int(input('Guess a number : '))
            if guess_num<rand_num:
                print('Your guess is to low') 
                print('Guess again')  
            elif guess_num>rand_num:
                print('Your guess is to high')
                print('Guess again')
            else:
                print(f'You guessed in {easy} attempts')  
                break   
            easy-=1
        if easy==0:
            print('You loose!!')
            
    case 'hard':
        while hard>=1:
            print(f'You have {hard} attempts remaining to guess the number!!')
            guess_num = int(input('Guess a number : '))
            if guess_num<rand_num:
                print('Your guess is to low') 
                print('Guess again')  
            elif guess_num>rand_num:
                print('Your guess is to high')
                print('Guess again')
            else:
                print(f'You guessed in {hard} attempts!!')  
                break   
            hard-=1
        if hard==0:
            print('You loose!!')
            
        

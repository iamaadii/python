print("!!!! WELCOME TO CALCULATOR !!!!")

flag = 'n'
while flag=='n':
    a = int(input('Enter first number : '))
    print('+\n-\n*\n/\n%')

    flag = 'y'
    while(flag=='y'):
        ope = input('Pick an operation : ')
        b=int(input('enter next number : '))
        match ope:
            case '+':
                res=a+b
                print(f'{a} + {b} = {res}')
                a=res
                flag = input(f'enter "y" to continue calculation with {res} ,"n" to start new calculation and "x" for exit : ')
            case '-':
                res=a-b
                print(f'{a} - {b} = {res}')
                a=res
                flag = input(f'enter "y" to continue calculation with {res} ,"n" to start new calculation and "x" for exit : ')
            case '*':
                res=a*b
                print(f'{a} * {b} = {res}')
                a=res
                flag = input(f'enter "y" to continue calculation with {res} ,"n" to start new calculation and "x" for exit : ')
            case '/':
                res=a/b
                print(f'{a} / {b} = {res}')
                a=res
                flag = input(f'enter "y" to continue calculation with {res} ,"n" to start new calculation and "x" for exit : ')
            case '%':
                res=a%b
                print(f'{a} % {b} = {res}')
                a=res
                flag = input(f'enter "y" to continue calculation with {res} ,"n" to start new calculation and "x" for exit : ')


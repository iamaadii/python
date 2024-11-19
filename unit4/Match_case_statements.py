x = int(input("Enter x : "))

match x:
    case 0: 
        print("x is zero")
    case 1 if(x == 1):
        print("x is one")
    
    #default case
    case _ if x!=10:   
        print("x is not equal to 10")
    case _ if x!=20:   
        print("x is not equal to 20")
import string as s

l = [i for i in s.ascii_letters]

stop = 'yes'
while(stop == 'yes'):
    a = int(input('Type 1 for encyption and 2 for decrption :'))

    msg = input("enter ur message : ")
    shift = int(input("Enter shift number : "))
    match a:
        case 1:
            encypt = ''
            for char in msg:
                if char not in l:
                    encypt += char
                elif char.lower() in l:
                    index = l.index(char)
                    new_index=(index+shift)%26
                    encypt += l[new_index]
            print("encrpted msg : ",encypt)
            stop = input("Do you want to continue ? (yes/no) : ")
            
        case 2:
            decrypt = ''
            for char in msg:
                if char not in l:
                    decrypt += char
                elif char.lower() in l:
                    index = l.index(char)
                    new_index=(index+shift)%26
                    decrypt += l[new_index]
            print("decrpted msg : ",decrypt)
            stop = input("Do you want to continue ? (yes/no) : ")
                
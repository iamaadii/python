#default arguments
def avg(a=9,b=1):
    print("avg : ",(a+b)/2)

avg()
avg(3,1) 
avg(5) 

#positional arguments
def fun(name,Department):
    print(f'My name is {name}')
    print(f'I am from {Department} department')

fun('Aditya','CSE')  


#keyword arguments
def addition(a=9,b=2):
    print("addition : ",a+b)
    
addition(a=3,b=2)
addition(a=5)
addition(b=9)
addition(b=10,a=20)

#positional+keyword
def fun(name,Department):
    print(f'My name is {name}')
    print(f'I am from {Department} department')

fun('Aditya',Department='CSE')
# fun(Department='CSE','Aditya') error becoz positional argument cannot appear after keyword args.


#required arguments
def product(a,b=2):  
    print("product : ",a*b)

# product() gives an error bcoz here value of a must be required
product(a=3) #product(3)
product(5,4) #product(a=5,b=4)
product(b=2,a=3)


#Arbitary/variable length argument
def avrge(*num):
    avg = sum(num) / len(num)
    print("Average : ",avg);
    
avrge(10)
avrge(10,20)
avrge(10,20,30)

def total(*num):
    sum = 0
    for i in num:
        sum =sum+i
    print("Total : ",sum);
    
total(5)
total(5,2)
total(5,2,9)

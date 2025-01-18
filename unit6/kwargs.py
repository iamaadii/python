#for passing normal,*args,**kwargs at a time
def my_function(a,*args,**kwargs):
    print(args)
    print(kwargs)
    print(a)

my_function(23,34,'harry',name='Aditya',age=18)
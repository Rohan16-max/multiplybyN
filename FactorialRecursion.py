def fac (x):
    if (x==0 or x==1 ):

        return 1
    
    return x * fac (x-1)

user = int(input("Enter any number:-"))

print("This is the factorial",fac(user))
        

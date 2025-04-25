def setornot (number,n):
    
    if number&((1<<n-1)):
        print("It is a set bit.")
    else:
        print("It is not a set bit.")


x = int(input("Enter any number:-"))
y = int(input("Enter the bit number:-"))

setornot(x,y)
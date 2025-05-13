def num (x):
    count = 0      

    while x:
       

       count = count + 1 
       x>>=1

    return count 

user = int(input("Enter a number:-")) 

print("TThe total bits are this",num(user))
number = int(input("Enter a  number:-"))

r = 0
temp = number
while number > 0:

    remainder = number % 10 
    r  += remainder ** 3
    
    number //= 10

if temp == r:
     print("This is a armstrong number")
else :
     print( "It is not a armstrong number")

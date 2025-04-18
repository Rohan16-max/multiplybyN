user = int(input ("Enter a any number to know if it is a prime number:-"))

if user >1:
    for i in range(2,user):
        if user%i==0:
            print("It is not a prime number")
            break
    else:
        print(" It is a prime number ")
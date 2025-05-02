def log(x,y):
    r = 1
    while y > 0:
        if y%2 == 0:
            x = x*x
            y >>= 1
        else :
            r = r * x

            y = y - 1

    return r

x = int(input("enter first number :-"))

y = int(input("enter second number:-"))

print(x,"raise to the power of ",y,log(x,y))
def x (n,num):
    if (n<1 or n>num):
        return
    print(n)
    x(n-1,num)
    print(n)

input = int(input("Enter a number:-"))
x(input,input)
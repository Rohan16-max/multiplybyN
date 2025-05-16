def head (n,num):
    if n>num:
        return
    head(n+1,num)
    print(n)

input = int(input("Enter a number:-"))

head(1,input)
def tail(n,num):
    if n>num:
        return
    print(n)
    tail(n+1,num)

input = int(input("Enter a number:- "))

tail(1,input)
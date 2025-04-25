def num(n):
    one = 0
    zero = 0


    while n:
        
        if n&1==1:
            one= one+1
        else:
            zero = zero+1

        n>>=1
    print("The total numbber of zeros is this",zero)

    print("The numbers of ones is this",one)

number = int(input("Enter a number:-"))

num(number)
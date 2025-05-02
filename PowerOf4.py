def power4(x):
    if x & x-1 == 0:
        if x == 1:
            print("it is a power of 4")
            exit()
        elif x%10==4  or x%10==6:
            print("it is a power of 4")
        else :
            print("it is not a power of 4")

    else :
        print('it is not a power of 4.')
Z = int(input("Enter any number:- "))

power4(Z)
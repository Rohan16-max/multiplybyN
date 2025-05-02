def power2(x):
    if x & x-1 == 0:
        print('It is a power of 2.')
    else :
        print('it is not a power of 2.')
Z = int(input("Enter any number:- "))

power2(Z)
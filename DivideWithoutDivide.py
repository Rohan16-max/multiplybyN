small = int(input("Enter the smallest number:-"))
big  =  int(input("Enter the biggest number :-"))

if small==0:
    print("error")
    exit()

count = 0

while big >=small:
    big = big - small
    count = count + 1

print("the quotient is this ",count)
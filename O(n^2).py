def onsquare(para):
    iteration = 0
    
    for i in range (1,para+1):
        for j in range(1,para+1):
            print("*",end="")
            iteration +=1
        print("")
    print("\nwhen the value of n is ",para,"te iteration is this",iteration)

onsquare(10)
onsquare(5)

print("\n with every value of n time will increase")

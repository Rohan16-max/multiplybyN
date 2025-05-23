def  sot(x):
    len1 = len(x)

    if len1==0 or len1==1:
        return True
    
    
    return x[0]<=x[1] and sot(x[1:])
x= [1,2,3,4,5,6,7,8,2]

if sot(x):
    print("\nYes it is a sorted array.")
else:
    print("No it is no a sorted array.")
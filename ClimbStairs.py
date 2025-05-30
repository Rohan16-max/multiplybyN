def x(stairs):
    if stairs<0:
        return 0
    if stairs == 0:
        return 1
    
    onestep = 0
    twostep = 0

    if(stairs>=2):
        twostep = x(stairs - 2)
    onestep = x(stairs - 1)
    return onestep + twostep

y = int(input("ENTER THE NUMBER OF STAIRS:-"))

print(x(y))
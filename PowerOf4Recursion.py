z = int (input (" Enter  a the  number:-"))

def x (z):
    if (z<=0):
        return False
    if (z==1):
        return True
    if (z% 4==0):
        return x (z/4)
    return False

print(x (z))
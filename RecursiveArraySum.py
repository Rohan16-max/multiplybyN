def array (z):

    length = len(z)

    if len(z) == 1:
        return z[0]
    
    return z[0] + array(z[1:])

z = [1,2,3,6]

print(array(z))


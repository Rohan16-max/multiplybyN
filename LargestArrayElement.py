def x(a):
    length = len(a)

    if len(a) == 1:
        return a[0]
    
    return max(a[0],x(a[1:]))

z = [1,2,4,8,123,16,2435]

print(x(z))
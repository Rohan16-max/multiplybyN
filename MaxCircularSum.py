def maxSubArraySum(a,a_size):
    max = 0
    cmax = 0
    for i in range(0,a_size):
        cmax = cmax + a[i]
        if (max<cmax):
            max = cmax
        if cmax < 0:
            cmax = 0
    return max

def maxcircular(a):
    n = len(a)
    max_kadane = maxSubArraySum(a,n)
    max_warp = 0
    for i in range (0,n):
        max_warp += a[i]
        a[i] = -a[i]
    max_warp = max_warp + maxSubArraySum(a,n)
    if max_warp > max_kadane:
        return max_warp
    else:
        return max_kadane

a = [11,10,20,-3,-21,70,45,22,-345]
print("Maximum circular sum is :- ",maxcircular(a))
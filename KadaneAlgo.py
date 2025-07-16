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
a = [1,2,4,-4,-56,5,45,24,-22]
print(maxSubArraySum(a,len(a)))
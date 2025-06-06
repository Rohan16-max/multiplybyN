def mean (arr):
    sum1 = 0
    for i in range (0,len(arr)):
        sum1+=arr[i]
    print("mean is",sum1/len(arr))
arr = [1,5,8,9]
mean(arr)

def find_median(arr):
    arr.sort()
    n = len(arr)
    if n%2==1:
        median= arr[n//2]
    else:
        mid1 = arr[n//2-1]
        mid2 = arr[n//2]
        median = (mid1 +mid2)/2
    return median
arr = [7,3,5,2,9]
print("median is",find_median(arr))
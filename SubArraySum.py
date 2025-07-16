def maxsubarraysum(arr):
    n = len(arr)
    max_sum = arr[0]
    for i in range (n):
        current_sum = 0
        for s in range(i,n):
            current_sum += arr[s]
            if i == 0 and s == 0:
                max_sum = current_sum
            elif current_sum > max_sum:
                max_sum = current_sum
    return max_sum

arr = [2,1,3,5,-9]
print("Maximum SubArray Sum :-",maxsubarraysum(arr))
def binary_search_recursive(arr,target,low ,high):
    if low >high :
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target :
        return binary_search_recursive(arr,target,mid +1,high)
    else:
        return binary_search_recursive(arr,target,low,mid - 1)
    
arr = [5,15,25,35,45,55]
print(binary_search_recursive(arr,25,0,len(arr)-1))

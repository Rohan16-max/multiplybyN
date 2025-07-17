def find_missing_number (arr):
    arr.sort()
    for i in range(arr[0],arr[-1]):
        if i not in arr :
            return i 
    return None

arr = [1,2,4,6]
print(find_missing_number(arr))

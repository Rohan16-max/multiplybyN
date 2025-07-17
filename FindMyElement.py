def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid  
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1 

    return -1

arr = [2, 4, 10, 15, 20, 25, 30]
target = 15

index = binary_search(arr, target)

if index != -1:
    print(f"Element {target} found at index {index}")
else:
    print(f"Element {target} not found in the array")
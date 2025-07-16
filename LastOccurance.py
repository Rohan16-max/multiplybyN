def find_last_index(arr, target):
    last_index = -1  
    
    for i in range(len(arr)):
        if arr[i] == target:
            last_index = i 
    
    return last_index

array = [5, 3, 7, 3, 9, 3, 2]
target = 3
result = find_last_index(array, target)

print(f"The last index of {target} is: {result}")
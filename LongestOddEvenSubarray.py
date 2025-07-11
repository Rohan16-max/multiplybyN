def longest_alternating_subarray(arr):

    if not arr:
        return 0

    max_length = 1
    current_length = 1

    for i in range(1, len(arr)):
        if (arr[i] % 2 != arr[i - 1] % 2):
            current_length += 1
        else:
            max_length = max(max_length, current_length)
            current_length = 1

    max_length = max(max_length, current_length)
    return max_length


arr1 = [1, 2, 3, 4, 5, 7, 9]
print(f"Longest alternating subarray length: {longest_alternating_subarray(arr1)}")  

arr2 = [10, 12, 14, 7, 6]
print(f"Longest alternating subarray length: {longest_alternating_subarray(arr2)}") 

arr3 = [1, 2, 3, 4, 5]
print(f"Longest alternating subarray length: {longest_alternating_subarray(arr3)}") 

arr4 = [1, 3, 5, 7]
print(f"Longest alternating subarray length: {longest_alternating_subarray(arr4)}")
def max_difference(arr):
    if len(arr) < 2:
        return "Array must have at least two elements"

    min_element = arr[0]
    max_diff = arr[1] - arr[0]

    for i in range(1, len(arr)):
        max_diff = max(max_diff, arr[i] - min_element)
        min_element = min(min_element, arr[i])

    return max_diff

# Example usage
arr = [2, 10, 1, 15, 8]
print("Maximum difference:", max_difference(arr))
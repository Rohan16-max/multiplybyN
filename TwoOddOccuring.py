# Program to find two numbers that are odd occurring

def findTwoOddOccurring(arr):
    # XOR of all elements in the array
    xor_result = 0
    for num in arr:
        xor_result ^= num

    # Find the rightmost set bit in xor_result
    rightmost_set_bit = xor_result & -xor_result

    # Divide elements into two groups and find the odd occurring numbers
    num1, num2 = 0, 0
    for num in arr:
        if num & rightmost_set_bit:
            num1 ^= num
        else:
            num2 ^= num

    return num1, num2

# Input array
arr = list(map(int, input("Enter array elements separated by space: ").split()))

# Find and print the two odd occurring numbers
odd1, odd2 = findTwoOddOccurring(arr)
print("The two numbers that are odd occurring are:", odd1, "and", odd2)
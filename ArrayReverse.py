arr = [6, 5, 4, 3, 2, 1]

# Method 1: Using reverse()
arr.reverse()
print("Reversed array:", arr)

# Method 2: Using slicing
arr = [6, 5, 4, 3, 2, 1]
reversed_arr = arr[::-1]
print("Reversed array:", reversed_arr)

# Method 3: Using a loop
arr = [6, 5, 4, 3, 2, 1]
reversed_arr = []
for i in range(len(arr) - 1, -1, -1):
    reversed_arr.append(arr[i])
print("Reversed array:", reversed_arr)




#The second method was from gooogle  :)
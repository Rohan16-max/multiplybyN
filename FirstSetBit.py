def rightmost_set_bit(n):
    # Check for zero
    if n == 0:
        return 0
    
    
    return n & -n


number = int(input("Enter a number: "))
result = rightmost_set_bit(number)

if result == 0:
    print("The number has no set bits (it's zero).")
else:
    print(f"The rightmost set bit of {number} is: {result}")

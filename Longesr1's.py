def longest_consecutive_ones(n):
    max_count = 0
    while n != 0:
        
        n = n & (n << 1)
        max_count += 1
    return max_count


number = int(input("Enter a number: "))
result = longest_consecutive_ones(number)
print(f"Longest consecutive 1's in binary representation: {result}")




#or this way



def longest_consecutive_ones2(n):
    count = 0
    max_count = 0

    while n > 0:
        if n & 1:          
            count += 1
            max_count = max(max_count, count)
        else:
            count = 0
        n >>= 1            

    return max_count


number = int(input("Enter a number: "))
result = longest_consecutive_ones2(number)
print(f"Longest consecutive 1's in binary representation: {result}")

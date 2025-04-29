def reverse_bits(num):
    # The total number of bits in the number
    bit_length = num.bit_length()

    
    reversed_num = 0
    for i in range(bit_length):
        
        reversed_num <<= 1
        
        reversed_num |= (num & 1)
        
        num >>= 1

    
    return reversed_num

def reverse_bits_32(num):

    
    return reverse_bits(num)  


if __name__ == "__main__":
    num = int(input("Enter a number: "))
    reversed_number = reverse_bits_32(num)
    
    # Print results
    print(f"Original number: {num} ({bin(num)})")
    print(f"Reversed number: {reversed_number} ({bin(reversed_number)})")

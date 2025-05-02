def is_power_of_8(n):
    if n == 1:
        return True
    if n % 8 != 0 or n == 0:
        return False
    return is_power_of_8(n // 8)

# Example usage:
num = int(input("Enter a number: "))
if is_power_of_8(num):
    print(f"{num} is a power of 8.")
else:
    print(f"{num} is not a power of 8.")
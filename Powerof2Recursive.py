def is_power_of_two_recursive(n):
    if n <= 0:
        return False
    if n == 1:
        return True
    if n % 2 != 0:
        return False
    return is_power_of_two_recursive(n // 2)

# Taking user input
num = int(input("Enter a number: "))


if is_power_of_two_recursive(num):
    print("(num) is a power of 2.")
else:
    print("(num) is not a power of 2.")
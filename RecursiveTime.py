# Factorial function (O(n))
def fac(n):
    if n == 0 or n == 1:
        return 1
    return n * fac(n - 1)

print(fac(5))  # Output: 120

# Print numbers from 1 to 10 (O(1))
def print1to10(n):
    if n > 10:
        return
    print(n)
    print1to10(n + 1)

print1to10(1)  # Output: 1 to 10
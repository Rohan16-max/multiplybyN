def find_substrings(s):
    substrings = []
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substrings.append(s[i:j])
    return substrings

# Taking input from the user
str = input("Enter a string:- ")
print("All substrings:", find_substrings(str))
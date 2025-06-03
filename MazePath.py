def count_paths(n, m):
    
    if n == 1 or m == 1:
        return 1

    
    return count_paths(n - 1, m) + count_paths(n, m - 1)


n = 4  # Number of rows
m = 3  # Number of columns
print("Total possible ways:", count_paths(n, m))
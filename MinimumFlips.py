def count_flips(arr):
    
    count_0 = arr.count(0)
    count_1 = arr.count(1)
    
    
    min_flips = min(count_0, count_1)
    
    print(f"Minimum number of flips needed: {min_flips}")


arr = [0, 1, 0, 1, 1, 0]
count_flips(arr)
def find_duplicates(arr):
    seen = set()
    duplicates = set()
    for num in arr :
        if num in seen :
            duplicates.add(num)
        else:
            seen.add(num)
    return list (duplicates)

arr = [1,2,3,4,1,2,5,6,7,7]
            
print(find_duplicates(arr))
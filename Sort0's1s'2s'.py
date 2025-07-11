def sort_012(arr):
    count = [0, 0, 0]  

    
    for num in arr:
        count[num] += 1

    i = 0
    for num in range(3):
        for _ in range(count[num]):
            arr[i] = num
            i += 1

    return arr
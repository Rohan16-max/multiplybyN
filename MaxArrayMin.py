def minmax (arr):
    temp = arr[0]
    for i in range (1,len(arr)):
        temp = min(temp,arr[i])

    print("minimum element is ",temp)
arr = [5,1,2,6,8]
minmax(arr)




def minmax1 (arr):
    temp = arr[0]
    for i in range (1,len(arr)):
        temp = max(temp,arr[i])

    print("minimum element is ",temp)
arr = [5,1,2,6,8]
minmax1(arr)
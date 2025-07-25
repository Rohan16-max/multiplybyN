def bubblesort (arr):
    n = len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]> arr[j+1]:
                arr [j],arr[j+1] = arr[j+1],arr[j]
            

arr = [64,51,35,12,1,5,89]
bubblesort(arr)
print("Sorted Array :-")
for i in range(len(arr)):
    print(arr[i],end=" , ")
arr.pop()